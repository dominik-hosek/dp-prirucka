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
- Strana: `guide-08-03-checklist`
- Layout: `Checklist`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Co si zarezervovat dopředu

- [ ] **Ubytování** — na léto 3 až 6 měsíců dopředu (viz kapitola Ubytování).
- [ ] **Registrační číslo u apartmánu** — NRU, HUT, NIRTC. Nabídka bez čísla je varovný signál
      (viz kapitola Ubytování).
- [ ] **Park Güell** — vstupenka na časový slot. Kapacita 1 400 lidí za hodinu, po čase na vstupence
      máš 30 minut na vstup a zpátky už se nedostaneš (viz kapitola Památky, výlety a itineráře).
- [ ] **Museu Picasso, pokud chceš zdarma** — bezplatné sloty se uvolňují **přesně 4 dny dopředu
      v 10:00 barcelonského času** a rychle mizí. Tohle si dej do kalendáře.
- [ ] **Sagrada Família** — a hlavně **si ověř, jestli je vůbec otevřená.** Zdroje si k létu 2026
      odporují (viz kapitola Památky, výlety a itineráře). Kontakt: informacio@sagradafamilia.org,
      +34 932 080 414.
- [ ] **Montserrat**, pokud ho plánuješ — spontánně se tam nevyrazí tak snadno jako do Sitges
      (viz kapitola Doprava po městě a do okolí).

### Co vyřešit ještě doma

- [ ] **eSIM aktivovat před odletem.** Ceny se u eSIM mění častěji než u fyzických SIM, takže
      zkontroluj ceník až těsně před cestou — a hlídej si, jestli je v eurech, nebo v dolarech
      (viz kapitola Praktické základy).
- [ ] **Rozhodnout jízdenku na MHD.** T-casual, nebo Hola Barcelona? Zlom leží kolem 21 jízd
      za tři dny. A hlavně: **T-casual neplatí na letištních stanicích metra** (viz kapitola
      Doprava po městě a do okolí).
- [ ] **Započítat turistickou daň do rozpočtu.** V ceně rezervace obvykle není a platí se na místě;
      6 až 12 EUR na osobu a noc podle typu ubytování (viz kapitola Rozpočet).
- [ ] **Zkontrolovat aktuální doporučení MZV** na mzv.gov.cz — bezpečnostní situace i vstupní
      podmínky se mohou změnit.

Chráněné tokeny, které musí zůstat přesně: `["4 dny","12 EUR","10:00","3","6","1","400","30","4","10","00","2026","34","932","080","414","21","12","obvykle","Co","Ubytování","Registrační","Nabídka","Park","Kapacita","Památky","Museu Picasso","Tohle","Sagrada Família","Zdroje","Kontakt","Montserrat","Sitges","Doprava","Ceny","Praktické","Rozhodnout","T-casual","Hola Barcelona","Zlom","Započítat","Rozpočet","Zkontrolovat","Registrační číslo u apartmánu","Park Güell","Museu Picasso, pokud chceš zdarma","si ověř, jestli je vůbec otevřená.","eSIM aktivovat před odletem.","Rozhodnout jízdenku na MHD.","T-casual neplatí na letištních stanicích metra","Započítat turistickou daň do rozpočtu.","Zkontrolovat aktuální doporučení MZV"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
