# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Barcelona`
- Země: `Španělsko`
- Oddíl: `Památky, výlety a itineráře`
- Strana: `guide-05-07-comparison`
- Layout: `Comparison`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Rychlé shrnutí

- **Ověř si stav Sagrady Famílie před cestou** — zdroje si odporují a náhradou je Sant Pau
  pět minut odtud.
- **Park Güell: slot, 30 minut na vstup, bez návratu, 1 400 lidí za hodinu.**
- **Museu Picasso zdarma vyžaduje rezervaci 4 dny dopředu v 10:00**, MNAC ne.
- **MNAC v sobotu po 15:00 zdarma** je nejméně známá bezplatná varianta ve městě.
- **Camp Nou se přestavuje** — je to muzeum a imerzivní prohlídka, ne celý stadion.
- Kupuj **na oficiálních webech**, přes prodejce se ceny výrazně liší.

Chráněné tokeny, které musí zůstat přesně: `["4 dny","10:00","15:00","30","1","400","4","10","00","15","ne","Rychlé","Ověř","Sagrady Famílie","Sant Pau","Park","Museu Picasso","Camp Nou","Kupuj","Ověř si stav Sagrady Famílie před cestou","Park Güell: slot, 30 minut na vstup, bez návratu, 1 400 lidí za hodinu.","Museu Picasso zdarma vyžaduje rezervaci 4 dny dopředu v 10:00","MNAC v sobotu po 15:00 zdarma","Camp Nou se přestavuje","na oficiálních webech"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
