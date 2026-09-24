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
- Strana: `guide-08-01-two-equal-sections`
- Layout: `Two equal sections`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Doklady

- **Občanský průkaz nebo pas.** Španělsko je v EU i v Schengenu, nic dalšího nepotřebuješ.
- **ETIAS se tě netýká.** Je určený pro cestující ze třetích zemí osvobozených od víz, ne pro občany
  EU. Titulky o něm plní zprávy, tak si od zprostředkovatelů nekupuj „vyřízení ETIAS" — nepotřebuješ
  ho.
- Pro pořádek: samotné spuštění ETIAS je nejisté. Termín se posouval, v polovině července 2026
  Evropská unie z oficiálního webu odstranila cíl „poslední čtvrtletí 2026" a mluví se o odkladu
  na rok 2027; po spuštění se počítá s šestiměsíčním přechodným obdobím. Systém **EES** se ve
  Španělsku už postupně zavádí na letištích (Madrid-Barajas, Malaga) a týká se cestujících ze
  třetích zemí.

### Pojištění — dvě věci, ne jedna

Nejčastější omyl je, že stačí EHIC. Nestačí.

**EHIC (Evropský průkaz zdravotního pojištění)** ve Španělsku platí. S ním máš nárok na lékařsky
nezbytnou péči za stejných podmínek jako místní — ale **jen ve zdravotnických zařízeních financovaných
z veřejných zdrojů**.

**Co EHIC nekryje:**

- zdravotní repatriaci ani repatriaci ostatků,
- spoluúčast pacienta při hospitalizaci,
- spoluúčast při nákupu předepsaných léků.

**Cestovní pojištění** řeší jiné situace a jedno druhé nenahrazuje — pokrývá záchranné akce (které
stojí tisíce korun), asistenční služby, komunikaci s lékaři a tlumočení. Konkrétní produkt ani výši
krytí ti tu nedoporučujeme, to je na tobě a na tvé pojišťovně; podstatné je vědět, že samotný EHIC
tyhle položky nepokryje.

Chráněné tokeny, které musí zůstat přesně: `["2026","2027","ne","jen","Doklady","Občanský","Španělsko","Schengenu","Je","Titulky","Pro","Termín","Evropská","Systém","Španělsku","Madrid-","Barajas","Malaga","Pojištění","Nejčastější","Nestačí","Evropský","Co","Cestovní","Konkrétní","Občanský průkaz nebo pas.","ETIAS se tě netýká.","EES","EHIC (Evropský průkaz zdravotního pojištění)","Co EHIC nekryje:","Cestovní pojištění","vyřízení ETIAS","poslední čtvrtletí 2026"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
