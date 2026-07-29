# Kontrolní list — kapitola 04: Jídlo a pití

Zdroj: `../../../01-tvorba-textu/content/lloret-de-mar/text/04-jidlo-a-piti.md`

Postup generování je v `../../docs/prompt-guide.md`. Tenhle list slouží ke **kontrole vygenerovaných
stránek proti zdroji**.

## Sekce (počet, pořadí, nadpisy)

Kapitola má **6 podsekcí** v tomto pořadí:

1. Co ochutnat
2. Kde jíst
3. Menu del día
4. Tři nejlépe hodnocené restaurace
5. Tip navíc
6. Otevřít oči na ceny

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
| La Parrilla | **4,7** na Googlu · **4,7** na Tripadvisoru · víc než **2 000** hodnocení na Tripadvisoru |
| Restaurant Al Freskito | **4,7** na Googlu · **4,6** na Tripadvisoru · víc než **3 000** hodnocení na Googlu |
| Bodega Manolo Cotano | **4,7** na Googlu · **4,6** na Tripadvisoru |

Všechny známky jsou **z 5** na obou platformách — tady na rozdíl od kapitoly 03 stupnice nekolidují.
Zato jsou si čísla podobná až k nerozeznání: **třikrát 4,7 na Googlu**, pak **4,7 / 4,6 / 4,6** na
Tripadvisoru. Záměna se pozná jen porovnáním se zdrojem, protože každá kombinace vypadá věrohodně.

U počtů hodnocení hlídej, aby zůstaly **u správného podniku a u správné platformy** — „přes 2 000"
patří k La Parrilla na Tripadvisoru, „přes 3 000" k Al Freskito na Googlu. Prohozením vznikne
tvrzení, které neprošlo fact-checkem.

## Opatrné formulace — nesmí se z nich stát tvrzení najisto

- U menu del día musí zůstat, že cena je **orientační a liší se podnik od podniku**.
- U doporučení vzdálit se od promenády musí zůstat, že jde **spíš o obecné pravidlo než o konkrétní
  adresu**. Bez téhle půlky věty se z tipu stane slib.
- U menu del día musí zůstat, že je to **standardní katalánský zvyk, ne specifikum Lloretu** — je to
  důvod, proč tip funguje i mimo Lloret.
- Poslední sekce („Otevřít oči na ceny") je celá jen odkaz do kapitoly Rozpočet. Když ji model
  „vylepší" konkrétním číslem, je to nález.

## Jména restaurací — přesně tato tři a žádné jiné

Od 2026-07-29 kapitola konkrétní restaurace **jmenuje**, na základě doloženého výběru podle
`../../../01-tvorba-textu/docs/metodika-hodnoceni.md`. Pravidlo se tím obrací: nehlídá se, aby
žádné jméno neproniklo dovnitř, ale aby jich bylo **přesně těchto tři**.

1. **La Parrilla**
2. **Restaurant Al Freskito**
3. **Bodega Manolo Cotano**

Na co si dát pozor:

- **`Al Freskito`** — psáno s „k", ne „Fresquito". Je to vlastní jméno podniku, ne španělské slovo,
  takže model bude chtít „opravit" pravopis na správnou španělštinu.
- **`Bodega Manolo Cotano`** — tři slova, žádné z nich nezkracovat.
- **`La Parrilla`** — dvě „l" uprostřed.
- **Žádné čtvrté jméno.** Research zná další podniky (Can Guidet, Via Amalfi, La Fusta, Bodega Sa
  Xarxa, La Lonja, Can Sabata) a **žádný z nich do textu nepatří** — buď neprošly prahem, nebo
  filtrem na kuchyni. Zvlášť **Can Guidet** je riziko: objevuje se v research souboru jako
  „autentická restaurace" z dřívějšího sběru a při ověření dvěma platformami se do top 3 nedostal.
- Chiringuita se pořád **nejmenují**. Sběr 2026-07-29 pro ně použitelná data nenašel, takže tady
  původní pravidlo platí beze změny.

## Dodatek o původu výběru — musí zůstat celý

Odstavec pod trojicí říká, odkud výběr pochází a **že si tam nikdo umístění nezaplatil**. Bez toho
vypadá seznam jako placená reklama.

Musí v něm zůstat všech pět částí:

1. platformy (Google Maps a Tripadvisor),
2. datum (červenec 2026),
3. filtr — jen španělská, katalánská nebo středomořská kuchyně a dost hodnocení,
4. **„nikdo si tady umístění nezaplatil"** a že s podniky nemáme vztah,
5. že se hodnocení mění a podnik může zavřít.

## Fotky

- **Jmenované restaurace se nefotí.** Model konkrétní podnik nevygeneruje věrně — vznikl by smyšlený
  interiér vydávaný za reálnou restauraci, podle které čtenář utratí peníze. Sekce s trojicí je
  čistě grafická (srovnávací tabulka známek), viz shot list.
- **Nejrizikovější kapitola z hlediska cedulí.** Jídlo se fotí v podnicích a model má silnou tendenci
  domalovat ceduli, menu ve výloze nebo logo na markýze. Přesně tak vznikla vymyšlená „CHIRINGUITO
  SA BOADELLA" v kapitole 01. Teď je riziko větší, protože na stránce **skutečná jména podniků
  jsou** — model je může chtít přenést na ceduli v obrázku.
- Žádné čitelné menu s cenami na fotce — vzniklo by tím cenové tvrzení, které neprošlo fact-checkem.
- Generická cedule („CHIRINGUITO", „TAPAS") je v pořádku, konkrétní jméno ne.
- Talíře a jídlo se fotí bez problému — riziko je jen tam, kde je v záběru kus interiéru nebo ulice.

## Poznámka k obsahu

Fact-check kapitoly je `Stav: OK`, třetí kolo 2026-07-29 po doplnění trojice — 1 nález, opravený
(neopodstatněný superlativ „nejvíc hodnocení ze všech porovnávaných podniků" u Al Freskito).

Otevřené otázky z Fáze 1 (aktuální ceny menu del día, seznam chiringuit) jsou vedené
v `../../../01-tvorba-textu/docs/open-questions-lloret-de-mar.md` a řeší se **až před vydáním**.

**Žebříček se přeověřuje před každým vydáním** — restaurace zavírají častěji než hotely.
