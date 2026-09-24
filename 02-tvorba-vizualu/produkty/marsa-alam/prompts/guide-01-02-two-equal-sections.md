# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Marsa Alam`
- Země: `Egypt`
- Oddíl: `Praktické základy`
- Strana: `guide-01-02-two-equal-sections`
- Layout: `Two equal sections`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Peníze

Platí se egyptskou librou (EGP). Kurz vůči dolaru silně kolísá — orientačně se drž hodnoty kolem
**52 EGP za 1 USD**, ale před cestou si aktuální kurz vždy dohledej, protože se může výrazně
posunout. Výběr z bankomatu tě přijde na poplatek **50–100 EGP** za transakci a denní limit výběru
bývá **5 000–10 000 EGP** — pokud budeš potřebovat víc hotovosti najednou, počítej s víc výběry
nebo směnárnou. Přehled dalších cen najdeš v kapitole Rozpočet.

### SIM a internet

V resortech i větších dive centrech bývá wifi standardem, mimo ně signál kolísá. Lokální SIM
kartu si nejsnáz pořídíš přímo na letišti po příletu — konkrétní ceny a datové balíčky si ověř na
místě, nabídky egyptských operátorů se mění.

Chráněné tokeny, které musí zůstat přesně: `["52","1","50–100","5","000–10","000","může","Peníze\n\nPlatí","Kurz","Výběr","Přehled","Rozpočet","Lokální","52 EGP za 1 USD","50–100 EGP","5 000–10 000 EGP"]`

## Country system
`{"palette":{"background":"#F4E9D8","primary":"#0F6473","secondary":"#C96A32","accent":"#CBA85B","text":"#201A16"},"heading_fonts":["Cormorant Garamond","Prata"],"body_fonts":["Manrope","Source Sans 3"],"motifs":["jemné vlny Rudého moře","korálové větvení","pouštní horizont","stylizované slunce"],"photo_style":"čistá tyrkysová voda, teplý pouštní písek, korálové detaily a přirozené slunce","character":"klidný prémiový red-sea editorial s kontrastem moře a pouště"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
