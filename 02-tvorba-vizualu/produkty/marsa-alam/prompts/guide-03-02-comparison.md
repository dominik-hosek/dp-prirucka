# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Marsa Alam`
- Země: `Egypt`
- Oddíl: `Ubytování`
- Strana: `guide-03-02-comparison`
- Layout: `Comparison`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Na co se zeptat před rezervací

- Jaký je stav house reefu a jak se k němu dostaneš — pěšky po písku, přes mělčinu, nebo je nutné
  molo/žebřík kvůli korálům až u břehu?
- Je vstup do vody z pláže, nebo je potřeba molo/platforma (časté tam, kde je reef blízko břehu a
  chodidly by se poškodil)?
- Co přesně zahrnuje all-inclusive — jen jídlo a nápoje, nebo i vybavení na šnorchlování a část
  výletů?
- Jak daleko je resort od letiště a od případného dive centra, pokud plánuješ organizované výlety
  (viz kapitola Výběr oblasti a doprava)?
- Nabízí hotel vlastní dive centrum, nebo je potřeba domlouvat výlety nezávisle? Oboje má své
  výhody — hotelové centrum je pohodlnější, nezávislé bývá levnější (viz kapitola Potápění a
  šnorchlování).

### Rychlé shrnutí

- Hlavní rozhodnutí není "kolik hvězdiček", ale all-inclusive resort vs. dive camp a kvalita house
  reefu.
- Než rezervuješ, zjisti si stav útesu před hotelem a způsob vstupu do vody — ne jen fotky z
  brožury.
- Konkrétní ceny ubytování se v čase i podle cestovky výrazně liší — porovnávej aktuální nabídky u
  prodejce balíčku.

Chráněné tokeny, které musí zůstat přesně: `["jen","ne","Na","Jaký","Je","Co","Jak","Výběr","Nabízí","Oboje","Potápění","Rychlé","Hlavní","Než","Konkrétní"]`

## Country system
`{"palette":{"background":"#F4E9D8","primary":"#0F6473","secondary":"#C96A32","accent":"#CBA85B","text":"#201A16"},"heading_fonts":["Cormorant Garamond","Prata"],"body_fonts":["Manrope","Source Sans 3"],"motifs":["jemné vlny Rudého moře","korálové větvení","pouštní horizont","stylizované slunce"],"photo_style":"čistá tyrkysová voda, teplý pouštní písek, korálové detaily a přirozené slunce","character":"klidný prémiový red-sea editorial s kontrastem moře a pouště"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
