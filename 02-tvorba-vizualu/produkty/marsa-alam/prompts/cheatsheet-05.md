# A4 cheatsheet page generation

## Use case
Jedna fyzická A4 strana taháčku k turistickému průvodci, kompaktní a rychle skenovatelná.

## Identity
- Destinace: `Marsa Alam`
- Země: `Egypt`
- Oddíl: `Hotel vs. nezávislé`
- Strana taháčku: `cheatsheet-05`

## Exact content contract
Použij výhradně tento text:

# Rychlotaháček 05 — Potápění a šnorchlování

## Hotel vs. nezávislé
- Hotel: pohodlí, ale dražší (marže recepce + dive centra navrch).
- Nezávislé dive centrum: levnější, vyber sám, ověř vybavení a velikost skupiny.
- Dive camp u Marsa Shagra → nezávislá varianta je tam standard.

## Kam za čím
- Abu Dabab — mělký záliv, želvy a dugongové, vhodné i pro nejisté šnorchlaře.
- Dolphin House (Sha'ab Samadai) — delfíni, celodenní lodní výlet, šnorchl i potápění.
- Elphinstone — driftový proud, náročnější, spíš pro certifikované potápěče.

## Ceny (orientačně)
- Šnorchlování Abu Dabab 48–60 USD/os. · Dolphin House 55–62 USD/os.
- Potápění Elphinstone (2 ponory) 85–130 USD.
- + poplatek mořského parku u Elphinstone 15–25 USD/ponor, mimo cenu výletu.

## Kurz pro nepotápěče
- OW kurz = nejrychlejší cesta k Elphinstone.
- Cenu kurzu se nepodařilo spolehlivě dohledat — ověř přímo na místě před rezervací.
- Standardní cestovní pojištění potápění často nekryje — ověř si to u pojišťovny předem.

## Bezpečnost a korály
- Nedotýkej se korálu, nestůj na dně u útesu — i lehký dotek ho může zabít.
- Nekrm ani nehoň zvířata, u Dolphin House a Abu Dabab platí zpřísněná pravidla.
- Šnorchluj vždy s někým, drž se skupiny nebo lodi.

Chráněné tokeny: `["05","48–60","55–62","2","85–130","15–25","může","Rychlotaháček","Potápění","Hotel","Nezávislé","Dive","Marsa Shagra","Kam","Abu Dabab","Dolphin House","Sha'ab Samadai","Elphinstone","Ceny","Šnorchlování Abu Dabab","Potápění Elphinstone","Kurz","Cenu","Standardní","Bezpečnost","Nedotýkej","Nekrm","Šnorchluj"]`

## Design
Použij stabilní A4 mřížku všech osmi stran: nadpis oddílu, krátké obsahové bloky a jasně odlišené praktické body. Přizpůsob pouze barvy, typografický pocit, motivy a fotografie systému země: `{"palette":{"background":"#F4E9D8","primary":"#0F6473","secondary":"#C96A32","accent":"#CBA85B","text":"#201A16"},"heading_fonts":["Cormorant Garamond","Prata"],"body_fonts":["Manrope","Source Sans 3"],"motifs":["jemné vlny Rudého moře","korálové větvení","pouštní horizont","stylizované slunce"],"photo_style":"čistá tyrkysová voda, teplý pouštní písek, korálové detaily a přirozené slunce","character":"klidný prémiový red-sea editorial s kontrastem moře a pouště"}`.

## Constraints
- Přesný A4 poměr 1:1.41421356237, bezpečné okraje, žádné přetečení.
- Všechna fakta, čísla, měny, časy, data, vlastní jména, negace a varování zachovej přesně.
- Všechen text česky; žádné smyšlené názvy, loga, watermarky, cedule ani anglické popisky.
- Vytvoř jednu jedinou finální variantu.
