# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Barcelona`
- Země: `Španělsko`
- Oddíl: `Checklist před odjezdem`
- Strana: `guide-08-02-two-equal-sections`
- Layout: `Two equal sections`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Registrace DROZD

Velvyslanectví ČR v Madridu doporučuje registraci do systému **DROZD** (Dobrovolná registrace občanů
ČR při cestách do zahraničí). Je to zdarma a zabere pár minut.

### Kontakt na konzulát — měj ho offline

Když přijdeš o telefon a doklady najednou, potřebuješ adresu a číslo na papíře, ne v mailu.

**Honorární konzulát ČR v Barceloně** (údaje podle oficiální stránky MZV ČR):

- **Adresa:** Carrer de Mallorca 272, 9-1, 08037 Barcelona
- **Telefon:** +34 933 128 044
- **E-mail:** Barcelona.Honorary@mzv.gov.cz
- **Nouzová linka MZV:** +420 222 420 222
- **Úřední hodiny:** pondělí, středa, pátek 10:00–12:00

Vyřizuje náhradní cestovní doklady a cestovní průkazy, předávání cestovních pasů, ověřovací činnost
a zápis do seznamu voličů.

Dvě poznámky. **Úřední hodiny jsou úzké** — tři dny v týdnu po dvou hodinách. S náhradním dokladem
proto nepočítej „hned". A na internetu kolují i jiné kontaktní údaje (jiné telefonní číslo, jiný
e-mail, jiné hodiny), takže **si je před cestou ověř přímo na mzv.gov.cz** a neřiď se tímhle výpisem
slepě, pokud jedeš dlouho po vydání průvodce.

Chráněné tokeny, které musí zůstat přesně: `["10:00","12:00","272","9-1","08037","34","933","128","044","420","222","10","00–12","00","ne","Registrace","Velvyslanectví","Madridu","Dobrovolná","Je","Kontakt","Když","Honorární","Barceloně","Adresa","Carrer","Mallorca","Barcelona","Telefon","E-mail","Honorary","Nouzová","Úřední","Vyřizuje","Dvě","DROZD","Honorární konzulát ČR v Barceloně","Adresa:","Telefon:","E-mail:","Nouzová linka MZV:","Úřední hodiny:","Úřední hodiny jsou úzké","si je před cestou ověř přímo na mzv.gov.cz","hned"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
