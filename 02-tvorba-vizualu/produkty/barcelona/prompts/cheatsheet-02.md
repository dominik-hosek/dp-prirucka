# A4 cheatsheet page generation

## Use case
Jedna fyzická A4 strana taháčku k turistickému průvodci, kompaktní a rychle skenovatelná.

## Identity
- Destinace: `Barcelona`
- Země: `Španělsko`
- Oddíl: `Jízdenky (ceník od 15. 1. 2026, zóna 1)`
- Strana taháčku: `cheatsheet-02`

## Exact content contract
Použij výhradně tento text:

# Rychlotaháček 2 — Doprava po městě a do okolí

## Jízdenky (ceník od 15. 1. 2026, zóna 1)
- Jednotlivá 2,90 € · T-casual 10 jízd 13,00 € (2 zóny 25,50 €) · T-familiar 11,50 €
- T-usual 30 dní neomezeně 22,80 € (státní sleva 50 %, osobní) · Letištní 5,90 € · T-jove 45,50 €
- Ověř ceny před cestou — TMB je mění typicky k lednu

## 3 pravidla
- **Letiště:** T-casual neplatí → letištní jízdenka 5,90 € nebo Hola Barcelona
- T-casual přenosná (dvojice vystačí s 1 kartou), T-usual osobní
- T-casual = 1,30 €/jízda → pod ~21 jízd/3 dny výhodnější než Hola Barcelona 72 h

## Hola Barcelona (zóna 1, ověř před nákupem)
- 48 h 18,70 € · 72 h 27,30 € · 96 h 35,60 € · 120 h 43,60 €
- Pokrývá metro/bus TMB, NitBus, lanovku Montjuïc, FGC zóna 1, TRAM, Rodalies zóna 1
- Nezahrnuje Montjuïc Cable Car
- Výhoda: zahrnuje cestu metrem na letiště i zpět

## Metro — provozní doba
- Po–čt + svátky: 5:00–půlnoc · Pá + noci před svátky: 5:00–2:00
- So: nepřetržitě · Ne: do půlnoci
- Celonoční i o Sant Joan (24.6.), Festa Major Gràcia (22.8.), La Mercè (24.9. a 26.9.), Nový rok
- Jinak NitBus (sbíhá se na Pl. Catalunya)

## Taxi (od 1/2026)
- Nástupní 2,80 € · km 1,35 €(den)/1,66 €(noc) · příplatek letiště 4,60 € · min. z letiště 21 €
- Moll Adossat pevně 46 € · svátky (Vánoce/NY/Sant Joan) příplatky až +30 %

## Výlety vlakem
- Montserrat: R5 6,90/13,80 € → Cremallera 8,70/14,50 € (zpáteční i 15 €, ověř) nebo Aeri
- Trans Montserrat balíček 50 € vs. à la carte den ~36,80 € — porovnej podle využití
- Sitges: R2 Sud, 30–40 min, spoje 15–20 min, od ~6 €
- Tarragona: R14, 1–1,5 h
- Girona/Figueres: Rodalies, cena jen v USD (~12 USD) nedoložena v EUR → ověř u Renfe/Rodalies
- Mimo zónu 1 ověř zónové zařazení (rozdíl 1 vs 2 zóny T-casual: 12,50 €)

Chráněné tokeny: `["2,90 €","13,00 €","25,50 €","11,50 €","22,80 €","50 %","5,90 €","45,50 €","3 dny","72 h","48 h","18,70 €","27,30 €","96 h","35,60 €","120 h","43,60 €","2,80 €","4,60 €","21 €","46 €","30 %","13,80 €","14,50 €","15 €","50 €","36,80 €","30–40 min","15–20 min","6 €","1–1,5 h","12,50 €","5:00","2:00","2","15","1","2026","2,90","10","13,00","25,50","11,50","30","22,80","50","5,90","45,50","3","1,30","21","72","48","18,70","27,30","96","35,60","120","43,60","5","00","00–2","24.6","22.8","24.9","26.9","2,80","1,35","1,66","4,60","46","6,90","13,80","8,70","14,50","36,80","30–40","15–20","6","1–1,5","12","12,50","Ne","jen","Rychlotaháček","Doprava","Jízdenky","Jednotlivá","T-casual","T-familiar","T-usual","Letištní","T-jove","Ověř","Letiště","Hola Barcelona","Pokrývá","Rodalies","Nezahrnuje","Cable Car","Výhoda","Metro","Po","Pá","So","Celonoční","Sant Joan","Festa Major","La","Nový","Jinak","Pl","Catalunya","Taxi","Nástupní","Moll Adossat","Vánoce","Výlety","Montserrat","Cremallera","Aeri","Trans Montserrat","Sitges","Sud","Tarragona","Girona","Figueres","Renfe","Mimo","Letiště:"]`

## Design
Použij stabilní A4 mřížku všech osmi stran: nadpis oddílu, krátké obsahové bloky a jasně odlišené praktické body. Přizpůsob pouze barvy, typografický pocit, motivy a fotografie systému země: `{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`.

## Constraints
- Přesný A4 poměr 1:1.41421356237, bezpečné okraje, žádné přetečení.
- Všechna fakta, čísla, měny, časy, data, vlastní jména, negace a varování zachovej přesně.
- Všechen text česky; žádné smyšlené názvy, loga, watermarky, cedule ani anglické popisky.
- Vytvoř jednu jedinou finální variantu.
