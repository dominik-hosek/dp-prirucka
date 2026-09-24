# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Barcelona`
- Země: `Španělsko`
- Oddíl: `Doprava po městě a do okolí`
- Strana: `guide-02-05-topic-quick-summary`
- Layout: `Topic and Quick summary`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Rychlé shrnutí

- **Na letišti T-casual neplatí** — letištní jízdenka 5,90 EUR, nebo Hola Barcelona, která cestu
  na letiště a zpět obsahuje.
- **Pod ~21 jízd za 3 dny vyhrává T-casual** (1,30 EUR za jízdu) nad Hola Barcelona na 72 h.
- **V sobotu jezdí metro celou noc**, v pátek jen do 2:00.
- **Do Sitges spontánně** (spoje po 15–20 min), **do Montserratu s předem vyřešenou jízdenkou.**

Chráněné tokeny, které musí zůstat přesně: `["5,90 EUR","3 dny","1,30 EUR","72 h","15–20 min","2:00","5,90","21","3","1,30","72","2","00","15–20","jen","Rychlé","Na","T-casual","Hola Barcelona","Pod","Do Sitges","Montserratu","Na letišti T-casual neplatí","Pod ~21 jízd za 3 dny vyhrává T-casual","V sobotu jezdí metro celou noc","Do Sitges spontánně","do Montserratu s předem vyřešenou jízdenkou."]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
