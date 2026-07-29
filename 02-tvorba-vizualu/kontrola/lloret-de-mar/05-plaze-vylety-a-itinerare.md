# Kontrolní list — kapitola 05: Pláže, výlety a itineráře

Zdroj: `../../../01-tvorba-textu/content/lloret-de-mar/text/05-plaze-vylety-a-itinerare.md`

Postup generování je v `../../docs/prompt-guide.md`. Tenhle list slouží ke **kontrole vygenerovaných
stránek proti zdroji**.

> **Nejdelší a číselně nejhustší kapitola průvodce** (~600 slov, přes 20 samostatných údajů, z toho
> datumy, časy i ceny). Počítej s tím, že zabere víc stránek a víc kontrolních kol než ostatní.
> Kontroluj ji **po sekcích, ne najednou** — na jedno přečtení se tolik čísel uhlídat nedá.

## Sekce (počet, pořadí, nadpisy)

Kapitola má **7 podsekcí** v tomto pořadí:

1. Pláže v Lloret de Mar
2. Tossa de Mar
3. Girona
4. Rodinné atrakce
5. Co má nejlepší hodnocení
6. Itinerář: 3 dny v Lloretu a okolí
7. Itinerář: 5 dní s výletem do Girony

Plus úvodní odstavec pod nadpisem kapitoly, bez vlastního podnadpisu, a jedna závěrečná věta úplně
na konci (odkaz na kapitolu Doprava po okolí).

Struktura uvnitř sekcí, která musí zůstat:

