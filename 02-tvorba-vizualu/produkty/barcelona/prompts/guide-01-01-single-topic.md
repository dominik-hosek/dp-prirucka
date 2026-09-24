# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Barcelona`
- Země: `Španělsko`
- Oddíl: `Praktické základy`
- Strana: `guide-01-01-single-topic`
- Layout: `Single topic`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Kdy jet

Nejteplejší jsou červenec a srpen — denní maxima se běžně drží kolem 28–29 °C a k tomu vysoká
vlhkost. V srpnu navíc odjíždí na dovolenou hodně místních a ceny ubytování jsou nejvyšší v roce.

Konsenzuální doporučení napříč zdroji je **květen a září**: pořád teplo, ale znatelně méně lidí než
v hlavní sezóně, což se v Barceloně pozná hlavně na kapacitě památek. Pokud jedeš kvůli koupání,
sezóna běží od června do září s teplotou moře zhruba 22–26 °C; červen a začátek července mají moře
kolem 22–25 °C a míň lidí než srpen.

Nejlevnější a nejklidnější je leden a únor. Leden je nejchladnější měsíc — přes den kolem 8–15 °C,
v noci kolem 5 °C. Nejdeštivější měsíc je říjen, obecně je vlhčí celý podzim, ale přeháňky bývají
krátké.

Chráněné tokeny, které musí zůstat přesně: `["28–29 °C","22–26 °C","22–25 °C","8–15 °C","5 °C","28–29","22–26","22–25","8–15","5","Kdy","Nejteplejší","Konsenzuální","Barceloně","Pokud","Nejlevnější","Leden","Nejdeštivější","květen a září"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
