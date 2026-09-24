# A4 cheatsheet page generation

## Use case
Jedna fyzická A4 strana taháčku k turistickému průvodci, kompaktní a rychle skenovatelná.

## Identity
- Destinace: `Marsa Alam`
- Země: `Egypt`
- Oddíl: `Ceny navíc k balíčku`
- Strana taháčku: `cheatsheet-07`

## Exact content contract
Použij výhradně tento text:

# Rychlotaháček 07 — Rozpočet

## Ceny navíc k balíčku
| Položka | Rozptyl |
|---|---|
| Vízum (e-visa / on arrival) | 25–30 USD |
| Transfer letiště → Port Ghalib | 13–25 USD |
| Šnorchlování Abu Dabab (den) | 48–60 USD/os. |
| Šnorchlování Dolphin House (den) | 55–62 USD/os. |
| Potápění Elphinstone (2 ponory) | 85–130 USD |
| Poplatek mořského parku (na ponor) | 15–25 USD |
| Safari Wadi El Gemal (skup.–soukr.) | 90–228 USD/os. |
| Vstup NP Wadi El Gemal | ~40 EGP (≈ 2 EUR) |
| Kempování v NP (os./noc) | ~200 EGP |
| Výběr z bankomatu (poplatek) | 50–100 EGP |

Orientační rozptyly z aktuálních nabídek, ne ceníky — v Egyptě se mění rychle i s kurzem.

## Jak si postavit rozpočet
- Hlavní volba: voda, nebo kombinace s pouští — podle toho škrtej.
- Jen šnorchlování → Abu Dabab + Dolphin House + jeden poušťní výlet navíc.
- Chceš i potápět → přičti Elphinstone a poplatek parku (násobí se podle počtu ponorů, ne dní).
- Skupinové safari výrazně levnější než soukromé — soukromé jen když ti stojí za vlastní tempo.
- Přičti hotovost na drobné (voda, spropitné) a poplatek za výběr z bankomatu.

Chráněné tokeny: `["2 EUR","07","25–30","13–25","48–60","55–62","2","85–130","15–25","90–228","40","200","50–100","ne","Jen","jen","Rychlotaháček","Rozpočet","Ceny","Položka","Rozptyl","Vízum","Transfer","Port Ghalib","Šnorchlování Abu Dabab","Šnorchlování Dolphin House","Potápění Elphinstone","Poplatek","Safari Wadi El Gemal","Vstup","Wadi El Gemal","Kempování","Výběr","Orientační","Egyptě","Jak","Hlavní","Abu Dabab","Dolphin House","Chceš","Elphinstone","Skupinové","Přičti"]`

## Design
Použij stabilní A4 mřížku všech osmi stran: nadpis oddílu, krátké obsahové bloky a jasně odlišené praktické body. Přizpůsob pouze barvy, typografický pocit, motivy a fotografie systému země: `{"palette":{"background":"#F4E9D8","primary":"#0F6473","secondary":"#C96A32","accent":"#CBA85B","text":"#201A16"},"heading_fonts":["Cormorant Garamond","Prata"],"body_fonts":["Manrope","Source Sans 3"],"motifs":["jemné vlny Rudého moře","korálové větvení","pouštní horizont","stylizované slunce"],"photo_style":"čistá tyrkysová voda, teplý pouštní písek, korálové detaily a přirozené slunce","character":"klidný prémiový red-sea editorial s kontrastem moře a pouště"}`.

## Constraints
- Přesný A4 poměr 1:1.41421356237, bezpečné okraje, žádné přetečení.
- Všechna fakta, čísla, měny, časy, data, vlastní jména, negace a varování zachovej přesně.
- Všechen text česky; žádné smyšlené názvy, loga, watermarky, cedule ani anglické popisky.
- Vytvoř jednu jedinou finální variantu.
