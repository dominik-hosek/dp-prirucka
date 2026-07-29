# Kontrolní list — kapitola 03: Ubytování

Zdroj: `../../../01-tvorba-textu/content/lloret-de-mar/text/03-ubytovani.md`

Postup generování je v `../../docs/prompt-guide.md`. Tenhle list slouží ke **kontrole vygenerovaných
stránek proti zdroji**.

## Sekce (počet, pořadí, nadpisy)

Kapitola má **5 podsekcí** v tomto pořadí:

1. Centrum a Avinguda Just Marlès
2. Fenals
3. Směr Cala Boadella
4. Typ ubytování
5. Rychlé shrnutí

Plus úvodní odstavec pod nadpisem kapitoly, bez vlastního podnadpisu, a jedna závěrečná věta pod
Rychlým shrnutím (odkaz na kapitolu Off the beaten path) — ta se snadno ztratí, protože stojí až za
odrážkami.

Sekce **Rychlé shrnutí** má tři odrážky ve formátu „chceš X → jdi do Y". Musí zůstat seznamem se
šipkami, ne se rozpustit do odstavce — je to rozhodovací pravidlo celé kapitoly.

## Čísla — musí sedět přesně

Nejmenší tabulka ze všech kapitol. O to snazší je přehlédnout, když se jedno z čísel posune.

| Údaj | Správně |
|---|---|
| Vzdálenost Fenals od centra | asi **1 kilometr** |
| Začátek nočního života | kolem **22. hodiny** |

## Opatrné formulace — nesmí se z nich stát tvrzení najisto

- U cen ubytování musí zůstat, že se **výrazně liší podle sezóny, typu pokoje a předstihu rezervace**
  a že si má čtenář ověřit aktuální ceny přímo na rezervačním portálu. Konkrétní číslo do téhle
  kapitoly nepatří — je v kapitole Rozpočet.
- U Fenals musí zůstat, že tam **jsou** rodinné bary a hospůdky, takže se kvůli klidu neobětuje
  společenský život úplně. Když tohle vypadne, vyzní Fenals jako mrtvá čtvrť.
- U směru Cala Boadella musí zůstat, že jde o **delší docházku do centra výměnou za klid** — ne jen
  ta příjemná půlka věty.

## Vlastní jména — musí být přesně

- **Avinguda Just Marlès** (hlavní zábavní třída — nejrizikovější jméno v kapitole, je dlouhé a
  katalánské)
- **Platja de Lloret** (hlavní pláž)
- **Fenals**
- **Castell de Sant Joan** (zbytky hradu na vršku mezi centrem a Fenals)
- **Santa Clotilde** (zahrady)
- **Cala Boadella**

## Žádné konkrétní hotely

Kapitola je záměrně postavená na **výběru čtvrti, ne konkrétního hotelu** — a to je i její prodejní
argument („hotel za rok zastará"). Research sice jména hotelů zná (Rosamar, Best Lloret Splash,
Costa Encantada), ale do textu se vědomě nedostala.

Když model do stránky doplní jméno hotelu — v textu, v popisku nebo na ceduli na fotce — je to
nález, i kdyby to jméno bylo náhodou reálné.

## Fotky

- Žádná čitelná cedule s názvem hotelu, aparthotelu ani baru. Tohle je u téhle kapitoly
  nejpravděpodobnější chyba, protože téma přímo svádí k záběru hotelové recepce nebo fasády.
- Castell de Sant Joan a Cala Boadella nepodepisovat — model konkrétní místo nevygeneruje věrně.
- U záběru noční Avinguda Just Marlès nesmí být čitelná jména klubů.

## Poznámka k obsahu

Fact-check kapitoly je `Stav: OK`, přeověřeno 2026-07-29. Otevřená otázka z Fáze 1 (konkrétní ceny
za noc a přesné časy chůze mezi čtvrtěmi) je vedená
v `../../../01-tvorba-textu/docs/open-questions-lloret-de-mar.md` a řeší se **až před vydáním**.
Proto v kapitole žádné časy chůze nejsou — když je model „dopočítá", vznikne tvrzení bez opory.
