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
- Strana: `guide-06-02-two-equal-sections`
- Layout: `Two equal sections`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Pouštní safari — skupinově, nebo soukromě

Safari do Wadi El Gemal se prodává jako skupinový nebo soukromý výlet, cena se podle toho výrazně
liší — orientačně 90–228 USD na osobu. Skupinový výlet je levnější, ale jsi vázaný na program a
tempo skupiny; soukromý dává víc flexibility v tom, kde a jak dlouho se zastavíte. Zdroj:
[viator.com](https://www.viator.com/tours/Marsa-Alam/Private-Safari-Day-Tour-To-Wadi-El-Gamal-National-Park-From-Marsa-Alam/d25556-300010P27).

### Off the beaten path

Pokud máš čas navíc a chceš se poušti věnovat víc než jedním odpoledním výletem, zvaž vícedenní
nebo večerní program (přespání v poušti, pozorování hvězd) místo klasického denního safari — nabídka
i cena se ale liší podle cestovky a sezóny, takže konkrétní variantu si domluv na místě nebo přes
hotel. Kdo chce vidět poušť jinak než z klimatizovaného mikrobusu, ať počítá s tím, že si za
flexibilitu připlatí.

Chráněné tokeny, které musí zůstat přesně: `["90–228","Pouštní","Safari","Wadi El Gemal","Skupinový","Zdroj","Marsa-","Alam","Private-","Safari-","Day-","Tour-","To-","Wadi-","El-","Gamal-","National-","Park-","From-","Off","Pokud","Kdo"]`

## Country system
`{"palette":{"background":"#F4E9D8","primary":"#0F6473","secondary":"#C96A32","accent":"#CBA85B","text":"#201A16"},"heading_fonts":["Cormorant Garamond","Prata"],"body_fonts":["Manrope","Source Sans 3"],"motifs":["jemné vlny Rudého moře","korálové větvení","pouštní horizont","stylizované slunce"],"photo_style":"čistá tyrkysová voda, teplý pouštní písek, korálové detaily a přirozené slunce","character":"klidný prémiový red-sea editorial s kontrastem moře a pouště"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
