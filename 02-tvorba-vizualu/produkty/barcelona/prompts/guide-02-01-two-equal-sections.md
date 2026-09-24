# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Barcelona`
- Země: `Španělsko`
- Oddíl: `Doprava po městě a do okolí`
- Strana: `guide-02-01-two-equal-sections`
- Layout: `Two equal sections`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Jízdenky — ceník 2026

Ceny platí od 15. ledna 2026 (TMB mění tarify typicky k lednu, takže si je před cestou ověř):

| Jízdenka | Cena (zóna 1) |
|---|---|
| Jednotlivá jízdenka | 2,90 EUR |
| T-casual — 10 jízd | 13,00 EUR |
| T-familiar | 11,50 EUR |
| T-usual — 30 dní neomezeně | 22,80 EUR |
| Letištní jízdenka | 5,90 EUR |
| T-jove (všechny zóny) | 45,50 EUR |

T-casual pro dvě zóny stojí 25,50 EUR.

Jedna věc, která na první pohled nedává smysl: **T-usual je za 30 dní neomezeného jezdění dražší
jen o 9,80 EUR než T-casual za 10 jízd.** Důvod je, že na T-usual a T-jove se uplatňuje padesátiprocentní
státní sleva, na T-casual ne. T-usual je ale osobní jízdenka, takže tuhle úvahu dělej podle svého,
ne za celou skupinu.

### Tři pravidla, která ti ušetří peníze i nervy

**1. Na letišti T-casual neplatí.** Stanice metra Aeroport T1 a Aeroport T2 na lince L9 Sud vyžadují
zvláštní letištní jízdenku za 5,90 EUR — TMB to uvádí přímo v podmínkách T-casual. Kdo si kartu koupí
předem a spoléhá na ni, stojí u brány.

**2. T-casual je přenosná, T-usual ne.** Nedá se použít dvakrát ve stejnou chvíli, ale dá se podat
dál — dvojice si tedy vystačí s jednou kartou. T-usual je osobní.

**3. Spočítej si to, nehádej.** T-casual vychází na **1,30 EUR za jízdu**. Hola Barcelona na 72 hodin
stojí 27,30 EUR — to je hranice zhruba 21 jízd za tři dny, což je při běžném tempu prohlídky města
hodně. Kdo jezdí míň, s T-casual ušetří.

Chráněné tokeny, které musí zůstat přesně: `["2,90 EUR","13,00 EUR","11,50 EUR","22,80 EUR","5,90 EUR","45,50 EUR","25,50 EUR","9,80 EUR","1,30 EUR","27,30 EUR","15. ledna","2026","15","1","2,90","10","13,00","11,50","30","22,80","5,90","45,50","25,50","9,80","2","3","1,30","72","27,30","21","jen","ne","Jízdenky","Ceny","Jízdenka","Cena","Jednotlivá","T-casual","T-familiar","T-usual","Letištní","T-jove","Jedna","Důvod","Tři","Na","Stanice","Aeroport","Sud","Kdo","Nedá","Spočítej","Hola Barcelona","1. Na letišti T-casual neplatí.","2. T-casual je přenosná, T-usual ne.","3. Spočítej si to, nehádej.","1,30 EUR za jízdu"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
