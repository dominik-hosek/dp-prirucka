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
- Strana: `guide-01-01-two-equal-sections`
- Layout: `Two equal sections`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Vízum

Jako český občan potřebuješ do Egypta vízum. Máš dvě možnosti: **e-visa** vyřízenou předem online
(zpracování trvá orientačně 3 pracovní dny, žádej klidně týden dopředu, ať máš rezervu), nebo
**visa on arrival** přímo na letišti — platí se u přepážky banky ještě před pasovou kontrolou.
Turistické vízum je na 30 dní a na jeden vstup. Počítej s **25–30 USD**, aktuální cenu i postup si
ověř na [visa2egypt.gov.eg](https://visa2egypt.gov.eg) — zdroje se v přesné částce rozcházejí a
sazby se mění. Pas musí platit ještě aspoň 6 měsíců od vstupu do země a mít volnou stránku na
vízum — bez toho tě na letišti nepustí dál.

### Let a doprava na místo

Hlavním vstupním bodem je letiště **Marsa Alam International (RMF)**. Z Prahy tam létá přímý
charter SmartWings, let trvá zhruba 4,5 hodiny. Frekvence je sezónní — mimo hlavní sezónu linka
nemusí jet vůbec, takže si rozpis ověř přímo u dopravce nebo cestovky ještě před nákupem letenky.

Z letiště do resortu tě čeká smluvený transfer nebo taxi. Nejblíž je **Port Ghalib**, cesta trvá
zhruba 15 minut a transfer vyjde na **13–25 USD** (přibližně 350–700 EGP). Severní a jižní resorty
i dive campy u Marsa Shagra mají transfer podstatně delší — konkrétní čas i cena se liší podle
resortu, takže si to nech potvrdit u hotelu nebo cestovky předem.

Chráněné tokeny, které musí zůstat přesně: `["3","30","25–30","6","4,5","15","13–25","350–700","nemusí","Vízum\n\nJako","Egypta","Máš","Turistické","Počítej","Pas","Let","Hlavním","Marsa Alam International","Prahy","Frekvence","Nejblíž","Port Ghalib","Severní","Marsa Shagra","e-visa","visa on arrival","25–30 USD","Marsa Alam International (RMF)","13–25 USD"]`

## Country system
`{"palette":{"background":"#F4E9D8","primary":"#0F6473","secondary":"#C96A32","accent":"#CBA85B","text":"#201A16"},"heading_fonts":["Cormorant Garamond","Prata"],"body_fonts":["Manrope","Source Sans 3"],"motifs":["jemné vlny Rudého moře","korálové větvení","pouštní horizont","stylizované slunce"],"photo_style":"čistá tyrkysová voda, teplý pouštní písek, korálové detaily a přirozené slunce","character":"klidný prémiový red-sea editorial s kontrastem moře a pouště"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
