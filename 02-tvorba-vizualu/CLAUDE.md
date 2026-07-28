# 02-tvorba-vizualu

Projekt 2 ze 3 (viz `../docs/project-split-plan.md` v rootu `dp-prirucka`) — pokrývá Fázi 3:
proměnu hotového textu ve vizuálně kvalitní, prodejný PDF produkt.

Celý fázový proces je popsaný v `../plan.md`. Živý stav skills/agentů patřících sem je v
`docs/automation-registry.md`.

> **⛔ Tento projekt je blokovaný otevřeným rozhodnutím.** Dosavadní postup (Canva `poster`
> design_type + Canva vlastní stock fotky, zdokumentovaný v `docs/design-brief-albanie.md` a
> `.claude/skills/layout-guide/`) je od 2026-07-17 pozastavený kvůli limitům Canva MCP API a
> generickým fotkám. Čím se nahradí, **není rozhodnuto** — tři varianty a doporučení jsou
> v `docs/brief-vizualni-proces.md`, rozhodnutí je vedené jako otevřené #1 v
> `../docs/stav-projektu.md`. Do rozhodnutí se nepokračuje v žádné variantě ani na dalších
> kapitolách/destinacích.

## Struktura

```
content/
  _template/assets/       # šablona – místo pro fotky/ilustrace nové destinace
  <destinace>/assets/     # fotky/ilustrace použité v PDF (research a text jsou v Projektu 1)
design/
  <destinace>/
    wireframes/           # návrhové kostry stránek (SVG) – ZDROJ, gituje se
    pdf-parts/, preview/, proof-*/   # exporty a náhledy – build output, negituje se
  inspirace/              # moodboard/reference pro grafický styl – ZDROJ, gituje se
docs/
  design-brief-<destinace>.md   # styl, barvy, fonty, layout, historie Canva pokusů (v1/v2)
  brief-vizualni-proces.md      # analýza variant nového procesu + doporučení (čeká na rozhodnutí)
.claude/
  agents/design.md
  skills/layout-guide/
```

## Vstup z ostatních projektů

Z Projektu 1 (`../01-tvorba-textu/content/<destinace>/`):

- `text/*.md` — fact-checked kapitoly. **Nikdy se nepřepisují**, jde jen o vizuální sazbu.
- `text/_shot-list/*.md` — shot list vizuálů ke každé kapitole (co za fotku kam patří). Vzniká
  automaticky až po tom, co jsou všechny kapitoly destinace na `Stav: OK` — jeho existence je
  signál, že destinace je připravená k sazbě.

Dokud jsou projekty v jednom repu, cesty se odkazují relativně; po fyzickém rozdělení do
samostatných repozitářů půjde o ruční/skriptovaný hand-off hotových kapitol.

## Výstup pro Projekt 3

Finální PDF v `design/<destinace>/` — vstup pro QA (Fáze 4) a "value proof" marketing v
`../03-komercializace/`.

## Konvence

- Vygenerované binárky (PDF exporty, obrázky z designu) se negitují — zdroj pravdy je design
  brief + zdrojový Canva design, PDF je build output.
- Nikdy neměnit obsah textu kapitol při sazbě — jen vizuální/layoutová práce.
