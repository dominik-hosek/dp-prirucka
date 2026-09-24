# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Marsa Alam`
- Země: `Egypt`
- Oddíl: `Praktický checklist před odjezdem`
- Strana: `guide-08-02-two-equal-sections`
- Layout: `Two equal sections`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Peníze

- Vezmi si platební kartu i trochu hotovosti v USD nebo EUR na drobné výdaje a vízum on arrival,
  pokud ho neřešíš e-visou předem.
- Počítej s poplatkem za výběr z bankomatu a s tím, že kurz EGP silně kolísá — nevyměňuj větší
  částku najednou bez ověření aktuálního kurzu (viz kapitola Praktické základy).

### Výlety a voda

- Než rezervuješ jakýkoli výlet na moře nebo do pouště, porovnej nabídku hotelu s nezávislým dive
  centrem nebo cestovkou (viz kapitoly Potápění a šnorchlování, Výlety mimo vodu, Rozpočet).
- Zabal reef-safe opalovací krém a vybavení na šnorchlování, pokud ho hotel nezapůjčuje — usnadní ti
  to ochranu korálů i vlastní pohodlí.

Chráněné tokeny, které musí zůstat přesně: `["Peníze","Vezmi","Počítej","Praktické","Výlety","Než","Potápění","Rozpočet","Zabal"]`

## Country system
`{"palette":{"background":"#F4E9D8","primary":"#0F6473","secondary":"#C96A32","accent":"#CBA85B","text":"#201A16"},"heading_fonts":["Cormorant Garamond","Prata"],"body_fonts":["Manrope","Source Sans 3"],"motifs":["jemné vlny Rudého moře","korálové větvení","pouštní horizont","stylizované slunce"],"photo_style":"čistá tyrkysová voda, teplý pouštní písek, korálové detaily a přirozené slunce","character":"klidný prémiový red-sea editorial s kontrastem moře a pouště"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
