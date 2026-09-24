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
- Strana: `guide-07-05-two-equal-sections`
- Layout: `Two equal sections`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Výlety

- **Montserrat:** vlak R5 zpáteční 13,80 EUR + Cremallera zpáteční 14,50 EUR (jeden zdroj uvádí
  15 EUR). Kombinovaná jízdenka Trans Montserrat 50 EUR. À la carte vychází celý den orientačně
  na 36,80 EUR včetně vstupu do baziliky (8 EUR online) — tenhle součet ovšem počítá s Cremallerou
  za 15 EUR; s částkou 14,50 EUR vyjde o půl eura míň.
- **Sitges:** jízdenka od zhruba 6 EUR při nákupu předem.

### Orientační denní rozpočet

Zdroje uvádějí pro cestovatele se středním rozpočtem (tříhvězdičkový hotel, restaurace, hlavní
památky) **120–180 EUR na den**, jiné odhady 150–180 EUR, resp. průměr 179 EUR na den.

Ber to jako orientaci pro plánování, ne jako výpočet — jde o průměry ze sekundárních zdrojů bez
uvedené metodiky. Přesnější číslo si sestavíš sám z položek výše podle toho, kolik plánuješ platit
za ubytování a kolik vstupů si dáš.

Chráněné tokeny, které musí zůstat přesně: `["13,80 EUR","14,50 EUR","15 EUR","50 EUR","36,80 EUR","8 EUR","6 EUR","120–180 EUR","150–180 EUR","179 EUR","13,80","14,50","15","50","36,80","8","6","120–180","150–180","179","ne","Výlety","Montserrat","Cremallera","Kombinovaná","Trans Montserrat","Cremallerou","Sitges","Orientační","Zdroje","Ber","Přesnější","Montserrat:","Sitges:","120–180 EUR na den"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
