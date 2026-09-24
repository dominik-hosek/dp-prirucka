# A4 cheatsheet page generation

## Use case
Jedna fyzická A4 strana taháčku k turistickému průvodci, kompaktní a rychle skenovatelná.

## Identity
- Destinace: `Marsa Alam`
- Země: `Egypt`
- Oddíl: `All-inclusive resort vs. dive camp`
- Strana taháčku: `cheatsheet-03`

## Exact content contract
Použij výhradně tento text:

# Rychlotaháček 3 — Ubytování

## All-inclusive resort vs. dive camp
- Většina jede přes all-inclusive CK → jídlo, pití, často i výlety v ceně.
- Dive campy (Marsa Shagra): jednodušší, bez all-inclusive, přímo u moře → může vyjít levněji.

## Proč se vybírá podle house reefu
- House reef = útes u pláže hotelu, dostupný pěšky, bez lodi a organizace.
- Kvalita se mezi resorty výrazně liší → od plného ryb po poškozený/za mělčinou.
- Pro šnorchlování bez denní organizace důležitější než hvězdičky nebo vzdálenost od letiště.

## Na co se zeptat před rezervací
- Stav house reefu a přístup → pěšky, přes mělčinu, nebo molo/žebřík?
- Vstup do vody z pláže, nebo přes molo/platformu?
- All-inclusive: jen jídlo/pití, nebo i vybavení na šnorchlování a část výletů?
- Vzdálenost od letiště a od dive centra pro plánované výlety?
- Vlastní dive centrum hotelu (pohodlnější), nebo nezávislé výlety (levnější)?

Konkrétní ceny ubytování se v čase i podle cestovky výrazně liší → porovnávej aktuální nabídky u prodejce balíčku.

Chráněné tokeny: `["3","může","jen","Rychlotaháček","Ubytování","All-inclusive","Většina","Dive","Marsa Shagra","Proč","House","Kvalita","Pro","Na","Stav","Vstup","Vzdálenost","Vlastní","Konkrétní"]`

## Design
Použij stabilní A4 mřížku všech osmi stran: nadpis oddílu, krátké obsahové bloky a jasně odlišené praktické body. Přizpůsob pouze barvy, typografický pocit, motivy a fotografie systému země: `{"palette":{"background":"#F4E9D8","primary":"#0F6473","secondary":"#C96A32","accent":"#CBA85B","text":"#201A16"},"heading_fonts":["Cormorant Garamond","Prata"],"body_fonts":["Manrope","Source Sans 3"],"motifs":["jemné vlny Rudého moře","korálové větvení","pouštní horizont","stylizované slunce"],"photo_style":"čistá tyrkysová voda, teplý pouštní písek, korálové detaily a přirozené slunce","character":"klidný prémiový red-sea editorial s kontrastem moře a pouště"}`.

## Constraints
- Přesný A4 poměr 1:1.41421356237, bezpečné okraje, žádné přetečení.
- Všechna fakta, čísla, měny, časy, data, vlastní jména, negace a varování zachovej přesně.
- Všechen text česky; žádné smyšlené názvy, loga, watermarky, cedule ani anglické popisky.
- Vytvoř jednu jedinou finální variantu.
