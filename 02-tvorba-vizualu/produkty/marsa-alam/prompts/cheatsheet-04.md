# A4 cheatsheet page generation

## Use case
Jedna fyzická A4 strana taháčku k turistickému průvodci, kompaktní a rychle skenovatelná.

## Identity
- Destinace: `Marsa Alam`
- Země: `Egypt`
- Oddíl: `Realita all-inclusive`
- Strana taháčku: `cheatsheet-04`

## Exact content contract
Použij výhradně tento text:

# Rychlotaháček 4 — Jídlo a pití

## Realita all-inclusive
- All-inclusive = bufet v restauraci hotelu + nápoje (i alkohol), obvykle jen u hotelového baru.
- Kvalita/nabídka i pitná voda z kohoutku se liší resort od resortu → ověř u hotelu, ne z brožury.
- Pij výhradně balenou vodu, i v resortu — platí i pro led mimo hotel.

## Kdy a jak mimo resort
- Jídlo mimo hotel dává smysl hlavně v Port Ghalib → marína plná restaurací, pěšky dostupná.
- Jinde restaurace mimo hotel spíš výjimka → žádná v docházkové vzdálenosti, nebo nutný transfer.
- Celodenní výlet (potápění, poušť): jídlo bývá v balíčku → ověř, jestli si vzít něco s sebou.

## Ceny
- Ceny mimo resort se nepodařilo spolehlivě dohledat → hodně se liší a rychle mění.
- Orientační ceny výletů s jídlem viz kapitola Rozpočet; cenu restaurace/baru ověř na místě.

Chráněné tokeny: `["4","obvykle","jen","ne","Rychlotaháček","Jídlo","Realita","All-inclusive","Kvalita","Pij","Kdy","Port Ghalib","Jinde","Celodenní","Ceny","Orientační","Rozpočet"]`

## Design
Použij stabilní A4 mřížku všech osmi stran: nadpis oddílu, krátké obsahové bloky a jasně odlišené praktické body. Přizpůsob pouze barvy, typografický pocit, motivy a fotografie systému země: `{"palette":{"background":"#F4E9D8","primary":"#0F6473","secondary":"#C96A32","accent":"#CBA85B","text":"#201A16"},"heading_fonts":["Cormorant Garamond","Prata"],"body_fonts":["Manrope","Source Sans 3"],"motifs":["jemné vlny Rudého moře","korálové větvení","pouštní horizont","stylizované slunce"],"photo_style":"čistá tyrkysová voda, teplý pouštní písek, korálové detaily a přirozené slunce","character":"klidný prémiový red-sea editorial s kontrastem moře a pouště"}`.

## Constraints
- Přesný A4 poměr 1:1.41421356237, bezpečné okraje, žádné přetečení.
- Všechna fakta, čísla, měny, časy, data, vlastní jména, negace a varování zachovej přesně.
- Všechen text česky; žádné smyšlené názvy, loga, watermarky, cedule ani anglické popisky.
- Vytvoř jednu jedinou finální variantu.
