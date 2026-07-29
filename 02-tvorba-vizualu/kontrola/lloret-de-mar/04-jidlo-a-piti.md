# Kontrolní list — kapitola 04: Jídlo a pití

Zdroj: `../../../01-tvorba-textu/content/lloret-de-mar/text/04-jidlo-a-piti.md`

Postup generování je v `../../docs/prompt-guide.md`. Tenhle list slouží ke **kontrole vygenerovaných
stránek proti zdroji**.

## Sekce (počet, pořadí, nadpisy)

Kapitola má **5 podsekcí** v tomto pořadí:

1. Co ochutnat
2. Kde jíst
3. Menu del día
4. Tip navíc
5. Otevřít oči na ceny

Plus úvodní odstavec pod nadpisem kapitoly, bez vlastního podnadpisu.

Sekce **Co ochutnat** obsahuje odrážkový seznam **6 položek**, každá s tučně zvýrazněným názvem
pokrmu a vysvětlením za pomlčkou. Musí zůstat seznamem a musí jich zůstat šest.

## Katalánské názvy — největší riziko téhle kapitoly

Tady se nekontrolují čísla, ale **cizí slova s diakritikou, kterou čeština nemá**. Model češtinu
zvládá, ale tohle nejsou česká slova a zkomolené jídlo v menu čtenář nenajde.

| Název | Správně — pozor na |
|---|---|
| **Pa amb tomàquet** | tři samostatná slova, `à` s **obrácenou** čárkou (ne `á`) |
| **Zarzuela** | dvě „z", ne „sarzuela" |
| **Allioli** | dvě „l" uprostřed, ne „alioli", ne „aioli" |
| **Crema catalana** | malé „c" u druhého slova |
| **Escudella** | dvě „l" |
| **Paella** | dvě „l" |
| **Menu del día** | `í` s čárkou — a je to i **nadpis sekce**, tam se chyba pozná nejvíc |
| **chiringuitos** | množné číslo s „s", jak to má text |

Zkontroluj i `crème brûlée` v závorce u crema catalana — francouzský přízvuk a stříška, dvě místa,
kde model rád uklouzne.

## Čísla — musí sedět přesně

| Údaj | Správně |
|---|---|
| Menu del día | orientačně **20-25 EUR** podle podniku |

Jediné číslo v celé kapitole. Tím pádem se na něj při kontrole snadno zapomene — a zároveň je to
jediné místo, kde může vzniknout cenový nesmysl.

## Opatrné formulace — nesmí se z nich stát tvrzení najisto

- U menu del día musí zůstat, že cena je **orientační a liší se podnik od podniku**.
- U doporučení vzdálit se od promenády musí zůstat, že jde **spíš o obecné pravidlo než o konkrétní
  adresu**. Bez téhle půlky věty se z tipu stane slib.
- U menu del día musí zůstat, že je to **standardní katalánský zvyk, ne specifikum Lloretu** — je to
  důvod, proč tip funguje i mimo Lloret.
- Poslední sekce („Otevřít oči na ceny") je celá jen odkaz do kapitoly Rozpočet. Když ji model
  „vylepší" konkrétním číslem, je to nález.

## Žádné konkrétní restaurace

Research jednu restauraci jmenuje (Can Guidet), ale do textu se vědomě nedostala — chybí ověření
z víc zdrojů. Totéž platí pro chiringuita: research výslovně říká psát obecně o typu podniku, ne
o konkrétních jménech.

Jakékoliv jméno restaurace, baru nebo chiringuita, které se objeví na stránce — v textu i na fotce —
je nález.

## Fotky

- **Nejrizikovější kapitola z hlediska cedulí.** Jídlo se fotí v podnicích a model má silnou tendenci
  domalovat ceduli, menu ve výloze nebo logo na markýze. Přesně tak vznikla vymyšlená „CHIRINGUITO
  SA BOADELLA" v kapitole 01.
- Žádné čitelné menu s cenami na fotce — vzniklo by tím cenové tvrzení, které neprošlo fact-checkem.
- Generická cedule („CHIRINGUITO", „TAPAS") je v pořádku, konkrétní jméno ne.
- Talíře a jídlo se fotí bez problému — riziko je jen tam, kde je v záběru kus interiéru nebo ulice.

## Poznámka k obsahu

Fact-check kapitoly je `Stav: OK`, přeověřeno 2026-07-29. Otevřené otázky z Fáze 1 (aktuální ceny
menu del día a seznam konkrétních chiringuit) jsou vedené
v `../../../01-tvorba-textu/docs/open-questions-lloret-de-mar.md` a řeší se **až před vydáním**.
