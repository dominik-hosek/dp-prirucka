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
- Strana: `guide-08-04-checklist`
- Layout: `Checklist`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Co si sbalit

Konkrétní seznam věcí do kufru ti tu vědomě nedáváme — je to jediná část checklistu, pro kterou
nemáme ověřený podklad, a nechceme ho vyplňovat obecnostmi, které znáš. Dvě věci ale z předchozích
kapitol vyplývají:

- **Pohodlná obuv na výšlap** k Bunkers del Carmel (viz kapitola Off the beaten path).
- **Drobná hotovost** — ve Španělsku se platí eurem a konkrétní platební zvyklosti v Barceloně
  jsme nedokázali spolehlivě doložit, takže je bezpečnější mít trochu hotovosti u sebe (viz
  kapitola Praktické základy).

### Rychlé shrnutí

- **EHIC i cestovní pojištění.** EHIC nekryje repatriaci ani spoluúčast.
- **Registrace DROZD** před odletem.
- **Kontakt na konzulát vytištěný**, ne jen v telefonu. Úřední hodiny po, st, pá 10:00–12:00.
- **Časové sloty:** Park Güell předem, Museu Picasso zdarma 4 dny dopředu v 10:00.
- **Ověř stav Sagrady Famílie.**
- **ETIAS nepotřebuješ.**

Chráněné tokeny, které musí zůstat přesně: `["4 dny","10:00","12:00","10","00–12","00","4","ne","jen","Co","Konkrétní","Dvě","Pohodlná","Bunkers","Carmel","Off","Drobná","Španělsku","Barceloně","Praktické","Rychlé","Registrace","Kontakt","Úřední","Časové","Park","Museu Picasso","Ověř","Sagrady Famílie","Pohodlná obuv na výšlap","Drobná hotovost","EHIC i cestovní pojištění.","Registrace DROZD","Kontakt na konzulát vytištěný","Časové sloty:","Ověř stav Sagrady Famílie.","ETIAS nepotřebuješ."]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
