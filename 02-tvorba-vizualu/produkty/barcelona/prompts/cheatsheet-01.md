# A4 cheatsheet page generation

## Use case
Jedna fyzická A4 strana taháčku k turistickému průvodci, kompaktní a rychle skenovatelná.

## Identity
- Destinace: `Barcelona`
- Země: `Španělsko`
- Oddíl: `Kdy jet`
- Strana taháčku: `cheatsheet-01`

## Exact content contract
Použij výhradně tento text:

# Rychlotaháček 1 — Praktické základy

## Kdy jet
- Nejlepší poměr počasí/davu: **květen a září**
- Nejdražší a nejplnější: **červenec–srpen** (28–29 °C, vysoká vlhkost)
- Koupání: červen–září, moře 22–26 °C
- Nejlevnější a nejklidnější: **leden–únor** (8–15 °C den, ~5 °C noc)
- Nejdeštivější: říjen, vlhčí celý podzim (přeháňky krátké)

## Z letiště (BCN, T1/T2)
- Aerobús → Pl. Catalunya, 25–35 min, 24/7 · 7,45/12,85 € u dopravce (weby i 9,50/16,50 €, ověř)
- Metro L9 Sud (Aeroport T1/T2) → 5,90 €, **T-casual tu neplatí**
- Vlak R2 Nord → 19–26 min, jen z T2 (shuttle z T1) · cena 4,60/2,90 € — zdroje se rozcházejí
- Bus 46 → Pl. Espanya, orientačně 2,65 €
- Taxi → orientačně 30–40 €, min. 21 € z letiště

## Turistická daň (od 1. 4. 2026, os./noc)
- Hotel 5*/luxus kemp 12 € · 4* 8,40 € · apartmány 9,50 € · hostely 6 € · ostatní kempy 7 €
- Děti do 17 let osvobozeny automaticky, od 8. noci se dál nenačítá
- 1–3* kategorie nedoloženo → ověř u ubytovatele
- Přirážka poroste: 6 € (2027), 7 € (2028), 8 € (2029)

## SIM/eSIM
- SIM ve Španělsku od ~10 € (60–90 GB)
- eSIM pozor na měnu: USD (od ~3 USD/GB) i EUR (od 7,95 €) — nemíchat, ověř těsně před cestou

## Peníze
- Platí euro, platební zvyklosti (hotovost/karta) nedoloženo → drobná hotovost jistota

## Bezpečnost a kapsáři
- K létu 2026 žádné mimořádné varování MZV ČR, doporučena registrace DROZD
- Kapsáři reálné téma, orientačně ~259 krádeží denně (2024, sekundární zdroj)
- Riziková místa: La Rambla, Gotická čtvrť, metro L1/L3/L5
- Uzly: Diagonal, Sants, Sagrada Família, Barceloneta
- Trend zlepšení: -40 % meziročně po operaci Pla Kanpai (sekundární zdroj, ber opatrně)

Chráněné tokeny: `["28–29 °C","22–26 °C","8–15 °C","5 °C","25–35 min","12,85 €","16,50 €","5,90 €","19–26 min","2,90 €","2,65 €","30–40 €","21 €","12 €","8,40 €","9,50 €","6 €","7 €","8 €","10 €","7,95 €","40 %","1","28–29","22–26","8–15","5","25–35","24","7","7,45","12,85","9,50","16,50","5,90","19–26","4,60","2,90","46","2,65","30–40","21","4","2026","12","8,40","6","17","8","1–3","2027","2028","2029","10","60–90","3","7,95","259","2024","40","jen","Rychlotaháček","Praktické","Kdy","Nejlepší","Nejdražší","Koupání","Nejlevnější","Nejdeštivější","Aerobús","Pl","Catalunya","Metro","Sud","Aeroport","T-casual","Vlak","Nord","Bus","Espanya","Taxi","Turistická","Hotel","Děti","Přirážka","Španělsku","Peníze","Platí","Bezpečnost","Kapsáři","Riziková","La Rambla","Gotická","Uzly","Diagonal","Sants","Sagrada Família","Barceloneta","Trend","Pla Kanpai","květen a září","červenec–srpen","leden–únor","T-casual tu neplatí","/luxus kemp 12 € · 4"]`

## Design
Použij stabilní A4 mřížku všech osmi stran: nadpis oddílu, krátké obsahové bloky a jasně odlišené praktické body. Přizpůsob pouze barvy, typografický pocit, motivy a fotografie systému země: `{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`.

## Constraints
- Přesný A4 poměr 1:1.41421356237, bezpečné okraje, žádné přetečení.
- Všechna fakta, čísla, měny, časy, data, vlastní jména, negace a varování zachovej přesně.
- Všechen text česky; žádné smyšlené názvy, loga, watermarky, cedule ani anglické popisky.
- Vytvoř jednu jedinou finální variantu.
