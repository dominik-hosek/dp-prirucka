# Rozpad projektu na 3 samostatné celky (rozhodnuto 2026-07-17, fyzicky provedeno 2026-07-17)

Tohle je zdroj pravdy pro rozhodnutí rozdělit `dp-prirucka` na 3 nezávislé projekty. Fyzická
reorganizace složek (`01-tvorba-textu/`, `02-tvorba-vizualu/`, `03-komercializace/`) proběhla
2026-07-17 — root `dp-prirucka` je teď jen řídící složka, veškerý obsah/skills/agenti/hooky/loopy
žijí uvnitř příslušné projektové podsložky. Repozitář (git) zůstává zatím jeden společný — teprve
až se ukáže potřeba, rozdělí se i na 3 samostatné repozitáře. Ostatní soubory (CLAUDE.md,
automation-registry.md v každém projektu, design brief, skills/agents) na tento dokument jen
odkazují, aby se stejná informace neduplikovala na více místech.

## Proč rozpad

Tři fáze procesu mají zásadně jiný charakter práce (obsahová vs. vizuální vs. obchodní) a jiné
tempo iterace, takže dává smysl je oddělit i jako samostatné pracovní kontexty, ne je řešit
v jednom prompt-scope.

## Mapování na fáze z `plan.md`

| # | Složka | Fáze | Stav |
|---|---|---|---|
| 1 | **`01-tvorba-textu/`** | Fáze 0 + 1 + 2 (research, sběr dat, psaní kapitol) | Funguje dobře, beze změny. Zdroj pravdy: `content/<destinace>/research/` → `text/` uvnitř této složky. |
| 2 | **`02-tvorba-vizualu/`** | Fáze 3 (design, sazba, export) | **Blokováno otevřeným rozhodnutím** — viz sekce níže. Existující `docs/design-brief-<destinace>.md`, `.claude/skills/layout-guide/`, `.claude/agents/design.md` popisují DOSAVADNÍ (Canva-stock-foto) přístup, který je pozastavený. |
| 3 | **`03-komercializace/`** | Fáze 4–9 (QA, prodejní web, PPC příprava/spuštění, post-launch, škálování) | Zatím z velké části naplánováno, ne postaveno — viz `docs/automation-registry.md` uvnitř této složky. |

Projekt 1 je vstupem (výstup = fact-checked text) pro projekt 2, jehož výstup (finální PDF) je
zase vstup pro projekt 3. Dokud je vše v jednom repu, tohle napojení funguje přes relativní cesty
(`../01-tvorba-textu/...` apod.) zdokumentované v CLAUDE.md a automation-registry.md každého
projektu — až se projekty fyzicky rozdělí i na samostatné repozitáře, nahradí se ručním/
skriptovaným hand-off krokem.

## Fáze 3 — vizuální proces (rozhodnuto 2026-07-29)

**Stránky PDF generuje člověk v Nano Banana 2 / GPT Image podle promptů, které připraví agent.**
Canva ani jiný sazeč se nepoužívá. Agent do generování nevstupuje — nemá k těmto nástrojům přístup,
jeho výstupem jsou prompty a text k vložení.

Zadání je minimální: modelu se přiloží 4 vzorové inspirace a hotový text kapitoly a nechá se, ať si
rozvržení stránky zvolí sám. Ověřeno 2026-07-29 — vzhled i česká diakritika vycházejí spolehlivě,
layout si model volí rozumně podle délky textu.

**Kde je riziko:** ne v písmenkách, ale v obsahu. Model si dovolí text potichu zkrátit nebo změnit
předložku, aniž by to bylo na stránce vidět. Proto je povinným krokem **porovnání vygenerovaného
textu proti zdrojové kapitole** — k tomu slouží kontrolní listy v `02-tvorba-vizualu/kontrola/`.

Detail postupu a kontrolní seznamy: `02-tvorba-vizualu/docs/prompt-guide.md`.

