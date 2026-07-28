# Šablony stránek (znovupoužitelné napříč kapitolami i destinacemi)

Textové stránky (typ T) se negenerují jednotlivě — vygeneruješ **jednou** tuhle sadu prázdných
šablon a pak do nich vkládáš text kapitol. Ušetří to práci a hlavně to zaručí, že stránky vypadají
stejně.

Před každý prompt vlož styl blok z `docs/prompt-guide.md`.

Vygeneruj si z každé šablony 3–4 varianty, vyber nejlepší a ulož do
`design/<destinace>/sablony/`. Pak už jen doplňuješ text.

---

## Šablona T1 — textová strana s fotkou nahoře

Nejběžnější stránka. Fotka v horní třetině, pod ní prostor na nadpis a dva až tři odstavce.

```
Empty page template for a printed travel guide. NO TEXT ANYWHERE on the page — this is a blank
layout frame that text will be added to later.

Layout, top to bottom:
- Top third: a photograph area filled with a soft, out-of-focus warm Mediterranean coastal scene
  (sea, sky, greenery) with rounded bottom corners. Generic, not a recognizable specific location.
- Below it: a clearly empty cream area with generous margins, where a heading and two to three
  paragraphs of body text will be placed. Leave this area completely blank — flat cream #F3ECE0,
  no lines, no boxes, no placeholder marks.
- Bottom edge: a thin dotted decorative line in olive green and an empty small circle in the outer
  corner for a page number.

Absolutely no letters, words, numbers, or text-like marks anywhere in the image.
```

---

## Šablona T2 — textová strana s tip/pozor kartou

Když má stránka nést insider tip nebo varování („ověř si cenu", „pozor na…").

```
Empty page template for a printed travel guide. NO TEXT ANYWHERE — blank layout frame only.

Layout, top to bottom:
- Upper half: empty cream area with generous margins for a heading and body paragraphs. Completely
  blank, flat cream #F3ECE0.
- Lower middle: two soft rounded-corner cards stacked with clear vertical spacing between them.
  The first card has an off-white #FFFDF9 fill with a thin olive green #6B7A3A left edge accent and
  a small empty circular badge in its top-left corner. The second card has a pale terracotta tinted
  fill with a thin terracotta #C1502E left edge accent and its own small empty circular badge.
  Both cards are empty inside — no text, no icon glyphs, just the card shape and the badge circle.
- Bottom: thin dotted olive line and an empty small circle for a page number.

The cards must have clearly generous internal padding so text fits comfortably later.
Absolutely no letters, words, numbers, or text-like marks anywhere in the image.
```

---

## Šablona T3 — strana s číslovaným seznamem / checklistem

Na „Rychlé shrnutí", checklisty a kroky.

```
Empty page template for a printed travel guide. NO TEXT ANYWHERE — blank layout frame only.

Layout:
- Top: empty cream area with generous margin for a heading. Completely blank.
- Main body: five evenly spaced horizontal rows. Each row has, on the left, a filled circular badge
  (alternating olive green #6B7A3A and terracotta #C1502E) that is EMPTY inside — no number, no
  glyph — and to the right of it a wide blank cream area where a line or two of text will go.
  Rows separated by generous vertical spacing and a very thin dotted divider.
- Bottom: thin dotted olive line and an empty small circle for a page number.

Absolutely no letters, words, numbers, or text-like marks anywhere in the image.
```

---

## Šablona T4 — dvousloupcová srovnávací strana

Na srovnání dvou možností (SIM vs. eSIM, autobus vs. taxi, hotel vs. apartmán).

```
Empty page template for a printed travel guide. NO TEXT ANYWHERE — blank layout frame only.

Layout:
- Top: empty cream area for a heading. Completely blank.
- Main body: two tall rounded-corner cards side by side, equal width, with a clear gutter between
  them. Left card off-white #FFFDF9 with a thin olive green top edge band; right card off-white with
  a thin terracotta top edge band. Each card has a small empty circular badge centered near its top,
  and generous blank space below for a short list of items. Cards completely empty inside.
- Bottom: thin dotted olive line and an empty small circle for a page number.

Absolutely no letters, words, numbers, or text-like marks anywhere in the image.
```

---

## Poznámka k opakovanému generování

Když se ti podaří šablona, se kterou jsi spokojený, **ulož si i přesný prompt a nástroj**, kterým
vznikla. Až budeš za měsíc dodělávat kapitolu 6, budeš potřebovat stejný vzhled — a z paměti se to
netrefí.