- **Pláže** — odrážkový seznam **4 pláží**, každá s tučným názvem.
- **Rodinné atrakce** — odrážkový seznam **2 atrakcí** s tučným názvem.
- **Itinerář 3 dny** — **číslovaný** seznam 1–3, každý den s tučným nadpisem („**Den 1 — Lloret
  naplno.**").
- **Itinerář 5 dní** — číslovaný seznam, kde **první položka je „1.–3. Stejné jako itinerář výše"**
  a pak následují body 4 a 5. Tenhle zkrácený zápis je pro model neobvyklý a rád ho „opraví" na
  plných pět dní — pak by ale musel obsah dnů 1–3 vymyslet znovu. Musí zůstat odkazem.

## Čísla — musí sedět přesně

| Údaj | Správně |
|---|---|
| Fenals — délka | cca **700 m** |
| Santa Cristina — délka | necelých **500 m** |
| Pobřežní stezka Cala Canyelles – Santa Cristina | asi **11 km** |
| Vzdálenost Lloret → Tossa de Mar | asi **12 km** |
| Vila Vella — původ pevnosti | **12. století** |
| Vila Vella — přestavba | rok **1387** |
| Maják nad Vila Vella | rok **1917** |
| Plavba lodí do Tossy | cca **30 minut** |
| Vzdálenost Lloret → Girona | asi **půl hodiny cesty** |
| Water World — sezóna 2026 | **23. 5.–13. 9.** |
| Water World — otevírací doba | **10:00-18:00**, na vrcholu sezóny **10:00-19:00** |
| Water World — kdy platí delší doba | **8. 7.–31. 8.** |
| Water World — vstupné | **37,20 EUR** pro osoby vyšší než **1,2 m** |
| Marineland — vstupné | **23 EUR** dospělí / **16,5 EUR** děti do 12 let / zdarma do 4 let |
| Marineland — papoušci | **10:30 a 17:00** |
| Marineland — lachtani | **11:30 a 16:00** |
| Marineland — delfíni | **12:00 a 16:30** |
| Zahrady Santa Clotilde — hodnocení | **4,5** na Googlu (přes **9 000** hodnocení) · **4,4** na Tripadvisoru (přes **2 500**) |
| Sa Boadella a Santa Cristina — hodnocení | obě **4,6** na Googlu |
| Water World — hodnocení | **4,1** na Googlu · **3,9** na Tripadvisoru |

**Nejrizikovější místo: časy vystoupení v Marinelandu.** Šest časů ve dvou závorkách za sebou, ve
stejném formátu, bez ničeho, co by je od sebe odlišilo — přesně ten typ konstrukce, na které model
prohazuje hodnoty. Kontroluj je po dvojicích a proti tabulce výše, ne z paměti.

Druhé nejrizikovější: **37,20 EUR** (desetinná čárka) a **16,5 EUR** (jedno desetinné místo, ne
16,50). A datumy Water Worldu — čtyři datumy ve dvou různých rolích (sezóna vs. vrchol sezóny).

## Sekce „Co má nejlepší hodnocení" — nejcitlivější místo kapitoly

Doplněno 2026-07-29 podle `../../../01-tvorba-textu/docs/metodika-hodnoceni.md`. Je to jediné místo
v celém průvodci, kde se o jmenované atrakci píše, že je hodnocená hůř než ostatní — a taky největší
argument, proč si čtenář průvodce koupil místo běžného seznamu „co dělat v Lloretu".

Proto se tu hlídají věci, které jinde nehrozí:

- **Ladění o Water Worldu musí zůstat neutrální.** Text uvádí čísla, výslovně dodává, že to
  **neznamená, že tam nemáš jet**, a nabízí srovnání s levnější alternativou. Když z toho model
  udělá varování („radši tam nechoď", „zklamání"), vzniká negativní tvrzení o jmenované firmě —
  metodika to výslovně zakazuje.
- **Věta „neznamená to, že tam nemáš jet — s dětmi je to pořád zážitek na celý den" nesmí vypadnout.**
  Je to jediná protiváha v celém odstavci. Bez ní zbude jen nejnižší známka a nejvyšší cena vedle
  sebe.
- **Zahrady Santa Clotilde jsou „z velkých atrakcí ta nejlépe hodnocená", ne „nejlépe hodnocené
  místo Lloretu".** Přesně tenhle superlativ fact-check 2026-07-29 opravoval — pláže mají 4,6, tedy
  víc. Když se superlativ vrátí, kapitola si odporuje sama se sebou o dva řádky níž.
- **U pláží musí zůstat „z pláží, ke kterým se hodnocení podařilo dohledat".** Hodnocení hlavní
  pláže Platja de Lloret se najít nepodařilo, takže srovnání není úplné a bez téhle výhrady jde
  o tvrzení bez opory.
- **Dodatek o původu výběru** (veřejná hodnocení k červenci 2026, jen místa s dost recenzemi,
  **„nikdo si tady umístění nezaplatil"**, hodnocení se mění) musí zůstat celý.
- **Modernistický hřbitov se tu nesmí objevit.** Má sice nejlepší známky v okolí, ale žádný další
  research k němu není — žádná otevírací doba, vstupné ani poloha. Kdyby ho model doplnil, vzniklo
  by doporučení bez jakéhokoliv podkladu.

## Opatrné formulace — nesmí se z nich stát tvrzení najisto

- U Water Worldu musí zůstat, že se **ceny a otevírací doba mezi sezónami mění** a že si má čtenář
  ověřit aktuální ceník před cestou.
- U Marinelandu musí zůstat, že si má čtenář **ověřit aktuální program před návštěvou**.
- U itinerářů musí zůstat, že si je čtenář **může přizpůsobit délce pobytu** — nejsou to závazné
  plány.
- V Dni 1 musí zůstat **odkaz na kapitolu Off the beaten path** místo konkrétního podvečerního tipu.
  Právě tady dřív stálo doporučení na zahrady Santa Clotilde „za zlatého světla" a fact-check ho
  odsud odstranil, protože patří do jiné kapitoly. Když se tam vrátí, je to nález.
- U dopravy do Tossy musí zůstat obě varianty (loď i autobus) a doporučení kombinace — ne jen jedna
  z nich.

## Vlastní jména — musí být přesně

- **Platja de Lloret**, **Fenals**, **Santa Cristina**, **Cala Canyelles**, **Sa Boadella**
- **Tossa de Mar**, **Vila Vella** (opevněné staré město — dvě samostatná slova, obojí velkým)
- **Girona**, řeka **Onyar**, židovská čtvrť **El Call**
- **Water World**, **Marineland Catalunya**, **Santa Susanna** (obec, kde Marineland leží)

Pozor na seznam pláží s modrou vlajkou: **Lloret, Fenals, Sa Boadella a Santa Cristina** — čtyři
jména, a Sa Boadella je jediné, které není v odrážkovém seznamu pláží výš. Právě proto z výčtu
nejsnáz vypadne.

## Fotky

- **Water World ani Marineland nesmí mít na fotce čitelné logo ani ceduli.** Jsou to reálné firmy —
  vymyšlené logo je horší než žádné.
- Vila Vella, maják, Onyar, katedrála v Gironě: pojmenovaná místa **nepodepisovat**. Model
  vygeneruje věrohodné, ale smyšlené místo, a u tak známé siluety jako Vila Vella to čtenář pozná.
- U mapy vzdáleností nesmí vzniknout vymyšlené názvy obcí kolem trasy.
- Ikona modré vlajky je v pořádku, ale nesmí být doplněná jmény pláží, které v seznamu nejsou.
- **Sekce s hodnocením je čistě grafická** — srovnávací graf a porovnání ceny s hodnocením, žádná
  fotka. Grafika musí ukázat obě platformy zvlášť, ne zprůměrovanou známku.

## Poznámka k obsahu

Fact-check kapitoly je `Stav: OK`, třetí kolo 2026-07-29 po doplnění sekce s hodnocením — 2 nálezy,
oba opravené (superlativ u zahrad Santa Clotilde, chybějící výhrada u pláží).

Otevřené otázky z Fáze 1 (ceník lodní linky do Tossy, vstupné a otevírací doby atrakcí pro další
sezónu) jsou vedené v `../../../01-tvorba-textu/docs/open-questions-lloret-de-mar.md` a řeší se
**až před vydáním**. Nově k nim přibylo hodnocení Platja de Lloret a případné doplnění
modernistického hřbitova.

**Hodnocení se přeověřuje před každým vydáním** — u Water Worldu zvlášť, protože jeho nízká známka
je v textu použitá jako konkrétní tvrzení.

Sezónní údaje Water Worldu jsou v textu explicitně označené jako **sezóna 2026** — kdyby se guide
vydával později, tohle je první místo, které zastará.
