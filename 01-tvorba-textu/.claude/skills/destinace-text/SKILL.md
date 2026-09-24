---
name: destinace-text
description: Vyrobí kompletní text destinace (Fáze 1+2) — fakta, 8 kapitol, kontrolní list a rychlotaháček — ve čtyřech až pěti bězích subagentů pod kontrolou nákladů. Volání: `/destinace-text <destinace>` pro celou destinaci, `/destinace-text <destinace> <kapitoly>` pro dávku.
---

# Text destinace levně

Naměřeno na Krétě 2026-08-06: **~460 tis. tokenů v 5 bězích.** Starý postup (32 běhů) stál ~1,2 mil.
a nevešel se do jednoho sezení.

## Co ve skutečnosti stojí tokeny

Původní domněnka byla „žere to čtení webu". **Měření ji vyvrátilo:** běhy na Krétě spotřebovaly
**nula volání webu** a přesto stály 84–102 tis. každý. Taháček přečte 17 KB textu a stojí 87 tis.

Skutečný vzorec:

> **cena běhu ≈ počet volání nástrojů × velikost kontextu**

Při každém volání nástroje se agentovi přeúčtuje celý dosavadní kontext. 18 volání × ~5 tis. ≈
90 tis. Z toho plynou tři pravidla, seřazená podle síly:

1. **Míň běhů.** Každý běh má fixní režii ~80 tis. bez ohledu na to, co dělá. Nikdy nepouštěj
   subagenta po jedné kapitole.
2. **Míň volání nástrojů v běhu.** Dej agentovi **přesné cesty k souborům**, ať nehledá Globem
   a nečte navíc. Řekni mu, ať zapisuje rovnou, ne po částech.
3. **Kratší vstupy.** Definice agentů jsou schválně ~1,5 KB — přeposílají se při každém volání.
   Nenafukuj je a nepřidávej agentovi ke čtení nic, co k práci nepotřebuje.

**Nejdražší chyba je dlouhé zadání.** Přešvih 2026-08-06 vznikl tím, že každý agent dostal
~600slovný nákupní seznam a odpracoval ho na 30 voláních webu a 34KB souboru — proti 3–7 KB
u Lloretu, kde byla zadání krátká. **Strop: 120 slov.** Osnovu si agent přečte v briefu sám.

## Předpoklad

`docs/brief-<destinace>.md` s potvrzenou personou a osnovou 8 kapitol.

## Sekvence

| # | Běh | Agent | Výstup |
|---|---|---|---|
| 1 | Fakta | `fakta-collector` | `content/<destinace>/fakta.md` |
| 2 | Kapitoly 01–04 | `chapter-writer` | `text/01…04`, `kontrola.md` |
| 3 | Kapitoly 05–08 | `chapter-writer` | `text/05…08`, `kontrola.md` |
| 4–5 | Taháček | `tahacek-creator` | `text/_tahacek/*` (max. 4 kapitoly na běh) |

Běhy pouštěj **za sebou, ne paralelně** — 2 a 3 připisují do téhož `kontrola.md`.

Zadání piš ve smyslu: *„Řiď se `.claude/agents/<agent>.md`. Napiš kapitoly 01–04 destinace X.
Vstupy: brief, style guide, `fakta.md`."* Nic víc — žádný seznam témat.

Po běhu 1 zkontroluj `wc -c content/<destinace>/fakta.md` → **max. 8 KB**. Větší soubor zaplatí
každý další běh znovu.

## Předání člověku

Kontrolu **nedělá agent**. Až je hotovo, řekni uživateli:

1. Otevři `content/<destinace>/kontrola.md`.
2. **Sekce A** — proklikej odkazy a porovnej čísla. Nesedí-li, přepiš údaj rovnou v kapitole;
   jedna hodnota nepotřebuje nový běh agenta (ten stojí ~80 tis. tokenů, oprava nic).
3. **Sekce B** — tvrzení bez zdroje, z obecné znalosti modelu. Přečti a zvaž.
4. Přidej **pár vlastních namátek** mimo seznam — agent označuje, čím si není jistý, jenže
   nejnebezpečnější je to, co považoval za jisté.
5. Po úpravě kapitoly je její taháček zastaralý → `/tahacek <destinace> <kapitola>`.