Analýza, ze které se rozhodovalo (varianty A/B/C), zůstává v
`02-tvorba-vizualu/docs/brief-vizualni-proces.md` jako historický záznam — zvolený postup je čtvrtá
cesta, která v ní nebyla, protože počítá s nástroji, které má člověk předplacené.

### Historie: proč se opustil původní postup

Dosavadní přístup (Canva `poster` design_type + Canva vlastní stock fotky, zdokumentovaný
v `02-tvorba-vizualu/docs/design-brief-albanie.md`) je **pozastavený** — narazil na tvrdé limity
Canva MCP API (needitovatelná hero sekce, `merge-designs` nefunguje na unbounded designy,
`format_text` neumí letter-spacing) a hlavně na obsahový problém: fotku, kterou si nástroj vybere
sám bez cíleného zadání, spojuje s destinací jen podpis pod ní.

Zvažovaly se tři varianty (A – dál automatizovat přes Canva MCP, B – hybrid: wireframe + rozlišení
místopisných/náladových fotek + ruční sazba, C – opustit Canvu pro DTP nástroj), rozepsané
v `02-tvorba-vizualu/docs/brief-vizualni-proces.md`. Rozhodnutí padlo mimo ně — na generování
stránek ve vlastních předplacených nástrojích, viz výše.

Z Canva analýzy zůstává v platnosti jedno zjištění pro případ, že by se ke Canvě někdy vracelo:
**fotky do Canva účtu musí nahrát člověk sám**, nástroj `upload-asset-from-url` přijímá jen veřejně
dostupné URL.

**Status existujícího v2 proofu (cover + kapitola 1 Albánie, Canva stock fotky):** technicky
hotový a funkční, ale zmrazený — nerozšiřuje se a novým postupem se nahrazuje.

## Co se v žádném z výše uvedených dokumentů nemá opakovat

- Detailní popis fází 0–9 → jen `plan.md` (root).
- Kde v procesu právě jsme, stav destinací, otevřená rozhodnutí a další krok → jen
  `docs/stav-projektu.md` (root).
- Živý stav toho, co je 🟢 vytvořeno / ⚪ naplánováno z automatizace → jen
  `docs/automation-registry.md` uvnitř příslušné projektové složky (každý projekt má vlastní,
  nesdílí se jeden společný).
- Detail Canva technického postupu a historie pokusů (v1/v2) → jen
  `02-tvorba-vizualu/docs/design-brief-<destinace>.md`.
- Analýza variant nového vizuálního procesu a doporučení → jen
  `02-tvorba-vizualu/docs/brief-vizualni-proces.md`.
- Rozhodnutí o rozpadu na 3 projekty a jejich vzájemné napojení → jen tento soubor.

## Fyzická reorganizace (provedeno 2026-07-17)

Přesunuto beze změny obsahu (jen cesty): `.claude/agents/{researcher,writer,fact-checker}.md` a
`.claude/skills/{research-topic,write-chapter}` → `01-tvorba-textu/`; `.claude/agents/design.md` a
`.claude/skills/layout-guide/` → `02-tvorba-vizualu/`; `content/<destinace>/{research,text}/` →
`01-tvorba-textu/content/`; `content/<destinace>/assets/` → `02-tvorba-vizualu/content/`;
`design/` → `02-tvorba-vizualu/design/`; `landing-page/` a `ads/` → `03-komercializace/`;
`docs/brief-<destinace>.md`, `open-questions-albanie.md`, `style-guide.md` → `01-tvorba-textu/docs/`;
`docs/design-brief-<destinace>.md` → `02-tvorba-vizualu/docs/`. Cesty uvnitř přesunutých
skills/agentů/dokumentů, které teď míří mezi projekty (hlavně layout-guide skill a design agent
čtoucí text z Projektu 1), byly přepsané na relativní `../01-tvorba-textu/...`.
