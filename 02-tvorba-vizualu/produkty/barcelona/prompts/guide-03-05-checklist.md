# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Barcelona`
- Země: `Španělsko`
- Oddíl: `Ubytování`
- Strana: `guide-03-05-checklist`
- Layout: `Checklist`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Rychlé shrnutí

- **Krátký pobyt a nevadí ti hluk** → Gotická čtvrť (ale pozor, nemá uvnitř metro).
- **První návštěva, chceš jistotu** → Eixample (v létě 180–200 EUR/noc).
- **Klid a místní život** → Gràcia.
- **Delší pobyt, klidnější pláže, nižší ceny** → Poblenou.
- **Šetřit a přitom být blízko** → Poble Sec nebo Sant Antoni.
- **U apartmánu si vždy zkontroluj registrační číslo** (NRU / HUT / NIRTC).
- **Na léto rezervuj 3–6 měsíců dopředu** a připočítej turistickou daň.

Chráněné tokeny, které musí zůstat přesně: `["180–200","3–6","Rychlé","Krátký","Gotická","První","Eixample","Klid","Delší","Poblenou","Šetřit","Poble Sec","Sant Antoni","Na","Krátký pobyt a nevadí ti hluk","První návštěva, chceš jistotu","Klid a místní život","Delší pobyt, klidnější pláže, nižší ceny","Šetřit a přitom být blízko","U apartmánu si vždy zkontroluj registrační číslo","Na léto rezervuj 3–6 měsíců dopředu"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
