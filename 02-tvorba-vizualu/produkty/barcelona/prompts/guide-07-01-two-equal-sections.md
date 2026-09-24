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
- Strana: `guide-07-01-two-equal-sections`
- Layout: `Two equal sections`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Cesta

- **Zpáteční letenka Praha – Barcelona:** průměrně kolem 3 500 Kč. Ceny 1 500–2 500 Kč se považují
  za výhodné, akční nabídky výjimečně i pod 1 500 Kč, nejnižší uváděná částka od 1 180 Kč při včasné
  rezervaci. Létá 5 přímých spojů denně, doba letu 2 hodiny 25 minut. Doporučuje se rezervovat
  aspoň 3 týdny dopředu.

Pozor, tohle je jediná položka v Kč — všechno ostatní je v eurech a nesčítej si to dohromady bez
přepočtu.

### Z letiště do centra

- **Aerobús:** 7,45 EUR jednosměrně, 12,85 EUR zpáteční
- **Metro L9 (letištní jízdenka):** 5,90 EUR
- **Městský autobus 46:** cca 2,65 EUR
- **Taxi:** orientačně 30–40 EUR přes den, minimální jízdné z letiště 21 EUR včetně příplatků

Rozdíl mezi městským autobusem a taxíkem je řádový — 2,65 EUR proti minimálně 21 EUR — a je to
nejjednodušší úspora hned první den (detail v kapitole Doprava po městě a do okolí).

Chráněné tokeny, které musí zůstat přesně: `["500 Kč","180 Kč","7,45 EUR","12,85 EUR","5,90 EUR","2,65 EUR","30–40 EUR","21 EUR","3","500","1","500–2","180","5","2","25","7,45","12,85","5,90","46","2,65","30–40","21","minimálně","Cesta","Zpáteční","Praha","Barcelona","Kč","Ceny","Létá","Doporučuje","Pozor","Aerobús","Metro","Městský","Taxi","Rozdíl","Doprava","Zpáteční letenka Praha – Barcelona:","Aerobús:","Metro L9 (letištní jízdenka):","Městský autobus 46:","Taxi:"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
