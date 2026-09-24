# Otevřené otázky z Fáze 1 (research) — Barcelona

Souhrn napříč všemi research soubory (`content/barcelona/research/`), co se rozcházelo mezi zdroji
nebo se nepodařilo spolehlivě ověřit. Před vydáním produktu (Fáze 4 QA) je potřeba tyto body
proklepnout — buď doověřit, nebo zkontrolovat, že je text formuluje dostatečně opatrně.

Seskupeno podle toho, co s tím má QA udělat, ne podle research souborů.

Stav k 2026-08-02 (sběr dat 2026-07-31).

## 0. Blokující — vyřešit jako první

- **🔴 Je Sagrada Família vůbec otevřená?** Oficiální web `sagradafamilia.org` na stránce vstupenek
  a v kalendáři akcí uvádí, že je bazilika **dočasně uzavřená pro veřejnost** a odkazuje na
  virtuální prohlídky. Cenová stránka téhož webu přitom normálně zobrazuje ceník a jiné zdroje
  tvrdí, že v roce 2026 nejsou žádné dny uzavření. Důvod ani termín znovuotevření se nepodařilo
  zjistit.
  **Dopad:** mění kapitolu 05 (Památky), oba dvoudenní itineráře, kapitolu 07 (Rozpočet)
  i kapitolu 08 (Checklist). Kapitoly to teď řeší tak, že otevření **netvrdí** a nabízejí náhradu
  (Sant Pau, 5 minut chůze).
  **Jak ověřit:** informacio@sagradafamilia.org, +34 932 080 414. Ověřit **těsně před vydáním**,
  ne dopředu.

## 1. Ceny a jízdní řády — doověřit těsně před vydáním

Konkrétní čísla, která v produktu zůstanou vytištěná. Všechna jsou z podstaty proměnlivá.

- **Aerobús** — oficiální ceník Monbus uvádí 7,45 / 12,85 EUR od 1. 3. 2026, ale cestovatelský web
  uvádí 9,50 / 16,50 EUR za „advance tickets". Není jasné, jestli jde o zastaralý údaj, jiný typ
  jízdenky nebo prodej přes zprostředkovatele. Ceníková stránka dopravce má ceny jen v obrázcích.
  Doověřit na aerobusbarcelona.es.
- **Vlak Rodalies R2 Nord z letiště** — zdroje uvádějí 4,60 EUR i 2,90 EUR. Doověřit u Rodalies
  de Catalunya.
- **Hola Barcelona Travel Card** (48/72/96/120 h za 18,70 / 27,30 / 35,60 / 43,60 EUR) — čísla
  pocházejí z cestovatelského webu, ne z ceníku provozovatele (oficiální stránka ceny v textu
  neuvádí). Doověřit na holabarcelona.com. **Blokuje i doporučení T-casual vs. Hola Barcelona**,
  protože na těch cenách stojí zlomová hranice ~21 jízd.
- **Zpáteční Cremallera na Montserrat** — 14,50 EUR proti 15 EUR. Doověřit u FGC /
  cremallerademontserrat.cat. Ovlivňuje i součet 36,80 EUR za celý den.
- **Girona a Figueres vlakem** — jediný nalezený údaj je „kolem 12 USD" jedním směrem, tedy v cizí
  měně a bez rozlišení příměstského a rychlého vlaku (mají výrazně jinou cenu i čas). Doověřit
  v EUR u Renfe/Rodalies. **Neuvádět v EUR bez přepočtu z ověřeného zdroje.**
- **Vstupné Museu Picasso** — 12/14 EUR proti 15/19 EUR. Doověřit na museupicasso.bcn.cat.
- **Vstupné Recinte Modernista de Sant Pau** — 34 EUR proti „od 17 EUR". Rozdíl je dvojnásobný,
  může jít o různé typy vstupenky nebo o slevu přes Barcelona Card. Doověřit na
  santpaubarcelona.org.
- **Vstupné Parc del Laberint d'Horta** — 2,23 EUR proti 2,50 EUR. Doověřit na webu města.
- **Casa Batlló a La Pedrera** — ceny jsou ze sekundárních zdrojů a všechny jako „od" (dynamické
  ceny podle termínu). Doověřit na casabatllo.org a lapedrera.com; v textu držet formulaci „od".
- **Stoletý příplatek k Sagradě Famílii 2–5 EUR (květen–prosinec 2026)** — zmiňuje ho jen prodejní
  web, na oficiálním ceníku nebyl vidět. Doověřit, nebo z textu vypustit.
