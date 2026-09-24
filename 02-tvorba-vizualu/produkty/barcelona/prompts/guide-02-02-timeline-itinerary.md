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
- Strana: `guide-02-02-timeline-itinerary`
- Layout: `Timeline ininerary`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Hola Barcelona Travel Card

Ceny pro zónu 1: **48 h za 18,70 EUR**, **72 h za 27,30 EUR**, **96 h za 35,60 EUR** a **120 h za
43,60 EUR**. Tyhle částky pocházejí z cestovatelského zdroje, ne přímo z ceníku provozovatele —
ověř si je před nákupem.

Karta pokrývá metro a autobusy TMB, NitBus, lanovku na Montjuïc, městskou železnici FGC v zóně 1,
tramvaj TRAM a příměstské vlaky Rodalies v zóně 1. **Nezahrnuje** lanovku Montjuïc Cable Car.

Její hlavní výhoda proti T-casual: **zahrnuje jednu cestu metrem na letiště a jednu zpět.** Tím řeší
přesně ten problém, na kterém T-casual selhává.

### Provozní doba metra

Tohle rozhoduje o tom, jak si naplánuješ večery:

- **Pondělí až čtvrtek a svátky ve všední dny:** 5:00 – půlnoc
- **Pátek a noci před svátky:** 5:00 – 2:00
- **Sobota:** od 5:00 **nepřetržitě celou noc**
- **Neděle:** provoz končí o půlnoci

Celonoční provoz běží i mimo sobotu o vybraných svátcích — v noci na 24. června (Sant Joan),
na 22. srpna (Festa Major de Gràcia), na 24. a na 26. září (La Mercè) a na Nový rok. Mimo tyhle
noci jezdí **NitBus**, který obsluhuje Barcelonu i první metropolitní prstenec; většina linek se
sbíhá na Plaça de Catalunya.

Chráněné tokeny, které musí zůstat přesně: `["48 h","72 h","96 h","120 h","5:00","2:00","24. června","22. srpna","26. září","1","48","18,70","72","27,30","96","35,60","120","43,60","5","00","00 – 2","24","22","26","ne","Hola Barcelona Travel Card\n\nCeny","Tyhle","Karta","Rodalies","Nezahrnuje","Cable Car","Její","T-casual","Tím","Provozní","Tohle","Pondělí","Pátek","Sobota","Neděle","Celonoční","Sant Joan","Festa Major","La","Nový","Mimo","Barcelonu","Catalunya","48 h za 18,70 EUR","72 h za 27,30 EUR","96 h za 35,60 EUR","zahrnuje jednu cestu metrem na letiště a jednu zpět.","Pondělí až čtvrtek a svátky ve všední dny:","Pátek a noci před svátky:","Sobota:","nepřetržitě celou noc","Neděle:","NitBus"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
