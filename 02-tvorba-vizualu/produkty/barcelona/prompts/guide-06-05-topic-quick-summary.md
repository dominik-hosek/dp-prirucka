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
- Strana: `guide-06-05-topic-quick-summary`
- Layout: `Topic and Quick summary`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Rychlé shrnutí

- **Bunkers del Carmel: zdarma, ale zavírá v 19:30 v létě a 17:30 v zimě.** Není to místo na západ
  slunce.
- **Sant Pau je 5 minut od Sagrady Famílie a poloprázdný.** Zdarma 23. 4. a 24. 9. Cenu si ověř,
  zdroje se rozcházejí (34 EUR vs. „od 17 EUR").
- **Parc del Laberint zdarma každou středu a neděli**, ale jen prvních 750 lidí za den.
- **Nedělní dopoledne v Sant Antoni:** knižní bazar před tržnicí a snídaně na terase.
- **Sants** jako tip na levný oběd, **Mercat de Sants** bez turistů.

Chráněné tokeny, které musí zůstat přesně: `["34 EUR","19:30","17:30","19","30","17","5","23","4","24","9","34","750","jen","Rychlé","Bunkers","Carmel","Není","Sant Pau","Sagrady Famílie","Zdarma","Cenu","Parc","Laberint","Nedělní","Sant Antoni","Sants","Mercat","Bunkers del Carmel: zdarma, ale zavírá v 19:30 v létě a 17:30 v zimě.","Sant Pau je 5 minut od Sagrady Famílie a poloprázdný.","Parc del Laberint zdarma každou středu a neděli","Nedělní dopoledne v Sant Antoni:","Mercat de Sants","od 17 EUR"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
