# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Marsa Alam`
- Země: `Egypt`
- Oddíl: `Jídlo a pití`
- Strana: `guide-04-02-two-equal-sections`
- Layout: `Two equal sections`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Ceny

Konkrétní ceny jídla a pití mimo resort se nám nepodařilo spolehlivě dohledat — u jednotlivých
podniků v Port Ghalib i jinde se hodně liší a rychle se mění. Orientační ceny výletů, které jídlo
zahrnují, najdeš v kapitole Rozpočet; cenu konkrétní restaurace nebo baru si ověř až na místě.

### Rychlé shrnutí

- Naprostá většina jídla je řešená přes all-inclusive — rozsah balíčku (voda, alkohol, kde přesně)
  si ověř u hotelu předem, ne z brožury.
- Pij výhradně balenou vodu, i v resortu.
- Restaurace mimo hotel reálně dávají smysl hlavně v Port Ghalib — jinde počítej s transferem nebo
  se spolehni na hotel.

Chráněné tokeny, které musí zůstat přesně: `["ne","Ceny\n\nKonkrétní","Port Ghalib","Orientační","Rozpočet","Rychlé","Naprostá","Pij","Restaurace"]`

## Country system
`{"palette":{"background":"#F4E9D8","primary":"#0F6473","secondary":"#C96A32","accent":"#CBA85B","text":"#201A16"},"heading_fonts":["Cormorant Garamond","Prata"],"body_fonts":["Manrope","Source Sans 3"],"motifs":["jemné vlny Rudého moře","korálové větvení","pouštní horizont","stylizované slunce"],"photo_style":"čistá tyrkysová voda, teplý pouštní písek, korálové detaily a přirozené slunce","character":"klidný prémiový red-sea editorial s kontrastem moře a pouště"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
