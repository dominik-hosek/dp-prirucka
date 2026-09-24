# A4 cheatsheet page generation

## Use case
Jedna fyzická A4 strana taháčku k turistickému průvodci, kompaktní a rychle skenovatelná.

## Identity
- Destinace: `Barcelona`
- Země: `Španělsko`
- Oddíl: `Čtvrti — co si za co koupíš`
- Strana taháčku: `cheatsheet-03`

## Exact content contract
Použij výhradně tento text:

# Rychlotaháček 03 — Ubytování

## Čtvrti — co si za co koupíš
- Eixample → nejjistější pro první návštěvu, pěšky ke Gaudímu; léto 180–200 EUR/noc, vyprodá se
- Gotická čtvrť → krátký pobyt, středověké uličky; bez metra uvnitř, kapsáři, hluk do noci
- Gràcia → klid a místní život · Barceloneta → nejblíž pláži, v sezóně přeplněná
- Poblenou → klidnější pláže Bogatell/Mar Bella, nižší ceny, metro L4; na delší pobyt
- Poble Sec / Sant Antoni → levnější, míň centrální (Poble Sec ~20 min pěšky, Sant Antoni L2)
- Přesný cenový rozdíl čtvrtí vůči centru se dohledat nepodařilo — doložená cena je jen pro Eixample

## Ceny a rezervace
- Průměr 2026: 110–130 EUR/noc, roste květen–září
- Srpen nejdražší: až kolem 312 USD/noc (pozor, dolary, ne eura)
- Na léto rezervuj 3–6 měsíců dopředu; k ceně připočítej turistickou daň (od 1.4.2026 zvýšená)

## Turistická daň
- Apartmán 9,50 EUR/osoba/noc, 4★ hotel 8,40 EUR — zdánlivě levnější apartmán rozdíl vrátí zpět

## Turistické apartmány — co se mění
- ~10 101 licencí HUT se neobnoví, platnost do listopadu 2028; potvrdil Ústavní soud (3/2025)
- Legální nabídka musí mít NRU, HUT, NIRTC — bez čísla je varovný signál
- Airbnb/Vrbo/Booking musí nabídku bez NRU stáhnout do 48 h
- Situace se mění → stav licence ověř před cestou (registr Ajuntament de Barcelona)

## Proč tu nejsou konkrétní hotely
- Žebříček podle recenzí se nepodařilo doložit (chybí počty recenzí / druhá platforma)
- Radši žádné jméno než jméno bez dat za sebou

## Rychlé rozhodnutí
- Krátký pobyt, nevadí hluk → Gotická čtvrť (bez metra uvnitř)
- První návštěva, jistota → Eixample (180–200 EUR/noc v létě)
- Klid, místní život → Gràcia
- Delší pobyt, klidnější pláže, nižší ceny → Poblenou
- Šetřit a být blízko → Poble Sec / Sant Antoni
- U apartmánu vždy zkontroluj NRU/HUT/NIRTC

Chráněné tokeny: `["20 min","8,40 EUR","48 h","03","180–200","20","2026","110–130","312","3–6","1.4","9,50","4","8,40","10","101","2028","3","2025","48","jen","ne","Rychlotaháček","Ubytování","Čtvrti","Eixample","Gaudímu","Gotická","Barceloneta","Poblenou","Bogatell","Mar Bella","Poble Sec","Sant Antoni","Přesný","Ceny","Průměr","Srpen","Na","Turistická","Apartmán","Turistické","Ústavní","Legální","Airbnb","Vrbo","Booking","Situace","Ajuntament","Barcelona","Proč","Žebříček","Radši","Rychlé","Krátký","První","Klid","Delší","Šetřit"]`

## Design
Použij stabilní A4 mřížku všech osmi stran: nadpis oddílu, krátké obsahové bloky a jasně odlišené praktické body. Přizpůsob pouze barvy, typografický pocit, motivy a fotografie systému země: `{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`.

## Constraints
- Přesný A4 poměr 1:1.41421356237, bezpečné okraje, žádné přetečení.
- Všechna fakta, čísla, měny, časy, data, vlastní jména, negace a varování zachovej přesně.
- Všechen text česky; žádné smyšlené názvy, loga, watermarky, cedule ani anglické popisky.
- Vytvoř jednu jedinou finální variantu.
