# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Marsa Alam`
- Země: `Egypt`
- Oddíl: `Výlety mimo vodu`
- Strana: `guide-06-01-two-equal-sections`
- Layout: `Two equal sections`

## Exact content contract
Na stránce smí být pouze následující obsah:

Marsa Alam není jen moře — poušť za resortem je druhá polovina zážitku a většina návštěvníků ji
kvůli plážím a potápění přehlíží. Tahle kapitola ti řekne, co tam jet a co čekat, když se pár hodin
rozhodneš strávit mimo vodu.

### Wadi El Gemal

Národní park Wadi El Gemal je hlavní poušťní cíl v okolí — kombinace hor, vádí a pobřeží s vlastními
mangrovy. Vstup pro cizince stojí orientačně 40 EGP (přepočet cca 2 EUR), pokud chceš zůstat přes
noc, kempování v parku vyjde na cca 200 EGP na osobu a noc. Zdroj:
[abughosoun.org](https://www.abughosoun.org/wgnp/). Do parku se běžně jezdí jako součást
organizovaného výletu s vyzvednutím od hotelu — samostatná doprava veřejnou dopravou tu není (viz
kapitola Výběr oblasti a doprava).

### Beduínské výlety

Součástí poušťních výletů bývá i zastávka v beduínské osadě nebo u čajového posezení — je to
turisticky zprostředkovaný kontakt, ne autentické setkání bez přípravy, ale pořád dobrý způsob, jak
získat představu o životě v poušti mimo hotelový resort. Neočekávej od toho víc, než co to je: krátkou
zastávku v rámci většího programu.

Chráněné tokeny, které musí zůstat přesně: `["2 EUR","40","2","200","jen","ne","Marsa Alam","Tahle","Wadi El Gemal\n\nNárodní","Wadi El Gemal","Vstup","Zdroj","Do","Výběr","Beduínské","Součástí","Neočekávej"]`

## Country system
`{"palette":{"background":"#F4E9D8","primary":"#0F6473","secondary":"#C96A32","accent":"#CBA85B","text":"#201A16"},"heading_fonts":["Cormorant Garamond","Prata"],"body_fonts":["Manrope","Source Sans 3"],"motifs":["jemné vlny Rudého moře","korálové větvení","pouštní horizont","stylizované slunce"],"photo_style":"čistá tyrkysová voda, teplý pouštní písek, korálové detaily a přirozené slunce","character":"klidný prémiový red-sea editorial s kontrastem moře a pouště"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
