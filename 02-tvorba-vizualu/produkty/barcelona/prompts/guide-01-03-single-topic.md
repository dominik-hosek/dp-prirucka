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
- Strana: `guide-01-03-single-topic`
- Layout: `Single topic`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Turistická daň — počítej s ní zvlášť

Tohle je položka, kterou v ceně rezervace obvykle nenajdeš a platí se až na místě. V Barceloně se
skládá ze dvou vrstev: regionální katalánské daně a **městské přirážky 5 EUR na osobu a noc**.

Po sečtení obou vrstev platí **od 1. dubna 2026** tyto sazby na osobu a noc:

| Typ ubytování | Daň za osobu a noc |
|---|---|
| Hotel 5\* / grand luxe / luxusní kemp | 12,00 EUR |
| Hotel 4\* a 4\* superior | 8,40 EUR |
| Turistické byty a apartmány | 9,50 EUR |
| Hostely | 6,00 EUR |
| Ostatní kempy a zařízení | 7,00 EUR |

Dvě věci, které tuhle částku výrazně mění a samy se u rezervace nepřipomenou:

- **Děti do 17 let jsou osvobozené** od obou složek, osvobození se uplatní automaticky.
- **Od osmé noci se daň dál nenačítá.**

Městská přirážka má růst o 1 EUR ročně — 6 EUR v roce 2027, 7 EUR v roce 2028 a 8 EUR v roce 2029.
Sazby pro hotely kategorie 1–3\* se v dostupných zdrojích samostatně neuvádějí, takže si u nižších
kategorií ověř konkrétní částku u ubytovatele.

Chráněné tokeny, které musí zůstat přesně: `["5 EUR","12,00 EUR","8,40 EUR","9,50 EUR","6,00 EUR","7,00 EUR","1 EUR","6 EUR","7 EUR","8 EUR","1. dubna","5","1","2026","12,00","4","8,40","9,50","6,00","7,00","17","6","2027","7","2028","8","2029","1–3","obvykle","Turistická","Tohle","Barceloně","Po","Typ","Daň","Hotel","Turistické","Hostely","Ostatní","Dvě","Děti","Od","Městská","Sazby","městské přirážky 5 EUR na osobu a noc","od 1. dubna 2026","Děti do 17 let jsou osvobozené","Od osmé noci se daň dál nenačítá.","a 4\\"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
