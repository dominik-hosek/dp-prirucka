---
name: travel-guide-visuals
description: Automate the visual phase of this repository's Czech tourist guides with country templates, destination pages, resumable manifests, QA checkpoints and reproducible PDFs. Use when the user invokes country, destination, resume or status for travel-guide visuals, asks to turn the read-only text project into visual pages, or needs image-generation prompt packets and PDF assembly under 02-tvorba-vizualu.
---

# Travel Guide Visuals

Orchestrate visual production from read-only Czech source text. Use Codex's built-in `$imagegen` for every bitmap page and use `scripts/pipeline.py` for all deterministic planning, state and PDF work.

## Non-negotiable boundaries

1. Treat `01-tvorba-textu` as read-only. Never edit, rename, move or delete anything there.
2. Read `02-tvorba-vizualu/AGENTS.md` before acting inside the visual project.
3. Treat `02-tvorba-vizualu/config/*.yaml` as the machine-readable source of truth. Keep both DOCX files unchanged as original documentation.
4. Use the built-in image generation tool only. Do not create an API client, request an API key, call an image CLI or batch multiple distinct pages into one generation.
5. Make exactly one ImageGen call per page. Keep at most two references: the selected layout and, when available, one country anchor.
6. Never overwrite an approved PNG. Let the pipeline assign a versioned path when an input changes.
7. Keep approved PNGs, manifests, prompt packets and QA reports. Do not keep drafts or rejected variants. PDFs and rendered PDF QA are reproducible ignored builds.

## Runtime setup

Locate the repository root by the presence of `01-tvorba-textu` and `02-tvorba-vizualu`. Load the bundled workspace dependencies before running the pipeline. Use the bundled Python executable reported by the workspace dependency loader.

Set `PIPELINE` conceptually to `<repo>/.agents/skills/travel-guide-visuals/scripts/pipeline.py`. Run `python PIPELINE validate-config` before a new production run. The script emits JSON-compatible YAML without requiring PyYAML.

For an isolated dry-run created with `--output-root`, pass its exact path back to state commands as `resume <destinace> --manifest <path>` or `status <destinace> --manifest <path>`.

## Public mode router

- `$travel-guide-visuals country <země>`: follow Country mode.
- `$travel-guide-visuals destination <destinace> --country <země>`: follow Destination mode.
- `$travel-guide-visuals resume <destinace>`: follow Resume mode.
- `$travel-guide-visuals status <destinace>`: follow Status mode and do not generate.

Additional explicit cover text may be collected during Destination mode; never infer missing marketing copy.

## Country mode

1. Run `python PIPELINE init-country "<země>"`.
2. Read the returned manifest under `02-tvorba-vizualu/šablony/<země>/manifest.yaml`.
3. Process pending pages in manifest order. For each page:
   - read its complete `prompt_file`;
   - inspect the `REFERENCE_LAYOUT` PNG;
   - call built-in ImageGen once with that prompt and that exact reference path;
   - copy the generated asset into the manifest's `output` path through `record-output`;
   - visually inspect the saved PNG and apply the QA procedure below;
   - mark it using `mark-qa`.
4. Retry a failed page with one targeted corrective sentence appended to its original prompt. Make at most three total attempts.
5. After all 14 pages are `passed`, stop. Report the `country_master` checkpoint and wait for explicit human approval.
6. After approval, run `approve <manifest> country_master --notes "..."`.

Use one reference only in this mode. The Spanish PNG is the structural baseline; the configured country profile supplies the visual transformation.

## Destination mode

1. Run `python PIPELINE preflight "<destinace>"`.
2. Stop if there are not exactly eight long chapters, eight taháčky and eight fact-check files with `Stav: OK`.
3. Require explicit cover title and subtitle from the user. Never invent a missing subtitle.
4. Run `python PIPELINE init-destination "<destinace>" --country "<země>" --cover-title "<explicit>" --cover-subtitle "<explicit>"`.
5. Read the manifest and generate pages returned by `resume`, one page per ImageGen call.
6. Use `REFERENCE_LAYOUT` as the first reference. Add `COUNTRY_ANCHOR` only when the page entry contains it. Never exceed two references.
7. Save and QA every page through `record-output` and `mark-qa`.
8. Before first-section approval, generate only the cover and the first complete guide section selected by `resume`.
9. Once every page of that first section is `passed`, stop at the `first_section` checkpoint. Continue only after explicit approval using `approve <manifest> first_section --notes "..."`.
10. Then resume remaining guide pages and all eight A4 taháček pages.
11. Assemble PDFs only when every relevant page is `passed` and no page is blocked. Run `python PIPELINE assemble "<destinace>" all`, then `python PIPELINE render-pdf "<destinace>" all --dpi 150`.
12. Inspect every rendered page after Poppler rendering. Confirm order, count, dimensions, sharpness and absence of clipping before reporting completion.

## Resume mode

1. Run `python PIPELINE resume "<destinace>"`.
2. If `checkpoint` is non-null, stop and request the corresponding human approval.
3. If `blocked` contains pages, do not assemble PDFs. Report them as requiring human review.
4. Process `next_pages` in order, using the prompt and references already recorded in the manifest.
5. Skip `passed` pages whose source, prompt, configuration, reference and output hashes remain valid.
6. A stale page gets a new versioned output path; never overwrite its previous approved PNG.

## Status mode

Run `python PIPELINE status "<destinace>"`. Summarize counts for `passed`, `pending`, `failed`, `stale` and `needs-human-review`, list active checkpoints and blocked pages, and perform no generation or file mutation.

## Page QA procedure

Read `references/qa.md` before evaluating generated pages. Compare the image against the manifest's full `content_contract`, `protected_tokens`, selected layout and country profile.

Mark `passed` only when all content and visual checks pass. For a failure:

1. write one precise corrective instruction;
2. run `mark-qa <manifest> <page> failed --notes "<specific issue>"`;
3. regenerate once with the original prompt plus that instruction;
4. after the third total attempt, let the pipeline mark `needs-human-review` and stop that branch.

Do not rely on image aesthetics alone. Dense generated text always requires direct visual comparison with the source contract.

## Manifest and output contract

Read `references/manifest-schema.md` when diagnosing invalidation or editing pipeline behavior. Use manifest order as the only PDF page order. A guide PDF uses 2:3 pages. A taháček PDF has exactly eight physical A4 portrait pages, fits PNGs without deformation and fills any remaining area with the country background color.
