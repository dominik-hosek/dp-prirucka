# Registr automatizace — Projekt 2: Tvorba vizuálního PDF (Fáze 3)

Živý přehled Skills, subagentů, hooků a loopů, které patří do tohoto projektu (design, sazba,
export PDF). Celkový přehled napříč všemi 3 projekty a rozhodnutí o rozpadu je v
`../docs/project-split-plan.md` (root) — sem patří jen detail vlastní tomuto projektu.

Zdroj procesu: `../plan.md` (root, Fáze 3).

> **Postup rozhodnutý 2026-07-29.** Stránky PDF generuje člověk v Nano Banana 2 / GPT Image podle
> promptů připravených agentem — viz `prompt-guide.md`. Canva skill i agent níže jsou **odstavené**;
> zůstávají jako historický záznam, nespouštět.

Legenda stavu: 🟢 vytvořeno · ⚪ naplánováno (zatím neexistuje) · ⚫ odstaveno (nepoužívat)

## Jak je Fáze 3 automatizovaná

Tenhle projekt je záměrně z velké části **ruční** — generování běží v nástrojích, ke kterým agent
nemá přístup (Nano Banana 2, GPT Image; obojí předplacené člověkem). Dělba práce:

| Kdo | Co dělá |
|---|---|
| 🤖 Agent | Připraví prompty ze shot listů a textu kapitol, udržuje styl blok, dodá přesné znění textu k vložení do šablon |
| 🙋 Člověk | Generuje stránky, vybírá z variant, kontroluje text slovo po slovu, vkládá text do šablon, skládá PDF |

Není tu tedy skill ani subagent, který by Fázi 3 „spustil" — výstupem agenta jsou soubory
v `prompts/`, ne hotové stránky.

## Skills

Umístění: `.claude/skills/<název>/SKILL.md`

| Skill | Účel | Fáze | Umístění | Stav |
|---|---|---|---|---|
| `/layout-guide` | Sazba textu + vizuálů do PDF šablony (Canva MCP) | 3 | `.claude/skills/layout-guide/` | ⚫ odstaveno 2026-07-29 |

## Subagenti

Umístění: `.claude/agents/<název>.md`

| Agent | Účel | Fáze | Umístění | Stav |
|---|---|---|---|---|
| Design | Sestaví Canva design z hotových kapitol podle briefu, exportuje PDF | 3 | `.claude/agents/design.md` | ⚫ odstaveno 2026-07-29 |

## Hooks

Zatím žádné pro tento projekt.

## Loops

Zatím žádné pro tento projekt.

## Vstup/výstup tohoto projektu

- **Vstup:** fact-checked text z Projektu 1 (`../01-tvorba-textu/content/<destinace>/text/*.md`)
  a k němu shot listy (`.../text/_shot-list/*.md`) — shot list je podklad, ze kterého se píšou
  prompty.
- **Mezivýstup agenta:** prompty v `prompts/<destinace>/` + šablony v `prompts/_sablony-stranek.md`.
- **Vygenerované stránky** (`design/<destinace>/pages/`) se **verzují**, i když jsou to obrázky —
  nejsou reprodukovatelné, stejný prompt podruhé vrátí jiný výsledek.
- **Výstup:** finální PDF produkt (`design/<destinace>/`) — vstup pro Projekt 3 (prodej/QA).

## Jak s tímto registrem pracovat

- Než se něco z výše uvedeného skutečně vytvoří, je to jen záměr (⚪) — neexistuje žádný soubor.
- Jakmile něco vytvořím, změním stav na 🟢 a doplním poznámku, pokud se od návrhu odchýlí.
