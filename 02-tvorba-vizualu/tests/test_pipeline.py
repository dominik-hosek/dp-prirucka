from __future__ import annotations

import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
PIPELINE_PATH = ROOT / ".agents" / "skills" / "travel-guide-visuals" / "scripts" / "pipeline.py"
SPEC = importlib.util.spec_from_file_location("travel_visual_pipeline", PIPELINE_PATH)
pipeline = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(pipeline)


class PipelineTests(unittest.TestCase):
    def setUp(self) -> None:
        temp_base = ROOT / "02-tvorba-vizualu" / ".test-tmp"
        temp_base.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=temp_base)
        self.temp_path = Path(self.temp.name)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def make_png(self, path: Path, size: tuple[int, int]) -> Path:
        from PIL import Image

        path.parent.mkdir(parents=True, exist_ok=True)
        Image.new("RGB", size, (242, 238, 228)).save(path, format="PNG")
        return path

    def test_config_has_exactly_fourteen_real_layouts(self) -> None:
        result = pipeline.validate_config(ROOT)
        self.assertTrue(result["ok"], result["errors"])
        self.assertEqual(result["layout_count"], 14)
        self.assertTrue(all((ROOT / path).is_file() for path in result["references"]))

    def test_barcelona_preflight_requires_eight_ok_sections(self) -> None:
        result = pipeline.preflight(ROOT, "Barcelona")
        self.assertTrue(result["ok"], result["errors"])
        self.assertEqual((result["long_count"], result["cheatsheet_count"], result["fact_check_count"]), (8, 8, 8))
        self.assertEqual(set(result["fact_states"].values()), {"OK"})

    def test_missing_cover_copy_is_rejected_for_full_destination(self) -> None:
        with self.assertRaisesRegex(pipeline.PipelineError, "explicitní text obálky"):
            pipeline.init_destination(ROOT, "Barcelona", "Španělsko", None, None, self.temp_path)

    def test_protected_tokens_keep_ranges_names_and_caution(self) -> None:
        text = "Barcelona: **menú del día** stojí 10–15 EUR, někdy 13–20 EUR; ber to jako orientaci, ne jako ceník. Večeře (*sopar*) je ve 20:30."
        tokens = pipeline.protected_tokens(text)
        for expected in ("Barcelona", "menú del día", "10–15 EUR", "13–20 EUR", "ne", "sopar", "20:30"):
            self.assertIn(expected, tokens)

    def test_finland_country_dry_run_writes_fourteen_prompt_packets(self) -> None:
        manifest_path = pipeline.init_country(ROOT, "Finsko", self.temp_path / "finsko")
        manifest = pipeline.load_yaml(manifest_path)
        self.assertEqual(len(manifest["pages"]), 14)
        self.assertEqual({page["qa"]["status"] for page in manifest["pages"]}, {"pending"})
        for page in manifest["pages"]:
            prompt = pipeline.resolve_repo_path(page["prompt_file"], ROOT)
            self.assertTrue(prompt.is_file())
            self.assertNotIn("{{", prompt.read_text(encoding="utf-8"))
            self.assertTrue(page["content_contract"].strip())
            self.assertIn(page["content_contract"], prompt.read_text(encoding="utf-8"))
            self.assertEqual(len(page["references"]), 1)

    def test_barcelona_food_section_dry_run_preserves_section_boundaries(self) -> None:
        manifest_path = pipeline.init_destination(
            ROOT, "Barcelona", "Španělsko", None, None,
            self.temp_path / "barcelona-food", only_section="04",
        )
        manifest = pipeline.load_yaml(manifest_path)
        guide = [page for page in manifest["pages"] if page["kind"] == "guide"]
        cheat = [page for page in manifest["pages"] if page["kind"] == "cheatsheet"]
        self.assertGreaterEqual(len(guide), 2)
        self.assertEqual(len(cheat), 1)
        self.assertEqual({page["section"] for page in manifest["pages"]}, {"04"})
        self.assertEqual(guide[0]["layout"], "section-cover")
        self.assertTrue(all("{{" not in pipeline.resolve_repo_path(page["prompt_file"], ROOT).read_text(encoding="utf-8") for page in manifest["pages"]))
        isolated_resume = pipeline.resume_state(manifest_path, ROOT)
        self.assertTrue(isolated_resume["next_pages"])
        self.assertTrue(all(page_id.startswith("guide-04-") for page_id in isolated_resume["next_pages"]))

    def test_prompt_hash_change_marks_only_affected_page_stale(self) -> None:
        manifest_path = pipeline.init_destination(
            ROOT, "Barcelona", "Španělsko", None, None,
            self.temp_path / "barcelona-food", only_section="04",
        )
        manifest = pipeline.load_yaml(manifest_path)
        first = manifest["pages"][0]
        image = self.make_png(self.temp_path / "generated.png", (1000, 1500))
        pipeline.record_output(manifest_path, first["id"], image, ROOT)
        pipeline.mark_qa(manifest_path, first["id"], "passed", "test pass", ROOT)
        prompt = pipeline.resolve_repo_path(first["prompt_file"], ROOT)
        prompt.write_text(prompt.read_text(encoding="utf-8") + "\nchanged\n", encoding="utf-8")
        result = pipeline.status_manifest(manifest_path, ROOT)
        states = {page["id"]: page["status"] for page in result["pages"]}
        self.assertEqual(states[first["id"]], "stale")
        self.assertTrue(all(state != "stale" for page_id, state in states.items() if page_id != first["id"]))

    def test_guide_prompt_config_change_does_not_invalidate_cheatsheet(self) -> None:
        manifest_path = pipeline.init_destination(
            ROOT, "Barcelona", "Španělsko", None, None,
            self.temp_path / "barcelona-food", only_section="04",
        )
        manifest = pipeline.load_yaml(manifest_path)
        manifest["config_hashes"]["page_prompt"] = "0" * 64
        pipeline.write_yaml(manifest_path, manifest)
        result = pipeline.status_manifest(manifest_path, ROOT)
        guide_states = {page["status"] for page in result["pages"] if page["kind"] == "guide"}
        cheat_states = {page["status"] for page in result["pages"] if page["kind"] == "cheatsheet"}
        self.assertEqual(guide_states, {"stale"})
        self.assertEqual(cheat_states, {"pending"})
        self.assertEqual(result["changed_config_keys"], ["page_prompt"])

    def test_third_failed_attempt_needs_human_review(self) -> None:
        manifest_path = pipeline.init_destination(
            ROOT, "Barcelona", "Španělsko", None, None,
            self.temp_path / "barcelona-food", only_section="04",
        )
        page_id = pipeline.load_yaml(manifest_path)["pages"][0]["id"]
        image = self.make_png(self.temp_path / "generated.png", (1000, 1500))
        final = None
        for attempt in range(3):
            pipeline.record_output(manifest_path, page_id, image, ROOT)
            final = pipeline.mark_qa(manifest_path, page_id, "failed", f"failure {attempt + 1}", ROOT)
        self.assertEqual(final["status"], "needs-human-review")

    def test_pdf_order_count_and_dimensions(self) -> None:
        guide_pages = []
        cheat_pages = []
        for index in range(2):
            image = self.make_png(self.temp_path / "guide" / f"g{index}.png", (1000, 1500))
            guide_pages.append({
                "id": f"guide-{index}", "kind": "guide", "section": "01", "order": index + 1,
                "output": str(image), "output_sha256": pipeline.sha256_file(image),
                "qa": {"status": "passed"},
            })
        for index in range(8):
            image = self.make_png(self.temp_path / "cheat" / f"c{index}.png", (1000, 1414))
            cheat_pages.append({
                "id": f"cheat-{index}", "kind": "cheatsheet", "section": f"{index + 1:02d}", "order": index + 1,
                "output": str(image), "output_sha256": pipeline.sha256_file(image),
                "qa": {"status": "passed"},
            })
        manifest_path = self.temp_path / "manifest.yaml"
        pipeline.write_yaml(manifest_path, {
            "schema_version": 1, "type": "destination", "destination": "Test", "destination_slug": "test",
            "country": "Španělsko", "pages": guide_pages + cheat_pages,
        })
        guide = pipeline.assemble_pdf(manifest_path, "guide", ROOT)
        cheat = pipeline.assemble_pdf(manifest_path, "cheatsheet", ROOT)
        self.assertEqual(guide["status"], "passed")
        self.assertEqual(guide["order"], ["guide-0", "guide-1"])
        self.assertEqual(cheat["status"], "passed")
        self.assertEqual(cheat["page_count"], 8)
        self.assertTrue(all(page["ok"] for page in guide["dimensions"] + cheat["dimensions"]))
        guide_render = pipeline.render_pdf(manifest_path, "guide", ROOT, dpi=72)
        cheat_render = pipeline.render_pdf(manifest_path, "cheatsheet", ROOT, dpi=72)
        self.assertEqual(guide_render["status"], "passed")
        self.assertEqual(cheat_render["status"], "passed")
        self.assertEqual(cheat_render["page_count"], 8)


if __name__ == "__main__":
    unittest.main()
