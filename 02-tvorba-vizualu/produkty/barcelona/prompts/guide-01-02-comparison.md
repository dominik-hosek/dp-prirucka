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
- Strana: `guide-01-02-comparison`
- Layout: `Comparison`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Z letiště do centra

Letiště Barcelona-El Prat (BCN) má dva terminály a **na každém dává smysl jiná doprava**. To je
první věc, kterou se vyplatí vědět dopředu.

- **Aerobús (linka A1 z T1, A2 z T2)** — na Plaça Catalunya za 25–35 minut, jezdí 24 hodin denně,
  365 dní v roce. Ve špičce po zhruba 5 minutách (A1), v noci po 20. Zastavuje na Plaça Espanya,
  Gran Via–Borrell, Plaça Universitat a Plaça Catalunya. Podle oficiálního ceníku dopravce
  **7,45 EUR jednosměrně a 12,85 EUR zpáteční**, přičemž zpáteční část platí 90 dní. Pozor —
  cestovatelské weby uvádějí i výrazně vyšší částky (kolem 9,50 / 16,50 EUR), takže si cenu ověř
  přímo u dopravce těsně před cestou.
- **Metro L9 Sud** ze stanic Aeroport T1 a Aeroport T2 stojí **5,90 EUR** za zvláštní letištní
  jízdenku. **Běžná T-casual tady neplatí** — to je nejčastější tarifní omyl v Barceloně vůbec
  a TMB to na svém webu uvádí výslovně (viz kapitola Doprava po městě a do okolí).
- **Vlak Rodalies R2 Nord** je nejrychlejší kolejová varianta — do centra za 19–26 minut. Háček:
  **staví jen u T2.** Kdo přilétá na T1, musí nejdřív bezplatným shuttlem, a tím výhoda mizí. Cenu
  zdroje uvádějí rozporně (4,60 i 2,90 EUR), takže si ji ověř na místě.
- **Městský autobus 46** na Plaça Espanya je nejlevnější, orientačně 2,65 EUR.
- **Taxi** vyjde orientačně na 30–40 EUR přes den, přičemž **minimální jízdné z letiště je 21 EUR**
  včetně příplatků (detail sazeb v kapitole Doprava po městě a do okolí).

Chráněné tokeny, které musí zůstat přesně: `["7,45 EUR","12,85 EUR","16,50 EUR","2,90 EUR","2,65 EUR","30–40 EUR","25–35","24","365","5","20","7,45","12,85","90","9,50","16,50","5,90","19–26","4,60","2,90","46","2,65","30–40","21","jen","Letiště Barcelona-","El Prat","To","Aerobús","Catalunya","Ve","Zastavuje","Espanya","Gran Via","Borrell","Universitat","Podle","Pozor","Metro","Sud","Aeroport","Běžná T-casual","Barceloně","Doprava","Vlak Rodalies","Nord","Háček","Kdo","Cenu","Městský","Taxi","na každém dává smysl jiná doprava","Aerobús (linka A1 z T1, A2 z T2)","7,45 EUR jednosměrně a 12,85 EUR zpáteční","Metro L9 Sud","5,90 EUR","Běžná T-casual tady neplatí","Vlak Rodalies R2 Nord","staví jen u T2.","Městský autobus 46","minimální jízdné z letiště je 21 EUR"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
