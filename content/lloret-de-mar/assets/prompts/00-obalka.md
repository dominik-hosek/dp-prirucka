# 00 — Obálka

Formát: **1:1.414 na výšku** · Model: Nano Banana Pro (appka Gemini) · Rozlišení: 2K

> Generuj až **po schválení kotvy `01`** a vždy s přiloženou kotvou.
> Obálka je vlastní scéna, ne opakování ilustrace z kapitoly.

## Prompt k vložení

```
Pohled z výšky na řetěz skalnatých zálivů Costa Bravy mizící v oparu, tyrkysové
mělčiny mezi tmavými útesy, piniový les spadající k vodě. Bez staveb v popředí.
Pozdní jaro.

Kompozice: objektiv 35 mm, pohled z vyvýšeného skalního bodu shora dolů na
pobřeží, linie zálivů vede oko do hloubky zprava doleva. Spodní dvě třetiny
nesou detail, horní třetina je otevřené moře a obloha — musí zůstat klidná
a tmavší, protože přes ni půjde velký titulek.

Styl: cestovatelská reportážní fotografie, estetika obálky magazínu.
Barevný grading do hluboké mořské modři #0E3A53 a tyrkysu #1B9AAA, skalní
stěny v teplé oranžové #E76F51, borovice tlumeně zelené #3F6B4F. Filmový
kontrast, zavřené stíny, jemné zrno.

Světlo: modrá hodina těsně po západu slunce, poslední teplý dosvit na horizontu,
moře už chladné a tmavé.

Technicky: poměr stran 1:1.414 na výšku, velká hloubka ostrosti.

Bez jakéhokoli textu, písmen, nápisů, log a vodoznaků. Bez lidí. Bez hotelů,
bez lehátek, bez davů. Bez stock estetiky, přesycených barev a HDR efektu.

Zachovej stejný fotografický styl, barevný grading, atmosféru a filmový kontrast
jako v přiloženém obrázku. Změň pouze scénu.
```

## Po vygenerování zkontroluj

- [ ] Horní třetina je tmavá a klidná — titulek v teplé bílé `#FAF7F0` tam bude čitelný
- [ ] Sedí ke kotvě `01` (stejný fotograf, stejná sezóna, stejný grading)
- [ ] Žádný text, žádná stavba, žádný člověk
- [ ] Rozlišení min. 2480 × 3508 px

## Sazba obálky

Titulek se **nesází do obrázku** — skládá ho `layout` jako skutečnou typografii:

- nadtitul „PRŮVODCE PRO OBJEVITELE" — Inter 600, prostrkání 0.22em
- titul „Lloret de Mar" — Archivo 900, wdth 118, 52 pt
- podtitul — Source Serif 4 kurzíva, 13 pt
- pod textem leží přechodová plocha `.stin`, aby byl titulek čitelný
