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
- Strana: `guide-01-05-checklist`
- Layout: `Checklist`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Bezpečnost a kapsáři

Španělsko nemá k létu 2026 od Ministerstva zahraničních věcí ČR vydané mimořádné varování pro cesty.
Velvyslanectví ČR v Madridu doporučuje registraci do systému **DROZD** (viz kapitola Checklist před
odjezdem). Pokud jedeš autem, počítej s vysokými pokutami za dopravní přestupky.

Kapesní krádeže jsou ale v Barceloně reálné téma, ne strašení. Město patří k evropským městům
s nejvyšší mírou drobných krádeží — za rok 2024 jich bylo nahlášeno 94 517, tedy zhruba 259 denně,
a podle téhož zdroje se hlásí jen asi pětina trestných činů. Čísla pocházejí ze sekundárních zdrojů,
takže je ber jako řádovou orientaci.

**Kde se to děje:**

- **La Rambla, Gotická čtvrť** — hustý pěší provoz, úzké uličky.
- **Metro, zvlášť linky L1, L3 a L5** — v metru je hustota krádeží nejvyšší.
- **Konkrétní uzly:** Diagonal, Plaça Catalunya, Sants Estació, Sagrada Família, Barceloneta.

Dobrá zpráva: trend se podle dostupných zdrojů zlepšuje. Po policejní operaci *Pla Kanpai* se uvádí
meziroční pokles kapesních krádeží o 40 % a zadržení 85 recidivistů od ledna do června 2026. I tohle
číslo ale pochází ze sekundárního zdroje, ne přímo od policie — ber ho stejně opatrně jako to
předchozí.

### Rychlé shrnutí

- Nejlepší poměr počasí a davu: **květen a září.** Nejdražší a nejplnější: srpen.
- **T-casual na letišti neprojde** — buď letištní jízdenka za 5,90 EUR, nebo Aerobús, nebo
  Hola Barcelona (viz kapitola Doprava po městě a do okolí).
- **Turistická daň 6–12 EUR na osobu a noc** podle typu ubytování se platí navíc k rezervaci. Děti
  do 17 let ji neplatí, od osmé noci se nenačítá.
- Kapsáře čekej v metru na L1/L3/L5 a na La Rambla, ne rozptýleně po celém městě.

Chráněné tokeny, které musí zůstat přesně: `["40 %","5,90 EUR","6–12 EUR","2026","2024","94","517","259","40","85","5,90","6–12","17","ne","jen","Bezpečnost","Španělsko","Ministerstva","Velvyslanectví","Madridu","Checklist","Pokud","Kapesní","Barceloně","Město","Čísla","Kde","La Rambla","Gotická","Metro","Konkrétní","Diagonal","Catalunya","Sants Estació","Sagrada Família","Barceloneta","Dobrá","Po","Pla Kanpai","Rychlé","Nejlepší","Nejdražší","T-casual","Aerobús","Hola Barcelona","Doprava","Turistická","Děti","Kapsáře","DROZD","Kde se to děje:","La Rambla, Gotická čtvrť","Metro, zvlášť linky L1, L3 a L5","Konkrétní uzly:","květen a září.","T-casual na letišti neprojde","Turistická daň 6–12 EUR na osobu a noc"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
