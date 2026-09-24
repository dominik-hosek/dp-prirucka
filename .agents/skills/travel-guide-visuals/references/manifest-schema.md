# Manifest contract

The pipeline writes JSON-compatible YAML 1.2 with `schema_version: 1`.

## Top-level destination fields

- `type`: `destination`
- `destination`, `destination_slug`, `country`
- `cover.title`, `cover.subtitle`: explicit user text
- `preflight`: counts, fact-check states, source paths and SHA-256 hashes
- `config_hashes`: country, layout and prompt-template hashes
- `approvals.first_section`, `approvals.final`
- `page_order`: canonical output order
- `pages`: page records

Country manifests use `type: country`, `country`, `country_slug`, `approvals.country_master` and exactly 14 page records.

## Page record

- `id`, `kind`, `section`, `order`, `layout`
- `content_contract`: exact source material assigned to the page
- `protected_tokens`: numbers, currency, time, dates, names, negations and cautious terms
- `sources[]`: repo-relative path and SHA-256
- `prompt_file`, `prompt_sha256`: final fully rendered prompt packet
- `references[]`: role, path and SHA-256
- `inputs_sha256`: aggregate invalidation key
- `output`, `output_sha256`
- `attempts`: maximum 3
- `image`: dimensions, format and aspect validation
- `qa.status`, `qa.notes`, `qa.checked_at`

## Invalidation

A page becomes stale when any source, prompt packet, config input, reference or approved output hash changes. Re-initialization preserves a valid passed page. A stale page receives the next free `-vNN` output name. Only affected pages and their dependent PDFs are invalidated.

## State meanings

- `pending`: ready for generation or waiting for content QA
- `passed`: approved by automatic/agent QA and hash-valid
- `failed`: correctable failure with attempts remaining
- `stale`: an input or output changed
- `needs-human-review`: three attempts exhausted or ambiguity requires a human

