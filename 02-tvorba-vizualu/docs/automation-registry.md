# Registr automatizace — Projekt 2: Tvorba vizuálního PDF (Fáze 3)

Živý přehled Skills, subagentů, hooků a loopů, které patří do tohoto projektu (design, sazba,
export PDF). Celkový přehled napříč všemi 3 projekty a rozhodnutí o rozpadu je v
`../docs/project-split-plan.md` (root) — sem patří jen detail vlastní tomuto projektu.

Zdroj procesu: `../plan.md` (root, Fáze 3).

> **⛔ Vizuální proces je od 2026-07-17 pozastavený a náhrada není rozhodnutá** — varianty
> v `brief-vizualni-proces.md`, rozhodnutí #1 v `../docs/stav-projektu.md`. Skill i agent níže
> popisují DOSAVADNÍ postup (Canva `poster` + Canva stock fotky), který se nepoužívá.

Legenda stavu: 🟢 vytvořeno · ⚪ naplánováno (zatím neexistuje) · 🟡 pozastaveno

## Skills

Umístění: `.claude/skills/<název>/SKILL.md`

| Skill | Účel | Fáze | Umístění | Stav |
|---|---|---|---|---|
| `/layout-guide` | Sazba textu + vizuálů do PDF šablony (Canva MCP) | 3 | `.claude/skills/layout-guide/` | 🟡 |

## Subagenti

Umístění: `.claude/agents/<název>.md`

| Agent | Účel | Fáze | Umístění | Stav |
|---|---|---|---|---|
| Design | Sestaví Canva design z hotových kapitol podle briefu, exportuje PDF | 3 | `.claude/agents/design.md` | 🟡 |

## Hooks

Zatím žádné pro tento projekt.

## Loops

Zatím žádné pro tento projekt.

## Vstup/výstup tohoto projektu

- **Vstup:** fact-checked text z Projektu 1 (`../01-tvorba-textu/content/<destinace>/text/*.md`)
  a k němu shot listy (`.../text/_shot-list/*.md`) + fotky. Fotky do Canva účtu nahrává vždy člověk
  sám (agent je nemůže nahrát za něj — `upload-asset-from-url` přijímá jen veřejné URL, viz
  `../docs/project-split-plan.md`). Odkud fotky pocházejí (AI vs. licencovaný stock), určí až
  rozhodnutí o variantě vizuálního procesu.
- **Výstup:** finální PDF produkt (`design/<destinace>/`) — vstup pro Projekt 3 (prodej/QA).

## Jak s tímto registrem pracovat

- Než se něco z výše uvedeného skutečně vytvoří, je to jen záměr (⚪) — neexistuje žádný soubor.
- Jakmile něco vytvořím, změním stav na 🟢 a doplním poznámku, pokud se od návrhu odchýlí.
