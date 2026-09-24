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
- Strana: `guide-02-03-topic-quick-summary`
- Layout: `Topic and Quick summary`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Taxi

Sazby v metropolitní oblasti Barcelony platné od ledna 2026 (pro rok 2026 se zvedly o 2,3 %):

- **Nástupní sazba: 2,80 EUR**
- **Za kilometr: 1,35 EUR** (denní tarif T1), **1,66 EUR** (noční a sváteční tarif T2)
- **Příplatek za letiště: 4,60 EUR**
- **Minimální jízdné z letiště: 21 EUR** včetně všech příplatků
- Pevná sazba **46 EUR** mezi letištěm a přístavním molem Moll Adossat

Pokud jedeš o Vánocích, na Nový rok nebo na Sant Joan, počítej s tím, že příplatky se v roce 2026
zvyšují až o 30 %.

Chráněné tokeny, které musí zůstat přesně: `["2,3 %","30 %","2026","2,3","2,80","1,35","1,66","4,60","21","46","30","Taxi\n\nSazby","Barcelony","Nástupní","Za","Příplatek","Minimální","Pevná","Moll Adossat\n\nPokud","Vánocích","Nový","Sant Joan","Nástupní sazba: 2,80 EUR","Za kilometr: 1,35 EUR","1,66 EUR","Příplatek za letiště: 4,60 EUR","Minimální jízdné z letiště: 21 EUR","46 EUR"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
