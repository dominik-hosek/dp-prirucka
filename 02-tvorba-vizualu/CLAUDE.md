# 02-tvorba-vizualu

Projekt 2 ze 3 (viz `../docs/project-split-plan.md` v rootu `dp-prirucka`) — pokrývá Fázi 3:
proměnu hotového textu ve vizuálně kvalitní, prodejný PDF produkt.

Celý fázový proces je popsaný v `../plan.md`. Živý stav skills/agentů patřících sem je v
`docs/automation-registry.md`.

> **Postup rozhodnutý 2026-07-29: stránky PDF generuje člověk v Nano Banana 2 / GPT Image podle
> připravených promptů.** Canva se nepoužívá — dosavadní postup (`docs/design-brief-albanie.md`,
> `.claude/skills/layout-guide/`, `.claude/agents/design.md`) je odstavený, zůstává jen jako
> historie. Vizuální styl z design briefu (paleta, typografie, prvky) platí dál.
>
> Jak se pracuje: `docs/prompt-guide.md`. Kontrolní listy kapitol: `kontrola/<destinace>/`.

## Struktura

```
content/
  _template/assets/       # šablona – místo pro fotky/ilustrace nové destinace
  <destinace>/assets/     # fotky/ilustrace použité v PDF (research a text jsou v Projektu 1)
kontrola/
  <destinace>/            # kontrolní listy po kapitolách – čísla, opatrné formulace, sekce
design/
  <destinace>/
    pages/                # hotové vygenerované stránky – ZDROJ, gituje se (nejsou reprodukovatelné)
    wireframes/           # návrhové kostry stránek (SVG) – ZDROJ, gituje se
    pdf-parts/, preview/, proof-*/   # starší Canva exporty – build output, negituje se
  inspirace/              # moodboard/reference pro grafický styl – ZDROJ, gituje se
docs/
  prompt-guide.md               # JAK se pracuje – zadání, co model umí/neumí, kontrola proti zdroji
  design-brief-<destinace>.md   # CO má vzniknout – paleta, typografie, layout (+ historie Canvy)
  brief-vizualni-proces.md      # historie: analýza variant, ze které se rozhodovalo
.claude/                        # odstavené, popisuje starý Canva postup
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
