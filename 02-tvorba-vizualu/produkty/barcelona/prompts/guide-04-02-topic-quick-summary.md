# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Barcelona`
- Země: `Španělsko`
- Oddíl: `Jídlo a pití`
- Strana: `guide-04-02-topic-quick-summary`
- Layout: `Topic and Quick summary`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Co ochutnat

- **Pa amb tomàquet** — opečený chléb potřený zralým rajčetem, zalitý olivovým olejem a osolený.
  Označovaný za symbol katalánské kuchyně.
- **Escalivada** — jedno z nejstarších katalánských jídel: pečená paprika, lilek, cibule a rajče,
  pečené přímo na uhlí.
- **Fideuà** — obdoba paelly, ale z krátkých nudlí místo rýže, s mořskými plody. Typicky katalánská.
- **Calçots** — jarní cibulka z okolí Tarragony, grilovaná na otevřeném ohni, dokud vnější vrstvy
  nezčernají a vnitřek nezměkne. Jí se společně na akcích zvaných *calçotada*. **Pozor na sezónu:
  typicky od konce prosince do března** — na letní dovolené je to informace na příště.

Řada katalánských jídel má jména v katalánštině (což je samostatný románský jazyk, ne dialekt
španělštiny) a váže se ke katalánskému svátečnímu kalendáři.

Podle zdrojů se jednotlivá jídla soustředí do různých částí města: tapas a vermut v Gotické čtvrti
a v El Born, mořské plody a rýžová jídla u vody v Barcelonetě, moderní katalánská kuchyně v Gràcii
a Eixample.

Chráněné tokeny, které musí zůstat přesně: `["ne","Co","Pa","Označovaný","Escalivada","Typicky","Tarragony","Jí","Pozor","Řada","Podle","Gotické","El Born","Barcelonetě","Eixample","Pa amb tomàquet","Fideuà","Calçots","calçotada"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
