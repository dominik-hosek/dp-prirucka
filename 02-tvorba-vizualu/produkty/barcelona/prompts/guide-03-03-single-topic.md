# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Barcelona`
- Země: `Španělsko`
- Oddíl: `Ubytování`
- Strana: `guide-03-03-single-topic`
- Layout: `Single topic`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Ceny a rezervace

Průměr napříč Barcelonou vychází v roce 2026 zhruba na **110–130 EUR za noc**, s prudkým nárůstem
v hlavní sezóně od května do září. **Srpen je nejdražší měsíc** — jeden zdroj uvádí průměrnou cenu
pokoje až kolem 312 USD za noc (pozor, ta částka je v dolarech, ne v eurech). Na léto se doporučuje
rezervovat **3 až 6 měsíců dopředu**.

Ke všem těmto cenám **připočítej turistickou daň**, která se od 1. dubna 2026 zvýšila a v ceně
rezervace obvykle není — detail sazeb je v kapitole Praktické základy, dopad na rozpočet v kapitole
Rozpočet.

Jedna věc, která se snadno přehlédne: **u turistického apartmánu je daň 9,50 EUR na osobu a noc,
u čtyřhvězdičkového hotelu 8,40 EUR.** Apartmán, který na první pohled vypadá levněji, si tím část
rozdílu vezme zpátky.

Chráněné tokeny, které musí zůstat přesně: `["110–130 EUR","9,50 EUR","8,40 EUR","1. dubna","2026","110–130","312","3","6","1","9,50","8,40","ne","obvykle","Ceny","Průměr","Barcelonou","Srpen","Na","Ke","Praktické","Rozpočet","Jedna","Apartmán","110–130 EUR za noc","Srpen je nejdražší měsíc","3 až 6 měsíců dopředu","připočítej turistickou daň"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
