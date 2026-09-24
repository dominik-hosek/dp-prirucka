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
- Strana: `guide-08-03-checklist`
- Layout: `Checklist`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Na místě

- Ověř si u hotelu, co přesně zahrnuje all-inclusive (voda, alkohol, kde přesně) — brožury cestovek
  bývají v tomhle bodě obecné (viz kapitola Jídlo a pití).
- Pij výhradně balenou vodu, i v resortu.
- Naplánuj si dopředu, jestli chceš zajet do Port Ghalib na večeři mimo hotel — jinde je to spíš
  výjimka, počítej s domluveným transferem.

### Rychlé shrnutí

Tenhle checklist nenahrazuje předchozí kapitoly — je to jen rychlá kontrola těsně před odjezdem.
Pokud si u některého bodu nejsi jistý, vrať se do příslušné kapitoly, kde je rozhodnutí i s
odkazem na ověření.

Chráněné tokeny, které musí zůstat přesně: `["jen","Na","Ověř","Jídlo","Pij","Naplánuj","Port Ghalib","Rychlé","Tenhle","Pokud"]`

## Country system
`{"palette":{"background":"#F4E9D8","primary":"#0F6473","secondary":"#C96A32","accent":"#CBA85B","text":"#201A16"},"heading_fonts":["Cormorant Garamond","Prata"],"body_fonts":["Manrope","Source Sans 3"],"motifs":["jemné vlny Rudého moře","korálové větvení","pouštní horizont","stylizované slunce"],"photo_style":"čistá tyrkysová voda, teplý pouštní písek, korálové detaily a přirozené slunce","character":"klidný prémiový red-sea editorial s kontrastem moře a pouště"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
