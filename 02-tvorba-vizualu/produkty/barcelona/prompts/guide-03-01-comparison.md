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
- Strana: `guide-03-01-comparison`
- Layout: `Comparison`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Čtvrti — co si za co koupíš

**Eixample** je nejjistější volba pro první návštěvu. Široké ulice v pravidelné mřížce, snadná
orientace a pěšky ke Gaudímu — Casa Batlló i Sagrada Família. Passeig de Gràcia funguje zároveň
jako hlavní nákupní osa i jako památková trasa. Nevýhody jsou dvě: je to nejvyhledávanější oblast
a hotely se vyprodávají rychle, a v létě tu ceny běžně sedí na **180–200 EUR za noc**.

**Gotická čtvrť (Barri Gòtic)** dává středověké uličky, náměstí a katedrálu, všechno pěšky. Funguje
dobře pro **krátké pobyty**. Tři věci, které rezervační portály nenapíšou: je tu extrémní koncentrace
turistů, v hustých pěších uličkách jsou **aktivnější kapsáři** (viz kapitola Praktické základy), hluk
jde dlouho do noci — a **uvnitř Gotické čtvrti nejsou stanice metra.** S kufrem po dlažebních
kostkách je to informace, která se hodí předem.

**Gràcia** je klidnější a rezidenční, převažuje tu místní život nad turistickým. Je dál od hlavních
památek, ale dobře napojená metrem, a má vlastní modernistickou architekturu a spoustu příjemných
náměstí.

**Barceloneta** znamená nejcentrálnější přístup k pláži, staré rybářské domky a úzké uličky. V teplých
měsících je ale přeplněná a rušná.

**Poblenou** je bývalá průmyslová čtvrť, dnes technologické centrum města. Má **vlastní pláže
Bogatell a Mar Bella, které jsou výrazně méně přeplněné než Barceloneta**, a nižší ceny ubytování než
centrum. Dává smysl spíš na delší pobyty — do Gotické čtvrti nebo centrálního Eixample je odsud
potřeba metro (L4, stanice Llacuna nebo Poblenou) a z odlehlejšího konce čtvrti se pěšky nedojde.

**Poble Sec a Sant Antoni** jsou volba pro rozpočtově uvážlivé: méně centrální, ale levnější. Poble
Sec leží pod Montjuïcem, obsluhují ho stanice Poble Sec, Plaça d'Espanya a Paral·lel, a do centra
to jsou čtyři stanice metrem nebo pod 20 minut pěšky. Sant Antoni je na lince **L2**.

Chráněné tokeny, které musí zůstat přesně: `["180–200 EUR","180–200","20","Čtvrti","Eixample","Široké","Gaudímu","Casa Batlló","Sagrada Família","Passeig","Nevýhody","Gotická","Barri","Funguje","Tři","Praktické","Gotické","Je","Barceloneta","Poblenou","Má","Bogatell","Mar Bella","Dává","Llacuna","Poble Sec","Sant Antoni","Poble\nSec","Espanya","Paral","180–200 EUR za noc","Gotická čtvrť (Barri Gòtic)","krátké pobyty","aktivnější kapsáři","uvnitř Gotické čtvrti nejsou stanice metra.","Gràcia","Poble Sec a Sant Antoni","L2"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
