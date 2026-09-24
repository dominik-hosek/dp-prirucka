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
- Strana: `guide-05-01-single-topic`
- Layout: `Single topic`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Nejdřív ta nejdůležitější informace: Sagrada Família

**Před cestou si ověř, jestli je bazilika vůbec otevřená.** K datu přípravy tohoto průvodce si
zdroje přímo odporují: oficiální web sagradafamilia.org na stránce vstupenek uvádí, že je bazilika
dočasně uzavřená pro veřejnost a odkazuje na virtuální prohlídky, zatímco cenová stránka téhož webu
běžně zobrazuje ceník a jiné zdroje tvrdí, že v roce 2026 nejsou žádné dny uzavření. Důvod ani
termín znovuotevření se nám zjistit nepodařilo.

Neplánuj si proto Sagradu Famílii jako jistotu — **ověř si stav přímo** (informacio@sagradafamilia.org,
+34 932 080 414) a měj připravenou náhradu. Nejlepší je Recinte Modernista de Sant Pau, který je
pět minut chůze odtud (viz kapitola Off the beaten path).

Oficiální ceník, pokud otevřeno bude:

| Vstupenka | Základní | Senior | Do 30 let / student | Do 11 let |
|---|---|---|---|---|
| S audioprůvodcem (aplikace) | 26,00 EUR | 21,00 EUR | 24,00 EUR | zdarma |
| S průvodcem | 30,00 EUR | 23,00 EUR | 28,00 EUR | zdarma |
| S věžemi | 36,00 EUR | 28,00 EUR | 34,00 EUR | zdarma |
| S průvodcem a věžemi | 40,00 EUR | 32,00 EUR | 38,00 EUR | zdarma |

Držitelé průkazu ZTP mají vstup zdarma. Doprovod platí podle typu vstupenky: 0 EUR
s audioprůvodcem, 4 EUR s průvodcem, 10 EUR s věžemi a 14 EUR s průvodcem a věžemi.

Dvě věci ke stavu stavby. **Poslední díl věže Ježíše Krista byl osazen 20. února 2026** — bazilika
tím dosáhla plné výšky 172,5 metru a je nejvyšším kostelem světa. Ale **vyhlídková plošina na téhle
věži se má otevřít až v roce 2027**; v roce 2026 jsou přístupné jen věže Narození a Umučení, takže
vstupenka „s věžemi" znamená tyhle dvě. Fasáda Slávy, hlavní vstup, je stále ve výstavbě
s odhadovaným dokončením 2034–2035.

Chráněné tokeny, které musí zůstat přesně: `["26,00 EUR","21,00 EUR","24,00 EUR","30,00 EUR","23,00 EUR","28,00 EUR","36,00 EUR","34,00 EUR","40,00 EUR","32,00 EUR","38,00 EUR","0 EUR","4 EUR","10 EUR","14 EUR","20. února","2026","34","932","080","414","30","11","26,00","21,00","24,00","30,00","23,00","28,00","36,00","34,00","40,00","32,00","38,00","0","4","10","14","20","172,5","2027","2034–2035","jen","Nejdřív","Sagrada Família","Před","Důvod","Neplánuj","Sagradu Famílii","Nejlepší","Recinte Modernista","Sant Pau","Off","Oficiální","Vstupenka","Základní","Senior","Do","Držitelé","Doprovod","Dvě","Poslední","Ježíše Krista","Ale","Narození","Umučení","Fasáda Slávy","Před cestou si ověř, jestli je bazilika vůbec otevřená.","ověř si stav přímo","Poslední díl věže Ježíše Krista byl osazen 20. února 2026","s věžemi"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
