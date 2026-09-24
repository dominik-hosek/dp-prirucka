# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Barcelona`
- Země: `Španělsko`
- Oddíl: `Jídlo a pití`
- Strana: `guide-04-03-list-of-places`
- Layout: `List of places`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Jak poznat turistickou past

**La Rambla je opakovaně jmenovaná jako místo, kde se nemá jíst.** Podniky tu nabízejí nápadné,
předražené a nekvalitní jídlo — od ohřívané paelly po zmrazené mořské plody vydávané za čerstvé.
Jeden zdroj uvádí konkrétní rozdíl: kola, která jinde stojí kolem 3 dolarů, se tu prodává až za 11
(částky jsou v dolarech, ne v eurech).

**Varovné signály, které fungují okamžitě:**

- Nahaněč před podnikem.
- Velké fotografické menu.
- Nabídka typu „sangria a paella".
- Předpřipravená paella pod ohřívací lampou. **Fotka paelly vyvěšená před podnikem** na nábřeží
  nebo na La Rambla je popisovaná jako nejjasnější varovný signál ve městě.
- **Zářivě žlutá paella.** Pravý šafrán je drahý a jeho barva jemná — neonový odstín obvykle znamená
  potravinářské barvivo.

A jeden pozitivní ukazatel: **paella je ve Španělsku tradičně obědové jídlo.** Místní si rýžová
jídla objednávají odpoledne. Dobrá paella i fideuà se dělají čerstvě na objednávku, takže počítej
s **20 minutami a víc** — čekání je tady dobrá zpráva.

**Nezaměňuj La Rambla a Rambla de Catalunya.** Jsou to dvě různé ulice s podobným jménem. Rambla de
Catalunya leží o pár bloků výš, je stále centrální, ale klidnější, s lepšími podniky a místními
hosty.

### Ceny nápojů a drobností

Orientační ceny (jde o agregátory cen, ne o ceníky konkrétních podniků):

- **Espresso: 1,20–1,80 EUR**, v turistických místech až 2,50 EUR. Cappuccino kolem 2,30 EUR.
- **Pivo v baru: kolem 2,50 EUR.** Tady ale pozor — jiný zdroj uvádí průměr až 7 EUR za pivo
  ve čtvrťové hospodě. Rozdíl je nejspíš v objemu a lokalitě, ale doložit se to nepodařilo, takže
  ber 2,50 EUR jako spodní orientaci, ne jako pravidlo.
- **Pivo ze supermarketu (0,5 l): kolem 1,23–1,25 EUR.** Dva litry Coca-Coly 2,09 EUR.
- **Rychlé občerstvení nebo jídlo s sebou: 4–8 EUR.**

Chráněné tokeny, které musí zůstat přesně: `["2,50 EUR","2,30 EUR","7 EUR","1,23–1,25 EUR","2,09 EUR","4–8 EUR","3","11","20","1,20–1,80","2,50","2,30","7","0,5","1,23–1,25","2,09","4–8","ne","obvykle","Jak","La Rambla","Podniky","Jeden","Varovné","Nahaněč","Velké","Nabídka","Předpřipravená","Fotka","Zářivě","Pravý","Španělsku","Místní","Dobrá","Nezaměňuj La Rambla","Rambla","Catalunya","Jsou","Ceny","Orientační","Espresso","Cappuccino","Pivo","Tady","Rozdíl","Dva","Coca-","Coly","Rychlé","La Rambla je opakovaně jmenovaná jako místo, kde se nemá jíst.","Varovné signály, které fungují okamžitě:","Fotka paelly vyvěšená před podnikem","Zářivě žlutá paella.","paella je ve Španělsku tradičně obědové jídlo.","20 minutami a víc","Nezaměňuj La Rambla a Rambla de Catalunya.","Espresso: 1,20–1,80 EUR","Pivo v baru: kolem 2,50 EUR.","Pivo ze supermarketu (0,5 l): kolem 1,23–1,25 EUR.","Rychlé občerstvení nebo jídlo s sebou: 4–8 EUR.","sangria a paella"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
