# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Barcelona`
- Země: `Španělsko`
- Oddíl: `Jídlo a pití`
- Strana: `guide-04-01-timeline-itinerary`
- Layout: `Timeline ininerary`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Kdy se tu jí

Španělský denní rytmus je posunutý a je to první věc, o kterou se cizinec zbytečně připraví.

- **Oběd se podává od 13:30 do 16:00**, špička je kolem 14:00.
- **Večeře (*sopar*) málokdy před 20:30**, běžně se protahuje do 22:00 a dál.
- **Nedělní *vermut* mezi 12:00 a 14:00** je popisovaný jako nejvíc „místní" chvíle, kterou v Barceloně
  můžeš mít — je to společenská tradice, ne jen nápoj. A nestojí nic navíc ani nepotřebuje rezervaci.

Kdo přijde na večeři v sedm, najde otevřeno hlavně tam, kde se vaří pro turisty.

### Menú del día — nejsilnější úspora, jakou v Barceloně máš

Polední **menú del día** stojí zhruba **10–15 EUR** a obsahuje předkrm, hlavní chod, dezert a nápoj.
Jiné zdroje uvádějí rozptyl 8–15 EUR, další 13–20 EUR, takže ber tohle jako orientaci, ne jako
ceníkovou položku. Tradičně jde o první chod zeleninový, druhý masový nebo rybí, k tomu dezert,
chleba, nápoj a voda.

Podstatné je tohle: **večerní set menu je vzácnější a dražší než polední.** Často jde o tentýž
podnik a tutéž kuchyni — jen v jinou hodinu a za jinou cenu. Nejjednodušší úsporné pravidlo v celém
průvodci proto zní: **jez hlavní jídlo v poledne.**

V turistických oblastech je menú del día dražší než ve čtvrtích, kde jedí místní.

Chráněné tokeny, které musí zůstat přesně: `["8–15 EUR","13–20 EUR","13:30","16:00","14:00","20:30","22:00","12:00","13","30","16","00","14","20","22","12","10–15","8–15","13–20","ne","jen","Kdy","Španělský","Oběd","Večeře","Nedělní","Barceloně","Kdo","Menú","Polední","Jiné","Tradičně","Podstatné","Často","Nejjednodušší","Oběd se podává od 13:30 do 16:00","menú del día","10–15 EUR","večerní set menu je vzácnější a dražší než polední.","jez hlavní jídlo v poledne.","sopar","vermut","místní"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
