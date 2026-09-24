# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Barcelona`
- Země: `Španělsko`
- Oddíl: `Off the beaten path`
- Strana: `guide-06-02-timeline-itinerary`
- Layout: `Timeline ininerary`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Recinte Modernista de Sant Pau — druhá velká modernistická památka

Areál od Lluíse Domènecha i Montanera, památka UNESCO, do roku 2009 fungoval jako nemocnice.
**Je pět minut chůze od Sagrady Famílie a má výrazně menší davy.**

To je nejlepší poměr užitku k námaze v celé Barceloně: kdo si po Sagradě myslí, že modernismus
už viděl, míjí druhou velkou modernistickou památku doslova za rohem — a v případě, že by Sagrada
byla zavřená (viz kapitola Památky, výlety a itineráře), je to přirozená náhrada.

Vstupné jeden zdroj uvádí jako **34 EUR** základní, 27 EUR pro seniory 65+ a 12 EUR pro děti 3–11 let,
s tím že děti do 12 let a držitelé průkazu ZTP mají zdarma. Jiný zdroj ale mluví o vstupu „od 17 EUR".
Rozdíl je dvojnásobný a může jít o různé typy vstupenky — **cenu si ověř na santpaubarcelona.org
před cestou**, tady ti ji netvrdíme.

Otevírací doba je **duben–říjen 9:30–18:30** a **listopad–březen 9:30–17:00**, pokladna zavírá
30 minut před koncem. Otevřeno je celý rok kromě 25. prosince.

A jedna položka, která u památky za desítky eur není detail: **vstup je zdarma na Sant Jordi
(23. dubna) a na La Mercè (24. září).**

Chráněné tokeny, které musí zůstat přesně: `["27 EUR","12 EUR","9:30","18:30","17:00","25. prosince","23. dubna","24. září","2009","34","27","65","12","3–11","17","9","30–18","30","30–17","00","25","23","24","může","Recinte Modernista","Sant Pau","Areál","Lluíse","Montanera","Je","Sagrady Famílie","To","Barceloně","Sagradě","Sagrada","Památky","Vstupné","Jiný","Rozdíl","Otevírací","Otevřeno","Sant Jordi","La","Je pět minut chůze od Sagrady Famílie a má výrazně menší davy.","34 EUR","duben–říjen 9:30–18:30","listopad–březen 9:30–17:00","od 17 EUR"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
