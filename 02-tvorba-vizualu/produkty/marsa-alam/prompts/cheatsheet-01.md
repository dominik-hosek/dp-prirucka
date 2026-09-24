# A4 cheatsheet page generation

## Use case
Jedna fyzická A4 strana taháčku k turistickému průvodci, kompaktní a rychle skenovatelná.

## Identity
- Destinace: `Marsa Alam`
- Země: `Egypt`
- Oddíl: `Vízum`
- Strana taháčku: `cheatsheet-01`

## Exact content contract
Použij výhradně tento text:

# Rychlotaháček 1 — Praktické základy

## Vízum
- E-visa (~3 dny, žádej týden dopředu) nebo visa on arrival na letišti (u přepážky banky).
- 30 dní, 1 vstup, 25–30 USD → ověř na visa2egypt.gov.eg (zdroje se rozcházejí).
- Pas platný min. 6 měsíců od vstupu + volná stránka na vízum.

## Let a doprava na místo
- RMF, přímý charter SmartWings z Prahy ~4,5 h, sezónní → ověř rozpis před koupí letenky.
- Transfer do Port Ghalib: ~15 min, 13–25 USD (~350–700 EGP).
- Severní/jižní resorty a Marsa Shagra: transfer delší, liší se → ověř u hotelu/cestovky.

## Peníze
- EGP, kurz kolísá, orientačně ~52 EGP/USD → ověř aktuální kurz před cestou.
- Bankomat: poplatek 50–100 EGP/transakce, denní limit 5 000–10 000 EGP.

## SIM a internet
- Wifi standard v resortech/dive centrech, mimo ně signál kolísá.
- SIM nejsnáz na letišti po příletu → ceny/balíčky ověř na místě.

## Zdraví a očkování
- Egypt od 2024 bez malárie (WHO), CDC profylaxi nedoporučuje → přesto ochrana proti hmyzu.
- Očkování: přeočkování, hepatitida A/B, tyfus; poušť/zvířata → zvaž vzteklinu.
- Informační přehled, ne lékařské doporučení → konzultuj s očkovacím centrem.

## Kdy jet
- Chladněji říjen–duben (~20–28 °C), horko květen–září.
- Nejvyváženější: pol. března–duben nebo pol. října–listopad.
- Zima (prosinec–únor): lepší na poušť, chladnější na vodu.

Chráněné tokeny: `["3 dny","4,5 h","15 min","20–28 °C","1","3","30","25–30","6","4,5","15","13–25","350–700","52","50–100","5","000–10","000","2024","20–28","ne","Rychlotaháček","Praktické","Vízum","E-visa","Pas","Let","Prahy","Transfer","Port Ghalib","Severní","Marsa Shagra","Peníze","Bankomat","Wifi","Zdraví","Egypt","Očkování","Informační","Kdy","Chladněji","Nejvyváženější","Zima"]`

## Design
Použij stabilní A4 mřížku všech osmi stran: nadpis oddílu, krátké obsahové bloky a jasně odlišené praktické body. Přizpůsob pouze barvy, typografický pocit, motivy a fotografie systému země: `{"palette":{"background":"#F4E9D8","primary":"#0F6473","secondary":"#C96A32","accent":"#CBA85B","text":"#201A16"},"heading_fonts":["Cormorant Garamond","Prata"],"body_fonts":["Manrope","Source Sans 3"],"motifs":["jemné vlny Rudého moře","korálové větvení","pouštní horizont","stylizované slunce"],"photo_style":"čistá tyrkysová voda, teplý pouštní písek, korálové detaily a přirozené slunce","character":"klidný prémiový red-sea editorial s kontrastem moře a pouště"}`.

## Constraints
- Přesný A4 poměr 1:1.41421356237, bezpečné okraje, žádné přetečení.
- Všechna fakta, čísla, měny, časy, data, vlastní jména, negace a varování zachovej přesně.
- Všechen text česky; žádné smyšlené názvy, loga, watermarky, cedule ani anglické popisky.
- Vytvoř jednu jedinou finální variantu.
