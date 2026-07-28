# Registr automatizace — Projekt 1: Tvorba textu (Fáze 0+1+2)

Živý přehled Skills, subagentů, hooků a loopů, které patří do tohoto projektu (výběr destinace,
research, psaní kapitol). Celkový přehled napříč všemi 3 projekty a rozhodnutí o rozpadu je
v `../docs/project-split-plan.md` (root) — sem patří jen detail vlastní tomuto projektu.

Zdroj procesu: `../plan.md` (root, Fáze 0/1/2).

Legenda stavu: 🟢 vytvořeno · ⚪ naplánováno (zatím neexistuje)

## Skills

Umístění: `.claude/skills/<název>/SKILL.md`

| Skill | Účel | Fáze | Umístění | Stav |
|---|---|---|---|---|
| `/validate-destination` | Research poptávky/konkurence pro výběr destinace | 0 | `.claude/skills/validate-destination/` | ⚪ |
| `/research-topic` | Sběr dat k jednomu tématu/kapitole destinace + zdroje | 1 | `.claude/skills/research-topic/` | 🟢 |
| `/write-chapter` | Napsání kapitoly z research databáze (ne z paměti modelu) | 2 | `.claude/skills/write-chapter/` | 🟢 |

## Subagenti

Umístění: `.claude/agents/<název>.md`

| Agent | Účel | Fáze | Umístění | Stav |
|---|---|---|---|---|
| Market Research | Prohledá web, shrne poptávku/konkurenci/mezery na trhu | 0 | `.claude/agents/market-research.md` | ⚪ |
| Researcher (per kapitola) | Paralelní sběr dat k jedné kapitole osnovy | 1 | `.claude/agents/researcher.md` | 🟢 |
| Writer | Píše kapitoly z research databáze | 2 | `.claude/agents/writer.md` | 🟢 |
| Fact-Checker | Nezávisle ověřuje tvrzení v textu proti research datům | 2 | `.claude/agents/fact-checker.md` | 🟢 |
| Shot-List-Creator | Nezávisle navrhuje shot list vizuálů k jedné hotové kapitole, jen z jejího textu | 2 | `.claude/agents/shot-list-creator.md` | 🟢 |

## Hooks

Umístění: skript v `.claude/hooks/`, definice ve **dvou** `settings.json` — v `.claude/settings.json`
tohoto projektu a zároveň v `../.claude/settings.json` (root). Důvod: Claude Code načítá hooky jen
z kořene složky, ve které je spuštěný. Když se pracuje z řídící složky `dp-prirucka`, nested
definice se nenačte (ověřeno testem 2026-07-28) — proto ta v rootu. Vždycky se uplatní právě jedna
podle toho, kde je session otevřená, takže hook neběží dvakrát. Po fyzickém rozdělení na samostatné
repozitáře root definice zanikne.

| Hook | Spouští se při | Účel | Fáze | Umístění | Stav |
|---|---|---|---|---|---|
| Fact-check po uložení kapitoly | `PostToolUse` (Write\|Edit) na souboru v `content/*/text/*.md` | Dá Claudovi v session najevo, ať spustí Fact-Checker subagenta pro danou kapitolu, pokud pro ni ještě není aktuální fact-check | 2 | `.claude/hooks/fact-check-on-save.js` | 🟢 |
| Shot-list po dokončení fact-checku destinace | `PostToolUse` (Write\|Edit) na souboru v `content/*/text/_fact-check/*.md` | Když mají všechny kapitoly destinace `Stav: OK` a shot-list chybí/je starší než text, dá Claudovi v session najevo, ať spustí Shot-List-Creator subagenta pro každou kapitolu destinace | 2 | `.claude/hooks/fact-check-on-save.js` (stejný skript, druhá větev) | 🟢 |

## Známá omezení

- **Fact-checker nekonverguje na jeden běh.** Ověřeno 2026-07-28 na kapitole 01 Lloretu: čtyři po
  sobě jdoucí běhy nad prakticky stejným textem našly pokaždé jinou sadu nálezů (kolo 1 měnu u eSIM,
  kolo 2 cenu autobusu, kolo 3 tvrzení o placení kartou, kolo 4 chybějící výhradu u slabého zdroje).
  `Stav: OK` proto neznamená "text je čistý", jen "tenhle běh nic nenašel". Má to dva důsledky:
  u důležité kapitoly se vyplatí pustit fact-check víckrát, a `Stav: OK` jako spouštěč shot listů
  (hook níže) je spíš procesní milník než záruka kvality.
- Pomáhá dát agentovi v promptu explicitní pokyn projít kapitolu systematicky sekci po sekci —
  bez něj má tendenci prohledat jen část textu.

## Loops

| Loop | Interval | Účel | Fáze | Stav |
|---|---|---|---|---|
| Revalidace cen/otevíracích dob | čtvrtletně | Kontrola, že vydaný obsah nezastarává (spouštěč navazuje na post-launch péči v Projektu 3, Fáze 8) | 1 / 8 | ⚪ |
| Zpracování zbývajících kapitol | dokud nejsou všechny hotové | Postupné psaní kapitol přes `/write-chapter` | 2 | ⚪ |

## Výstup tohoto projektu

Fact-checked text kapitol v `content/<destinace>/text/*.md` a k nim odpovídající shot listy v
`content/<destinace>/text/_shot-list/*.md` — oba vstup pro Projekt 2 (vizuální PDF). Shot-listy
vznikají automaticky až poté, co jsou všechny kapitoly destinace fact-checked na `Stav: OK` (viz
hooky výše), takže Projekt 2 je nemusí čekat ručně. Dokud jsou projekty v jednom repu, Projekt 2 na
tuto cestu odkazuje relativně (`../01-tvorba-textu/content/<destinace>/text/`); po fyzickém
rozdělení do samostatných repozitářů půjde o ruční/skriptovaný hand-off hotových kapitol.

## Jak s tímto registrem pracovat

- Než se něco z výše uvedeného skutečně vytvoří, je to jen záměr (⚪) — neexistuje žádný soubor.
- Jakmile něco vytvořím, změním stav na 🟢 a doplním poznámku, pokud se od návrhu odchýlí.
