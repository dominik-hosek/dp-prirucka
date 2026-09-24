#!/usr/bin/env python3
"""Deterministic orchestration for the travel-guide-visuals repo skill.

The script never calls an image API. It prepares prompt packets, manifests,
hash invalidation, QA state and reproducible PDFs around Codex's built-in
ImageGen tool. Files with a .yaml suffix are emitted as JSON, which is valid
YAML 1.2 and requires no third-party YAML dependency.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from collections import Counter
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable


SCHEMA_VERSION = 1
GUIDE_RATIO = 2 / 3
A4_RATIO = 1 / math.sqrt(2)
MAX_ATTEMPTS = 3
VALID_QA = {"pending", "passed", "failed", "needs-human-review", "stale"}


class PipelineError(RuntimeError):
    pass


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def repo_root(start: Path | None = None) -> Path:
    current = (start or Path(__file__)).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "01-tvorba-textu").is_dir() and (candidate / "02-tvorba-vizualu").is_dir():
            return candidate
    raise PipelineError("Nelze najít kořen repozitáře s 01-tvorba-textu a 02-tvorba-vizualu.")


def visual_root(root: Path) -> Path:
    return root / "02-tvorba-vizualu"


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise PipelineError(f"Chybí soubor: {path}") from exc
    except json.JSONDecodeError as exc:
        raise PipelineError(f"Neplatný JSON-kompatibilní YAML {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise PipelineError(f"Kořen {path} musí být objekt/mapa.")
    return data


def write_yaml(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


@lru_cache(maxsize=512)
def _sha256_file_cached(path_text: str, size: int, mtime_ns: int) -> str:
    digest = hashlib.sha256()
    with Path(path_text).open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256_file(path: Path) -> str:
    stat = path.stat()
    return _sha256_file_cached(str(path.absolute()), stat.st_size, stat.st_mtime_ns)


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


def relative(path: Path, root: Path) -> str:
    try:
        return path.absolute().relative_to(root.absolute()).as_posix()
    except ValueError:
        return path.absolute().as_posix()


def resolve_repo_path(value: str, root: Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else root / path


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", "-", ascii_value.lower()).strip("-")


def canonical_name(value: str) -> str:
    return slugify(value)


def config(root: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    vr = visual_root(root)
    return load_yaml(vr / "config" / "countries.yaml"), load_yaml(vr / "config" / "layouts.yaml")


def find_country(countries: dict[str, Any], value: str) -> dict[str, Any]:
    key = canonical_name(value)
    for country in countries.get("countries", []):
        if key in {canonical_name(country.get("name", "")), country.get("slug", "")}:
            return country
    raise PipelineError(f"Země '{value}' není v config/countries.yaml.")


def layout_map(layouts: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {item["id"]: item for item in layouts.get("layouts", [])}


def validate_config(root: Path) -> dict[str, Any]:
    countries, layouts = config(root)
    errors: list[str] = []
    layout_items = layouts.get("layouts", [])
    ids = [item.get("id") for item in layout_items]
    refs: list[str] = []
    if len(layout_items) != 14:
        errors.append(f"Katalog musí mít přesně 14 layoutů, nalezeno {len(layout_items)}.")
    if len(ids) != len(set(ids)):
        errors.append("ID layoutů nejsou unikátní.")
    for item in layout_items:
        for required in ("id", "name", "reference", "properties", "best_for", "template_content", "content_limits"):
            if required not in item:
                errors.append(f"Layout {item.get('id', '?')} nemá pole {required}.")
        ref = visual_root(root) / item.get("reference", "")
        refs.append(relative(ref, root))
        if not ref.is_file():
            errors.append(f"Chybí reference layoutu: {relative(ref, root)}")
    names = [country.get("name") for country in countries.get("countries", [])]
    slugs = [country.get("slug") for country in countries.get("countries", [])]
    if not countries.get("countries"):
        errors.append("Katalog zemí je prázdný.")
    if len(names) != len(set(names)) or len(slugs) != len(set(slugs)):
        errors.append("Názvy nebo slugy zemí nejsou unikátní.")
    for country in countries.get("countries", []):
        for required in ("name", "slug", "palette", "fonts", "motifs", "photo_style", "character"):
            if required not in country:
                errors.append(f"Profil země {country.get('name', '?')} nemá pole {required}.")
    return {"ok": not errors, "errors": errors, "layout_count": len(layout_items), "country_count": len(names), "references": refs}


def content_directory(root: Path, destination: str) -> Path:
    base = root / "01-tvorba-textu" / "content"
    wanted = canonical_name(destination)
    direct = base / wanted
    if direct.is_dir():
        return direct
    for candidate in base.iterdir() if base.is_dir() else []:
        if candidate.is_dir() and canonical_name(candidate.name) == wanted:
            return candidate
    raise PipelineError(f"Textový projekt destinace '{destination}' nebyl nalezen v 01-tvorba-textu/content.")


def section_files(content_dir: Path) -> tuple[list[Path], list[Path], list[Path]]:
    text_dir = content_dir / "text"
    long_files = sorted(path for path in text_dir.glob("[0-9][0-9]-*.md") if path.is_file())
    quick_files = sorted(path for path in (text_dir / "_tahacek").glob("[0-9][0-9]-*.md") if path.is_file())
    fact_files = sorted(path for path in (text_dir / "_fact-check").glob("[0-9][0-9]-*.md") if path.is_file())
    return long_files, quick_files, fact_files


def section_number(path: Path) -> str:
    match = re.match(r"(\d{2})-", path.name)
    return match.group(1) if match else ""


def fact_is_ok(path: Path) -> bool:
    return bool(re.search(r"(?im)^\s*(?:[-*]\s*)?(?:\*\*)?Stav(?:\*\*)?\s*:\s*(?:\*\*)?OK(?:\*\*)?\s*$", path.read_text(encoding="utf-8")))


def is_human_checked(path: Path) -> bool:
    """Return whether a destination-level human review replaces per-section fact checks."""
    return path.is_file() and bool(re.search(
        r"(?im)^\s*(?:[-*]\s*)?(?:\*\*)?Stav(?:\*\*)?\s*:\s*(?:\*\*)?zkontrolováno\s+člověkem",
        path.read_text(encoding="utf-8"),
    ))


def preflight(root: Path, destination: str) -> dict[str, Any]:
    content_dir = content_directory(root, destination)
    long_files, quick_files, fact_files = section_files(content_dir)
    human_check = content_dir / "kontrola.md"
    human_checked = not fact_files and is_human_checked(human_check)
    errors: list[str] = []
    if len(long_files) != 8:
        errors.append(f"Je vyžadováno 8 dlouhých kapitol, nalezeno {len(long_files)}.")
    if len(quick_files) != 8:
        errors.append(f"Je vyžadováno 8 taháčků, nalezeno {len(quick_files)}.")
    if len(fact_files) != 8 and not human_checked:
        errors.append(f"Je vyžadováno 8 fact-checků, nalezeno {len(fact_files)}.")
    long_numbers = {section_number(path) for path in long_files}
    quick_numbers = {section_number(path) for path in quick_files}
    fact_numbers = {section_number(path) for path in fact_files}
    if human_checked:
        fact_numbers = long_numbers
    if long_numbers != quick_numbers or long_numbers != fact_numbers:
        errors.append("Čísla oddílů se mezi dlouhými texty, taháčky a fact-checky neshodují.")
    fact_states = (
        {number: "HUMAN_CHECKED" for number in long_numbers}
        if human_checked
        else {section_number(path): ("OK" if fact_is_ok(path) else "NOT_OK") for path in fact_files}
    )
    bad_facts = sorted(number for number, state in fact_states.items() if state not in ("OK", "HUMAN_CHECKED"))
    if bad_facts:
        errors.append(f"Fact-check bez 'Stav: OK': {', '.join(bad_facts)}.")
    files = long_files + quick_files + fact_files + ([human_check] if human_checked else [])
    return {
        "ok": not errors,
        "errors": errors,
        "content_dir": relative(content_dir, root),
        "long_count": len(long_files),
        "cheatsheet_count": len(quick_files),
        "fact_check_count": len(fact_files),
        "fact_states": fact_states,
        "fact_check_mode": "human_checked" if human_checked else "per_section",
        "sources": [{"path": relative(path, root), "sha256": sha256_file(path)} for path in files],
    }


def render_template(template: str, values: dict[str, Any]) -> str:
    rendered = template
    for key, value in values.items():
        if isinstance(value, (dict, list)):
            value = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
        rendered = rendered.replace("{{" + key + "}}", str(value))
    leftovers = sorted(set(re.findall(r"{{([^{}]+)}}", rendered)))
    if leftovers:
        raise PipelineError(f"Nevyplněné proměnné promptu: {', '.join(leftovers)}")
    return rendered.strip() + "\n"


def prompt_template(root: Path, name: str) -> tuple[Path, str]:
    path = visual_root(root) / "prompts" / name
    return path, path.read_text(encoding="utf-8")


def country_system(country: dict[str, Any]) -> str:
    return json.dumps({
        "palette": country["palette"],
        "heading_fonts": country["fonts"]["heading"],
        "body_fonts": country["fonts"]["body"],
        "motifs": country["motifs"],
        "photo_style": country["photo_style"],
        "character": country["character"],
    }, ensure_ascii=False, separators=(",", ":"))


def source_record(path: Path, root: Path) -> dict[str, str]:
    return {"path": relative(path, root), "sha256": sha256_file(path)}


def ref_record(path: Path, root: Path, role: str) -> dict[str, str]:
    return {"role": role, "path": relative(path, root), "sha256": sha256_file(path)}


def protected_tokens(text: str) -> list[str]:
    patterns = [
        r"\b\d{1,4}(?:[.,]\d+)?(?:\s?[–—-]\s?\d{1,4}(?:[.,]\d+)?)?\s?(?:€|EUR|Kč|CZK|%|km|m|min|hod\.?|h|dnů|dny|°C)(?=\s|[.,;:)]|$)",
        r"\b\d{1,2}[:.]\d{2}\b",
        r"\b\d{1,2}\.\s*(?:ledna|února|března|dubna|května|června|července|srpna|září|října|listopadu|prosince)\b",
        r"\b\d+(?:[.,]\d+)?(?:\s?[–—-]\s?\d+(?:[.,]\d+)?)?\b",
        r"\b(?:ne|nikdy|pouze|jen|nejvýše|minimálně|maximálně|obvykle|zpravidla|může|nemusí)\b",
        r"\b[A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ][a-záčďéěíňóřšťúůýž’'\-]+(?:\s+[A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ][a-záčďéěíňóřšťúůýž’'\-]+)*\b",
    ]
    found: list[str] = []
    for pattern in patterns:
        found.extend(match.group(0).strip() for match in re.finditer(pattern, text, flags=re.IGNORECASE if "nikdy" in pattern else 0))
    for pattern in (r"\*\*([^*\n]+)\*\*", r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"„([^”\n]+)[”\"]"):
        found.extend(match.group(1).strip() for match in re.finditer(pattern, text))
    return list(dict.fromkeys(found))


def word_count(text: str) -> int:
    return len(re.findall(r"\b\w+[\w’-]*\b", text, flags=re.UNICODE))


def markdown_blocks(text: str) -> list[str]:
    lines = text.strip().splitlines()
    blocks: list[str] = []
    current: list[str] = []
    current_list = False
    for line in lines:
        is_list = bool(re.match(r"^\s*(?:[-*+] |\d+[.)] )", line))
        if not line.strip():
            if current:
                blocks.append("\n".join(current).strip())
                current = []
            current_list = False
            continue
        if current and is_list != current_list:
            blocks.append("\n".join(current).strip())
            current = []
        current.append(line)
        current_list = is_list
    if current:
        blocks.append("\n".join(current).strip())
    return [block for block in blocks if block]


def chunk_on_blocks(text: str, max_words: int = 300) -> list[str]:
    chunks: list[str] = []
    current: list[str] = []
    current_words = 0
    for block in markdown_blocks(text):
        count = word_count(block)
        if current and current_words + count > max_words:
            chunks.append("\n\n".join(current))
            current = []
            current_words = 0
        current.append(block)
        current_words += count
    if current:
        chunks.append("\n\n".join(current))
    return chunks or [text.strip()]


def parse_section(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8").strip()
    section_match = re.search(r"(?m)^##\s+(.+)$", text)
    title = section_match.group(1).strip() if section_match else path.stem
    body_start = section_match.end() if section_match else 0
    body = text[body_start:].strip()
    sub_matches = list(re.finditer(r"(?m)^###\s+(.+)$", body))
    intro = body[: sub_matches[0].start()].strip() if sub_matches else body
    subsections: list[dict[str, str]] = []
    for index, match in enumerate(sub_matches):
        end = sub_matches[index + 1].start() if index + 1 < len(sub_matches) else len(body)
        subsection_body = body[match.end():end].strip()
        subsections.append({"title": match.group(1).strip(), "content": f"### {match.group(1).strip()}\n\n{subsection_body}".strip()})
    if not subsections and body:
        subsections.append({"title": title, "content": body})
    return {"title": title, "intro": intro, "subsections": subsections, "raw": text}


def choose_layout(content: str, section_count: int = 1) -> str:
    lower = content.casefold()
    bullets = len(re.findall(r"(?m)^\s*(?:[-*+] |\d+[.)] )", content))
    times = len(re.findall(r"\b\d{1,2}[:.]\d{2}\b", content))
    if any(word in lower for word in ("checklist", "před odjezdem", "nezapomeň", "zkontroluj")) or "- [ ]" in lower:
        return "checklist"
    if any(word in lower for word in ("itinerář", "program dne", "den 1", "den 2")) or times >= 3:
        return "timeline-itinerary"
    if any(word in lower for word in ("srovnání", "výhody", "nevýhody", "oproti", "varianta")):
        return "comparison"
    if section_count == 3:
        return "top-3-cards"
    if section_count >= 4 or bullets >= 7:
        return "list-of-places"
    if section_count == 2:
        return "two-equal-sections"
    if bullets >= 4:
        return "topic-quick-summary"
    if word_count(content) > 340:
        return "editorial-article"
    return "single-topic"


def group_subsections(subsections: list[dict[str, str]], max_words: int = 300) -> list[str]:
    groups: list[str] = []
    pending: list[str] = []
    pending_words = 0
    for subsection in subsections:
        content = subsection["content"]
        count = word_count(content)
        if count > max_words:
            if pending:
                groups.append("\n\n".join(pending))
                pending, pending_words = [], 0
            groups.extend(chunk_on_blocks(content, max_words))
            continue
        if pending and (pending_words + count > max_words or len(pending) >= 2):
            groups.append("\n\n".join(pending))
            pending, pending_words = [], 0
        pending.append(content)
        pending_words += count
    if pending:
        groups.append("\n\n".join(pending))
    return groups


def page_input_hash(page: dict[str, Any], config_hashes: dict[str, str]) -> str:
    payload = {
        "kind": page["kind"],
        "layout": page["layout"],
        "content": page.get("content_contract", ""),
        "sources": page.get("sources", []),
        "references": page.get("references", []),
        "prompt_sha256": page.get("prompt_sha256"),
        "config_hashes": config_hashes,
    }
    return sha256_text(json.dumps(payload, ensure_ascii=False, sort_keys=True))


def next_versioned_path(base: Path) -> Path:
    if not base.exists():
        return base
    match = re.match(r"^(.*?)(?:-v(\d+))?$", base.stem)
    stem = match.group(1) if match else base.stem
    version = 2
    while True:
        candidate = base.with_name(f"{stem}-v{version:02d}{base.suffix}")
        if not candidate.exists():
            return candidate
        version += 1


def base_page(page_id: str, kind: str, order: int, section: str, layout: str, content: str,
              sources: list[dict[str, str]], references: list[dict[str, str]], output: Path,
              prompt_path: Path, prompt_text: str, root: Path) -> dict[str, Any]:
    prompt_path.parent.mkdir(parents=True, exist_ok=True)
    prompt_path.write_text(prompt_text, encoding="utf-8")
    return {
        "id": page_id,
        "kind": kind,
        "section": section,
        "order": order,
        "layout": layout,
        "content_contract": content,
        "protected_tokens": protected_tokens(content),
        "sources": sources,
        "prompt_file": relative(prompt_path, root),
        "prompt_sha256": sha256_file(prompt_path),
        "references": references,
        "output": relative(output, root),
        "output_sha256": None,
        "attempts": 0,
        "qa": {"status": "pending", "notes": [], "checked_at": None},
    }


def preserve_valid_page(new_page: dict[str, Any], old_pages: dict[str, dict[str, Any]], config_hashes: dict[str, str], root: Path) -> dict[str, Any]:
    new_page["inputs_sha256"] = page_input_hash(new_page, config_hashes)
    old = old_pages.get(new_page["id"])
    if not old:
        return new_page
    output = resolve_repo_path(old.get("output", ""), root)
    output_ok = output.is_file() and old.get("output_sha256") == sha256_file(output)
    if old.get("inputs_sha256") == new_page["inputs_sha256"] and output_ok and old.get("qa", {}).get("status") == "passed":
        for field in ("output", "output_sha256", "attempts", "qa"):
            new_page[field] = old[field]
        return new_page
    if old.get("output"):
        stale_base = resolve_repo_path(new_page["output"], root)
        new_page["output"] = relative(next_versioned_path(stale_base), root)
        new_page["qa"] = {"status": "stale", "notes": ["Změnil se zdroj, prompt, konfigurace nebo reference."], "checked_at": utc_now()}
        new_page["attempts"] = 0
    return new_page


def init_country(root: Path, country_name: str, output_root: Path | None = None) -> Path:
    cfg = validate_config(root)
    if not cfg["ok"]:
        raise PipelineError("Neplatná konfigurace:\n- " + "\n- ".join(cfg["errors"]))
    countries, layouts = config(root)
    country = find_country(countries, country_name)
    vr = visual_root(root)
    target = output_root or (vr / "šablony" / country["name"])
    manifest_path = target / "manifest.yaml"
    old = load_yaml(manifest_path) if manifest_path.is_file() else {}
    old_pages = {page["id"]: page for page in old.get("pages", [])}
    countries_path = vr / "config" / "countries.yaml"
    layouts_path = vr / "config" / "layouts.yaml"
    template_path, template = prompt_template(root, "country-template.md")
    config_hashes = {
        "countries": sha256_file(countries_path),
        "layouts": sha256_file(layouts_path),
        "country_prompt": sha256_file(template_path),
    }
    pages: list[dict[str, Any]] = []
    for order, layout in enumerate(layouts["layouts"], start=1):
        ref = vr / layout["reference"]
        exact_content = layout["template_content"].replace("{{country_name}}", country["name"])
        prompt = render_template(template, {
            "country_name": country["name"],
            "layout_name": layout["name"],
            "layout_properties": layout["properties"],
            "layout_best_for": layout["best_for"],
            "palette": country["palette"],
            "heading_fonts": country["fonts"]["heading"],
            "body_fonts": country["fonts"]["body"],
            "motifs": country["motifs"],
            "photo_style": country["photo_style"],
            "character": country["character"],
            "page_content": exact_content,
        })
        page_id = f"template-{order:02d}-{layout['id']}"
        page = base_page(
            page_id, "country-template", order, country["name"], layout["id"],
            exact_content, [],
            [ref_record(ref, root, "REFERENCE_LAYOUT")], target / f"{layout['id']}.png",
            target / "prompts" / f"{page_id}.md", prompt, root,
        )
        pages.append(preserve_valid_page(page, old_pages, config_hashes, root))
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "type": "country",
        "country": country["name"],
        "country_slug": country["slug"],
        "created_at": old.get("created_at", utc_now()),
        "updated_at": utc_now(),
        "config_hashes": config_hashes,
        "approvals": old.get("approvals", {"country_master": {"status": "pending", "at": None, "notes": None}}),
        "pages": pages,
    }
    write_yaml(manifest_path, manifest)
    return manifest_path


def destination_output(root: Path, destination: str, output_root: Path | None = None) -> Path:
    return output_root or (visual_root(root) / "produkty" / canonical_name(destination))


def build_destination_pages(root: Path, destination: str, country: dict[str, Any], cover_title: str,
                            cover_subtitle: str, output_dir: Path, only_section: str | None = None,
                            max_guide_pages: int | None = None) -> tuple[list[dict[str, Any]], dict[str, str]]:
    vr = visual_root(root)
    content_dir = content_directory(root, destination)
    long_files, quick_files, _ = section_files(content_dir)
    countries_path = vr / "config" / "countries.yaml"
    layouts_path = vr / "config" / "layouts.yaml"
    page_tpl_path, page_tpl = prompt_template(root, "page-generation.md")
    cheat_tpl_path, cheat_tpl = prompt_template(root, "cheatsheet-page.md")
    context_path, _ = prompt_template(root, "destination-context.md")
    config_hashes = {
        "countries": sha256_file(countries_path),
        "layouts": sha256_file(layouts_path),
        "page_prompt": sha256_file(page_tpl_path),
        "cheatsheet_prompt": sha256_file(cheat_tpl_path),
        "destination_context": sha256_file(context_path),
    }
    layouts_cfg = load_yaml(layouts_path)
    layouts_by_id = layout_map(layouts_cfg)
    pages: list[dict[str, Any]] = []
    order = 1
    compact_covers = max_guide_pages is not None and only_section is None

    if only_section is None:
        cover_ref = vr / layouts_by_id["cover-page"]["reference"]
        cover_content = f"# {cover_title}\n\n{cover_subtitle}"
        cover_prompt = render_template(page_tpl, {
            "destination": destination,
            "country": country["name"],
            "section_title": "Obálka",
            "page_id": "guide-000-cover",
            "layout_name": layouts_by_id["cover-page"]["name"],
            "page_content": cover_content,
            "protected_tokens": protected_tokens(cover_content),
            "country_system": country_system(country),
        })
        pages.append(base_page(
            "guide-000-cover", "guide", order, "00", "cover-page", cover_content, [],
            [ref_record(cover_ref, root, "REFERENCE_LAYOUT")], output_dir / "guide" / "pages" / "guide-000-cover.png",
            output_dir / "prompts" / "guide-000-cover.md", cover_prompt, root,
        ))
        order += 1

    selected_long = [path for path in long_files if only_section is None or section_number(path) == only_section.zfill(2)]
    for source in selected_long:
        number = section_number(source)
        parsed = parse_section(source)
        source_info = [source_record(source, root)]
        include_section_cover = not compact_covers or number == "01"
        if include_section_cover:
            section_ref = vr / layouts_by_id["section-cover"]["reference"]
            cover_content = f"## {parsed['title']}"
            if parsed["intro"]:
                cover_content += f"\n\n{parsed['intro']}"
            page_id = f"guide-{number}-00-section-cover"
            section_prompt = render_template(page_tpl, {
                "destination": destination,
                "country": country["name"],
                "section_title": parsed["title"],
                "page_id": page_id,
                "layout_name": layouts_by_id["section-cover"]["name"],
                "page_content": cover_content,
                "protected_tokens": protected_tokens(cover_content),
                "country_system": country_system(country),
            })
            pages.append(base_page(
                page_id, "guide", order, number, "section-cover", cover_content, source_info,
                [ref_record(section_ref, root, "REFERENCE_LAYOUT")], output_dir / "guide" / "pages" / f"{page_id}.png",
                output_dir / "prompts" / f"{page_id}.md", section_prompt, root,
            ))
            order += 1
        groups = group_subsections(parsed["subsections"])
        if not include_section_cover and parsed["intro"]:
            groups[0] = f"{parsed['intro']}\n\n{groups[0]}"
        for page_index, content in enumerate(groups, start=1):
            section_count = len(re.findall(r"(?m)^###\s+", content)) or 1
            layout_id = choose_layout(content, section_count)
            layout = layouts_by_id[layout_id]
            ref = vr / layout["reference"]
            page_id = f"guide-{number}-{page_index:02d}-{layout_id}"
            page_prompt = render_template(page_tpl, {
                "destination": destination,
                "country": country["name"],
                "section_title": parsed["title"],
                "page_id": page_id,
                "layout_name": layout["name"],
                "page_content": content,
                "protected_tokens": protected_tokens(content),
                "country_system": country_system(country),
            })
            pages.append(base_page(
                page_id, "guide", order, number, layout_id, content, source_info,
                [ref_record(ref, root, "REFERENCE_LAYOUT")], output_dir / "guide" / "pages" / f"{page_id}.png",
                output_dir / "prompts" / f"{page_id}.md", page_prompt, root,
            ))
            order += 1

    selected_quick = [path for path in quick_files if only_section is None or section_number(path) == only_section.zfill(2)]
    cheat_order = 1
    for source in selected_quick:
        number = section_number(source)
        parsed = parse_section(source)
        content = parsed["raw"]
        page_id = f"cheatsheet-{number}"
        cheat_prompt = render_template(cheat_tpl, {
            "destination": destination,
            "country": country["name"],
            "section_title": parsed["title"],
            "page_id": page_id,
            "page_content": content,
            "protected_tokens": protected_tokens(content),
            "country_system": country_system(country),
        })
        anchor = vr / "šablony" / country["name"] / "two-equal-sections.png"
        references = [ref_record(anchor, root, "COUNTRY_ANCHOR")] if anchor.is_file() else []
        pages.append(base_page(
            page_id, "cheatsheet", cheat_order, number, "cheatsheet-a4", content,
            [source_record(source, root)], references, output_dir / "tahacek" / "pages" / f"{page_id}.png",
            output_dir / "prompts" / f"{page_id}.md", cheat_prompt, root,
        ))
        cheat_order += 1
    guide_count = sum(page["kind"] == "guide" for page in pages)
    if max_guide_pages is not None and guide_count > max_guide_pages:
        raise PipelineError(f"Limit průvodce je {max_guide_pages} stran, ale obsah vyžaduje {guide_count} stran.")
    return pages, config_hashes


def init_destination(root: Path, destination: str, country_name: str, cover_title: str | None,
                     cover_subtitle: str | None, output_root: Path | None = None,
                     only_section: str | None = None, max_guide_pages: int | None = None) -> Path:
    cfg = validate_config(root)
    if not cfg["ok"]:
        raise PipelineError("Neplatná konfigurace:\n- " + "\n- ".join(cfg["errors"]))
    ready = preflight(root, destination)
    if not ready["ok"]:
        raise PipelineError("Preflight selhal:\n- " + "\n- ".join(ready["errors"]))
    if only_section is None and (not cover_title or not cover_subtitle):
        raise PipelineError("Chybí explicitní text obálky. Zadej --cover-title i --cover-subtitle; podtitul se nesmí vymýšlet.")
    countries, _ = config(root)
    country = find_country(countries, country_name)
    output_dir = destination_output(root, destination, output_root)
    manifest_path = output_dir / "manifest.yaml"
    old = load_yaml(manifest_path) if manifest_path.is_file() else {}
    old_pages = {page["id"]: page for page in old.get("pages", [])}
    pages, config_hashes = build_destination_pages(
        root, destination, country, cover_title or "", cover_subtitle or "", output_dir, only_section, max_guide_pages,
    )
    pages = [preserve_valid_page(page, old_pages, config_hashes, root) for page in pages]
    section_order = sorted({page["section"] for page in pages if page["kind"] == "guide" and page["section"] != "00"})
    first_section = section_order[0] if section_order else None
    approvals = old.get("approvals", {
        "first_section": {"section": first_section, "status": "pending", "at": None, "notes": None},
        "final": {"status": "pending", "at": None, "notes": None},
    })
    if approvals.get("first_section", {}).get("section") is None:
        approvals["first_section"]["section"] = first_section
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "type": "destination",
        "destination": destination,
        "destination_slug": canonical_name(destination),
        "country": country["name"],
        "cover": {"title": cover_title, "subtitle": cover_subtitle},
        "created_at": old.get("created_at", utc_now()),
        "updated_at": utc_now(),
        "preflight": ready,
        "config_hashes": config_hashes,
        "approvals": approvals,
        "page_order": [page["id"] for page in sorted(pages, key=lambda item: (0 if item["kind"] == "guide" else 1, item["order"]))],
        "pages": pages,
    }
    write_yaml(manifest_path, manifest)
    return manifest_path


def current_config_hashes(manifest: dict[str, Any], root: Path) -> dict[str, str]:
    vr = visual_root(root)
    paths = {
        "countries": vr / "config" / "countries.yaml",
        "layouts": vr / "config" / "layouts.yaml",
        "country_prompt": vr / "prompts" / "country-template.md",
        "page_prompt": vr / "prompts" / "page-generation.md",
        "cheatsheet_prompt": vr / "prompts" / "cheatsheet-page.md",
        "destination_context": vr / "prompts" / "destination-context.md",
    }
    return {key: sha256_file(path) for key, path in paths.items() if key in manifest.get("config_hashes", {}) and path.is_file()}


def page_config_keys(page: dict[str, Any]) -> set[str]:
    if page.get("kind") == "country-template":
        return {"countries", "layouts", "country_prompt"}
    if page.get("kind") == "cheatsheet":
        return {"countries", "layouts", "cheatsheet_prompt", "destination_context"}
    return {"countries", "layouts", "page_prompt", "destination_context"}


def refresh_page(page: dict[str, Any], manifest: dict[str, Any], root: Path,
                 changed_config_keys: set[str] | None = None) -> str:
    reasons: list[str] = []
    for key in sorted((changed_config_keys or set()) & page_config_keys(page)):
        reasons.append(f"config:{key}")
    for record in page.get("sources", []):
        path = resolve_repo_path(record["path"], root)
        if not path.is_file() or sha256_file(path) != record.get("sha256"):
            reasons.append(f"source:{record['path']}")
    for record in page.get("references", []):
        path = resolve_repo_path(record["path"], root)
        if not path.is_file() or sha256_file(path) != record.get("sha256"):
            reasons.append(f"reference:{record['path']}")
    prompt = resolve_repo_path(page.get("prompt_file", ""), root)
    if not prompt.is_file() or sha256_file(prompt) != page.get("prompt_sha256"):
        reasons.append(f"prompt:{page.get('prompt_file')}")
    output = resolve_repo_path(page.get("output", ""), root)
    if page.get("output_sha256") and (not output.is_file() or sha256_file(output) != page.get("output_sha256")):
        reasons.append(f"output:{page.get('output')}")
    if reasons:
        page["qa"] = {"status": "stale", "notes": ["Neplatné vstupy: " + ", ".join(reasons)], "checked_at": utc_now()}
        return "stale"
    return page.get("qa", {}).get("status", "pending")


def status_manifest(manifest_path: Path, root: Path, write: bool = False) -> dict[str, Any]:
    if not manifest_path.is_file():
        raise PipelineError(f"Manifest neexistuje: {manifest_path}")
    manifest = load_yaml(manifest_path)
    current_hashes = current_config_hashes(manifest, root)
    changed_config_keys = {
        key for key, stored in manifest.get("config_hashes", {}).items()
        if current_hashes.get(key) != stored
    }
    counts: Counter[str] = Counter()
    page_states: list[dict[str, str]] = []
    for page in manifest.get("pages", []):
        state = refresh_page(page, manifest, root, changed_config_keys)
        counts[state] += 1
        page_states.append({"id": page["id"], "kind": page["kind"], "section": page["section"], "status": state})
    builds: dict[str, str] = {}
    if manifest.get("type") == "destination":
        for build_kind, page_kind in (("guide", "guide"), ("cheatsheet", "cheatsheet")):
            relevant_states = [item["status"] for item in page_states if item["kind"] == page_kind]
            prior = manifest.get("builds", {}).get(build_kind)
            if relevant_states and all(state == "passed" for state in relevant_states):
                builds[build_kind] = prior.get("status", "ready") if prior else "ready"
            else:
                builds[build_kind] = "stale" if prior else "blocked"
            if write and prior:
                prior["status"] = builds[build_kind]
    if write:
        manifest["updated_at"] = utc_now()
        write_yaml(manifest_path, manifest)
    return {
        "manifest": relative(manifest_path, root),
        "type": manifest.get("type"),
        "target": manifest.get("destination") or manifest.get("country"),
        "counts": dict(sorted(counts.items())),
        "changed_config_keys": sorted(changed_config_keys),
        "builds": builds,
        "approvals": manifest.get("approvals", {}),
        "pages": page_states,
    }


def manifest_for_destination(root: Path, destination: str) -> Path:
    return visual_root(root) / "produkty" / canonical_name(destination) / "manifest.yaml"


def resume_state(manifest_path: Path, root: Path) -> dict[str, Any]:
    status_manifest(manifest_path, root, write=True)
    manifest = load_yaml(manifest_path)
    pages = manifest.get("pages", [])
    pending = [page for page in pages if page.get("qa", {}).get("status") in {"pending", "failed", "stale"} and page.get("attempts", 0) < MAX_ATTEMPTS]
    blocked = [page for page in pages if page.get("qa", {}).get("status") == "needs-human-review" or page.get("attempts", 0) >= MAX_ATTEMPTS]
    checkpoint = None
    if manifest.get("type") == "country":
        if pages and all(page.get("qa", {}).get("status") == "passed" for page in pages):
            if manifest.get("approvals", {}).get("country_master", {}).get("status") != "approved":
                checkpoint = "country-master"
                pending = []
    else:
        first = manifest.get("approvals", {}).get("first_section", {})
        first_section = first.get("section")
        first_pages = [page for page in pages if page["kind"] == "guide" and page["section"] == first_section]
        first_complete = bool(first_pages) and all(page.get("qa", {}).get("status") == "passed" for page in first_pages)
        if first_complete and first.get("status") != "approved":
            checkpoint = "first-section"
            pending = []
        elif first.get("status") != "approved":
            pending = [page for page in pending if page["kind"] == "guide" and page["section"] in {"00", first_section}]
    return {
        "checkpoint": checkpoint,
        "blocked": [page["id"] for page in blocked],
        "next_pages": [page["id"] for page in sorted(pending, key=lambda item: (0 if item["kind"] == "guide" else 1, item["order"]))],
        "complete": not pending and not blocked and checkpoint is None and all(page.get("qa", {}).get("status") == "passed" for page in pages),
    }


def image_info(path: Path, expected_kind: str) -> dict[str, Any]:
    try:
        from PIL import Image
    except ImportError as exc:
        raise PipelineError("Pro kontrolu obrázků je potřeba Pillow z workspace runtime.") from exc
    with Image.open(path) as image:
        width, height = image.size
        mode = image.mode
        fmt = image.format
    expected = GUIDE_RATIO if expected_kind != "cheatsheet" else A4_RATIO
    actual = width / height
    ratio_ok = abs(actual - expected) <= 0.015
    return {"width": width, "height": height, "mode": mode, "format": fmt, "ratio": actual, "expected_ratio": expected, "ratio_ok": ratio_ok}


def record_output(manifest_path: Path, page_id: str, output: Path, root: Path) -> dict[str, Any]:
    manifest = load_yaml(manifest_path)
    page = next((item for item in manifest.get("pages", []) if item["id"] == page_id), None)
    if not page:
        raise PipelineError(f"Strana {page_id} není v manifestu.")
    if not output.is_file():
        raise PipelineError(f"Výstupní obrázek neexistuje: {output}")
    attempts = int(page.get("attempts", 0)) + 1
    if attempts > MAX_ATTEMPTS:
        raise PipelineError(f"Strana {page_id} už vyčerpala {MAX_ATTEMPTS} pokusy.")
    info = image_info(output, page["kind"])
    expected = resolve_repo_path(page["output"], root)
    if output.resolve() != expected.resolve():
        expected.parent.mkdir(parents=True, exist_ok=True)
        if expected.exists():
            expected = next_versioned_path(expected)
            page["output"] = relative(expected, root)
        shutil.copy2(output, expected)
        output = expected
    page["attempts"] = attempts
    page["output_sha256"] = sha256_file(output)
    page["image"] = info
    if not info["ratio_ok"]:
        page["qa"] = {"status": "failed", "notes": [f"Nesprávný poměr stran: {info['ratio']:.5f}."], "checked_at": utc_now()}
    else:
        page["qa"] = {"status": "pending", "notes": ["Rozměry prošly; čeká obsahová a vizuální QA."], "checked_at": utc_now()}
    manifest["updated_at"] = utc_now()
    write_yaml(manifest_path, manifest)
    return {"page": page_id, "attempts": attempts, "output": relative(output, root), "image": info, "qa": page["qa"]}


def mark_qa(manifest_path: Path, page_id: str, state: str, notes: str, root: Path) -> dict[str, Any]:
    if state not in VALID_QA - {"pending", "stale"}:
        raise PipelineError(f"Neplatný QA stav: {state}")
    manifest = load_yaml(manifest_path)
    page = next((item for item in manifest.get("pages", []) if item["id"] == page_id), None)
    if not page:
        raise PipelineError(f"Strana {page_id} není v manifestu.")
    if state == "passed" and not page.get("output_sha256"):
        raise PipelineError("Stranu bez zaznamenaného výstupu nelze označit passed.")
    if state == "failed" and page.get("attempts", 0) >= MAX_ATTEMPTS:
        state = "needs-human-review"
    page["qa"] = {"status": state, "notes": [notes], "checked_at": utc_now()}
    qa_dir = manifest_path.parent / "qa"
    qa_dir.mkdir(parents=True, exist_ok=True)
    report = {
        "page": page_id,
        "status": state,
        "attempts": page.get("attempts", 0),
        "notes": notes,
        "checked_at": page["qa"]["checked_at"],
        "content_contract_sha256": sha256_text(page.get("content_contract", "")),
        "protected_tokens": page.get("protected_tokens", []),
    }
    write_yaml(qa_dir / f"{page_id}.yaml", report)
    manifest["updated_at"] = utc_now()
    write_yaml(manifest_path, manifest)
    return report


def approve(manifest_path: Path, checkpoint: str, notes: str | None) -> dict[str, Any]:
    manifest = load_yaml(manifest_path)
    approvals = manifest.setdefault("approvals", {})
    if checkpoint not in approvals:
        raise PipelineError(f"Checkpoint '{checkpoint}' není v manifestu. Dostupné: {', '.join(approvals)}")
    approvals[checkpoint].update({"status": "approved", "at": utc_now(), "notes": notes})
    manifest["updated_at"] = utc_now()
    write_yaml(manifest_path, manifest)
    return approvals[checkpoint]


def background_color(manifest: dict[str, Any], root: Path) -> tuple[int, int, int]:
    countries, _ = config(root)
    country = find_country(countries, manifest["country"])
    background = country["palette"].get("background", "#FFFFFF")
    if isinstance(background, list):
        background = background[0]
    value = str(background).lstrip("#")
    return tuple(int(value[index:index + 2], 16) for index in (0, 2, 4))


def require_passed(pages: list[dict[str, Any]], kind: str) -> list[dict[str, Any]]:
    selected = sorted((page for page in pages if page["kind"] == kind), key=lambda item: item["order"])
    bad = [page["id"] for page in selected if page.get("qa", {}).get("status") != "passed"]
    if bad:
        raise PipelineError(f"PDF nelze sestavit; stránky nejsou passed: {', '.join(bad)}")
    return selected


def assemble_pdf(manifest_path: Path, kind: str, root: Path) -> dict[str, Any]:
    try:
        from PIL import Image
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen import canvas
    except ImportError as exc:
        raise PipelineError("Sestavení PDF vyžaduje Pillow a reportlab z workspace runtime.") from exc
    manifest = load_yaml(manifest_path)
    page_kind = "guide" if kind == "guide" else "cheatsheet"
    pages = require_passed(manifest.get("pages", []), page_kind)
    if kind == "cheatsheet" and len(pages) != 8:
        raise PipelineError(f"Taháček musí mít přesně 8 stran, nalezeno {len(pages)}.")
    output_dir = manifest_path.parent / "dist"
    output_dir.mkdir(parents=True, exist_ok=True)
    suffix = "pruvodce" if kind == "guide" else "tahacek"
    output = output_dir / f"{manifest['destination_slug']}-{suffix}.pdf"
    page_size = (1200.0, 1800.0) if kind == "guide" else A4
    pdf = canvas.Canvas(str(output), pagesize=page_size, pageCompression=1)
    fill = background_color(manifest, root)
    for page in pages:
        image_path = resolve_repo_path(page["output"], root)
        if not image_path.is_file():
            raise PipelineError(f"Chybí schválený PNG: {image_path}")
        width, height = page_size
        with Image.open(image_path) as image:
            image_ratio = image.width / image.height
        page_ratio = width / height
        if image_ratio > page_ratio:
            draw_width = width
            draw_height = width / image_ratio
        else:
            draw_height = height
            draw_width = height * image_ratio
        x = (width - draw_width) / 2
        y = (height - draw_height) / 2
        pdf.setFillColorRGB(*(component / 255 for component in fill))
        pdf.rect(0, 0, width, height, stroke=0, fill=1)
        pdf.drawImage(str(image_path), x, y, draw_width, draw_height, preserveAspectRatio=True, mask="auto")
        pdf.showPage()
    pdf.save()
    report = verify_pdf(output, pages, kind)
    report["output"] = relative(output, root)
    qa_dir = manifest_path.parent / "qa"
    qa_dir.mkdir(parents=True, exist_ok=True)
    write_yaml(qa_dir / f"{kind}-pdf.yaml", report)
    manifest.setdefault("builds", {})[kind] = {
        "status": report["status"],
        "output": report["output"],
        "sha256": report["sha256"],
        "page_count": report["page_count"],
        "built_at": utc_now(),
    }
    manifest["updated_at"] = utc_now()
    write_yaml(manifest_path, manifest)
    return report


def verify_pdf(path: Path, pages: list[dict[str, Any]], kind: str) -> dict[str, Any]:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise PipelineError("Kontrola PDF vyžaduje pypdf z workspace runtime.") from exc
    reader = PdfReader(str(path))
    dimensions: list[dict[str, float]] = []
    expected_ratio = GUIDE_RATIO if kind == "guide" else A4_RATIO
    dimensions_ok = True
    for index, page in enumerate(reader.pages, start=1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        ratio = width / height
        ok = abs(ratio - expected_ratio) <= 0.002
        dimensions_ok &= ok
        dimensions.append({"page": index, "width_pt": width, "height_pt": height, "ratio": ratio, "ok": ok})
    return {
        "status": "passed" if len(reader.pages) == len(pages) and dimensions_ok else "failed",
        "page_count": len(reader.pages),
        "expected_page_count": len(pages),
        "order": [page["id"] for page in pages],
        "dimensions": dimensions,
        "sha256": sha256_file(path),
    }


def find_poppler(executable: str) -> Path | None:
    cache = Path.home() / ".cache" / "codex-runtimes"
    matches = sorted(cache.glob(f"**/poppler/Library/bin/{executable}.exe")) if cache.exists() else []
    if matches:
        return matches[-1]
    found = shutil.which(executable)
    return Path(found) if found else None


def render_pdf(manifest_path: Path, kind: str, root: Path, dpi: int = 150) -> dict[str, Any]:
    manifest = load_yaml(manifest_path)
    suffix = "pruvodce" if kind == "guide" else "tahacek"
    pdf_path = manifest_path.parent / "dist" / f"{manifest['destination_slug']}-{suffix}.pdf"
    if not pdf_path.is_file():
        raise PipelineError(f"PDF neexistuje: {pdf_path}")
    renderer = find_poppler("pdftoppm")
    if not renderer:
        raise PipelineError("Poppler pdftoppm nebyl nalezen.")
    render_dir = manifest_path.parent / "qa" / "rendered" / kind
    if render_dir.exists():
        shutil.rmtree(render_dir)
    render_dir.mkdir(parents=True, exist_ok=True)
    prefix = render_dir / "page"
    child_env = os.environ.copy()
    child_env["PATH"] = str(renderer.parent) + os.pathsep + child_env.get("PATH", "")
    completed = subprocess.run(
        [str(renderer), "-png", "-r", str(dpi), str(pdf_path), str(prefix)],
        capture_output=True, text=True, env=child_env,
    )
    if completed.returncode != 0:
        raise PipelineError(f"Poppler render selhal: {completed.stderr.strip()}")
    images = sorted(render_dir.glob("page-*.png"))
    source_kind = "guide" if kind == "guide" else "cheatsheet"
    expected = len([page for page in manifest["pages"] if page["kind"] == source_kind])
    sharp = True
    rendered: list[dict[str, Any]] = []
    for image in images:
        info = image_info(image, source_kind)
        sharp &= info["width"] >= 1000 or dpi < 150
        rendered.append({"path": relative(image, root), **info})
    report = {
        "status": "passed" if len(images) == expected and sharp and all(item["ratio_ok"] for item in rendered) else "failed",
        "pdf": relative(pdf_path, root),
        "page_count": len(images),
        "expected_page_count": expected,
        "dpi": dpi,
        "rendered": rendered,
    }
    write_yaml(manifest_path.parent / "qa" / f"{kind}-render.yaml", report)
    return report


def json_print(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Deterministická pipeline vizuálů turistických průvodců")
    parser.add_argument("--repo-root", type=Path, help="Kořen repozitáře; běžně se detekuje automaticky.")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate-config")
    pre = sub.add_parser("preflight")
    pre.add_argument("destination")

    country = sub.add_parser("init-country")
    country.add_argument("country")
    country.add_argument("--output-root", type=Path)

    dest = sub.add_parser("init-destination")
    dest.add_argument("destination")
    dest.add_argument("--country", required=True)
    dest.add_argument("--cover-title")
    dest.add_argument("--cover-subtitle")
    dest.add_argument("--only-section")
    dest.add_argument("--max-guide-pages", type=int, help="Maximální počet stran hlavního průvodce.")
    dest.add_argument("--output-root", type=Path)

    status = sub.add_parser("status")
    status.add_argument("destination")
    status.add_argument("--manifest", type=Path, help="Volitelný manifest mimo standardní produkty/<slug>.")
    status.add_argument("--write", action="store_true")

    resume = sub.add_parser("resume")
    resume.add_argument("destination")
    resume.add_argument("--manifest", type=Path, help="Volitelný manifest mimo standardní produkty/<slug>.")

    record = sub.add_parser("record-output")
    record.add_argument("manifest", type=Path)
    record.add_argument("page")
    record.add_argument("output", type=Path)

    qa = sub.add_parser("mark-qa")
    qa.add_argument("manifest", type=Path)
    qa.add_argument("page")
    qa.add_argument("state", choices=sorted(VALID_QA - {"pending", "stale"}))
    qa.add_argument("--notes", required=True)

    approval = sub.add_parser("approve")
    approval.add_argument("manifest", type=Path)
    approval.add_argument("checkpoint")
    approval.add_argument("--notes")

    assemble = sub.add_parser("assemble")
    assemble.add_argument("destination")
    assemble.add_argument("kind", choices=["guide", "cheatsheet", "all"])

    render = sub.add_parser("render-pdf")
    render.add_argument("destination")
    render.add_argument("kind", choices=["guide", "cheatsheet", "all"])
    render.add_argument("--dpi", type=int, default=150)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = repo_root(args.repo_root) if args.repo_root else repo_root()
    try:
        if args.command == "validate-config":
            result = validate_config(root)
            json_print(result)
            return 0 if result["ok"] else 2
        if args.command == "preflight":
            result = preflight(root, args.destination)
            json_print(result)
            return 0 if result["ok"] else 2
        if args.command == "init-country":
            path = init_country(root, args.country, args.output_root.resolve() if args.output_root else None)
            json_print({"manifest": relative(path, root), "status": status_manifest(path, root)})
            return 0
        if args.command == "init-destination":
            path = init_destination(root, args.destination, args.country, args.cover_title, args.cover_subtitle,
                                    args.output_root.resolve() if args.output_root else None, args.only_section, args.max_guide_pages)
            json_print({"manifest": relative(path, root), "status": status_manifest(path, root)})
            return 0
        if args.command == "status":
            manifest = args.manifest.resolve() if args.manifest else manifest_for_destination(root, args.destination)
            json_print(status_manifest(manifest, root, args.write))
            return 0
        if args.command == "resume":
            manifest = args.manifest.resolve() if args.manifest else manifest_for_destination(root, args.destination)
            json_print(resume_state(manifest, root))
            return 0
        if args.command == "record-output":
            json_print(record_output(args.manifest.resolve(), args.page, args.output.resolve(), root))
            return 0
        if args.command == "mark-qa":
            json_print(mark_qa(args.manifest.resolve(), args.page, args.state, args.notes, root))
            return 0
        if args.command == "approve":
            json_print(approve(args.manifest.resolve(), args.checkpoint, args.notes))
            return 0
        if args.command == "assemble":
            manifest = manifest_for_destination(root, args.destination)
            kinds = ["guide", "cheatsheet"] if args.kind == "all" else [args.kind]
            json_print({kind: assemble_pdf(manifest, kind, root) for kind in kinds})
            return 0
        if args.command == "render-pdf":
            manifest = manifest_for_destination(root, args.destination)
            kinds = ["guide", "cheatsheet"] if args.kind == "all" else [args.kind]
            json_print({kind: render_pdf(manifest, kind, root, args.dpi) for kind in kinds})
            return 0
    except PipelineError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
