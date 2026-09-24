# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Marsa Alam`
- Země: `Egypt`
- Oddíl: `Potápění a šnorchlování`
- Strana: `guide-05-01-comparison`
- Layout: `Comparison`

## Exact content contract
Na stránce smí být pouze následující obsah:

Voda je hlavní důvod, proč se do Marsa Alam jezdí, ale nemusíš umět potápět, abys ji naplno zažil.
Tahle kapitola ti řekne, jak si vybrat výlet nezávisle nebo přes hotel, kam jet za čím a jak se
u toho nezranit a nepoškodit útes, který si přijel vidět.

### Přes hotel, nebo nezávisle

Hotel ti výlet zorganizuje pohodlně — vyzvednutí od pokoje, jazyková bariéra vyřešená, není co
plánovat. Zaplatíš za to ale víc, protože v ceně je marže recepce navíc k marži dive centra. Lokální
dive centrum (často to samé, které hotelu výlety dodává) bývá levnější, ale musíš si ho vybrat sám
a ověřit, že má vybavení v pořádku a skupiny nejsou přeplněné. Pokud bydlíš v dive campu u Marsa
Shagra (viz kapitola Ubytování), nezávislá varianta je tam standard, ne výjimka.

### Kam za čím

- **Abu Dabab** — mělčí záliv, kde se pravidelně objevují mořské želvy a dugongové. Vhodné i pro
  šnorchlaře, co se necítí jistě na hlubší vodě.
- **Dolphin House (Sha'ab Samadai)** — útes proslulý delfíny; oblíbený celodenní výlet lodí,
  vhodný pro šnorchlování i pro potápěče.
- **Elphinstone** — proslulý potápěčský reef s driftovým proudem a vyšší náročností, spíš pro
  certifikované potápěče než začátečníky.

Orientační ceny: šnorchlování Abu Dabab 48–60 USD/os., Dolphin House 55–62 USD/os., potápění
Elphinstone (2 ponory) 85–130 USD — k tomu si u Elphinstone připočti povinný poplatek mořského
parku 15–25 USD za ponor, který bývá mimo cenu výletu. Zdroj:
[viator.com](https://www.viator.com/en-GB/tours/Marsa-Alam/Abu-Dabbab-Beach-full-day-trip-with-turtles/d25556-295073P2),
[redsea-scubadiving.com](https://redsea-scubadiving.com/marsa-alam-diving-prices/).

Chráněné tokeny, které musí zůstat přesně: `["48–60","55–62","2","85–130","15–25","ne","Voda","Marsa Alam","Tahle","Přes","Hotel","Zaplatíš","Lokální","Pokud","Marsa\nShagra","Ubytování","Kam","Abu Dabab","Vhodné","Dolphin House","Sha'ab Samadai","Elphinstone","Orientační","Zdroj","Marsa-","Alam","Abu-","Dabbab-","Beach-full-day-trip-with-turtles","Dolphin House (Sha'ab Samadai)"]`

## Country system
`{"palette":{"background":"#F4E9D8","primary":"#0F6473","secondary":"#C96A32","accent":"#CBA85B","text":"#201A16"},"heading_fonts":["Cormorant Garamond","Prata"],"body_fonts":["Manrope","Source Sans 3"],"motifs":["jemné vlny Rudého moře","korálové větvení","pouštní horizont","stylizované slunce"],"photo_style":"čistá tyrkysová voda, teplý pouštní písek, korálové detaily a přirozené slunce","character":"klidný prémiový red-sea editorial s kontrastem moře a pouště"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
