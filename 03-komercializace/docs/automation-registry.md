# Registr automatizace — Projekt 3: Komercializace a propagace (Fáze 4–9)

Živý přehled Skills, subagentů, hooků a loopů, které patří do tohoto projektu (QA, prodejní web,
PPC příprava/spuštění, post-launch péče, škálování). Celkový přehled napříč všemi 3 projekty a
rozhodnutí o rozpadu je v `../docs/project-split-plan.md` (root) — sem patří jen detail vlastní
tomuto projektu.

Zdroj procesu: `../plan.md` (root, Fáze 4–9).

Legenda stavu: 🟢 vytvořeno · ⚪ naplánováno (zatím neexistuje)

## Skills

Umístění: `.claude/skills/<název>/SKILL.md`

| Skill | Účel | Fáze | Umístění | Stav |
|---|---|---|---|---|
| `/qa-checklist` | Kontrolní seznam před vydáním produktu | 4 | `.claude/skills/qa-checklist/` | ⚪ |
| `/build-landing-page` | Generování struktury/copy prodejní stránky | 5 | `.claude/skills/build-landing-page/` | ⚪ |
| `/generate-ad-variants` | Sada headlinů/textů/CTA pro PPC A/B test | 6 | `.claude/skills/generate-ad-variants/` | ⚪ |
| `/weekly-ads-report` | Pravidelný report výkonu kampaní | 7 | `.claude/skills/weekly-ads-report/` | ⚪ |
| `/new-destination-guide` | Zastřešující skill: research→psaní→design→QA pro novou destinaci (orchestruje i Projekty 1+2) | 9 | `.claude/skills/new-destination-guide/` | ⚪ |
| `/evaluate-pilot` | Sběr dat napříč fázemi + vyhodnocení pilotu | 9 | `.claude/skills/evaluate-pilot/` | ⚪ |

## Subagenti

Umístění: `.claude/agents/<název>.md`

| Agent | Účel | Fáze | Umístění | Stav |
|---|---|---|---|---|
| Copywriter (landing page) | Prodejní texty webu z "value proof" | 5 | `.claude/agents/copywriter.md` | ⚪ |
| Ads Copywriter | Varianty reklamních textů/headlinů | 6 | `.claude/agents/ads-copywriter.md` | ⚪ |
| Campaign Analyst | Interpretuje metriky kampaní, navrhuje úpravy | 7 | `.claude/agents/campaign-analyst.md` | ⚪ |
| Pilot Analyst | Porovnává pilot proti cílům z Fáze 0, navrhuje úpravy procesu | 9 | `.claude/agents/pilot-analyst.md` | ⚪ |

## Hooks

Zatím žádné pro tento projekt.

## Loops

| Loop | Interval | Účel | Fáze | Stav |
|---|---|---|---|---|
| Weekly ads report | týdně | Pravidelný report výkonu PPC kampaní | 7 | ⚪ |
| Pilot log | týdně (jen v testovacím období pilotu) | Průběžný sběr metrik pilotu pro pozdější vyhodnocení | 9 | ⚪ |
| Revalidace cen/otevíracích dob | čtvrtletně | Post-launch spouštěč, samotná revalidace dat žije v Projektu 1 (`../01-tvorba-textu/docs/automation-registry.md`) | 8 | ⚪ |

## Vstup tohoto projektu

Finální PDF produkt z Projektu 2 (`../02-tvorba-vizualu/design/<destinace>/`) + "value proof" z QA.

## Jak s tímto registrem pracovat

- Než se něco z výše uvedeného skutečně vytvoří, je to jen záměr (⚪) — neexistuje žádný soubor.
- Jakmile něco vytvořím, změním stav na 🟢 a doplním poznámku, pokud se od návrhu odchýlí.
