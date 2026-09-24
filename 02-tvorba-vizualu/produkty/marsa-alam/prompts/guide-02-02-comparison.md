# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Marsa Alam`
- Země: `Egypt`
- Oddíl: `Výběr oblasti pobřeží a doprava po okolí`
- Strana: `guide-02-02-comparison`
- Layout: `Comparison`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Doprava po okolí

Mezi jednotlivými resorty podél pobřeží **nejezdí pravidelná veřejná doprava** — spoléhej na
soukromý transfer nebo taxi domluvené přes hotel nebo místního dopravce. Pokud plánuješ výlet do
jiné části pobřeží (jiná pláž, jiné dive centrum), počítej s tím, že si dopravu musíš zařídit
zvlášť a předem.

Výlety na moře (šnorchlování, potápění) i do pouště se typicky prodávají jako balíček včetně
vyzvednutí přímo u hotelu — doprava je tedy součástí ceny výletu, ne položka navíc. Orientační ceny
konkrétních výletů najdeš v kapitolách Potápění a šnorchlování a Rozpočet.

Pokud uvažuješ o pronájmu auta, věz, že vzhledem k charakteru destinace (transfery a balíčky
výletů jsou standard) je to spíš okrajová varianta než běžná volba — než si auto půjčíš, ověř si
u pronajímatele podmínky i to, jestli se ti to vzhledem k plánovaným výletům vůbec vyplatí.

### Rychlé shrnutí

- Klíčové rozhodnutí není "které město", ale "jaký typ pobřeží": Port Ghalib (noční život, blízko
  letišti) vs. severní/jižní resorty (klid) vs. Marsa Shagra (dive camp, house reef).
- Čím blíž centru dění, tím spíš horší house reef přímo od pláže — kombinaci obojího nečekej.
- Mezi resorty nejezdí veřejná doprava — počítej se soukromým transferem přes hotel.

Chráněné tokeny, které musí zůstat přesně: `["ne","Doprava","Mezi","Pokud","Výlety","Orientační","Potápění","Rozpočet","Rychlé","Klíčové","Port Ghalib","Marsa Shagra","Čím","nejezdí pravidelná veřejná doprava"]`

## Country system
`{"palette":{"background":"#F4E9D8","primary":"#0F6473","secondary":"#C96A32","accent":"#CBA85B","text":"#201A16"},"heading_fonts":["Cormorant Garamond","Prata"],"body_fonts":["Manrope","Source Sans 3"],"motifs":["jemné vlny Rudého moře","korálové větvení","pouštní horizont","stylizované slunce"],"photo_style":"čistá tyrkysová voda, teplý pouštní písek, korálové detaily a přirozené slunce","character":"klidný prémiový red-sea editorial s kontrastem moře a pouště"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
