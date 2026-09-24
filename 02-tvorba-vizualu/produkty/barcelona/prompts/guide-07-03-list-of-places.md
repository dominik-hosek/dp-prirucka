# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Barcelona`
- Země: `Španělsko`
- Oddíl: `Rozpočet`
- Strana: `guide-07-03-list-of-places`
- Layout: `List of places`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Jídlo

- **Menú del día (oběd):** 10–15 EUR (jiné zdroje uvádějí 8–15, další 13–20 EUR)
- **Rychlé občerstvení nebo jídlo s sebou:** 4–8 EUR
- **Jídlo v kvalitní restauraci:** 35–60 EUR na osobu
- **Espresso:** 1,20–1,80 EUR, v turistických místech až 2,50 EUR; cappuccino kolem 2,30 EUR
- **Pivo v baru:** kolem 2,50 EUR — ale jiný zdroj uvádí průměr až 7 EUR, doložit se to nepodařilo,
  takže s tím počítej jako se spodní hranicí
- **Pivo ze supermarketu (0,5 l):** 1,23–1,25 EUR. Dva litry Coca-Coly 2,09 EUR
- **Couvert (chléb) na stole:** až 2,50 EUR na osobu — a dá se odmítnout

Rozdíl mezi obědovým menu a večeří à la carte je tady největší jednotlivá úspora, kterou v Barceloně
uděláš, aniž bys na něčem šidil (viz kapitola Jídlo a pití).

Chráněné tokeny, které musí zůstat přesně: `["10–15 EUR","13–20 EUR","4–8 EUR","35–60 EUR","1,20–1,80 EUR","2,50 EUR","2,30 EUR","7 EUR","1,23–1,25 EUR","2,09 EUR","10–15","8–15","13–20","4–8","35–60","1,20–1,80","2,50","2,30","7","0,5","1,23–1,25","2,09","Jídlo","Menú","Rychlé","Espresso","Pivo","Dva","Coca-","Coly","Couvert","Rozdíl","Barceloně","Menú del día (oběd):","Rychlé občerstvení nebo jídlo s sebou:","Jídlo v kvalitní restauraci:","Espresso:","Pivo v baru:","Pivo ze supermarketu (0,5 l):","Couvert (chléb) na stole:"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
