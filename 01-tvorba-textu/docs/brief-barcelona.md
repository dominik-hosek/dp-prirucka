# Destinační brief: Barcelona

Status: návrh k potvrzení

## Proč Barcelona (shrnutí Fáze 0 validace)

- Barcelona je nejnavštěvovanější město Španělska a jedna z nejnavštěvovanějších destinací Evropy —
  oficiální odhady mluví o ~26 milionech turistů ročně, občanská hnutí o ~31 milionech, zhruba
  dvacetinásobku počtu obyvatel města. Poptávka je tedy trvalá, ne módní vlna.
- Nabídka pro českého čtenáře je hlavně **zájezdová**. Poznávací zájezdy a eurovíkendy nabízí Čedok,
  Fischer, Radynacestu, GEOPS, České kormidlo i agregátory (Zájezdy.cz, Dovolena.cz) — a všechny
  jedou stejný okruh: Sagrada Família, Park Güell, La Rambla, Camp Nou, Gotická čtvrť. To je přesně
  ta úroveň informace, kterou persona nechce.
- **Hlavní diferenciace: Barcelona se právě mění a čtenář o tom neví.** Město zavádí sadu opatření
  proti přeturističtění — rostoucí turistická daň, omezení výletních lodí a hlavně plán úplně
  ukončit krátkodobé turistické pronájmy (nové licence od listopadu 2028, stávající se od 2029
  neobnovují; potvrzeno španělským Ústavním soudem v březnu 2025). Průvodce, který tohle vysvětlí
  a řekne, co z toho pro plánování plyne, dává hodnotu, kterou zájezdový web dát nemůže.
- Druhá diferenciace je **provozní, ne inspirační**: v Barceloně se zážitek nerozhoduje podle toho,
  co vidíš, ale kdy a s jakou vstupenkou tam přijdeš. Vstupenky na Gaudího památky se vyprodávají
  dopředu, jízdenkový systém je netriviální a rozdíl mezi dobře a špatně naplánovaným dnem je
  několik hodin ve frontě.
- Riziko: Barcelona je nejpokrytější město v evropském cestovatelském obsahu. Diferenciace **nesmí**
  být v pokrytí ("co vidět"), ale v provozních rozhodnutích, v datech s datem ověření a v tom, co
  se v roce vydání reálně mění.

## Cílová persona

**"Nezávislý plánovač"** — stejná persona jako u ostatních destinací řady, aby produkty držely
pohromadě. Český/slovenský cestovatel 28–50 let, cestuje s partnerem, s kamarády nebo s rodinou,
letenku a ubytování si řeší sám. Do Barcelony jede typicky na **3–5 dní** (prodloužený víkend až
kratší dovolená), ne na dvoutýdenní pobyt. Chce vědět, jak si den poskládat, aby nestrávil polovinu
fronty a MHD, co si musí koupit dopředu, kde se najíst mimo La Ramblu a jak si udělat výlet
z města. Střední rozpočet — ne backpacker, ne luxus.

Rozdíl oproti pobytovým destinacím řady (Lloret): tady se neřeší "která pláž", ale **čas, vstupenky
a pořadí**. Osnova to musí odrážet.

## Rozsah obsahu (návrh osnovy)

1. Praktické základy (kdy jet, z letiště do centra, peníze, SIM/internet, bezpečnost a kapsáři,
   turistická daň)
2. Doprava po městě a do okolí (metro, jízdenky a pásma, taxi, kolo, vlaky na výlety)
3. Ubytování — čtvrti a typy (kde bydlet podle toho, co od pobytu chceš; co znamená konec
   krátkodobých pronájmů)
4. Jídlo a pití (tapas, menú del día, vermut, ceny, jak nesednout turistické pasti)
5. Památky, výlety a itineráře (Gaudí, muzea, vstupenky a rezervace, výlety z města) —
   2–3 hotové itineráře po dnech
6. "Off the beaten path" — místa a čtvrti mimo hlavní trasu
7. Rozpočtová kalkulačka / cenová orientace
8. Praktický checklist před odjezdem

Osnova záměrně kopíruje strukturu ostatních destinací řady (produkt má být rozpoznatelný), ale
kapitoly 2 a 5 mají jiné těžiště: u pobytové destinace je to "jak se dostat na výlet", tady "jak
zvládnout město a kdy z něj vyrazit ven".

## Rozsah produktu

Zákazník dostává dva soubory:

1. **Příručka** — 8 kapitol podle osnovy výše, plná verze ke čtení před cestou.
2. **Rychlotaháček do kapsy** — týchž 8 kapitol zhuštěných do frází, každá na max. 1 stranu A4.
   Obsahuje jen to, co se rozhoduje na místě (čísla, směry, otevírací doby, rozhodovací pravidla),
   nepřidává nic nad rámec příručky. Odvozuje se z uzavřeného textu — viz `/tahacek` v
   `docs/automation-registry.md`.

U městské destinace je taháček ještě užitečnější než u pobytové: čtenář se v Barceloně za den
rozhoduje mnohokrát (kterou jízdenku, kam na oběd, jestli stihne další památku) a příručku u toho
neotevře.

## Cena

- **199 Kč** za oba soubory — stejná vstupní cena jako u zbytku produktové řady (Albánie, Lloret),
  pro konzistenci. Zdůvodnění hodnoty: úspora času a peněz na jednom pobytu (jedna neprošvihnutá
  rezervace vstupenky nebo jedna správně zvolená jízdenka) přesahuje cenu produktu.

## Rozhodnutí

- [ ] Potvrdit destinaci: Barcelona
- [ ] Potvrdit personu (3–5denní pobyt, ne pobytová dovolená)
- [ ] Potvrdit cenu: 199 Kč
- [ ] Potvrdit osnovu

**Pozor — pravidlo pilota.** Kořenový `CLAUDE.md` říká, že se další destinace rozjíždějí až po
vyhodnocení pilota (Fáze 9). Barcelona vznikla na přímé zadání vedle běžícího pilota (Lloret);
než se do ní investuje dál (vizuál, web, PPC), je potřeba tohle rozhodnout vědomě.

Po potvrzení pokračujeme Fází 1 (research & sběr dat) do `content/barcelona/research/`.

## Zdroje k validaci

- Rozsah turismu a opatření města: https://denikreferendum.cz/clanek/36615-jak-omezit-masovy-turismus-barcelona-vybizi-cely-svet-k-novemu-pristupu — ověřeno 2026-07-31
- Konec krátkodobých pronájmů (2028/2029, Ústavní soud 3/2025): https://www.idealista.com/en/news/property-for-rent-in-spain/2025/06/12/848193-goodbye-airbnb-barcelona-sets-2028-deadline-to-phase-out-tourist-apartments — ověřeno 2026-07-31
- Nabídka českých CK: https://www.zajezdy.cz/poznavaci-barcelona-m23571/, https://www.cedok.cz/dovolena/barcelona/, https://www.fischer.cz/spanelsko/barcelona-a-okoli/barcelona — ověřeno 2026-07-31
