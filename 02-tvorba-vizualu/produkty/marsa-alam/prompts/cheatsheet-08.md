# A4 cheatsheet page generation

## Use case
Jedna fyzická A4 strana taháčku k turistickému průvodci, kompaktní a rychle skenovatelná.

## Identity
- Destinace: `Marsa Alam`
- Země: `Egypt`
- Oddíl: `Doklady a vízum`
- Strana taháčku: `cheatsheet-08`

## Exact content contract
Použij výhradně tento text:

# Rychlotaháček 08 — Checklist před odjezdem

## Doklady a vízum
- [ ] Pas platný min. 6 měsíců od vstupu, s volnou stránkou na vízum.
- [ ] Vízum vyřízené — e-visa (~3 prac. dny, žádej týden dopředu) nebo hotovost na visa on arrival.
- [ ] Aktuální cenu víza ověř na visa2egypt.gov.eg těsně před cestou.

## Zdraví a pojištění
- [ ] Zkontroluj doporučená očkování (hepatitida A/B, tyfus, případně vzteklina do pouště).
- [ ] Potápění nebo kurz → ověř u pojišťovny, jestli tě pojištění na potápění vůbec kryje.

## Peníze
- [ ] Platební karta + trocha hotovosti v USD/EUR na drobné a vízum on arrival.
- [ ] Počítej s poplatkem za výběr z bankomatu a kolísáním kurzu EGP — neměň větší částku najednou.

## Výlety a voda
- [ ] Před rezervací výletu porovnej hotel vs. nezávislé dive centrum/cestovku.
- [ ] Zabal reef-safe krém a vybavení na šnorchlování, pokud ho hotel nezapůjčuje.

## Na místě
- [ ] Ověř u hotelu, co přesně zahrnuje all-inclusive (voda, alkohol, kde přesně).
- [ ] Pij výhradně balenou vodu, i v resortu.
- [ ] Naplánuj dopředu večeři mimo hotel v Port Ghalib, počítej s domluveným transferem.

Chráněné tokeny: `["08","6","3","Rychlotaháček","Checklist","Doklady","Pas","Vízum","Aktuální","Zdraví","Zkontroluj","Potápění","Peníze","Platební","Počítej","Výlety","Před","Zabal","Na","Ověř","Pij","Naplánuj","Port Ghalib"]`

## Design
Použij stabilní A4 mřížku všech osmi stran: nadpis oddílu, krátké obsahové bloky a jasně odlišené praktické body. Přizpůsob pouze barvy, typografický pocit, motivy a fotografie systému země: `{"palette":{"background":"#F4E9D8","primary":"#0F6473","secondary":"#C96A32","accent":"#CBA85B","text":"#201A16"},"heading_fonts":["Cormorant Garamond","Prata"],"body_fonts":["Manrope","Source Sans 3"],"motifs":["jemné vlny Rudého moře","korálové větvení","pouštní horizont","stylizované slunce"],"photo_style":"čistá tyrkysová voda, teplý pouštní písek, korálové detaily a přirozené slunce","character":"klidný prémiový red-sea editorial s kontrastem moře a pouště"}`.

## Constraints
- Přesný A4 poměr 1:1.41421356237, bezpečné okraje, žádné přetečení.
- Všechna fakta, čísla, měny, časy, data, vlastní jména, negace a varování zachovej přesně.
- Všechen text česky; žádné smyšlené názvy, loga, watermarky, cedule ani anglické popisky.
- Vytvoř jednu jedinou finální variantu.
