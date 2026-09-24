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
- Strana: `guide-01-04-checklist`
- Layout: `Checklist`

## Exact content contract
Na stránce smí být pouze následující obsah:

### SIM a internet

Předplacené SIM ve Španělsku začínají zhruba na **10 EUR** a za tu cenu bývá 60–90 GB dat.
Z konkrétních nabídek k roku 2026: Orange 10 EUR za 80 GB, Vodafone 15 EUR za 270 GB (z toho 15 GB
roamingu v EU), 20 EUR za 330 GB nebo 30 EUR za 380 GB — vše na 28 dní s neomezeným voláním po
Španělsku.

Alternativou je **eSIM**, kterou si aktivuješ ještě před odletem. Tady pozor na měnu: část ceníků je
v dolarech (nejlevnější tarify od zhruba 3 USD za 1 GB, kolem 13 USD na 30 dní), část v eurech
(1 GB na 7 dní za 7,95 EUR, 5 GB na 30 dní za 16,95 EUR, 10 GB na 30 dní za 25,95 EUR). Nemíchej si
to dohromady — a ceny u eSIM se mění častěji než u klasických SIM, takže je zkontroluj až těsně před
cestou.

### Peníze

Ve Španělsku se platí eurem. Konkrétní platební zvyklosti přímo v Barceloně — jak často narazíš na
podnik, který bere jen hotovost, jestli má taxi povinnost vzít kartu, jaká bývá minimální částka pro
platbu kartou — se nám z dostupných zdrojů nepodařilo spolehlivě doložit, takže tady raději netvrdíme
nic natvrdo. Drobná hotovost u sebe je bezpečná volba a orientační ceny běžných výdajů najdeš
v kapitole Rozpočet.

Chráněné tokeny, které musí zůstat přesně: `["10 EUR","15 EUR","20 EUR","30 EUR","7,95 EUR","16,95 EUR","25,95 EUR","10","60–90","2026","80","15","270","20","330","30","380","28","3","1","13","7","7,95","5","16,95","25,95","jen","Předplacené","Španělsku","Orange","Vodafone","Alternativou","Tady","Nemíchej","Peníze\n\nVe Španělsku","Konkrétní","Barceloně","Drobná","Rozpočet","eSIM"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
