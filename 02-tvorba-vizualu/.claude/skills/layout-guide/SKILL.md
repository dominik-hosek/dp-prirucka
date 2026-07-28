---
name: layout-guide
description: Naskládá hotový, fact-checked text kapitol dané destinace do Canva designu podle design-briefu a připraví export do PDF. Fáze 3 procesu tvorby průvodce. Volání – `/layout-guide <destinace>`.
---

# Layout guide

> **⚫ ODSTAVENO 2026-07-29 — tento skill nespouštěj.** Nahradil ho postup, kde stránky PDF generuje
> člověk v Nano Banana 2 / GPT Image podle připravených promptů (`docs/prompt-guide.md`), bez Canvy.
> Text níže zůstává jen jako historický záznam Canva postupu a jeho limitů.

Tento skill proměňuje hotový text (Fáze 2, `../01-tvorba-textu/content/<destinace>/text/*.md`) ve vizuální PDF
produkt pomocí Canva MCP nástrojů, ve stylu definovaném v design briefu (editorialní travel guide
s fotkami, ne čistě typografický – viz `design/inspirace/` a v2 revize briefu).

**Nikdy nepoužívej `design_type: "doc"` s `verbatim: true` jako hlavní cestu pro celou kapitolu.**
V1 tímto způsobem narazila na tvrdé omezení Canva API – auto-vygenerovaná hero sekce takového
designu (unbounded typ) není vůbec editovatelná (`fills` prázdné, hero text mimo `richtexts`,
`update_title` nemění viditelný obsah) a `merge-designs` na unbounded designy nefunguje. Podrobnosti
viz "Výstup v1" v `docs/design-brief-<destinace>.md`.

## Postup

1. Přečti `docs/design-brief-<destinace>.md` (styl, barvy, fonty, struktura stránky, rozhodnutí o
   fotkách). Pokud pro destinaci neexistuje, over jestli existuje obecný `docs/design-brief.md` a
   řiď se jím; destinaci-specifické rozdíly (název, podnázev, barevný akcent, fotky) doplň.
2. Přečti všechny kapitoly v `../01-tvorba-textu/content/<destinace>/text/*.md` v pořadí podle čísla v názvu souboru.
   Nepřepisuj ani nezkracuj text – jde už o fact-checked finální verzi z Fáze 2.
3. Zjisti, který způsob generování v Canvě dá **bounded/stránkovaný design se skutečně
   editovatelnými elementy** a podporou fotek (vyzkoušej/porovnej `design_type: "document"`,
   `generate-design-structured`, případně `search-brand-templates` +
   `create-design-from-brand-template`). Cíl: fixní stránky, kde jde po vygenerování
   mazat/přebarvovat/nahrazovat elementy a kde funguje `merge-designs` – ne unbounded Doc z v1.
4. Vytvoř titulní stranu (cover) podle briefu – skutečná destinační fotka jako hero, název/podnázev
   přes ni, barevný akcent.
5. Pro každou kapitolu: nejdřív vygeneruj vizuální kostru/layout (fotka k tématu, boxy, ikony)
   podle briefu – v promptu popisuj STYL a STRUKTURU, ne skutečný text kapitoly (aby ho AI
   nepřeformulovala). Teprve poté vlož přesný text z `../01-tvorba-textu/content/<destinace>/text/*.md` do
   připravených textových elementů přes editační operace (`replace_text` /
   `find_and_replace_text`) – nikdy nenech text kapitoly projít přes generování jako prompt.
6. Aplikuj vizuální styl z briefu (barvy nadpisů, ikonové odznaky, boxy pro insider tipy/pozor)
   přes `start-editing-transaction` / `perform-editing-operations`.
7. **Proof-first checkpoint:** po dokončení obálky + PRVNÍ kapitoly zastav se, stáhni/zobraz
   thumbnail (`get-design-thumbnail` nebo export+render) a nech vizuálně potvrdit člověkem, než
   začneš zbývající kapitoly – teprve po potvrzení pokračuj na kapitoly 2–8 stejným postupem.
   Tohle je záměrná pojistka proti opakování chyby z v1 (vada zjištěná až po všech 8 kapitolách).
8. Spoj cover + všechny kapitoly do jednoho finálního designu (`merge-designs` – funguje jen na
   bounded designy, proto krok 3).
9. Exportuj finální design do PDF (`export-design`).
10. Zapiš odkaz/ID finálního Canva designu a exportu do `docs/design-brief-<destinace>.md`
    (sekce "Výstup v2") a stručně shrň, co bylo vytvořeno.

## Pravidla

- Text v PDF musí být identický s `../01-tvorba-textu/content/<destinace>/text/*.md` – žádné přepisování obsahu,
  jde jen o vizuální sazbu. Text se do designu dostává přes editační operace (replace), ne přes
  generování s textem kapitoly v promptu.
- Pokud brief pro destinaci předepisuje skutečné fotky (viz Albánie v2), používej Canva vlastní
  licencovanou stock knihovnu vyhledanou/vloženou přes Canva nástroje – fotky tematicky odpovídající
  destinaci a obsahu kapitoly, ne generické stock ani fotky stažené odjinud z webu.
- Vždy ověř vizuálně (thumbnail), než prohlásíš kapitolu/design za hotový – nespoléhej jen na to,
  že API volání proběhlo bez chyby (to bylo právě to, co v1 přehlédlo hero sekci).
- Finální krok je vždy `export-design` do PDF – bez exportu není fáze hotová.
