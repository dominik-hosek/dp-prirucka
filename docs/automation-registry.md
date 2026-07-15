# Registr automatizace

Živý přehled všech Skills, subagentů, hooků a loopů v projektu — co dělají, ke které fázi patří a kde přesně leží. Doplňuje se v okamžiku, kdy se daný kousek automatizace skutečně vytvoří (ne dopředu) — dokud řádek nemá stav `vytvořeno`, jde jen o záměr z plánu.

Zdroj procesu: `C:\Users\42073\.claude\plans\chci-vytvo-it-digi-ln-produkt-rosy-yeti.md`

Legenda stavu: 🟢 vytvořeno · ⚪ naplánováno (zatím neexistuje)

## Skills

Umístění: `.claude/skills/<název>/SKILL.md`

| Skill | Účel | Fáze | Umístění | Stav |
|---|---|---|---|---|
| `/validate-destination` | Research poptávky/konkurence pro výběr destinace | 0 | `.claude/skills/validate-destination/` | ⚪ |
| `/research-topic` | Sběr dat k jednomu tématu/kapitole destinace + zdroje | 1 | `.claude/skills/research-topic/` | 🟢 |
| `/write-chapter` | Napsání kapitoly z research databáze (ne z paměti modelu) | 2 | `.claude/skills/write-chapter/` | 🟢 |
| `/layout-guide` | Sazba textu + vizuálů do PDF šablony | 3 | `.claude/skills/layout-guide/` | ⚪ |
| `/qa-checklist` | Kontrolní seznam před vydáním produktu | 4 | `.claude/skills/qa-checklist/` | ⚪ |
| `/build-landing-page` | Generování struktury/copy prodejní stránky | 5 | `.claude/skills/build-landing-page/` | ⚪ |
| `/generate-ad-variants` | Sada headlinů/textů/CTA pro PPC A/B test | 6 | `.claude/skills/generate-ad-variants/` | ⚪ |
| `/weekly-ads-report` | Pravidelný report výkonu kampaní | 7 | `.claude/skills/weekly-ads-report/` | ⚪ |
| `/new-destination-guide` | Zastřešující skill: research→psaní→design→QA pro novou destinaci | 9 | `.claude/skills/new-destination-guide/` | ⚪ |
| `/evaluate-pilot` | Sběr dat napříč fázemi + vyhodnocení pilotu | 9 | `.claude/skills/evaluate-pilot/` | ⚪ |

## Subagenti

Umístění: `.claude/agents/<název>.md` (frontmatter: model, dostupné nástroje, systémový prompt/persona)

| Agent | Účel | Fáze | Umístění | Stav |
|---|---|---|---|---|
| Market Research | Prohledá web, shrne poptávku/konkurenci/mezery na trhu | 0 | `.claude/agents/market-research.md` | ⚪ |
| Researcher (per kapitola) | Paralelní sběr dat k jedné kapitole osnovy | 1 | `.claude/agents/researcher.md` | 🟢 |
| Writer | Píše kapitoly z research databáze | 2 | `.claude/agents/writer.md` | 🟢 |
| Fact-Checker | Nezávisle ověřuje tvrzení v textu proti research datům | 2 | `.claude/agents/fact-checker.md` | 🟢 |
| Design | Připravuje požadavky/prompty pro vizuály a layout | 3 | `.claude/agents/design.md` | ⚪ |
| Copywriter (landing page) | Prodejní texty webu z "value proof" | 5 | `.claude/agents/copywriter.md` | ⚪ |
| Ads Copywriter | Varianty reklamních textů/headlinů | 6 | `.claude/agents/ads-copywriter.md` | ⚪ |
| Campaign Analyst | Interpretuje metriky kampaní, navrhuje úpravy | 7 | `.claude/agents/campaign-analyst.md` | ⚪ |
| Pilot Analyst | Porovnává pilot proti cílům z Fáze 0, navrhuje úpravy procesu | 9 | `.claude/agents/pilot-analyst.md` | ⚪ |

## Hooks

Umístění: definice v `.claude/settings.json` (`hooks` sekce), skripty v `.claude/hooks/`

| Hook | Spouští se při | Účel | Fáze | Umístění | Stav |
|---|---|---|---|---|---|
| Fact-check po uložení kapitoly | uložení/úprava souboru v `content/*/text/` | Spustí Fact-Checker subagenta + kontrolu konzistence | 2 | `.claude/hooks/fact-check-on-save.*` | ⚪ |

## Loops

Spouští se přes `/loop` (interval nebo self-paced), definice promptu typicky v příslušném Skillu.

| Loop | Interval | Účel | Fáze | Stav |
|---|---|---|---|---|
| Revalidace cen/otevíracích dob | čtvrtletně | Kontrola, že vydaný obsah nezastarává | 1 / 8 | ⚪ |
| Zpracování zbývajících kapitol | dokud nejsou všechny hotové | Postupné psaní kapitol přes `/write-chapter` | 2 | ⚪ |
| Pilot log | týdně (jen v testovacím období pilotu) | Průběžný sběr metrik pilotu pro pozdější vyhodnocení | 9 | ⚪ |
| Weekly ads report | týdně | Pravidelný report výkonu PPC kampaní | 7 | ⚪ |

---

## Jak s tímto registrem pracovat

- Než se něco z výše uvedeného skutečně vytvoří, je to jen záměr (⚪) — neexistuje žádný soubor, nic se automaticky nespouští.
- Jakmile něco vytvořím, změním stav na 🟢 a doplním do tabulky odkaz/poznámku, případně stručně, co přesně dělá jinak než v plánu (pokud se od návrhu odchýlí).
- Tento soubor je tedy věrohodnější než samotný `plán` v otázce "co už reálně existuje" — plán popisuje záměr celého procesu, tento registr popisuje aktuální stav implementace.
