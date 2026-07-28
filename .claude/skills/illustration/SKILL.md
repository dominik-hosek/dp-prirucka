---
name: illustration
description: Generuje sérii ilustrací a obálku pro průvodce se zachováním jednotného stylu napříč celou destinací. Použij, když je potřeba vyrobit obrázky ke kapitolám, obálku, nebo přegenerovat vizuál, který neprošel kontrolou konzistence. Staví na skillu guide-style; v ručním režimu produkuje promptové soubory, které se vkládají do appky Gemini.
---

# illustration

Vyrábí obrazovou sérii jedné destinace. Klíčová vlastnost není kvalita jednoho
obrázku, ale **to, že 30 obrázků vypadá jako práce jednoho fotografa**.

## Předpoklady

1. Načti `guide-style/SKILL.md` a profil destinace `guide-style/destinations/<slug>.md`.
2. Načti `guide-style/references/prompt-formula.md`.
3. Zjisti, v jakém režimu se generuje — viz níže.

## Režimy generování

### Ruční (aktuální pilotní režim)

Obrázky vyrábí člověk v appce Gemini (Nano Banana Pro) na svém předplatném.
Skill negeneruje obrázky, ale **připravuje promptové soubory a přebírá výsledky**.

Postup:

1. Skill zapíše prompty do `content/<slug>/assets/prompts/NN-<popis>.md`.
2. Člověk je po jednom vloží do appky, nastaví poměr stran, vygeneruje.
3. Stažené obrázky uloží do `content/<slug>/assets/illustrations/NN-<popis>.png`
   — **stejné číslo a slug jako prompt**, jinak se pár rozpadne.
4. Skill při dalším běhu zkontroluje, co dorazilo, a doplní manifest.

### Automatický (kdyby se přešlo na API)

Stejné prompty, jen se posílají programově a krok 2–3 odpadá. Formule i manifest
zůstávají beze změny — proto je systém napsaný takhle.

## Kotevní obrázek — jak se drží styl

Konzistence série stojí a padá s **kotvou**.

1. Jako první se vygeneruje obrázek `01` — obvykle nejtypičtější krajinná scéna
   destinace. Na něm se ladí grading, dokud nesedí k paletě.
2. Schválený `01` se stane **kotvou celé série** a zapíše se do manifestu.
3. U každého dalšího promptu se v ručním režimu **do appky přiloží kotva**
   a připojí věta:

   > Zachovej stejný fotografický styl, barevný grading, atmosféru a filmový
   > kontrast jako v přiloženém obrázku. Změň pouze scénu.

4. Když se série po ~10 obrázcích začne rozjíždět (typicky se plíživě otepluje),
   nekotvi na poslední obrázek, ale **vždy zpátky na `01`**. Řetězení kotev
   drift zesiluje, kotvení na originál ho drží.

## Číslování a pojmenování

```
content/<slug>/assets/
  prompts/          NN-popis.md          prompt (verzovaný, zdroj pravdy)
  illustrations/    NN-popis.png         výsledný obrázek
  cover/            00-obalka.png        obálka
  asset-manifest.md                      přehled celé série
```

- `NN` je dvojmístné pořadové číslo, `00` je vždy obálka.
- `popis` je krátký slug bez diakritiky: `03-cami-de-ronda-utes`.
- Přegenerovaná verze **přepisuje** původní soubor; historii drží git.

## Manifest série

`content/<slug>/assets/asset-manifest.md` je přehled, co existuje a v jakém stavu.
Skill ho udržuje aktuální při každém běhu.

| # | Soubor | Kapitola | Formát | Kotva | Stav |
|---|---|---|---|---|---|
| 00 | `cover/00-obalka.png` | — | 1:1.414 | — | ⚪ čeká |
| 01 | `illustrations/01-....png` | 1 | 1:1.414 | **kotva série** | ⚪ čeká |

Stavy: ⚪ čeká na vygenerování · 🟡 vygenerováno, nezkontrolováno · 🟢 schváleno ·
🔴 vráceno k přegenerování (s důvodem)

## Jak se odvodí shot list

Z osnovy kapitol v `content/<slug>/text/` (nebo z osnovy v briefu, dokud text
neexistuje):

1. **Každá kapitola dostane jednu celostránkovou ilustraci** — otevírací obraz.
2. Kapitoly s vlastním dějem (itineráře, aktivity) dostanou navíc 1–2 pásové
   nebo půlstránkové.
3. Obálka je vlastní scéna, ne opakování ilustrace z kapitoly.
4. Scéna se odvozuje z **fotografického slovníku v profilu destinace**, ne
   z volné fantazie — a každý motiv se použije nejvýš jednou.

Cíl pro pilotní rozsah: **obálka + 8–12 celostránkových + 4–6 doplňkových.**

## Kontrola před předáním do sazby

Než se obrázek označí 🟢, projde kontrolou z `guide-style` (grading, sezóna,
ohnisko, absence textu, dojem jednoho fotografa). V plné smyčce to dělá subagent
`consistency-reviewer`; když neběží, projdi seznam ručně.

Obrázek, který obsahuje jakýkoli text, jde **vždy** zpátky — text do obrázků
v tomhle produktu nepatří.
