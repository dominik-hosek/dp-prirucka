# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Barcelona`
- Země: `Španělsko`
- Oddíl: `Rozpočet`
- Strana: `guide-07-04-timeline-itinerary`
- Layout: `Timeline ininerary`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Vstupné

- **Sagrada Família:** 26 EUR (audioprůvodce) až 40 EUR (s průvodcem a věžemi) — pokud bude otevřená,
  viz kapitola Památky, výlety a itineráře
- **Park Güell:** 18 EUR, děti 7–12 a senioři 13,50 EUR
- **Casa Batlló:** od 29 EUR · **La Pedrera:** od 25 EUR (noční 39 EUR)
- **Museu Picasso:** 12 EUR stálá expozice, 14 EUR s výstavou (zdroje se rozcházejí, jiné uvádí
  15 a 19 EUR)
- **Camp Nou / muzeum FC Barcelona:** 28 EUR dospělí, 21 EUR děti 6–13 a senioři
- **Recinte Modernista de Sant Pau:** 34 EUR podle jednoho zdroje, jiný uvádí „od 17 EUR" — ověř si
- **Parc del Laberint d'Horta:** 2,23 EUR (jeden zdroj uvádí 2,50 EUR), zdarma ve středu a v neděli
- **Bunkers del Carmel:** zdarma

**Gaudí je největší jednotlivá položka celého pobytu.** Kompletní obhlídka šesti hlavních Gaudího
památek UNESCO vyjde podle zdroje na **125–147 EUR na osobu** — víc než letenka z Prahy v akci.
Běžná kulturní atrakce se přitom pohybuje kolem 15–25 EUR.

Levnější varianta téhož: **Sant Pau, Parc del Laberint a Bunkers del Carmel** dají modernismus
a výhledy za zlomek ceny (viz kapitola Off the beaten path).

### Kolik toho dokážeš dostat zdarma

- **První neděle v měsíci:** Museu Picasso, Museu Blau, MNAC, Museu del Disseny a CCCB
- **MNAC v sobotu po 15:00** a o katalánských svátcích
- **Parc del Laberint každou středu a neděli**
- **Sant Pau 23. dubna a 24. září**
- **Bunkers del Carmel vždycky**

Detaily a podmínky (hlavně rezervace u Museu Picasso) jsou v kapitolách Památky, výlety a itineráře
a Off the beaten path.

Chráněné tokeny, které musí zůstat přesně: `["26 EUR","40 EUR","18 EUR","13,50 EUR","29 EUR","25 EUR","39 EUR","12 EUR","14 EUR","19 EUR","28 EUR","21 EUR","34 EUR","2,23 EUR","2,50 EUR","125–147 EUR","15–25 EUR","15:00","23. dubna","24. září","26","40","18","7–12","13,50","29","25","39","12","14","15","19","28","21","6–13","34","17","2,23","2,50","125–147","15–25","00","23","24","Vstupné","Sagrada Família","Památky","Park","Casa Batlló","La Pedrera","Museu Picasso","Camp Nou","Barcelona","Recinte Modernista","Sant Pau","Parc","Laberint","Horta","Bunkers","Carmel","Gaudí","Kompletní","Gaudího","Prahy","Běžná","Levnější","Off","Kolik","První","Museu Blau","Museu","Disseny","Detaily","Sagrada Família:","Park Güell:","Casa Batlló:","La Pedrera:","Museu Picasso:","Camp Nou / muzeum FC Barcelona:","Recinte Modernista de Sant Pau:","Parc del Laberint d'Horta:","Bunkers del Carmel:","Gaudí je největší jednotlivá položka celého pobytu.","125–147 EUR na osobu","Sant Pau, Parc del Laberint a Bunkers del Carmel","První neděle v měsíci:","MNAC v sobotu po 15:00","Parc del Laberint každou středu a neděli","Sant Pau 23. dubna a 24. září","Bunkers del Carmel vždycky","od 17 EUR"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
