# Kontrolní list — kapitola 06: Off the beaten path

Zdroj: `../../../01-tvorba-textu/content/lloret-de-mar/text/06-off-the-beaten-path.md`

Postup generování je v `../../docs/prompt-guide.md`. Tenhle list slouží ke **kontrole vygenerovaných
stránek proti zdroji**.

## Sekce (počet, pořadí, nadpisy)

Kapitola má **6 podsekcí** v tomto pořadí:

1. Skryté zátoky
2. Pobřežní stezka
3. Zahrady Santa Clotilde navečer
4. Modernistický hřbitov
5. Sousední města mimo hlavní trasu
6. Tip navíc

Sekce **Modernistický hřbitov** (doplněná 2026-07-29) je nejdelší v kapitole — pět odstavců, včetně
jmen architektů a čtyř letopočtů. Počítej u ní s vlastní stránkou.

Plus úvodní odstavec pod nadpisem kapitoly, bez vlastního podnadpisu.

Struktura, která musí zůstat:

- **Skryté zátoky** — odrážkový seznam **4 zátok** s tučnými názvy. Poslední odrážka (Cala Forcanera)
  je výrazně delší než ostatní, protože nese celou opatrnou formulaci — nesmí se zkrátit na úroveň
  předchozích tří.
- **Sousední města** — odrážkový seznam **3 měst** s tučnými názvy, a **za ním samostatný odstavec**
  s výčtem dalších městeček. Ten odstavec není součástí seznamu.

Název kapitoly je anglický („Off the beaten path") — je to záměr, tak je to i v osnově. Nepřekládat.

## Dlouhý výčet městeček — nejrizikovější místo kapitoly

V odstavci pod odrážkami stojí **12 jmen v závorce za sebou**:

> Pals, Begur, Tamariu, S'Agaró, Empuriabrava, Llafranc, L'Estartit, Aigua Blava, Fornells,
> Calella de Palafrugell, Calonge, Palamós

Dvanáct cizích jmen bez kontextu je přesně to, u čeho model tiše vypustí jednu položku nebo dvě
slepí dohromady — a při čtení stránky to nikdo nepozná, protože seznam vypadá pořád stejně
věrohodně. **Počítej je.** Musí jich být 12 a v tomhle pořadí.

Pozor na apostrofy: **S'Agaró** a **L'Estartit**. Apostrof i čárka nad „o" musí zůstat.
**Calella de Palafrugell** jsou tři slova, ne jedno.

Rámec věty: městečka leží **mezi Rosas a Tossa de Mar** — v textu je tvar „Rosas" (ne „Roses"),
drž se textu.

## Čísla — musí sedět přesně

| Údaj | Správně |
|---|---|
| Cala Sa Boadella — délka | cca **250 m** |
| Tossa de Mar — stálí obyvatelé | jen kolem **6 200** mimo sezónu |
| Santa Clotilde — vstupné | **6,10 EUR** dospělí / **3,10 EUR** snížené |
| Santa Clotilde — otevírací doba | duben–říjen denně **10:00–20:00** |
| Hřbitov — výběr pozemku | **1891** |
| Hřbitov — otevření | **1901** |
| Hrobka rodiny Costa i Macià | **1902** |
| Hřbitov — podzemní hrobky Conilla | **1903–1909** |
| Hřbitov — otevírací doba | duben–říjen **8:00–20:00**, listopad–březen **8:00–18:00** |
| Hřbitov — vzdálenost od St. Quirze | asi **200 metrů** |

Číslo 6 200 se píše s mezerou jako oddělovačem tisíců. Model rád doplní tečku nebo čárku.

**Čtyři letopočty v jedné sekci** (1891, 1901, 1902, 1903–1909) jsou nejrizikovější místo nové části.
Jsou si blízké, tři z nich začínají „190" a každý patří k jinému tvrzení. Kontroluj je jeden po
druhém proti tabulce, ne čtením.

**Dvojí otevírací doba** — zahrady mají 10:00–20:00, hřbitov 8:00–20:00. Liší se jen začátkem
a stojí pár odstavců od sebe.

## Opatrné formulace — nesmí se z nich stát tvrzení najisto

- U **Cala Forcanera** musí zůstat, že se **trasu ani vzdálenost nepodařilo ověřit z víc zdrojů**
  a že se bude potřeba doptat na místě (v půjčovně paddleboardů nebo v infocentru). Tohle je
  otevřená otázka z Fáze 1 — když z toho model udělá návod, vznikne tvrzení bez opory a čtenář
  vyrazí hledat cestu, která možná neexistuje.
- U **Cala dels Frares** musí zůstat, že je **bez základních služeb** (bez baru, sprch) — to je
  důvod, proč je prázdná, a zároveň praktické varování.
