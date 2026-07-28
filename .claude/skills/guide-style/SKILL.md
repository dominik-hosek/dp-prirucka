---
name: guide-style
description: Vizuální DNA průvodce — paleta, typografie, fotografický jazyk a promptové šablony pro generování obrázků. Použij vždy, když se pro nějakou destinaci tvoří obálka, ilustrace, mapa, ikona nebo infografika, nebo když je potřeba zkontrolovat, že nový vizuál sedí ke stylu série. Ostatní vizuální skilly (illustration, map-infographic, layout) si odsud berou závazné hodnoty — nikdy je nepiš natvrdo jinam.
---

# guide-style

Jediný zdroj pravdy pro vizuální stránku produktové řady. Systém je **destinačně nezávislý**: neměnné jádro (jak se staví prompt, jaké má produkt proporce, co je zakázáno) žije tady, zatímco barvy, motivy a fotografický slovník jedné destinace žijí v profilu v `destinations/`.

## Jak to použít

1. Zjisti destinaci a načti její profil: `destinations/<slug>.md`. Když neexistuje, založ ho zkopírováním `destinations/_template.md` a vyplň podle briefu v `docs/brief-<slug>.md`.
2. Načti `references/prompt-formula.md` — tam je závazná 5-komponentová formule a seznam zákazů.
3. Slož prompt: **jádro (tento soubor) + profil destinace + konkrétní scéna**.
4. Prompt nikdy nepředávej dál jako holý text uživatele. Vždy projde touto vrstvou.

## Nepřekročitelné pravidlo

**Syrový text průvodce se nikdy neposílá do generátoru obrázků.** Kapitola z `content/<dest>/text/` je vstup pro *tebe*, ne pro model. Tvoje práce je z ní vytěžit scénu a přeložit ji do 5-komponentové formule. Když do image modelu pošleš odstavec průvodce, dostaneš doslovnou ilustraci textu — tedy přesně ten generický „AI look", kterému se vyhýbáme.

## Neměnné jádro systému

Platí pro každou destinaci. Profil destinace tyhle hodnoty **nesmí přepsat** — smí je jen naplnit obsahem.

### Formát a proporce

| Účel | Poměr | Cílové rozlišení |
|---|---|---|
| Obálka | 1:1.414 (A4 na výšku) | min. 2480 × 3508 px |
| Celostránková ilustrace | 1:1.414 | min. 2480 × 3508 px |
| Půlstránková (na šířku) | 3:2 | min. 2400 × 1600 px |
| Pásová (přes sloupce) | 16:9 | min. 2400 × 1350 px |
| Mapa / infografika | 4:3 nebo 1:1.414 | min. 2000 px na delší straně |
| Ikona | 1:1 | vektor (SVG), ne raster |

Generuje se vždy **na 1K/2K**, ne 4K — do A4 tisku při 300 DPI to stačí a 4K je zbytečně drahé i pomalé.

### Fotografický jazyk (invarianty série)

Tohle drží sérii pohromadě napříč destinacemi i kapitolami:

- **Reportážní, ne reklamní.** Scéna vypadá zastižená, ne naaranžovaná. Blíž magazínu Sidetracked než katalogu cestovky.
- **Ohnisko 35 mm** jako výchozí (24 mm pro krajinu, 85 mm pro detail). Žádný rybí oko, žádné extrémní zkreslení.
- **Přirozené světlo.** Zlatá hodina a modrá hodina jsou preferované; polední ostré slunce jen když je to záměr (pláž, poušť).
- **Člověk v záběru je malý a anonymní** — měřítko krajiny, ne portrét. Nikdy rozpoznatelné obličeje.
- **Žádný HDR, žádná přesycená obloha, žádný stock úsměv.** Kontrast spíš filmový, stíny smí být zavřené.
- **Barevný grading vždy k paletě destinace**, ne k výchozímu vzhledu modelu.

### Zakázané prvky

Patří do negativního promptu u každé generace:

- text, písmena, nápisy, cedule s čitelným textem, watermark, logo (text do obrázků přidává až `layout` jako skutečnou typografii — viz `map-infographic`)
- lidé v popředí s rozpoznatelnou tváří, portréty
- stock-photo estetika, přesycené barvy, HDR halo, plastová kůže
- koláže, rámečky, okraje, více panelů v jednom obrázku
- moderní turistický balast, kde nemá být (odpadky, davy, reklamní bannery) — pokud to není záměr scény

### Typografický systém

Fonty jsou **společné pro celou řadu** — mění se barvy, ne písmo. Drží to značku napříč destinacemi.

| Role | Font | Řez | Použití |
|---|---|---|---|
| Titulky | Archivo | 700–900, Expanded | obálka, názvy kapitol |
| Text | Source Serif 4 | 400 / 600 | běžný text průvodce |
| Popisky a data | Inter | 400–600 | mapy, infografiky, popisky obrázků, čísla stran |

Fonty leží v `design/fonts/` a jsou součástí repa, aby byl PDF build reprodukovatelný. Všechny tři mají plnou českou i slovenskou diakritiku (ě š č ř ž ý á í é ů ú ň ť ď ó ľ ĺ ŕ).

## Profil destinace

Profil je krátký a konkrétní. Obsahuje:

- **Paletu** — 5–7 barev s hex kódy a rolí (primární, sekundární, akcent, doplňky, text, papír).
- **Fotografický slovník** — 8–15 konkrétních motivů destinace, kterými se plní komponenta *Subject*.
- **Světlo a atmosféru** — co je pro místo typické (ostré středomořské poledne vs. mlha v horách).
- **Sezónu a čas** — kdy se scény odehrávají, ať série nemíchá léto se zimou.
- **Zakázané klišé** — co konkrétně u téhle destinace nechceme (u Lloretu např. párty, opilí turisté, neónové bary).

Aktuální profily: `destinations/lloret-de-mar.md` (pilot).

## Kontrola konzistence

Než se vizuál přijme do série, projde tímhle:

1. Sedí barevný grading k paletě destinace? (Vzorkuj dominantní barvy a porovnej s hex kódy profilu.)
2. Sedí denní doba a sezóna k ostatním obrázkům v sérii?
3. Odpovídá ohnisko a odstup od objektu deklarovanému v promptu?
4. Není v obrázku text? (Pokud ano, jde ven — text řeší `layout`.)
5. Vypadá to jako z téhož fotografa jako obrázek #1 v sérii?

Když cokoli neprojde, vizuál se přegeneruje s upraveným promptem. Detailně to řeší subagent `consistency-reviewer` (Fáze 4).
