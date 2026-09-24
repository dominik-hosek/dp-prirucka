# A4 cheatsheet page generation

## Use case
Jedna fyzická A4 strana taháčku k turistickému průvodci, kompaktní a rychle skenovatelná.

## Identity
- Destinace: `Marsa Alam`
- Země: `Egypt`
- Oddíl: `Wadi El Gemal (hlavní cíl)`
- Strana taháčku: `cheatsheet-06`

## Exact content contract
Použij výhradně tento text:

# Rychlotaháček 06 — Výlety mimo vodu

## Wadi El Gemal (hlavní cíl)
- Národní park: hory, vádí, pobřeží s mangrovy.
- Vstup pro cizince ~40 EGP (≈ 2 EUR) · kempování v parku ~200 EGP/os./noc.
- Běžně jen jako součást organizovaného výletu s vyzvednutím od hotelu, veřejná doprava tam není.

## Beduínské výlety
- Zastávka v osadě nebo na čaji — turisticky zprostředkovaná, ne autentické setkání.
- Ber jako krátký doplněk v rámci většího programu, ne hlavní bod výletu.

## Safari — skupinově, nebo soukromě
- Cena orientačně 90–228 USD/os.
- Skupinové levnější, ale vázané na tempo skupiny.
- Soukromé dražší, ale flexibilní v místě a délce zastávek.

## Chceš víc než odpoledne
- Zvaž vícedenní nebo večerní program (přespání v poušti, pozorování hvězd).
- Nabídka i cena se liší podle cestovky a sezóny — domluv na místě nebo přes hotel.

Chráněné tokeny: `["2 EUR","06","40","2","200","90–228","jen","ne","Rychlotaháček","Výlety","Wadi El Gemal","Národní","Vstup","Běžně","Beduínské","Zastávka","Ber","Safari","Cena","Skupinové","Soukromé","Chceš","Zvaž","Nabídka"]`

## Design
Použij stabilní A4 mřížku všech osmi stran: nadpis oddílu, krátké obsahové bloky a jasně odlišené praktické body. Přizpůsob pouze barvy, typografický pocit, motivy a fotografie systému země: `{"palette":{"background":"#F4E9D8","primary":"#0F6473","secondary":"#C96A32","accent":"#CBA85B","text":"#201A16"},"heading_fonts":["Cormorant Garamond","Prata"],"body_fonts":["Manrope","Source Sans 3"],"motifs":["jemné vlny Rudého moře","korálové větvení","pouštní horizont","stylizované slunce"],"photo_style":"čistá tyrkysová voda, teplý pouštní písek, korálové detaily a přirozené slunce","character":"klidný prémiový red-sea editorial s kontrastem moře a pouště"}`.

## Constraints
- Přesný A4 poměr 1:1.41421356237, bezpečné okraje, žádné přetečení.
- Všechna fakta, čísla, měny, časy, data, vlastní jména, negace a varování zachovej přesně.
- Všechen text česky; žádné smyšlené názvy, loga, watermarky, cedule ani anglické popisky.
- Vytvoř jednu jedinou finální variantu.