- U Tossa de Mar musí zůstat, že jde o **počet stálých obyvatel mimo sezónu** — bez toho by 6 200
  vypadalo jako počet lidí ve městě v létě, což je nesmysl.
- V Tipu navíc musí zůstat, že si má čtenář **vzdálenost a dobu cesty ověřit podle aktuálního
  jízdního řádu** — je to druhá otevřená otázka z Fáze 1.

## Vlastní jména — musí být přesně

- **Cala Sa Boadella**, **Cala Banys**, **Cala dels Frares**, **Cala Forcanera**
- **Josep Puig i Cadafalch** (architekt hrobky Costa i Macià — čtyři slova, „i" je spojka a píše se
  malým písmem; model z toho udělá „Puig I Cadafalch" nebo jméno zkrátí)
- **Bonaventura Conill i Montobbio** (architekt podzemních hrobek, žák Gaudího — dvě „l" v Conill,
  dvě „b" v Montobbio)
- **Costa i Macià** (rodina, jejíž hrobku Puig i Cadafalch navrhl — `à` s obrácenou čárkou)
- **Antoni Gaudí** (`í` s čárkou)
- **indianos** (malým písmem, kurzívou nebo v uvozovkách podle sazby — je to označení skupiny lidí,
  ne vlastní jméno)
- **Camí del Repòs** (adresa hřbitova — `í` s čárkou, `ò` s obrácenou čárkou)
- **St. Quirze** (orientační bod u hřbitova)
- **Association of Significant Cemeteries in Europe** (anglický název organizace — jediné místo
  v průvodci, kde anglický text být má; nepřekládat a nezkracovat na ASCE, text zkratku nepoužívá)
- **Camí de Ronda** (pobřežní stezka — `í` s čárkou)
- **Cala Canyelles**, **Santa Cristina** (zmíněné jako navazující trasa)
- **Santa Clotilde** (zahrady)
- **Blanes**, **Sant Feliu de Guíxols** (`í` s čárkou), **Tossa de Mar**
- plus 12 městeček z výčtu výše

## Fotky

- Zátoky **nepodepisovat**. Cala Banys, Cala dels Frares a Cala Forcanera jsou reálná, málo známá
  místa — model si je vymyslí a nikdo to nepozná, dokud tam čtenář nedojede.
- U zahrad Santa Clotilde nesmí být čitelná informační cedule ani vstupné. Cena patří do textu
  a infografiky, ne na vymyšlenou ceduli u vchodu.
- **Konkrétní hrobky na hřbitově nepodepisovat.** Hrobka rodiny Costa i Macià je reálná stavba od
  reálného architekta — model ji nevygeneruje věrně a popisek by z vymyšlené stavby udělal doložený
  objekt. Záběry hřbitova musí zůstat bez jmen.
- Na hrobkách nesmí být **čitelná jména ani datumy**. Jsou to hroby skutečných rodin; vymyšlené
  jméno na náhrobku je jiná kategorie chyby než vymyšlená cedule chiringuita.
- Ladění fotek hřbitova drž **klidné a architektonické**, ne ponuré. V textu je to tip na
  pozoruhodné místo, ne strašidelná atrakce.
- V Blanes: záběr rybářského přístavu bez čitelných jmen lodí a bez cedulí podniků.
- Fotka paddleboardu / lodi u Cala Forcanera nesmí obsahovat logo půjčovny.

## Vstupné na hřbitov — v textu záměrně chybí

Text říká, že **výši vstupného oficiální zdroje města neuvádějí**, a žádné číslo nedává. Není to
opomenutí: agregátory tvrdí, že je vstup zdarma, ale oficiální weby to nepotvrzují, takže by šlo
o tvrzení bez opory.

Když model doplní „zdarma" nebo jakoukoliv částku, je to nález. Věta o tom, že to nebude položka,
která rozhodí rozpočet, musí zůstat — je to jediné, co si o ceně text dovoluje tvrdit.

## Poznámka k obsahu

Fact-check kapitoly je `Stav: OK`, třetí kolo 2026-07-29 po doplnění hřbitova a vstupného do zahrad
— **bez nálezů**. Sekce o hřbitově je jediná část kapitoly postavená na oficiálních městských
zdrojích místo na cestovatelských blozích, takže je z celé kapitoly nejlíp podložená.

Otevřené otázky z Fáze 1 (přístup ke Cala Forcanera a Cala dels Frares, vzdálenosti do Blanes
a Sant Feliu de Guíxols) jsou vedené
v `../../../01-tvorba-textu/docs/open-questions-lloret-de-mar.md` a **v textu jsou už ošetřené
opatrnou formulací** — tady jde jen o to, aby je model nesetřel. Nově k nim přibylo vstupné na
hřbitov a mimosezónní otevírací doba zahrad.
