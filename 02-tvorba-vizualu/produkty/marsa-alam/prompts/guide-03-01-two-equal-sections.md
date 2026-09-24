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
- Strana: `guide-03-01-two-equal-sections`
- Layout: `Two equal sections`

## Exact content contract
Na stránce smí být pouze následující obsah:

V Marsa Alam se ubytování nevybírá primárně podle hvězdiček nebo polohy jako v jiných destinacích
— rozhoduje hlavně to, co je přímo pod hladinou před hotelem. Tahle kapitola ti řekne, na co se
ptát před rezervací, ne který konkrétní hotel zvolit.

### All-inclusive resort vs. dive camp

Naprostá většina návštěvníků jede přes **all-inclusive balíček** cestovní kanceláře — jídlo, pití
a často i část výletů jsou v ceně, a pro rodinu nebo pár, co chce mít dovolenou vyřešenou předem,
je to pohodlná volba. Této realitě se věnuje kapitola Jídlo a pití.

Alternativou jsou **dive campy**, typické hlavně pro oblast Marsa Shagra — jednodušší ubytování
(často bez all-inclusive konceptu), ale postavené kolem přímého přístupu k moři a komunity lidí,
co tam jsou hlavně kvůli potápění a šnorchlování. Pokud je pro tebe voda hlavní náplní dovolené a
nepotřebuješ hotelový komfort, dive camp ti může sedět víc než klasický resort — i za nižší cenu.

### Proč se vybírá podle "house reef"

House reef je korálový útes přímo u pláže hotelu, kam se dostaneš pěšky nebo pár záběry od
břehu — bez lodi, bez organizovaného výletu. Kvalita house reefu se mezi resorty výrazně liší:
někde je útes v dobrém stavu a plný ryb hned od pláže, jinde je poškozený nebo je potřeba přejít
kus mělčiny, než se k němu dostaneš. Pro personu, co chce šnorchlovat bezpečně a bez organizování
výletu každý den, je tohle důležitější kritérium než hvězdičky nebo vzdálenost od letiště.

Chráněné tokeny, které musí zůstat přesně: `["ne","může","Marsa Alam","Tahle","All-inclusive","Naprostá","Této","Jídlo","Alternativou","Marsa Shagra","Pokud","Proč","House","Kvalita","Pro","all-inclusive balíček","dive campy"]`

## Country system
`{"palette":{"background":"#F4E9D8","primary":"#0F6473","secondary":"#C96A32","accent":"#CBA85B","text":"#201A16"},"heading_fonts":["Cormorant Garamond","Prata"],"body_fonts":["Manrope","Source Sans 3"],"motifs":["jemné vlny Rudého moře","korálové větvení","pouštní horizont","stylizované slunce"],"photo_style":"čistá tyrkysová voda, teplý pouštní písek, korálové detaily a přirozené slunce","character":"klidný prémiový red-sea editorial s kontrastem moře a pouště"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