- **Turistická daň pro hotely 1–3\*** — zdroje vyčíslují 5\*, 4\*, apartmány, hostely a „ostatní",
  kategorie 1–3\* samostatně chybí.
- **Ceny ubytování za noc** — orientační průměry ze sekundárního zdroje, navíc míchají EUR a USD.
  Doověřit na rezervačních portálech těsně před vydáním.
- **Ceny letenek Praha–Barcelona** — jediná položka v Kč, orientační. Ověřit před vydáním.

## 2. Nedoložená tvrzení — v textu držet opatrnou formulaci

Tady nejde o čísla k doplnění, ale o tvrzení, která by se **neměla** dostat do textu jako fakt.
Úkol QA je ověřit, že se tam nevloudila.

- **Platební zvyklosti přímo v Barceloně** — jak často narazíš na cash-only podnik, minimální
  částka pro platbu kartou, platba kartou v taxi. Nedoloženo pro Barcelonu. Netvrdit o Barceloně
  to, co je doložené o Španělsku obecně nebo o jiné destinaci.
- **Platí T-casual na příměstských vlacích Rodalies?** Jeden blog tvrdí, že ano v rámci svých zón.
  Je to zásadní tarifní tvrzení opřené o jediný neoficiální zdroj — **netvrdit bez doložení**
  u ATM / Rodalies de Catalunya. (Hola Barcelona Rodalies v zóně 1 zahrnuje doloženě.)
- **Konkrétní trasa a doprava na Bunkers del Carmel** — potvrzeno jen to, že z každé zastávky je
  nahoru výšlap. Konkrétní linka, zastávka ani délka výšlapu doložené nejsou.
- **Čísla o kapesních krádežích** — 94 517 za rok 2024 i pokles o 40 % v roce 2026 pocházejí ze
  sekundárních zdrojů (cestovatelské weby), ne přímo od Mossos d'Esquadra. Text u obou drží
  výhradu; ověřit, že tam zůstala.
- **Bicing** (sdílená kola) — nesbíráno. Podle obecně dostupných informací je pro rezidenty, ne
  pro turisty, ale **neověřeno** — do textu bez ověření nepatří.
- **Tísňová linka 112** — nepodařilo se doložit z oficiálního zdroje pro Španělsko. Text ji záměrně
  neuvádí. Doplnit až po ověření.
- **Tvrzení, že Sants má nejlepší poměr ceny a kvality u menú del día ve městě** — stojí na jediném
  zdroji a je subjektivní. V textu je podané jako zmínka zdroje, ne jako fakt.
- **PEUAT** (plán města regulující ubytovací kapacity) — dopad na turistu neověřen, text ho
  nezmiňuje.
- **Zásuvky a napětí, lékárny a pohotovost, seznam věcí do kufru** — neověřeno, text je vědomě
  neuvádí.

## 3. Chybějící detaily — doplnit při finalizaci

