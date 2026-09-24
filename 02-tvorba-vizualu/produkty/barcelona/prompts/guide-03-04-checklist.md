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
- Strana: `guide-03-04-checklist`
- Layout: `Checklist`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Turistické apartmány — co se právě mění

Tohle je věc, kterou v běžném průvodci Barcelonou nenajdeš, a přitom ovlivňuje, co si vůbec můžeš
zarezervovat.

Město v roce 2024 oznámilo, že **žádná z přibližně 10 101 stávajících licencí HUT pro turistické
byty nebude obnovena** — všechny vyprší do listopadu 2028. Nové licence se od listopadu 2028
nevydávají, stávající se od roku 2029 neobnovují. Opatření potvrdil španělský Ústavní soud v březnu
2025.

Pro tebe z toho plyne jedna praktická věc: **legální nabídka musí uvádět registrační čísla** — NRU,
místní licenci HUT a katalánské číslo NIRTC. Číslo HUT se musí zobrazovat u každé nabídky na Airbnb,
Vrbo i Booking.com a nabídky bez platného NRU musí platformy stáhnout do 48 hodin. **Nabídka bez
registračního čísla je varovný signál.**

Ověřit si číslo jde v registru města (Ajuntament de Barcelona — Habitatges d'Ús Turístic).
Konkrétní adresu registru jsme neověřovali, takže ji hledej na oficiálním webu města, ne přes
odkaz z nabídky.

Protože se situace mění průběžně, zkontroluj si stav před cestou — to, co platí dnes, nemusí platit
za rok.

### Proč tu nejsou konkrétní hotely

V ostatních průvodcích téhle řady bývá u ubytování žebříček konkrétních hotelů vybraných podle
doložené metody — hodnocení na dvou nezávislých platformách a minimální počet recenzí, aby nešlo
o pár náhodných dojmů.

Pro Barcelonu se takový žebříček sestavit nepodařilo. Dostupné seznamy „nejlepších hotelů" pocházely
z portálů, které neuvádějí počty recenzí, nebo je uváděly v desítkách, a hodnocení z druhé nezávislé
platformy se nepodařilo doložit. Raději ti tedy nedáme žádné jméno než jméno, za kterým nestojí data —
seznam bez metody je jen názor, který vypadá jako doporučení.

Chráněné tokeny, které musí zůstat přesně: `["2024","10","101","2028","2029","2025","48","ne","nemusí","jen","Turistické","Tohle","Barcelonou","Město","Nové","Opatření","Ústavní","Pro","Číslo","Airbnb","Vrbo","Booking","Nabídka","Ověřit","Ajuntament","Barcelona","Habitatges","Ús Turístic","Konkrétní","Protože","Proč","Pro Barcelonu","Dostupné","Raději","legální nabídka musí uvádět registrační čísla","nejlepších hotelů"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
