# Kontrolní list — kapitola 08: Checklist před odjezdem

Zdroj: `../../../01-tvorba-textu/content/lloret-de-mar/text/08-checklist-pred-odjezdem.md`

Postup generování je v `../../docs/prompt-guide.md`. Tenhle list slouží ke **kontrole vygenerovaných
stránek proti zdroji**.

## Sekce (počet, pořadí, nadpisy)

Kapitola má **6 podsekcí** v tomto pořadí:

1. Doklady
2. Registrace a pojištění
3. Peníze a připojení
4. Doprava z letiště
5. Balení
6. Rychlý checklist

Plus úvodní odstavec pod nadpisem kapitoly, bez vlastního podnadpisu, a **závěrečná věta pod
checklistem** (podmínky vstupu se mohou měnit, ověř na mzv.gov.cz). Ta věta stojí až za odrážkami
a je to poslední text celého průvodce — o to snáz ji model utne.

Sekce 1–5 jsou odrážkové seznamy, sekce 6 je **zaškrtávací** seznam.

## Rychlý checklist — 9 položek, musí sedět počet i pořadí

Poslední sekce je seznam se **zaškrtávacími políčky** `- [ ]`. Nejde o dekoraci — je to hlavní
praktická hodnota kapitoly, čtenář si ji odškrtává před odjezdem.

| # | Položka |
|---|---|
| 1 | Platný občanský průkaz nebo pas (i pro děti) |
| 2 | EHIC |
| 3 | Cestovní pojištění |
| 4 | Řidičský průkaz + zelená karta (pokud jedeš autem) |
| 5 | Registrace DROZD |
| 6 | SIM/eSIM zajištěná nebo naplánovaná |
| 7 | Hotovost v eurech na drobné výdaje |
| 8 | Rezervace autobusu/transferu z letiště |
| 9 | Plavky, opalovací krém, lehké oblečení |

**Co hlídat:**

- **Počet.** Musí jich zůstat devět. Devět krátkých, podobně vypadajících řádků za sebou je přesně
  ta situace, kdy jeden tiše vypadne a stránka vypadá pořád v pořádku.
- **Zaškrtávací políčka.** Musí zůstat prázdné čtverečky, ne odrážky ani očíslovaný seznam.
- **Pořadí.** Sleduje pořadí sekcí kapitoly (doklady → pojištění → peníze/připojení → doprava →
  balení). Když ho model přeskládá „logičtěji", ztratí se vazba na text nad ním.
- **Položky nesmí přibýt.** Model má u checklistů silnou tendenci doplnit „obvyklé" věci
  (adaptér, léky, kopie dokladů) — nic z toho v researchi není.

## Čísla — musí sedět přesně

| Údaj | Správně |
|---|---|
| Autobus z letiště Girona | linka **613**, dopravce **Sagalés** |
| Nejteplejší období | **červen-září** |

Nejmenší tabulka v průvodci — kapitola je záměrně bez cen. **To je její výhoda: jako jediná
nezastará.** Když se na stránce objeví jakákoliv cena nebo konkrétní čas odjezdu, je to nález.

## Opatrné formulace — nesmí se z nich stát tvrzení najisto

- U **občanky s odstřiženým rohem** musí zůstat obojí: že je **formálně platná**, ale v praxi může
  způsobit komplikace. Když vypadne první půlka, vznikne nepravda; když druhá, zmizí smysl tipu.
- U **EHIC** musí zůstat výčet toho, co **nekryje** (spoluúčast, plná hospitalizace, repatriace) —
  je to jediný důvod, proč si k němu čtenář sjednává komerční pojištění.
- U **řidičského průkazu** musí zůstat, že běžný český stačí a **mezinárodní není potřeba**.
- U **zelené karty** musí zůstat doporučení mít ji uloženou i **offline**.
- U **hotovosti** musí zůstat, že karty jsou běžně přijímané — hotovost je doplněk na drobné výdaje,
  ne varování před kartami.
- **Závěrečná věta** o měnících se podmínkách vstupu a ověření na mzv.gov.cz musí zůstat celá,
  včetně adresy webu.

## Vlastní jména a zkratky — musí být přesně

- **EHIC** (velkými písmeny), popisně „modrá kartička"
- **DROZD** (evidence Ministerstva zahraničních věcí ČR — velkými písmeny)
- **Sagalés** (dopravce — `é` s čárkou), linka **613**
- **mzv.gov.cz** (ne mzv.cz)

Zkomolená zkratka je tu horší než jinde — podle ní čtenář hledá konkrétní web nebo formulář.

## Fotky

- Detail občanky s odstřiženým rohem: **nesmí obsahovat čitelné osobní údaje ani realistické číslo
  dokladu.** Model rád domalovává jméno a rodné číslo — vypadá to jako reálný doklad reálného
  člověka. Tohle je jediná fotka v celém průvodci, kde tohle riziko hrozí.
- EHIC a zelená karta: ikona nebo generický vzor, ne konkrétní kartička se jménem.
- Autobus Sagalés je reálná značka — buď správně napsané logo, nebo raději bez čitelného.
- Záběr chiringuita: platí zákaz čitelných jmen podniků jako v kapitolách 01 a 04.

## Poznámka k obsahu

Fact-check kapitoly je `Stav: OK`, přeověřeno 2026-07-29, bez nálezů. Jediná otevřená otázka z Fáze 1
je obecná (podmínky vstupu se mohou měnit) a text ji už ošetřuje závěrečnou větou — nic dalšího se
tu před vydáním doověřovat nemusí.