- **Ověřená URL registru turistických bytů** města (Habitatges d'Ús Turístic). Text na registr
  odkazuje, ale bez konkrétní adresy — čtenáři se nedává návod, který nemá kam vést.
- **Zónové zařazení výletů** (Sitges, Montserrat, Tarragona) — bez něj nejde poradit, kdy se vyplatí
  dvouzónová T-casual za 25,50 EUR.
- **Kdy přesně se u Bunkers del Carmel přepíná letní a zimní režim** (19:30 / 17:30). Doložené je
  jen „léto/zima" bez dat.
- **Otevírací doby památek** kromě Park Güell a Sant Pau — nesbírány.
- **Ceny podle čtvrtí** — doložený je jen Eixample (180–200 EUR v létě). Pro Poblenou, Poble Sec
  a Sant Antoni chybí čísla, takže se nedá tvrdit, o kolik jsou levnější.
- **Doba chůze mezi čtvrtěmi a k památkám** — doložená je jen chůze Poble Sec → centrum (pod
  20 minut).
- **Rekonstrukce Mercat de Sant Antoni** — jeden zdroj mluví o probíhající kompletní rekonstrukci,
  jiné o funkčním místě k návštěvě. Stav si odporuje.
- **Cena vody v lahvi, ceny jednotlivých tapas, nákup v supermarketu na den** — chybí, takže se
  nedá sestavit varianta „vaříme si sami".
- **La Boqueria** — vůbec nesbírána, přestože je to jedno z nejnavštěvovanějších gastro míst města.
- **Barcelona Card** — nesbírána; u rozpočtu by dávalo smysl porovnat ji s jednotlivými vstupenkami.
- **Casa Vicens, Palau de la Música** — ceny se nepodařilo dohledat.

## 4. Kontrolovat při každém vydání (nezastarává jen jednou)

- **Stav ETIAS a EES** — spuštění se posouvalo, mluví se o odkladu na 2027, po spuštění má být
  šestiměsíční přechodné období. Občanů EU se ETIAS netýká, ale stav zkontrolovat na mzv.gov.cz.
- **Kontaktní údaje honorárního konzulátu ČR v Barceloně** — na internetu kolují dvě různé sady
  (jiné telefonní číslo, jiný e-mail, jiná nouzová linka, jiné úřední hodiny). V textu jsou údaje
  z oficiální stránky MZV. **Ověřit před každým vydáním** — špatné číslo na konzulát je v placeném
  průvodci nejhorší možná chyba.
- **Stav licencí HUT** — turistické apartmány dobíhají do listopadu 2028, licence se od 2029
  neobnovují. Zkontrolovat, jestli v době vydání pořád platí, že se legální apartmán dá
  zarezervovat.
- **Turistická daň** — městská přirážka roste o 1 EUR ročně (6 EUR v 2027, 7 v 2028, 8 v 2029).
  Sazby v kapitolách 01 a 07 se musí měnit s ní.
- **Ceník TMB** — mění se typicky k lednu (ceník 2026 platí od 15. 1. 2026).
- **Sezónnost cen** — všechny údaje o ubytování jsou letní. Text nesmí uvádět jedno číslo jako
  platné celoročně.
- **Vstupné** — u většiny památek se mění každoročně, část má dynamické ceny.

## 5. Žebříčky podle recenzí — nevznikly, rozhodnout, jestli je doplnit

Na rozdíl od Lloretu **Barcelona nemá v žádné kapitole jmenovaný konkrétní podnik**. Sběr podle
`docs/metodika-hodnoceni.md` se nepodařilo doložit:

- **Hotely (kapitola 03):** nalezené seznamy pocházely z Hotels.com, Tripadvisoru a Trip.com,
  počty recenzí byly nízké (např. 71) a hodnocení z Google Maps se nepodařilo dohledat vůbec.
  Metodika přitom žádá Google Maps + Booking.com, obě s min. 400 recenzemi.
- **Restaurace (kapitola 04):** nalezené seznamy byly SEO a blogové výběry bez počtů recenzí.
  Metodika žádá Google Maps + Tripadvisor, min. 500 na Google a 250 na Tripadvisoru.
- **Atrakce (kapitola 05):** žebříček nevznikl, kapitola atrakce neřadí podle hodnocení.
- **Podniky v Sant Antoni, Sants a Sarrià (kapitola 06):** nejmenované ze stejného důvodu.

Podle pravidla 6 metodiky („negativní nález je taky nález") je to zapsané a žebříčky se nedoplňují
slabšími daty. Kapitoly 03, 04 a 06 to čtenáři **otevřeně vysvětlují**.

**Rozhodnutí pro Fázi 4:** buď se udělá samostatný sběr přímo z Google Maps, Booking.com
a Tripadvisoru, nebo Barcelona zůstane bez jmenovaných podniků. Je to největší obsahový rozdíl
proti Lloretu a zároveň největší přidaná hodnota, kterou by šlo doplnit.

## Doporučení

1. **Sagrada Família (sekce 0) je jediná položka, která se musí vyřešit před čímkoli dalším** —
   ovlivňuje čtyři kapitoly a oba itineráře.
2. Body ze sekce 1 doověřit **až těsně před vydáním**, ne teď — jinak se do dne vydání stihnou
   znovu změnit. Do té doby je v textu psát s výhradou.
3. Sekci 2 projít jako kontrolní seznam proti hotovým kapitolám — jsou to místa, kde fact-checker
   opakovaně chytal ztracenou opatrnost.
4. Sekce 4 patří do QA checklistu jako **opakovaná** položka, ne jednorázová. Kontakty na konzulát
   mají v téhle sekci nejvyšší prioritu.
5. Sekce 5 je rozhodnutí o rozsahu produktu, ne úkol — vyřešit vědomě, ne mimochodem.
6. Pokud bude příležitost cokoli doověřit u někoho s reálnou znalostí Barcelony, nejlepší poměr
   užitku k námaze mají **platební zvyklosti** a **platnost T-casual na Rodalies** — obojí se týká
   každodenní situace čtenáře a obojí je teď v textu vědomě vágní.
