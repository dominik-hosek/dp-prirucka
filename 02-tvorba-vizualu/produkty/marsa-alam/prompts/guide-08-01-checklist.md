# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Marsa Alam`
- Země: `Egypt`
- Oddíl: `Praktický checklist před odjezdem`
- Strana: `guide-08-01-checklist`
- Layout: `Checklist`

## Exact content contract
Na stránce smí být pouze následující obsah:

Poslední kapitola shrnuje, co si zkontrolovat a zařídit před cestou — ne nové informace, ale
připomenutí toho, co už víš z předchozích kapitol, na jednom místě k odškrtání.

### Doklady a vízum

- Pas platný minimálně 6 měsíců od vstupu do Egypta, s volnou stránkou na vízum.
- Vízum vyřízené — buď e-visa předem (počítej s cca 3 pracovními dny na zpracování, žádej klidně
  týden dopředu), nebo hotovost na visa on arrival přímo na letišti. Aktuální cenu ověř na
  [visa2egypt.gov.eg](https://visa2egypt.gov.eg) těsně před cestou (viz kapitola Praktické
  základy).

### Zdraví a pojištění

- Zkontroluj doporučená očkování (hepatitida A/B, tyfus, případně vzteklina při plánu do pouště) u
  očkovacího centra v dostatečném předstihu.
- Pokud plánuješ potápění nebo kurz, ověř si u pojišťovny, jestli tvoje cestovní pojištění potápění
  vůbec kryje — standardní balíčky to často nepokrývají (viz kapitola Potápění a šnorchlování).

Chráněné tokeny, které musí zůstat přesně: `["6","3","ne","minimálně","Poslední","Doklady","Pas","Egypta","Vízum","Aktuální","Praktické","Zdraví","Zkontroluj","Pokud","Potápění"]`

## Country system
`{"palette":{"background":"#F4E9D8","primary":"#0F6473","secondary":"#C96A32","accent":"#CBA85B","text":"#201A16"},"heading_fonts":["Cormorant Garamond","Prata"],"body_fonts":["Manrope","Source Sans 3"],"motifs":["jemné vlny Rudého moře","korálové větvení","pouštní horizont","stylizované slunce"],"photo_style":"čistá tyrkysová voda, teplý pouštní písek, korálové detaily a přirozené slunce","character":"klidný prémiový red-sea editorial s kontrastem moře a pouště"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
