---
name: research-topic
description: Sesbírá strukturovaná, ověřená data k jednomu tématu/kapitole turistického průvodce pro danou destinaci — fakta se zdroji a datem ověření, plus insider tipy z fór/blogů. Používá se ve Fázi 1 procesu tvorby průvodce (research), jeden běh = jedno téma jedné destinace. Volání: `/research-topic <destinace> <téma>`.
---

# Research tématu pro turistického průvodce

Cíl: vytvořit strukturovaný, faktický podklad pro téma, ze kterého bude Writer agent (Fáze 2) psát kapitolu — nikdy nepsat prózu kapitoly tady, jen strukturovaná data.

## Postup

1. Over si osnovu a personu v `docs/brief-<destinace>.md`, ať je research zacílený na relevantní úroveň detailu (rozpočet, styl cestování persony).
2. Pomocí WebSearch/WebFetch nasbírej fakta k tématu z více zdrojů (oficiální info, cestovatelské blogy, fóra, recenze, Reddit).
3. U každého faktu/tipu zaznamenej: co, zdroj (URL), datum ověření (dnešní datum). Ceny a otevírací doby VŽDY označ jako "ověřeno k datu X, může se změnit".
4. Odděl fakta (ověřitelná, konkrétní) od insider tipů (subjektivní doporučení, méně ověřitelné) — u tipů uveď, kolik nezávislých zdrojů je zmiňuje.
5. Zapiš výstup do `content/<destinace>/research/<téma-slug>.md` podle šablony níže.
6. Neopakuj obecné turistické fráze bez konkrétní hodnoty (persona je hledá "deep knowledge", ne to, co najde v první výsledku Googlu).

## Šablona výstupního souboru

```markdown
# Research: <téma> — <destinace>

Datum sběru: <YYYY-MM-DD>

## Fakta

- <fakt> — zdroj: <URL>, ověřeno: <datum>
- ...

## Insider tipy

- <tip> — zmíněno v: <kolik zdrojů / jaké typy zdrojů>
- ...

## Otevřené otázky / potřeba ověřit před vydáním

- <cokoliv nejisté nebo protichůdné mezi zdroji>
```

## Napojení na zbytek procesu

- Vstup: `docs/brief-<destinace>.md` (persona, osnova).
- Výstup čte: Writer agent (Fáze 2, `.claude/agents/writer.md`, zatím nevytvořen) a Fact-Checker agent.
- Viz `docs/automation-registry.md` pro aktuální stav navazujících kroků.
