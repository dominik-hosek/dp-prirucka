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
- Strana: `guide-02-04-two-equal-sections`
- Layout: `Two equal sections`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Výlety z města vlakem

**Montserrat** je nejnáročnější na plánování, protože se skládá ze dvou úseků. Vlak **R5** společnosti
FGC z Plaça Espanya stojí 6,90 EUR jednosměrně a 13,80 EUR zpáteční. Nahoru se pak dostaneš buď
ozubnicovou dráhou **Cremallera** (dospělí 8,70 EUR jednosměrně, 14,50 EUR zpáteční; děti 4–13 let
4,35 a 7,25 EUR), nebo lanovkou **Aeri**. U zpáteční Cremallery se zdroje rozcházejí — objevuje se
i 15 EUR, takže si cenu ověř.

Existuje kombinovaná jízdenka **Trans Montserrat za 50 EUR**, která zahrnuje zpáteční R5 z Plaça
Espanya do Monistrol de Montserrat nebo Montserrat-Aeri a výstup Cremallerou i lanovkou.
**Automaticky to ale úspora není** — à la carte vychází celý den orientačně na 36,80 EUR včetně
vstupu do baziliky (8 EUR online). Porovnej to podle toho, co reálně využiješ.

**Sitges** je opak: dá se tam vyrazit spontánně. Linka Rodalies **R2 Sud** ze Sants, Passeig de
Gràcia nebo Estació de França jede 30–40 minut, spoje jezdí po 15–20 minutách a jízdenka stojí
od zhruba 6 EUR při nákupu předem.

**Tarragona** je na lince Rodalies **R14** ze Sants nebo Passeig de Gràcia, cesta trvá 1 až
1,5 hodiny.

**Girona a Figueres** jsou dostupné příměstskými vlaky Rodalies. Jediný údaj o ceně, který se nám
podařilo dohledat, je uvedený v dolarech (kolem 12 USD jedním směrem) a nerozlišuje mezi příměstským
a rychlým vlakem, které se cenou i časem výrazně liší — konkrétní eurovou částku si proto ověř
u Renfe nebo Rodalies.

### Tip navíc

Pokud plánuješ výlet mimo zónu 1, ověř si předem, do které zóny cíl spadá — zónové zařazení
jednotlivých výletů se nám doložit nepodařilo a rozdíl mezi jednozónovou a dvouzónovou T-casual je
12,50 EUR.

Chráněné tokeny, které musí zůstat přesně: `["6,90 EUR","13,80 EUR","8,70 EUR","14,50 EUR","7,25 EUR","15 EUR","36,80 EUR","8 EUR","6 EUR","12,50 EUR","6,90","13,80","8,70","14,50","4–13","4,35","7,25","15","50","36,80","8","30–40","15–20","6","1","1,5","12","12,50","Výlety","Montserrat","Vlak","Espanya","Nahoru","Cremallera","Aeri","Cremallery","Existuje","Trans Montserrat","Monistrol","Montserrat-","Cremallerou","Automaticky","Porovnej","Sitges","Linka Rodalies","Sud","Sants","Passeig","Estació","Tarragona","Rodalies","Girona","Figueres","Jediný","Renfe","Tip","Pokud","T-casual","R5","Trans Montserrat za 50 EUR","Automaticky to ale úspora není","R2 Sud","R14","Girona a Figueres"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
