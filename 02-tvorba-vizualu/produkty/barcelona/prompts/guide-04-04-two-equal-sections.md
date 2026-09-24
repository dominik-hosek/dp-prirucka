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
- Strana: `guide-04-04-two-equal-sections`
- Layout: `Two equal sections`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Spropitné a chleba na stole

Dvě věci, ve kterých se turisté systematicky chovají proti místnímu zvyku:

**Spropitné.** Servis se v účtu neúčtuje a **místní běžně spropitné nedávají**, nebo jen drobné.
Norma je zaokrouhlit nahoru, což vyjde možná na 5 % a často ani na to. V dražších podnicích je
zvykem nechat 5–10 %, ale povinné to není. Patnáct procent podle americké logiky tady není
velkorysost, ale nedorozumění.

**Chleba.** Když ti na stůl přinesou chleba, je to zpoplatněný couvert — **až 2,50 EUR na osobu**.
Podnik ho smí položit na stůl, i když sis o něj neřekl. **Když ho odmítneš, neplatíš ho; když mlčíš,
naúčtuje se.**

### Proč tu nejsou konkrétní restaurace

Stejně jako u ubytování platí, že konkrétní podnik smíme jmenovat jen tehdy, když jeho výběr stojí
na doložené metodě — hodnocení na dvou nezávislých platformách a dost recenzí na to, aby nešlo
o náhodu.

Nalezené seznamy restaurací v Barceloně tyhle podmínky nesplňovaly — šlo o blogové a SEO výběry
bez počtů recenzí. Místo jmen ti proto dáváme pravidla, podle kterých si vybereš sám: poledne místo
večera, čtvrť místo hlavní třídy, a signály z předchozí sekce.

Chráněné tokeny, které musí zůstat přesně: `["5 %","5–10 %","2,50 EUR","5","5–10","2,50","jen","Spropitné","Dvě","Servis","Norma","Patnáct","Chleba","Když","Podnik","Proč","Stejně","Nalezené","Barceloně","Místo","Spropitné.","místní běžně spropitné nedávají","Chleba.","až 2,50 EUR na osobu"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
