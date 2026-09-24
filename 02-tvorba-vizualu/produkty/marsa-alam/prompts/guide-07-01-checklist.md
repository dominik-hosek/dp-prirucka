# Destination page generation

## Use case
Jedna finální bitmapová strana prémiového digitálního turistického průvodce, poměr 2:3.

## Reference roles
- `REFERENCE_LAYOUT` je hlavní strukturální reference pro hierarchii, komponenty a rytmus.
- `COUNTRY_ANCHOR`, pokud je přiložen, určuje paletu, typografický pocit, dekorativní motivy a fotografické zpracování. Nepřenášej z něj žádný text.

## Page identity
- Destinace: `Marsa Alam`
- Země: `Egypt`
- Oddíl: `Rozpočtová kalkulačka`
- Strana: `guide-07-01-checklist`
- Layout: `Checklist`

## Exact content contract
Na stránce smí být pouze následující obsah:

All-inclusive balíček vyřeší ubytování a jídlo, ale výlety, potápění a poušť jsou skoro vždy extra.
Tahle kapitola shrnuje orientační ceny z celého průvodce na jedno místo, ať máš před cestou
představu, s kolik navíc počítat.

### Přehled cen navíc k balíčku

| Položka | Rozptyl | Kde v průvodci |
|---|---|---|
| Vízum (e-visa / on arrival) | 25–30 USD | kap. Praktické základy |
| Transfer z letiště do Port Ghalib | 13–25 USD | kap. Praktické základy, Výběr oblasti |
| Šnorchlování Abu Dabab (celý den) | 48–60 USD/os. | kap. Potápění a šnorchlování |
| Šnorchlování Dolphin House (celý den) | 55–62 USD/os. | kap. Potápění a šnorchlování |
| Potápění Elphinstone (2 ponory) | 85–130 USD | kap. Potápění a šnorchlování |
| Poplatek mořského parku (na ponor) | 15–25 USD | kap. Potápění a šnorchlování |
| Pouštní safari Wadi El Gemal (skup.–soukr.) | 90–228 USD/os. | kap. Výlety mimo vodu |
| Vstup NP Wadi El Gemal | ~40 EGP (≈ 2 EUR) | kap. Výlety mimo vodu |
| Kempování v NP (os./noc) | ~200 EGP | kap. Výlety mimo vodu |
| Výběr z bankomatu (poplatek) | 50–100 EGP | kap. Praktické základy |

Zdroje jednotlivých položek jsou uvedené u příslušných kapitol — ceny jsou orientační rozptyly z
aktuálních nabídek, ne ceníky, a v Egyptě se mění rychle i s kurzem.

### Jak si postavit vlastní rozpočet

Nejdřív si urči, co je pro tebe hlavní náplň pobytu — voda, nebo kombinace s pouští — a podle toho
škrtej. Týden zaměřený hlavně na šnorchlování si vystačí s Abu Dabab a Dolphin House a jedním
poušťním výletem navíc. Pokud chceš i potápět, přičti Elphinstone a poplatek parku — u vícedenního
potápění se tahle položka násobí podle počtu ponorů, ne podle dní. Skupinové safari do pouště
vychází výrazně levněji než soukromé; zvol soukromé jen tehdy, když ti stojí za to mít vlastní tempo.

K tomu si nezapomeň přičíst hotovost na drobné výdaje mimo balíček (voda, spropitné, drobné nákupy)
a počítat s poplatkem za výběr z bankomatu, pokud si peníze budeš vybírat na místě místo směny
předem.

Chráněné tokeny, které musí zůstat přesně: `["2 EUR","25–30","13–25","48–60","55–62","2","85–130","15–25","90–228","40","200","50–100","ne","jen","All-inclusive","Tahle","Přehled","Položka","Rozptyl","Kde","Vízum","Praktické","Transfer","Port Ghalib","Výběr","Šnorchlování Abu Dabab","Potápění","Šnorchlování Dolphin House","Potápění Elphinstone","Poplatek","Pouštní","Wadi El Gemal","Výlety","Vstup","Kempování","Zdroje","Egyptě","Jak","Nejdřív","Týden","Abu Dabab","Dolphin House","Pokud","Elphinstone","Skupinové"]`

## Country system
`{"palette":{"background":"#F4E9D8","primary":"#0F6473","secondary":"#C96A32","accent":"#CBA85B","text":"#201A16"},"heading_fonts":["Cormorant Garamond","Prata"],"body_fonts":["Manrope","Source Sans 3"],"motifs":["jemné vlny Rudého moře","korálové větvení","pouštní horizont","stylizované slunce"],"photo_style":"čistá tyrkysová voda, teplý pouštní písek, korálové detaily a přirozené slunce","character":"klidný prémiový red-sea editorial s kontrastem moře a pouště"}`

## Constraints
- Zachovej všechna čísla, měny, časy, data, vlastní jména, negace a opatrné formulace přesně.
- Nic věcně nepřidávej ani nevynechávej. Běžnou prózu smíš jen typograficky přeskupit nebo významově neutrálně zkrátit, pokud to manifest výslovně dovoluje.
- Pokud se obsah nevejde čitelně, nekomprimuj jej násilně: vrať jasně nehotovou stránku určenou k přeplánování, nikoli chybějící obsah.
- Všechen viditelný text musí být česky. Žádná loga, watermarky, anglické popisky, náhodné cedule ani smyšlené podniky či názvy.
- Bez přetečení, překryvů, nečitelných znaků a ořezaných komponent. Dodrž poměr 2:3 a bezpečné okraje.
- Vytvoř jednu jedinou finální variantu této stránky.
