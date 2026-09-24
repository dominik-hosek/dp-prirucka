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
- Strana: `guide-07-02-list-of-places`
- Layout: `List of places`

## Exact content contract
Na stránce smí být pouze následující obsah:

### MHD ve městě

- Jednotlivá jízdenka: **2,90 EUR**
- T-casual (10 jízd): **13,00 EUR** → **1,30 EUR za jízdu**
- T-usual (30 dní neomezeně): **22,80 EUR**
- Hola Barcelona: **18,70 EUR** (48 h), **27,30 EUR** (72 h), **35,60 EUR** (96 h), **43,60 EUR**
  (120 h)

Zlom mezi T-casual a Hola Barcelona na 72 hodin leží kolem 21 jízd za tři dny. Kdo jezdí míň,
s T-casual ušetří.

### Ubytování a turistická daň

Průměr napříč Barcelonou vychází v roce 2026 zhruba na **110–130 EUR za noc**, v hlavní sezóně
od května do září výrazně výš. Eixample v létě běžně **180–200 EUR za noc**. Srpen je nejdražší
měsíc — jeden zdroj uvádí průměrnou cenu pokoje až kolem 312 USD za noc (ta částka je v dolarech).
Na léto se doporučuje rezervovat 3–6 měsíců dopředu.

**A teď položka, kterou v ceně rezervace nenajdeš.** Turistická daň na osobu a noc, platná od
1. dubna 2026:

| Typ ubytování | Daň za osobu a noc |
|---|---|
| Hotel 5\* | 12,00 EUR |
| Hotel 4\* | 8,40 EUR |
| Turistické byty a apartmány | 9,50 EUR |
| Hostely | 6,00 EUR |
| Ostatní | 7,00 EUR |

Pro představu, co to dělá: **dvojice ve čtyřhvězdičkovém hotelu na pět nocí zaplatí navíc 84 EUR.**
To je víc než tři nejlevnější vstupenky do Sagrady Famílie (26 EUR).

Dvě věci, které tuhle částku srazí a samy se nepřipomenou:

- **Děti do 17 let neplatí nic** — u obou složek daně, automaticky.
- **Od osmé noci se daň dál nenačítá.**

Chráněné tokeny, které musí zůstat přesně: `["1,30 EUR","48 h","72 h","96 h","120 h","110–130 EUR","180–200 EUR","12,00 EUR","8,40 EUR","9,50 EUR","6,00 EUR","7,00 EUR","84 EUR","26 EUR","1. dubna","2,90","10","13,00","1,30","30","22,80","18,70","48","27,30","72","35,60","96","43,60","120","21","2026","110–130","180–200","312","3–6","1","5","12,00","4","8,40","9,50","6,00","7,00","84","26","17","Jednotlivá","T-casual","T-usual","Hola Barcelona","Zlom","Kdo","Ubytování","Průměr","Barcelonou","Eixample","Srpen","Na","Turistická","Typ","Daň","Hotel","Turistické","Hostely","Ostatní","Pro","To","Sagrady Famílie","Dvě","Děti","Od","2,90 EUR","13,00 EUR","1,30 EUR za jízdu","22,80 EUR","18,70 EUR","27,30 EUR","35,60 EUR","43,60 EUR","110–130 EUR za noc","180–200 EUR za noc","A teď položka, kterou v ceně rezervace nenajdeš.","dvojice ve čtyřhvězdičkovém hotelu na pět nocí zaplatí navíc 84 EUR.","Děti do 17 let neplatí nic","Od osmé noci se daň dál nenačítá."]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
