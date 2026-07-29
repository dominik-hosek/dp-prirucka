# Kontrolní list — kapitola 03: Ubytování

Zdroj: `../../../01-tvorba-textu/content/lloret-de-mar/text/03-ubytovani.md`

Postup generování je v `../../docs/prompt-guide.md`. Tenhle list slouží ke **kontrole vygenerovaných
stránek proti zdroji**.

## Sekce (počet, pořadí, nadpisy)

Kapitola má **6 podsekcí** v tomto pořadí:

1. Centrum a Avinguda Just Marlès
2. Fenals
3. Směr Cala Boadella
4. Nejlépe hodnocené hotely podle čtvrti
5. Typ ubytování
6. Rychlé shrnutí

Plus úvodní odstavec pod nadpisem kapitoly, bez vlastního podnadpisu, a jedna závěrečná věta pod
Rychlým shrnutím (odkaz na kapitolu Off the beaten path) — ta se snadno ztratí, protože stojí až za
odrážkami.

Sekce **Rychlé shrnutí** má tři odrážky ve formátu „chceš X → jdi do Y". Musí zůstat seznamem se
šipkami, ne se rozpustit do odstavce — je to rozhodovací pravidlo celé kapitoly.

## Čísla — musí sedět přesně

| Údaj | Správně |
|---|---|
| Vzdálenost Fenals od centra | asi **1 kilometr** |
| Začátek nočního života | kolem **22. hodiny** |
| Hotel Delamar | **4,7** na Googlu · **9,3** na Booking.com |
| L'Azure Hotel 4\* Sup | **4,6** na Googlu · **9,2** na Booking.com |
| Hotel Anabel | **4,5** na Googlu · **8,7** na Booking.com · **350 m** od pláže |
| Hotel Rigat Park & Spa | **4,4** na Googlu · **9,1** na Booking.com |
| htop Amatista | **4,4** na Googlu · **8,6** na Booking.com · víc než **15 tisíc** hodnocení |
| Hotel Santa Marta | **4,4** na Googlu |
| Hotel Delamar — vzdálenost | **2-3 minuty** pěšky k pláži |
| L'Azure — vzdálenost | **pět minut** pěšky k pláži |

