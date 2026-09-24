# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Barcelona`
- Země: `Španělsko`
- Oddíl: `Památky, výlety a itineráře`
- Strana: `guide-05-04-timeline-itinerary`
- Layout: `Timeline ininerary`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Muzea a Camp Nou

**Museu Picasso** — stálá expozice **12 EUR**, se zvláštní výstavou 14 EUR. Jiné zdroje uvádějí
15 a 19 EUR, takže si cenu ověř na museupicasso.bcn.cat.

**Camp Nou / muzeum FC Barcelona** — dospělí **28 EUR**, děti 6–13 let a senioři 65+ 21 EUR,
studenti s kartou 20 EUR, děti do 5 let zdarma. **Důležité: stadion se přestavuje**, takže část
původní prohlídky není přístupná. Původní „Camp Nou Experience" nahradilo muzeum a imerzivní
prohlídka s audioprůvodcem ve 12 jazycích — pokud sis prohlídku stadionu plánoval jako vrchol
pobytu, tohle je potřeba vědět předem.

### Kdy se dá dovnitř zdarma

**První neděli v měsíci** je vstup zdarma do Museu Picasso, Museu Blau, MNAC, Museu del Disseny
a CCCB.

Tady je ale rozdíl, který se v běžných seznamech „muzea zdarma" neuvádí a rozhodne o tom, jestli
se dovnitř dostaneš:

- **Museu Picasso vyžaduje i na bezplatný vstup rezervaci časového slotu online.** Sloty se
  uvolňují **přesně 4 dny dopředu v 10:00 barcelonského času** a rychle mizí, zvlášť na první
  neděle. Bezplatný vstup tu platí od 9:00 do 19:00. Muzeum má navíc zdarma v létě ve čtvrtek,
  pátek a sobotu mezi 19:00 a 21:00 a v zimě ve čtvrtek mezi 16:00 a 19:00, plus dny otevřených
  dveří.
- **MNAC rezervaci nepotřebuje**, ale první neděle znamenají fronty. Stálá expozice je tu navíc
  zdarma **v sobotu po 15:00** a o katalánských svátcích — a tohle je nejméně známá varianta ze
  všech, protože nevyžaduje ani rezervaci, ani konkrétní neděli v měsíci. Dále je zdarma 18. května
  (Mezinárodní den muzeí) a 11. září (Diada de Catalunya).

Chráněné tokeny, které musí zůstat přesně: `["14 EUR","19 EUR","21 EUR","20 EUR","4 dny","10:00","9:00","19:00","21:00","16:00","15:00","18. května","11. září","12","14","15","19","28","6–13","65","21","20","5","4","10","00","9","16","18","11","Muzea","Camp Nou","Museu Picasso","Jiné","Barcelona","Důležité","Původní","Camp Nou Experience","Kdy","První","Museu Blau","Museu","Disseny","Tady","Sloty","Bezplatný","Muzeum","Stálá","Dále","Mezinárodní","Diada","Catalunya","12 EUR","Camp Nou / muzeum FC Barcelona","28 EUR","Důležité: stadion se přestavuje","První neděli v měsíci","Museu Picasso vyžaduje i na bezplatný vstup rezervaci časového slotu online.","přesně 4 dny dopředu v 10:00 barcelonského času","MNAC rezervaci nepotřebuje","v sobotu po 15:00","muzea zdarma"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
