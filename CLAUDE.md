# dp-prirucka

Produktová řada digitálních turistických průvodců (PDF e-booky s tipy a "deep knowledge"). Každá
destinace = samostatný prodejný produkt a skládá se ze dvou souborů: **příručky** (8 kapitol) a
**rychlotaháčku do kapsy** (týchž 8 kapitol zhuštěných, 1 strana A4 na kapitolu). Co přesně
zákazník dostává, je v `01-tvorba-textu/docs/brief-<destinace>.md`. Prodej přes vlastní web + Meta/Google Ads. Obsah i data
od nuly.

**Aktuální pilot: Lloret de Mar a okolí.** Albánie byla původní pilotní destinace, ale je
pozastavená (text má neuzavřené nálezy z fact-checku) — Lloret ji předběhl s čistým výsledkem.
Detail a aktuální stav napříč fázemi je v `docs/stav-projektu.md`.

Tento root je od 2026-07-17 jen **řídící složka** — reálná práce žije ve 3 samostatných
projektových podsložkách, rozdělených podle fáze procesu. Každá podsložka má vlastní `CLAUDE.md`,
`.claude/agents+skills+hooks/` a `docs/automation-registry.md` — informace se mezi nimi
neduplikují, jen na sebe odkazují.

## 3 projekty

| Složka | Fáze | Co dělá |
|---|---|---|
| `01-tvorba-textu/` | 0+1+2 | Výběr destinace, research, psaní kapitol. Funguje dobře. |
| `02-tvorba-vizualu/` | 3 | Design a sazba do PDF. **Blokováno otevřeným rozhodnutím** o vizuálním procesu. |
| `03-komercializace/` | 4–9 | QA, prodejní web, PPC, post-launch, škálování. Zatím jen naplánováno. |

## Které dokumenty v rootu k čemu jsou

| Soubor | Role | Kdy se mění |
|---|---|---|
| `plan.md` | **Proces** — kompletní popis Fází 0–9 a co v nich lze automatizovat. Destinačně neutrální. | Zřídka — jen když se mění samotný postup. |
| `docs/stav-projektu.md` | **Stav** — kde přesně jsme, co je hotové, co je další krok, otevřená rozhodnutí. | Průběžně, po každém dokončeném kroku. |
| `docs/project-split-plan.md` | **Rozhodnutí** o rozpadu na 3 projekty a jejich vzájemné napojení. | Zřídka — jen při změně architektury projektů. |

Dokud fyzický rozpad na 3 samostatné repozitáře neproběhne, projekty na sebe odkazují relativními
cestami (`../01-tvorba-textu/...` apod.) — viz "Napojení na ostatní projekty" v CLAUDE.md každého
projektu.

## Konvence platné napříč projekty

- Nová destinace se zakládá zkopírováním `_template/` v příslušném projektu (research/text v
  Projektu 1, assets v Projektu 2) — viz `01-tvorba-textu/content/_template/README.md`.
- Vygenerované binárky (PDF exporty, obrázky z designu) se negitují — zdroj pravdy je text/design
  zdroje, PDF je build output. Výjimka: `02-tvorba-vizualu/design/inspirace/` (moodboard) a
  `design/*/wireframes/` (návrhové kostry) jsou zdroje, ty se gitují.
- Každá informace má **jedno** místo. Než něco někam připíšeš, ověř podle tabulky výše a podle
  sekce "Co se nemá opakovat" v `docs/project-split-plan.md`, jestli to nepatří jinam.
- **Cesty v dokumentech se píšou od kořene projektu, ne od umístění souboru.** V dokumentu uvnitř
  `02-tvorba-vizualu/docs/` tedy `docs/design-brief-albanie.md` znamená soubor ve stejné složce,
  `.claude/agents/design.md` je o úroveň výš a `../01-tvorba-textu/...` míří do vedlejšího projektu.
  V dokumentech v tomto rootu se stejně tak čte `docs/...` a `plan.md` od `dp-prirucka/`.

## Zásada práce s destinacemi

Plán počítá s pilotem na **jedné** destinaci — teprve po jeho vyhodnocení (Fáze 9) se škáluje na
další. Rozpracované destinace mimo aktuální pilot se nerozšiřují, jen se drží zmrazené; jejich stav
je v `docs/stav-projektu.md`.
