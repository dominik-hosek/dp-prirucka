# A4 cheatsheet page generation

## Use case
Jedna fyzická A4 strana taháčku k turistickému průvodci, kompaktní a rychle skenovatelná.

## Identity
- Destinace: `Barcelona`
- Země: `Španělsko`
- Oddíl: `Doprava`
- Strana taháčku: `cheatsheet-07`

## Exact content contract
Použij výhradně tento text:

# Rychlotaháček 07 — Rozpočet

## Doprava
- Letenka Praha–BCN zpáteční (Kč!): ~3500 Kč, výhodně 1500–2500, akce pod 1500, nejnižší 1180 Kč
- Rezervuj 3+ týdny dopředu · vše ostatní níže je v EUR
- Z letiště: Aerobús 7,45 EUR (12,85 tam-zpět) · metro L9 5,90 EUR · bus 46 ~2,65 EUR
- Taxi 30–40 EUR, min. z letiště 21 EUR

## MHD
- Jednotlivá 2,90 EUR · T-casual 10x 13,00 EUR (1,30/jízda) · T-usual 30 dní 22,80 EUR
- Hola Barcelona: 18,70 (48h) / 27,30 (72h) / 35,60 (96h) / 43,60 EUR (120h)
- Zlom T-casual vs. Hola 72h: cca 21 jízd za 3 dny

## Ubytování + turistická daň
- Průměr 110–130 EUR/noc, Eixample v létě 180–200, srpen nejdráž (jeden zdroj až 312 USD/noc!)
- Daň/os./noc od 1. 4. 2026: hotel 5★ 12 €, 4★ 8,40 €, apartmán 9,50 €, hostel 6 €, ostatní 7 €
- Děti do 17 let nic, od 8. noci se dál nenačítá

## Jídlo
- Menú del día 10–15 EUR (zdroje 8–15 i 13–20) · fast food 4–8 EUR · restaurace 35–60 EUR/os.
- Espresso 1,20–1,80 (turist. 2,50) · pivo v baru ~2,50 EUR (jinde až 7, nedoloženo, ber jako min.)
- Pivo ze supermarketu 1,23–1,25 EUR · couvert až 2,50 EUR (lze odmítnout)

## Vstupné
- Sagrada 26–40 EUR — jen pokud otevřená! · Park Güell 18 EUR · Casa Batlló od 29 · La Pedrera od 25
- Museu Picasso 12–14 EUR (jinde 15–19, zdroje se rozcházejí) · Camp Nou 28 EUR
- Sant Pau 34 vs. „od 17" EUR — ověř · Laberint 2,23 EUR · Bunkers zdarma
- 6 hl. Gaudí památek dohromady 125–147 EUR/os. — největší položka pobytu

## Zdarma a výlety
- 1. neděle v měsíci: Picasso, Blau, MNAC, Disseny, CCCB · MNAC so po 15:00
- Montserrat: vlak 13,80 + Cremallera 14,50 (jinde 15) EUR, kombi 50 EUR · Sitges od ~6 EUR
- Orientační denní rozpočet 120–180 EUR (jinde 150–180, průměr 179) — jen orientace, ne výpočet

Chráněné tokeny: `["3500 Kč","1180 Kč","7,45 EUR","5,90 EUR","2,65 EUR","30–40 EUR","21 EUR","2,90 EUR","13,00 EUR","22,80 EUR","48h","72h","96h","43,60 EUR","120h","3 dny","12 €","8,40 €","9,50 €","6 €","7 €","10–15 EUR","4–8 EUR","2,50 EUR","1,23–1,25 EUR","26–40 EUR","18 EUR","12–14 EUR","28 EUR","2,23 EUR","50 EUR","6 EUR","120–180 EUR","15:00","07","3500","1500–2500","1500","1180","3","7,45","12,85","5,90","46","2,65","30–40","21","2,90","13,00","1,30","30","22,80","18,70","27,30","35,60","43,60","110–130","180–200","312","1","4","2026","5","12","8,40","9,50","6","7","17","8","10–15","8–15","13–20","4–8","35–60","1,20–1,80","2,50","1,23–1,25","26–40","18","29","25","12–14","15–19","28","34","2,23","125–147","15","00","13,80","14,50","50","120–180","150–180","179","jen","ne","Rychlotaháček","Rozpočet","Doprava","Letenka Praha","Kč","Rezervuj","Aerobús","Taxi","Jednotlivá","T-casual","T-usual","Hola Barcelona","Zlom T-casual","Hola","Ubytování","Průměr","Eixample","Daň","Děti","Jídlo","Menú","Espresso","Pivo","Vstupné","Sagrada","Park","Casa Batlló","La Pedrera","Museu Picasso","Camp Nou","Sant Pau","Laberint","Bunkers","Gaudí","Zdarma","Picasso","Blau","Disseny","Montserrat","Cremallera","Sitges","Orientační","od 17"]`

## Design
Použij stabilní A4 mřížku všech osmi stran: nadpis oddílu, krátké obsahové bloky a jasně odlišené praktické body. Přizpůsob pouze barvy, typografický pocit, motivy a fotografie systému země: `{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`.

## Constraints
- Přesný A4 poměr 1:1.41421356237, bezpečné okraje, žádné přetečení.
- Všechna fakta, čísla, měny, časy, data, vlastní jména, negace a varování zachovej přesně.
- Všechen text česky; žádné smyšlené názvy, loga, watermarky, cedule ani anglické popisky.
- Vytvoř jednu jedinou finální variantu.
