# A4 cheatsheet page generation

## Use case
Jedna fyzická A4 strana taháčku k turistickému průvodci, kompaktní a rychle skenovatelná.

## Identity
- Destinace: `Marsa Alam`
- Země: `Egypt`
- Oddíl: `Tři základní varianty`
- Strana taháčku: `cheatsheet-02`

## Exact content contract
Použij výhradně tento text:

# Rychlotaháček 2 — Výběr oblasti pobřeží a doprava po okolí

## Tři základní varianty
- Port Ghalib: nejblíž letišti (~15 min), marína s restauracemi/obchody/nočním životem.
- Sever/jih: klidnější, izolovanější, na pláž/moře; transfer delší → ověř u hotelu/cestovky.
- Dive campy Marsa Shagra: jednodušší ubytování, přímý house reef, komunita potápěčů.

## Jak se rozhodnout
- Noční život + restaurace + krátký transfer → Port Ghalib.
- Klid a pláž, večer v resortu OK → sever/jih.
- Priorita kvalitní house reef od pláže → dive camp.
- „Noční život + top house reef" nefunguje → blíž centru = zatíženější reef.

## Doprava po okolí
- Mezi resorty žádná veřejná doprava → jen transfer/taxi přes hotel nebo dopravce.
- Výlet jinam po pobřeží → doprava zvlášť, domluvená předem.
- Výlety na moře i do pouště: balíček včetně vyzvednutí u hotelu → doprava v ceně.
- Pronájem auta okrajová varianta → ověř podmínky a jestli se vyplatí.

Chráněné tokeny: `["15 min","2","15","jen","Rychlotaháček","Výběr","Tři","Port Ghalib","Sever","Dive","Marsa Shagra","Jak","Noční","Klid","Priorita","Doprava","Mezi","Výlet","Výlety","Pronájem","Noční život + top house reef"]`

## Design
Použij stabilní A4 mřížku všech osmi stran: nadpis oddílu, krátké obsahové bloky a jasně odlišené praktické body. Přizpůsob pouze barvy, typografický pocit, motivy a fotografie systému země: `{"palette":{"background":"#F4E9D8","primary":"#0F6473","secondary":"#C96A32","accent":"#CBA85B","text":"#201A16"},"heading_fonts":["Cormorant Garamond","Prata"],"body_fonts":["Manrope","Source Sans 3"],"motifs":["jemné vlny Rudého moře","korálové větvení","pouštní horizont","stylizované slunce"],"photo_style":"čistá tyrkysová voda, teplý pouštní písek, korálové detaily a přirozené slunce","character":"klidný prémiový red-sea editorial s kontrastem moře a pouště"}`.

## Constraints
- Přesný A4 poměr 1:1.41421356237, bezpečné okraje, žádné přetečení.
- Všechna fakta, čísla, měny, časy, data, vlastní jména, negace a varování zachovej přesně.
- Všechen text česky; žádné smyšlené názvy, loga, watermarky, cedule ani anglické popisky.
- Vytvoř jednu jedinou finální variantu.
