# A4 cheatsheet page generation

## Use case
Jedna fyzická A4 strana taháčku k turistickému průvodci, kompaktní a rychle skenovatelná.

## Identity
- Destinace: `Barcelona`
- Země: `Španělsko`
- Oddíl: `Sagrada Família — OVĚŘ PŘED CESTOU`
- Strana taháčku: `cheatsheet-05`

## Exact content contract
Použij výhradně tento text:

# Rychlotaháček 5 — Památky, výlety, itineráře

## Sagrada Família — OVĚŘ PŘED CESTOU
- Zdroje si odporují, jestli je otevřená — web zmiňuje dočasné uzavření, jinde bez uzavření
- Kontakt: informacio@sagradafamilia.org, +34 932 080 414 · náhrada: Sant Pau (5 min pěšky)
- Ceník: audioprůvodce 26 € · průvodce 30 € · věže 36 € · průvodce+věže 40 € (slevy senior/děti)
- Věž Ježíše Krista hotová 2/2026 (172,5 m), vyhlídka až 2027 — v 2026 jen věže Narození a Umučení
- Možný příplatek 2–5 € nepotvrzen na ceníku
- Kupuj jen na oficiálním webu (partneři dráž: 46,80 € vs. 36 €)

## Park Güell
- Vstup 18 € (děti 7–12/65+ 13,50 €, do 6/ZTP zdarma)
- Slot + 30 min na vstup, pak propadá · bez návratu po odchodu · kapacita 1400/h
- Turisté 9:30–19:30, mimo to jen místní

## Gaudí a muzea
- Casa Batlló od 29 € · La Pedrera od 25 € (noc 39 €) — ceny „od", ověř na webu
- Museu Picasso 12/14 € (jinde 15–19 € — ověř na museupicasso.bcn.cat)
- Camp Nou/muzeum 28 € — stadion se přestavuje, jde jen o muzeum + imerzivní prohlídku

## Zdarma
- 1. neděle: Picasso, Museu Blau, MNAC, Museu del Disseny, CCCB
- Picasso zdarma: slot online otvírá se 4 dny předem v 10:00, rychle mizí
- MNAC bez rezervace, i sobota po 15:00 zdarma (málo známé) — 18. 5. a 11. 9. taky

## 3 itineráře (rámec, detaily viz kapitola)
- 2 dny: Sagrada+Sant Pau → oběd mimo centrum → Park Güell → Eixample → Gotická čtvrť/Picasso
- Den 2 večer: Rambla de Catalunya (ne La Rambla)
- 3 dny: +výlet — Sitges (spontánně) / Montserrat (naplánovat) / Tarragona / Girona-Figueres
- Levný den (1. neděle): MNAC/Picasso zdarma → Parc del Laberint (strop 750) → Bunkers del Carmel
- Bunkers zavírá 19:30 léto/17:30 zima — ne program na západ slunce

Chráněné tokeny: `["5 min","26 €","30 €","36 €","40 €","172,5 m","2–5 €","46,80 €","18 €","13,50 €","30 min","29 €","25 €","39 €","14 €","15–19 €","28 €","4 dny","2 dny","3 dny","9:30","19:30","10:00","15:00","17:30","5","34","932","080","414","26","30","36","40","2","2026","172,5","2027","2–5","46,80","18","7–12","65","13,50","6","1400","9","30–19","29","25","39","12","14","15–19","28","1","4","10","00","15","11","3","750","19","17","jen","ne","Rychlotaháček","Památky","Sagrada Família","Zdroje","Kontakt","Sant Pau","Ceník","Věž Ježíše Krista","Narození","Umučení","Možný","Kupuj","Park","Vstup","Slot","Turisté","Gaudí","Casa Batlló","La Pedrera","Museu Picasso","Camp Nou","Zdarma","Picasso","Museu Blau","Museu","Disseny","Sagrada","Eixample","Gotická","Den","Rambla","Catalunya","La Rambla","Sitges","Montserrat","Tarragona","Girona-","Figueres","Levný","Parc","Laberint","Bunkers","Carmel","od"]`

## Design
Použij stabilní A4 mřížku všech osmi stran: nadpis oddílu, krátké obsahové bloky a jasně odlišené praktické body. Přizpůsob pouze barvy, typografický pocit, motivy a fotografie systému země: `{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`.

## Constraints
- Přesný A4 poměr 1:1.41421356237, bezpečné okraje, žádné přetečení.
- Všechna fakta, čísla, měny, časy, data, vlastní jména, negace a varování zachovej přesně.
- Všechen text česky; žádné smyšlené názvy, loga, watermarky, cedule ani anglické popisky.
- Vytvoř jednu jedinou finální variantu.
