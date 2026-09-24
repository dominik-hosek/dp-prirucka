# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Marsa Alam`
- Země: `Egypt`
- Oddíl: `Výběr oblasti pobřeží a doprava po okolí`
- Strana: `guide-02-01-two-equal-sections`
- Layout: `Two equal sections`

## Exact content contract
Na stránce smí být pouze následující obsah:

Marsa Alam není město s centrem, kolem kterého se rozhoduješ, kde bydlet — je to zhruba
200kilometrový pás pobřeží s jednotlivými resorty postavenými kolem korálových útesů. Rozhodnutí,
které tu nahrazuje "kterou čtvrť/město zvolit" z jiných destinací, je **jaký typ pobřeží a jaký
typ resortu** ti sedne. Tohle rozhodnutí ovlivní zážitek i cenu víc než konkrétní hotel.

### Tři základní varianty

**Port Ghalib** je nejblíž letišti (transfer cca 15 minut) a má vlastní marínu s restauracemi,
obchody a nočním životem — nejbližší k tomu, co znáš z klasických přímořských letovisek. Hodí se,
pokud chceš mít večer kam zajít pěšky a nevadí ti rušnější prostředí.

**Severní a jižní resorty** podél pobřeží jsou typicky klidnější, izolovanější a víc zaměřené na
pláž a moře než na večerní program. Transfer z letiště je podstatně delší než do Port Ghalib —
konkrétní čas se liší resort od resortu, ověř si ho u hotelu nebo cestovky před rezervací.

**Dive campy u Marsa Shagra** jsou specializované na potápění a šnorchlování — jednodušší
ubytování, ale přímý přístup k house reefu a komunita lidí, kteří přijeli hlavně kvůli vodě. Víc
o rozdílu mezi all-inclusive resortem a dive campem najdeš v kapitole Ubytování.

### Jak se rozhodnout

Pokud chceš noční život, restaurace mimo hotel a nechceš dlouhý transfer z letiště, zvol **Port
Ghalib**. Pokud ti jde hlavně o klid a pláž a nevadí ti, že večer strávíš v resortu, zvol
**severní nebo jižní pobřeží**. Pokud je pro tebe priorita číslo jedna kvalita podmořského života
přímo od pláže a nevadí ti jednodušší vybavenost, zvol **dive camp**. Kombinace "chci noční život
i výborný house reef ve stejném resortu" tu reálně nefunguje — čím blíž centru dění, tím spíš je
reef před hotelem zatížený provozem.

Chráněné tokeny, které musí zůstat přesně: `["15","Marsa Alam","Rozhodnutí","Tohle","Tři","Port Ghalib","Hodí","Severní","Transfer","Dive","Marsa Shagra","Víc","Ubytování","Jak","Pokud","Port\nGhalib","Kombinace","Severní a jižní resorty","Dive campy u Marsa Shagra","severní nebo jižní pobřeží","dive camp"]`

## Country system
`{"palette":{"background":"#F4E9D8","primary":"#0F6473","secondary":"#C96A32","accent":"#CBA85B","text":"#201A16"},"heading_fonts":["Cormorant Garamond","Prata"],"body_fonts":["Manrope","Source Sans 3"],"motifs":["jemné vlny Rudého moře","korálové větvení","pouštní horizont","stylizované slunce"],"photo_style":"čistá tyrkysová voda, teplý pouštní písek, korálové detaily a přirozené slunce","character":"klidný prémiový red-sea editorial s kontrastem moře a pouště"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
