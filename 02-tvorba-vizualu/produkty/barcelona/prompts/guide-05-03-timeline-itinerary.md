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
- Strana: `guide-05-03-timeline-itinerary`
- Layout: `Timeline ininerary`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Park Güell — nejvíc pravidel na jednom místě

Vstupné je **18 EUR**, děti 7–12 let a senioři 65+ platí **13,50 EUR**, děti do 6 let a držitelé
průkazu ZTP mají zdarma (doprovod 13,50 EUR). Kombinovaná vstupenka MUHBA / Ruta del Modernisme
stojí 14,50 EUR. Ceny jsou včetně 21% DPH.

Tři pravidla, která rozhodnou o tom, jestli se dovnitř dostaneš:

1. **Vstup je na časový slot a po čase na vstupence máš 30 minut na to, abys prošel dovnitř.**
   Potom vstupenka propadá. Uvnitř už časový limit není.
2. **Jakmile jednou vyjdeš ven, nemůžeš se vrátit.**
3. **Kapacita je 1 400 návštěvníků za hodinu** a rezervace předem se doporučuje.

Vstupenky pro turisty jsou dostupné mezi 9:30 a 19:30. Časy 7:00–9:30 a 20:00–22:00 jsou vyhrazené
pro místní.

### Gaudí v Eixample

**Casa Batlló** — základní návštěva „Blue" od **29 EUR** online (vstup, audioprůvodce, Gaudí Cube),
„Silver" od 38 EUR navíc s terasou, „Gold" od 43 EUR navíc s tabletem, Gaudí Dome, pokojem konsjerže
a soukromými pokoji.

**La Pedrera (Casa Milà)** — denní návštěva „Essential La Pedrera" od **25 EUR** online
(audioprůvodce, střecha, podkroví s výstavou o Gaudím, byt nájemníků). Mladí 12–17 let 12,50 EUR,
děti do 11 let zdarma. **Noční zážitek stojí 39 EUR**, varianta při východu slunce 39,50 EUR.

U obou platí, že ceny jsou uvedené jako „od" — jde o dynamické ceny podle termínu a pocházejí ze
sekundárních zdrojů. Ověř si je na oficiálních webech (casabatllo.org, lapedrera.com).

Chráněné tokeny, které musí zůstat přesně: `["13,50 EUR","14,50 EUR","21%","38 EUR","43 EUR","12,50 EUR","39,50 EUR","9:30","19:30","7:00","20:00","22:00","18","7–12","65","13,50","6","14,50","21","1","30","2","3","400","9","19","7","00–9","20","00–22","00","29","38","43","25","12–17","12,50","11","39","39,50","Park","Vstupné","Kombinovaná","Ruta","Modernisme","Ceny","Tři","Vstup","Potom","Uvnitř","Jakmile","Kapacita","Vstupenky","Časy","Gaudí","Eixample","Casa Batlló","Blue","Gaudí Cube","Silver","Gold","Gaudí Dome","La Pedrera","Casa","Essential La Pedrera","Gaudím","Mladí","Noční","Ověř","18 EUR","Vstup je na časový slot a po čase na vstupence máš 30 minut na to, abys prošel dovnitř.","Jakmile jednou vyjdeš ven, nemůžeš se vrátit.","Kapacita je 1 400 návštěvníků za hodinu","29 EUR","La Pedrera (Casa Milà)","25 EUR","Noční zážitek stojí 39 EUR","Silver\" od 38 EUR navíc s terasou, „Gold","od"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
