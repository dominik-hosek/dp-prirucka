# Šablona nové destinace

Jak založit novou destinaci (Fáze 0 → 1 → 2).

## Krok 0 — brief (Fáze 0)

Než vznikne jediný řádek dat, musí existovat `docs/brief-<destinace>.md`: proč tuhle destinaci,
cílová persona, cena, osnova 8 kapitol. Osnova je jediné místo, kde je napsané, co se má sbírat —
subagenti si ji čtou sami.

## Krok 1 — založení složek

```bash
cp -r content/_template content/<destinace>
rm content/<destinace>/README.md
```

Vznikne `content/<destinace>/text/`. Soubory `fakta.md`, `kontrola.md` a podsložku `text/_tahacek/`
vytvoří příslušní agenti — ručně je nezakládej.

V Projektu 2 k tomu patří `../02-tvorba-vizualu/content/<destinace>/assets/` (fotky/ilustrace).

## Krok 2 — celý text (Fáze 1+2)

```
/destinace-text <destinace>
```

Jeden příkaz, čtyři běhy subagentů, ~130 tis. tokenů: sběr faktů → kapitoly 01–04 → kapitoly 05–08
→ rychlotaháček. Detail a rozpočty v `.claude/skills/destinace-text/SKILL.md`.

Přegenerování jedné dávky kapitol: `/destinace-text <destinace> 05-08`.

## Krok 3 — ruční kontrola (člověk)

Kontrolu **nedělá agent**. Otevři `content/<destinace>/kontrola.md`:

- **Sekce A** — proklikej odkazy a porovnej čísla. Nesedí-li, přepiš údaj rovnou v kapitole.
  Jedna hodnota nepotřebuje nový běh agenta.
- **Sekce B** — tvrzení bez zdroje, psaná z obecné znalosti modelu. Přečti a zvaž, jestli sedí.
- Přidej si **pár vlastních namátek** mimo seznam. Agent označuje, čím si není jistý — jenže
  nejnebezpečnější je to, co považoval za jisté.

Když kapitolu upravíš, její taháček je tím zastaralý → `/tahacek <destinace> <kapitola>`.

## Krok 4 — předání Projektu 2

Destinace je hotová pro Fázi 3 (vizuál), teprve když má každá kapitola obě verze: dlouhou v `text/`
a krátkou v `text/_tahacek/`, a když je `kontrola.md` projitá.
