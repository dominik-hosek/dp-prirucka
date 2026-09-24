# Visual and content QA

Inspect the saved project PNG, not only the transient ImageGen result.

## Content fidelity

- Match every number, currency, time, date, proper name, negation and cautious formulation against `content_contract`.
- Confirm every `protected_token` is present and exact.
- Confirm no fact, recommendation or qualification disappeared or was added.
- Allow only typographic rearrangement or meaning-neutral shortening of ordinary prose.
- Reject invented businesses, addresses, labels, signs, logos, watermarks and English captions.

## Visual integrity

- Confirm guide pages are 2:3 and taháček pages are A4 portrait ratio.
- Confirm safe margins, readable Czech text, no overflow, no overlaps and no clipped components.
- Compare component hierarchy to `REFERENCE_LAYOUT`.
- Compare palette, typography feeling, motifs and photographic treatment to the configured country system or `COUNTRY_ANCHOR`.
- Reject distorted photography, illegible generated glyphs and visual drift.

## Retry policy

On failure, identify the smallest concrete defect and append one targeted correction to the unchanged original prompt. Do not silently repair source text. Record every attempt. After attempt 3, mark `needs-human-review` and block PDF assembly.

## PDF render QA

After assembly, render both PDFs with Poppler. Inspect every page in order. Confirm page count, dimensions, sharpness, safe fit, no distortion, no unexpected crop and no blank page. The taháček must contain exactly eight physical A4 pages.
