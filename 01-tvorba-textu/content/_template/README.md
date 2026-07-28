# Šablona nové destinace

Jak založit novou destinaci (Fáze 0 → 1 → 2). Pořadí kroků není libovolné — každý krok čerpá
z výstupu předchozího.

## Krok 0 — brief (Fáze 0)

Než vznikne jediný research soubor, musí existovat `docs/brief-<destinace>.md`: proč tuhle
destinaci, cílová persona, cena, osnova kapitol. Bez schválené osnovy není jasné, kolik research
souborů se má vůbec sbírat.

## Krok 1 — založení složek

```bash
cp -r content/_template content/<destinace>
rm content/<destinace>/README.md
```

Vznikne `content/<destinace>/research/` a `content/<destinace>/text/`. Podsložky
`text/_fact-check/` a `text/_shot-list/` se vytvoří samy, až je naplní příslušní agenti — ručně
je nezakládej.

V Projektu 2 k tomu patří `../02-tvorba-vizualu/content/<destinace>/assets/` (fotky/ilustrace).

## Krok 2 — research (Fáze 1)

Jeden soubor v `research/` = jedna kapitola z osnovy, pojmenovaný stejně jako budoucí kapitola
(bez pořadového čísla): `prakticke-zaklady.md`, `doprava-po-okoli.md`, …

```
/research-topic <destinace> <téma>
```

Každý záznam musí mít zdroj a datum ověření. Co se nepodařilo spolehlivě ověřit nebo si zdroje
odporují, patří do `docs/open-questions-<destinace>.md` — ten pak čte QA ve Fázi 4.

## Krok 3 — psaní kapitol (Fáze 2)

```
/write-chapter <destinace> <kapitola>
```

Soubory v `text/` mají pořadové číslo podle osnovy: `01-prakticke-zaklady.md`, …
Píše se **výhradně** z `research/`, ne z volné paměti modelu.

Po uložení kapitoly se automaticky (hook) hlásí fact-check. Nálezy z `text/_fact-check/` se
opravují v textu a fact-check se pouští znovu, dokud kapitola nemá `Stav: OK`.

## Krok 4 — předání Projektu 2

Jakmile mají **všechny** kapitoly destinace `Stav: OK`, hook spustí Shot-List-Creator a vzniknou
shot listy v `text/_shot-list/`. Teprve tím je destinace hotová pro Fázi 3 (vizuál).
