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
- Strana: `guide-06-03-timeline-itinerary`
- Layout: `Timeline ininerary`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Parc del Laberint d'Horta — nejstarší zahrada ve městě

Historická zahrada z 18. století ve čtvrti Horta-Guinardó, nejstarší v Barceloně. Skutečné bludiště
ze stříhaných cypřišů a stinné zahrady.

Vstupné je **2,23 EUR**, snížené 1,42 EUR (jeden zdroj uvádí 2,50 EUR, takže drobný rozdíl ověř
na místě). **Zdarma je každou středu a neděli**, dále pro nezaměstnané, seniory, děti do 5 let,
obyvatele čtvrti Horta a 24. září na Festes de La Mercè.

Otevírací doba: **1. listopadu – 31. března od 10:00 do 19:00**, **1. dubna – 30. října od 10:00
do 20:00**.

Jedna věc, kterou seznamy „hidden gems" neuvádějí a která rozhoduje: **denní strop je 750
návštěvníků.** Jakmile se naplní, dovnitř se už nedostaneš — takže na bezplatnou středu nebo neděli
choď spíš dopoledne.

Chráněné tokeny, které musí zůstat přesně: `["1,42 EUR","2,50 EUR","10:00","19:00","20:00","24. září","1. listopadu","31. března","1. dubna","30. října","18","2,23","1,42","2,50","5","24","1","31","10","00","19","30","20","750","Parc","Laberint","Horta","Historická","Horta-","Guinardó","Barceloně","Skutečné","Vstupné","Zdarma","Festes","La","Otevírací","Jedna","Jakmile","2,23 EUR","Zdarma je každou středu a neděli","1. listopadu – 31. března od 10:00 do 19:00","hidden gems"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
