# 03-komercializace

Projekt 3 ze 3 (viz `../docs/project-split-plan.md` v rootu `dp-prirucka`) — pokrývá Fáze 4–9:
QA a finalizace produktu, prodejní web, příprava a spuštění PPC kampaní, post-launch péče a
škálování na další destinace.

Celý fázový proces je popsaný v `../plan.md`. Živý stav skills/agentů/loopů patřících sem (většina
zatím jen naplánovaná, ⚪) je v `docs/automation-registry.md`.

## Struktura

```
landing-page/    # Fáze 5 – copy a struktura prodejní stránky
ads/             # Fáze 6 – reklamní kreativy a texty pro Meta/Google Ads
docs/            # QA checklisty, pilot log, vyhodnocení (zatím jen automation-registry.md)
```

Složka `.claude/` tu zatím neexistuje — žádný agent ani skill této fáze není vytvořený. Až první
vznikne, založí se `.claude/agents/` resp. `.claude/skills/` podle `docs/automation-registry.md`.

## Vstup z ostatních projektů

- Z Projektu 1 (`../01-tvorba-textu/`): `docs/open-questions-<destinace>.md` (co doověřit v QA před
  vydáním), `docs/brief-<destinace>.md` (persona/cena pro landing page a ads).
- Z Projektu 2 (`../02-tvorba-vizualu/`): finální PDF v `design/<destinace>/`.

## Stav

Celý tento projekt je zatím jen naplánovaný (viz `docs/automation-registry.md`) — nic z něj
neexistuje jako soubor. Nejbližší reálný krok je Fáze 4 (QA), ta ale čeká na hotové PDF z Projektu
2. Aktuální stav a pořadí kroků napříč všemi projekty je v `../docs/stav-projektu.md`.
