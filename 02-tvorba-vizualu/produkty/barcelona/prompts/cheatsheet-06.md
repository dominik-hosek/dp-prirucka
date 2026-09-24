# A4 cheatsheet page generation

## Use case
Jedna fyzická A4 strana taháčku k turistickému průvodci, kompaktní a rychle skenovatelná.

## Identity
- Destinace: `Barcelona`
- Země: `Španělsko`
- Oddíl: `Bunkers del Carmel`
- Strana taháčku: `cheatsheet-06`

## Exact content contract
Použij výhradně tento text:

# Rychlotaháček 06 — Off the beaten path

## Bunkers del Carmel
- Zdarma, 360° výhled, výšlap do kopce → pohodlná obuv
- Otevřeno 9:00–19:30 v létě / 9:00–17:30 v zimě, v noci ZAVŘENO
- Na sunset v létě NEJDI — nestihneš. Přepnutí jaro/podzim neověřeno

## Sant Pau (modernismus)
- 5 min od Sagrady, míň lidí → náhrada, pokud bude Sagrada zavřená
- 34 EUR základní (senioři 27, děti 3–11 12 EUR) vs. jinde „od 17 EUR" — ověř před cestou
- Do 12 let a ZTP zdarma · zdarma 23. 4. a 24. 9.
- Otevřeno IV–X 9:30–18:30, XI–III 9:30–17:00

## Parc del Laberint d'Horta
- Nejstarší zahrada v BCN, bludiště ze stříhaných cypřišů
- 2,23 EUR (jinde 2,50 EUR), snížené 1,42 EUR
- Zdarma st + ne, děti do 5, nezaměstnaní, senioři, obyvatelé Horty, 24. 9.
- Denní strop 750 lidí → na zdarma dny choď dopoledne

## Čtvrti bez turistů
- Sant Antoni: Mercat de Sant Antoni, Carrer del Parlament → ne dopoledne: bazar knih + snídaně
- Tržnice možná v rekonstrukci — ověř
- Sants: Carretera de Sants, Mercat de Sants → tip na levné menú del día
- Sarrià: Mercat de Sarrià · Poblenou: klidnější pláže, bydlení (viz Ubytování)

## Poznámka
- Konkrétní podniky zde záměrně nejmenujeme — chybí ověřená data ze 2 platforem

Chráněné tokeny: `["5 min","34 EUR","12 EUR","2,23 EUR","2,50 EUR","1,42 EUR","9:00","19:30","17:30","9:30","18:30","17:00","06","360","9","00–19","30","00–17","5","34","27","3–11","12","17","23","4","24","30–18","30–17","00","2,23","2,50","1,42","750","2","ne","Rychlotaháček","Off","Bunkers","Carmel","Zdarma","Otevřeno","Na","Přepnutí","Sant Pau","Sagrady","Sagrada","Do","Parc","Laberint","Horta","Nejstarší","Horty","Denní","Čtvrti","Sant Antoni","Mercat","Carrer","Parlament","Tržnice","Sants","Carretera","Poblenou","Ubytování","Poznámka","Konkrétní","od 17 EUR"]`

## Design
Použij stabilní A4 mřížku všech osmi stran: nadpis oddílu, krátké obsahové bloky a jasně odlišené praktické body. Přizpůsob pouze barvy, typografický pocit, motivy a fotografie systému země: `{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`.

## Constraints
- Přesný A4 poměr 1:1.41421356237, bezpečné okraje, žádné přetečení.
- Všechna fakta, čísla, měny, časy, data, vlastní jména, negace a varování zachovej přesně.
- Všechen text česky; žádné smyšlené názvy, loga, watermarky, cedule ani anglické popisky.
- Vytvoř jednu jedinou finální variantu.