**Dvě různé stupnice v jedné tabulce.** Google je **z 5**, Booking.com **z 10** — model má silnou
tendenci je sjednotit, převést jednu na druhou nebo přidat „/5" k devítce. Každá známka musí zůstat
na své stupnici a text u prvního hotelu to explicitně říká („4,7 z 5 na Googlu, 9,3 z 10 na
Booking.com").

Pozor i na desetinné čárky: **4,7 · 4,6 · 4,5 · 4,4 · 9,3 · 9,2 · 9,1 · 8,7 · 8,6**. Devět čísel,
všechna na jedno desetinné místo, všechna vypadají podobně — ideální podmínky pro tichou záměnu.

## Opatrné formulace — nesmí se z nich stát tvrzení najisto

- U cen ubytování musí zůstat, že se **výrazně liší podle sezóny, typu pokoje a předstihu rezervace**
  a že si má čtenář ověřit aktuální ceny přímo na rezervačním portálu. Konkrétní číslo do téhle
  kapitoly nepatří — je v kapitole Rozpočet.
- U Fenals musí zůstat, že tam **jsou** rodinné bary a hospůdky, takže se kvůli klidu neobětuje
  společenský život úplně. Když tohle vypadne, vyzní Fenals jako mrtvá čtvrť.
- U směru Cala Boadella musí zůstat, že jde o **delší docházku do centra výměnou za klid** — ne jen
  ta příjemná půlka věty.

## Vlastní jména — musí být přesně

- **Avinguda Just Marlès** (hlavní zábavní třída — nejrizikovější jméno v kapitole, je dlouhé a
  katalánské)
- **Platja de Lloret** (hlavní pláž)
- **Fenals**
- **Castell de Sant Joan** (zbytky hradu na vršku mezi centrem a Fenals)
- **Santa Clotilde** (zahrady)
- **Cala Boadella**

## Jména hotelů — přesně těchto šest a žádné jiné

Od 2026-07-29 kapitola konkrétní hotely **jmenuje** — je to hlavní přidaná hodnota celé kapitoly
a stojí za tím doložený výběr podle `../../../01-tvorba-textu/docs/metodika-hodnoceni.md`.

Tím se ale pravidlo obrací: dřív se hlídalo, aby se žádné jméno neobjevilo. **Teď se hlídá, aby
se objevila přesně tahle jména a žádné další.**

| Čtvrť | Hotely |
|---|---|
| Centrum | **Hotel Delamar** · **L'Azure Hotel 4\* Sup** · **Hotel Anabel** |
| Fenals | **Hotel Rigat Park & Spa** · **htop Amatista** |
| Směr Cala Boadella | **Hotel Santa Marta** (jediný, není to žebříček) |

Na co si dát pozor:

- **`htop Amatista` se píše malým „h".** Je to obchodní značka, ne překlep na začátku věty. Model
  ho bude chtít opravit na „Htop".
- **`L'Azure` má apostrof** a za názvem stojí `4* Sup` — hvězdička i zkratka musí zůstat.
- **`Hotel Rigat Park & Spa`** — ampersand, ne „a".
- **Ve Fenals jsou jen dva hotely a je to záměr.** Text hned pod seznamem vysvětluje proč (třetí měl
  dost hodnocení jen na jedné platformě). Když model doplní třetí jméno, aby seznam „vypadal
  hotově", je to nález — a to nejzávažnější možný, protože by vzniklo doporučení bez opory.
- **Ve směru Cala Boadella nesmí vzniknout žebříček.** Text tam říká, že žádný nedostaneš a proč.
  Když z toho model udělá seznam tří hotelů, popírá to metodiku i obsah odstavce.
- **Žádné jiné jméno hotelu.** Research jich zná víc (Gran Hotel Flamingo, Helios, Rosamar, Best
  Lloret Splash, Costa Encantada, ALEGRIA Fenals Mar, Alva Park) a všechny do textu **vědomě
  nepatří** — buď neprošly metodikou, nebo jsou zavřené. Když se kterékoliv z nich objeví, je to
  nález.

## Dodatek o původu výběru — musí zůstat celý

Poslední odstavec sekce říká, odkud výběr pochází, proč zrovna Booking.com, a **že si tam nikdo
umístění nezaplatil**. Bez toho vypadá seznam jako placená reklama a poškozuje důvěryhodnost celého
produktu — což je přesně to, čím se průvodce odlišuje.

Musí v něm zůstat všech pět částí:

1. platformy (Google Maps a Booking.com),
2. datum (červenec 2026),
3. proč Booking.com — hodnotí jen ten, kdo tam skutečně bydlel,
4. **„nikdo si tady umístění nezaplatil"** a že s hotely nemáme vztah,
5. že se známky mění a je dobré je před rezervací ověřit.

Je to dlouhý odstavec s vloženými větami — přesně ten typ, na kterém model v kapitole 01 klopýtal.
**Čti ho celý proti zdroji, ne jen zběžně.**

## Fotky

- **Jmenované hotely se nefotí.** Model reálný hotel nevygeneruje věrně — vznikla by smyšlená budova
  vydávaná za konkrétní podnik, a to je horší než u pláže, protože podle toho čtenář utrácí peníze.
  Sekce s žebříčkem je čistě grafická (tabulka známek), viz shot list.
- Žádná čitelná cedule s názvem hotelu, aparthotelu ani baru — ani u ilustračních záběrů v ostatních
  sekcích. Téma svádí k záběru hotelové recepce nebo fasády.
- Castell de Sant Joan a Cala Boadella nepodepisovat.
- U záběru noční Avinguda Just Marlès nesmí být čitelná jména klubů.

## Poznámka k obsahu

Fact-check kapitoly je `Stav: OK`, třetí kolo 2026-07-29 po doplnění žebříčku — 2 nálezy, oba
opravené (neopodstatněný superlativ u Delamaru, poloha L'Azure vůči autobusovému nádraží).

Otevřené otázky z Fáze 1 (konkrétní ceny za noc, časy chůze mezi čtvrtěmi) jsou v
`../../../01-tvorba-textu/docs/open-questions-lloret-de-mar.md` a řeší se **až před vydáním**.
Proto v kapitole žádné časy chůze nejsou — když je model „dopočítá", vznikne tvrzení bez opory.

**Žebříček se přeověřuje před každým vydáním.** Hotel může zavřít nebo změnit majitele — Alva Park
Costa Brava je varovný příklad podniku, který se na seznamech „nejlepších hotelů" držel i po svém
zavření.
