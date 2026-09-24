# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Barcelona`
- Země: `Španělsko`
- Oddíl: `Off the beaten path`
- Strana: `guide-06-04-two-equal-sections`
- Layout: `Two equal sections`

## Exact content contract
Na stránce smí být pouze následující obsah:

### Čtvrti, kde se nehraje na turisty

**Sant Antoni** leží na styku spodního Eixample, El Raval a Poble-Sec. Má kavárny a tapas bary
a hlavně **Mercat de Sant Antoni**, popisovanou jako nejlepší tržnici ve městě pro nákup bez
turistické obsluhy. **Carrer del Parlament** je lemovaná nezávislými knihkupectvími, vinnými bary
a místními designéry.

Nejkonkrétnější program, jaký v téhle kapitole dostaneš: **nedělní dopoledne v Sant Antoni** —
bazar s knihami z druhé ruky před tržnicí a pak dlouhá snídaně na terase. Není to „projdi se
čtvrtí", je to naplánovatelný půlden.

Jedna výhrada: zdroje si nejsou jednotné v tom, jestli tržnice právě neprochází kompletní
rekonstrukcí. Ověř si to před cestou.

**Sants** je dělnická čtvrť se silným sousedským charakterem. Hlavní třída **Carretera de Sants**
má nezávislé obchody, pekárny a řeznictví, k tomu tržnici **Mercat Nou**. Zdroj ji označuje za
čtvrť s nejlepším poměrem ceny a kvality u menú del día ve městě — je to jediná konkrétní zmínka
tohohle typu, na kterou jsme narazili, a je z podstaty subjektivní, ale jako vodítko, kam vyrazit
na levný oběd, funguje. **Mercat de Sants** funguje úplně bez zaměření na turisty.

**Sarrià** má **Mercat de Sarrià**, nóbl čtvrťovou tržnici s klasickým katalánským charakterem.

**Poblenou**, bývalé textilní továrny přestavěné na ateliéry a střešní bary, je zároveň brána
ke klidnějším plážím — jako místo k bydlení je popsané v kapitole Ubytování.

### Proč tu nejmenujeme konkrétní podniky

V těchhle čtvrtích by se hodilo doporučit konkrétní bar nebo restauraci. Nedáváme je, protože
dostupné zmínky pocházejí z blogů a SEO webů, ne z ověřených hodnocení na dvou nezávislých
platformách. Radši ti dáme čtvrť a den, než jméno, za kterým nestojí data.

Chráněné tokeny, které musí zůstat přesně: `["ne","Čtvrti","Sant Antoni","Eixample","El Raval","Poble-","Sec","Má","Mercat","Carrer","Parlament","Nejkonkrétnější","Není","Jedna","Ověř","Sants","Hlavní","Carretera","Mercat Nou","Zdroj","Poblenou","Ubytování","Proč","Nedáváme","Radši","Mercat de Sant Antoni","Carrer del Parlament","nedělní dopoledne v Sant Antoni","Carretera de Sants","Mercat de Sants","Sarrià","Mercat de Sarrià"]`

## Country system
`{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
