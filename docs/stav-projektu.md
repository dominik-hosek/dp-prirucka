# Stav projektu

Jediné místo, kde je vidět, kde v procesu jsme a co je další krok. Aktualizuje se po každém
dokončeném kroku. Popis samotného procesu (co se v které fázi dělá) je v `plan.md`, sem patří
jen stav.

**Poslední aktualizace: 2026-09-02**

---

## ⚠️ Řada běží souběžně na víc destinacích (rozhodnuto 2026-08-06)

Kořenový `CLAUDE.md` říká, že se další destinace rozjíždějí až po vyhodnocení pilota (Fáze 9).
**Od 2026-08-06 se tímhle pravidlem vědomě neřídíme.** Barcelona vznikla mimo něj už 2026-08-02,
Kréta 2026-08-06 na přímé zadání. Fáze 0–2 (text) teď běží paralelně na víc destinacích, zatímco
pilot Lloret čeká na Fázi 3.

Co to znamená prakticky:

- **Nejde o zrušení pilota.** Lloret zůstává jediná destinace, která má projít celým procesem až
  do Fáze 9 a vyhodnotit se — teprve z něj se učíme, jestli produkt vůbec funguje.
- **Souběžně se rozšiřuje jen text (Fáze 0–2).** Investice do vizuálu, webu a PPC (Fáze 3+) se
  u Barcelony ani Kréty nezahajuje, dokud pilot neproběhne — tam je peněžní riziko.
- **Riziko, se kterým se do toho jde:** pokud se v pilotu ukáže, že osnova nebo persona jsou
  špatně, přepisuje se to zpětně na třech destinacích místo jedné.

---

## 👉 Další krok

**Generovat stránky kapitol 02–08** — postup v `02-tvorba-vizualu/docs/prompt-guide.md`, kontrola
podle listů v `02-tvorba-vizualu/kontrola/lloret-de-mar/`.

Text Lloretu je **uzavřený** — od 2026-07-29 se do vydání nemění. Vše potřebné je připravené:

| Co | Stav |
|---|---|
| Dlouhá verze — kapitoly 01–08, fact-check `Stav: OK` | ✅ všech 8 |
| Krátká verze — rychlotaháček, max. 1 A4 na kapitolu | ✅ všech 8 |
| Kontrolní listy pro sazbu | ✅ 8 kapitol + obálka |
| Vygenerované stránky | ◐ 1 z 8 (kapitola 01) + obálka |

**Doporučené pořadí:**

1. Začni **kapitolou 02** — je nejkratší a nejjednodušší, ověříš si na ní postup.
2. Pak **03, 04, 05, 06, 08** v libovolném pořadí.
3. **Kapitolu 07 (Rozpočet) nech úplně na konec.** Skoro každé číslo v ní se má doověřovat až
   těsně před vydáním — když ji vysázíš brzy, budeš ji dělat znovu.

**Nejnáročnější budou 05 a 06.** Kapitola 05 má přes 20 číselných údajů (včetně šesti časů
vystoupení za sebou), kapitola 06 má nově dlouhou sekci o modernistickém hřbitově se čtyřmi
letopočty a jmény katalánských architektů. U obou počítej s víc kontrolními koly.

**Pozor u kapitol 03, 04 a 05:** nově obsahují jména konkrétních podniků. Pravidlo se tím obrátilo —
dřív se hlídalo, aby žádné jméno neproniklo dovnitř, teď aby jich byla přesně ta správná sada
a žádné navíc. A jmenované podniky se **nefotí**, ty sekce jsou čistě grafické. Detail v jejich
kontrolních listech.

**Otevřené k rozhodnutí (neblokuje generování):** podtitul obálky vyšel jako „COSTA BRAVA,
ŠPANĚLSKO", tedy čistě místopisný, bez příslibu hodnoty pro personu. Jestli tam má být i něco jako
„pro ty, kdo si dovolenou plánují sami", je potřeba obálku přegenerovat — rozhodnout před vydáním.

✅ *Hotovo 2026-07-28: přeověření kapitoly 01 Lloretu (viz Fáze 2 níže).*
✅ *Hotovo 2026-07-29: `01-tvorba-textu/docs/open-questions-lloret-de-mar.md` — 18 otevřených otázek
z 8 research souborů seskupených podle toho, co s nimi má udělat QA ve Fázi 4.*
✅ *Hotovo 2026-07-29: přeověření kapitol 02–08 + kontrolní listy 03–08 (viz Fáze 2 níže).*
✅ *Hotovo 2026-07-29: žebříčky konkrétních hotelů, restaurací a atrakcí podle recenzí v kapitolách
03, 04 a 05 — nová metodika `01-tvorba-textu/docs/metodika-hodnoceni.md`.*
✅ *Hotovo 2026-07-29: modernistický hřbitov doplněn do kapitoly 06 (z oficiálních městských zdrojů)
a vstupné do zahrad Santa Clotilde do kapitol 06 a 07. Tím je text uzavřený pro Fázi 3.*
✅ *Hotovo 2026-07-30: každá kapitola má nově **dvě verze textu** — dlouhou (příručka) a krátkou
(rychlotaháček, max. 1 A4). Všech 8 krátkých verzí hotovo v
`01-tvorba-textu/content/lloret-de-mar/text/_tahacek/`. Nový agent `tahacek-creator`, skill
`/tahacek`, hook si krátkou verzi vyžádá sám, jakmile kapitola dostane `Stav: OK`. Rozsah produktu
doplněn do briefu.*

✅ *Hotovo 2026-08-02: **Barcelona** — celá Fáze 0–2 (brief, 8 research souborů, 8 kapitol se
`Stav: OK`, 8 rychlotaháčků, otevřené otázky). Vznikla mimo pravidlo pilota, viz její sekce níže.*
✅ *Hotovo 2026-08-02: **úspora tokenů ve Fázi 2.** Hook `fact-check-on-save.js` už nevyzývá ke
spuštění subagenta po každé jedné kapitole — hlásí celou čekající dávku a Fact-Checker
i Tahacek-Creator zvládnou až 4 kapitoly na běh (research se načte jednou místo osmkrát). Drobný
edit, který nepřidá číslo ani měnu, se nově ověřuje inline bez subagenta. Detail v
`01-tvorba-textu/docs/automation-registry.md`.*

🗑️ *Zrušeno 2026-07-30: **shot listy skončily úplně** — vizuální fázi řeší uživatel sám, takže
podklad pro Projekt 2 už není potřeba. Smazána složka `text/_shot-list/` (8 souborů), agent
`shot-list-creator`, větev v hooku a všechny odkazy v dokumentaci. Soubory zůstávají v git historii,
kdyby se pro ně někdy našel důvod.*

✅ *Hotovo 2026-08-26: **Marsa Alam** — celá Fáze 0–2 (brief, `fakta.md`, 8 kapitol, 8
rychlotaháčků, `kontrola.md` prošlá ruční kontrolou). Detail v její sekci níže. Cestou opravena
zastaralá dokumentace: `01-tvorba-textu/.claude/skills/tahacek/SKILL.md` ještě vyžadovala starý
`_fact-check/Stav: OK` gate zrušeného Fact-Checker agenta — nová destinace bez něj neprošla. Gate
nahrazen popisem skutečného stavu (kontrola dělá člověk nad `kontrola.md`, ne agent před vydáním).*

✅ *Hotovo 2026-08-26: **Kypr** — celá Fáze 0–2 (brief, `fakta.md`, 8 kapitol, 8 rychlotaháčků,
`kontrola.md` s 30 položkami). Detail v její sekci níže. `kontrola.md` čeká na člověka.*

✅ *Hotovo 2026-08-28: **Antálie (Turecko)** — celá Fáze 0–2 (brief, `fakta.md`, 8 kapitol,
8 rychlotaháčků, `kontrola.md` s 27 položkami). Detail v její sekci níže.*

✅ *Hotovo 2026-09-02: **ruční kontrola Antálie** — `content/antalie/kontrola.md` prošlá, bez oprav
v kapitolách. Rychlotaháčky proto zůstávají platné a text Antálie je hotový pro Fázi 3 (vizuál).*

---

## Otevřená rozhodnutí

### ✅ #1 — Jakým procesem vyrobit vizuální PDF? *(rozhodnuto 2026-07-29)*

Stránky generuje člověk v **Nano Banana 2 / GPT Image** podle promptů připravených agentem. Canva
se nepoužívá (skill i agent odstavené). Stránky se dělí na vizuální (text se generuje) a textové
(generuje se jen prázdný rám, fact-checked text se vkládá až potom) — důvod je nespolehlivá sazba
české diakritiky obrázkovými modely.

Detail: `02-tvorba-vizualu/docs/prompt-guide.md`. Rozhodnutí a jeho kontext:
`docs/project-split-plan.md`.

**Známé riziko, se kterým se do toho jde:** u fotek konkrétních pojmenovaných míst model vygeneruje
věrohodné, ale smyšlené místo. Řešení v prompt guide — buď licencovaná fotka, nebo místo
v popisku nepojmenovávat.

### #2 — Notion jako centrální databáze destinací? (neblokuje)

`plan.md` (technická příprava, bod 2) s ním počítá. Zatím nezaložený — repo pro dvě destinace
stačí. Rozhodnout, až bude destinací víc.

---

## Stav podle fází

Legenda: ✅ hotovo · ◐ rozpracováno · ⛔ blokováno · ⬜ nezačato

| Fáze | Co | Projekt | Stav |
|---|---|---|---|
| 0 | Validace destinace, persona, cena, osnova | 01 | ✅ pro Lloret i Albánii · ◐ Barcelona (brief napsaný, rozhodnutí nepotvrzená) · ✅ Kréta (brief potvrzený 2026-08-06) · ✅ Malta (brief potvrzený 2026-08-26) · ✅ Marsa Alam (brief potvrzený 2026-08-26) · ✅ Kypr (brief potvrzený 2026-08-26) · ✅ Antálie (brief potvrzený 2026-08-28) |
| 1 | Research "deep knowledge" dat | 01 | ✅ pro Lloret (8 témat) · ✅ pro Albánii · ✅ pro Barcelonu (8 témat) · ◐ Kréta (8 témat, sběr spuštěn 2026-08-06) · ✅ Malta (`fakta.md`, sběr 2026-08-26) · ✅ Marsa Alam (`fakta.md`, sběr 2026-08-26) · ✅ Kypr (`fakta.md`, sběr 2026-08-26) · ✅ Antálie (`fakta.md`, sběr 2026-08-28) |
| 2 | Psaní kapitol + fact-check + krátká verze | 01 | ✅ Lloret (8/8 `Stav: OK`, 8/8 krátkých verzí) · ✅ Barcelona (8/8 `Stav: OK`, 8/8 krátkých verzí, 1 blokující otevřená otázka) · ◐ Albánie (text opravený, fact-check nespuštěný znovu, krátké verze nejsou) · ⬜ Kréta (čeká na research) · ✅ Malta (8/8 kapitol, 8/8 krátkých verzí, `kontrola.md` čeká na člověka) · ✅ Marsa Alam (8/8 kapitol, 8/8 krátkých verzí, `kontrola.md` prošlá — nemá samostatný fact-check, viz jak vznikla níže) · ✅ Kypr (8/8 kapitol, 8/8 krátkých verzí, `kontrola.md` čeká na člověka) · ✅ Antálie (8/8 kapitol, 8/8 krátkých verzí, `kontrola.md` prošlá 2026-09-02 bez oprav) |
| 3 | Vizuál a sazba PDF | 02 | ◐ hotová obálka a kapitola 01 Lloretu (1/8), zbývá 02–08 · kontrolní listy 8/8 hotové · sazba taháčku (8 stran) nezačatá |
| 4 | QA a finalizace produktu | 03 | ⬜ čeká na PDF z Fáze 3 |
| 5 | Prodejní web | 03 | ⬜ |
| 6 | Příprava PPC kampaní | 03 | ⬜ |
| 7 | Spuštění a optimalizace PPC | 03 | ⬜ |
| 8 | Post-launch péče | 03 | ⬜ |
| 9 | Škálování na další destinace | 03 | ⬜ až po vyhodnocení pilotu |

---

## Destinace

Plán počítá s pilotem na jedné destinaci — další se rozjíždějí až po jeho vyhodnocení (Fáze 9).

### 🎯 Lloret de Mar a okolí — **aktuální pilot**

- **Fáze 0:** brief potvrzený (`01-tvorba-textu/docs/brief-lloret-de-mar.md`) — persona "Nezávislý
  plánovač", cena 199 Kč, osnova 8 kapitol.
- **Fáze 1:** research hotový, 8 souborů, datum sběru 2026-07-17. Sekce o penězích v
  `prakticke-zaklady.md` doplněná 2026-07-28 (karty vs. hotovost, chiringuita, limity).
- **Fáze 2:** hotovo a uzavřeno — všech 8 kapitol má aktuální fact-check se `Stav: OK` i aktuální
  krátkou verzi pro rychlotaháček. Kapitola 01 prošla 2026-07-28 přeověřením (4 kola: neshoda měny u eSIM, ztracená
  opatrnost u ceny autobusu z Girony, nepodložená tvrzení o placení kartou) — všechny nálezy
  opravené. Kapitoly 02–08 přeověřené 2026-07-29 druhým kolem: 6 z nich beze změny, v kapitole 07
  (Rozpočet) 2 nálezy, oba opravené — cena autobusu z Girony bez rozptylu zdrojů (10 vs. až 23 EUR,
  kapitola 01 ho nesla, kapitola 07 ne) a sloučení fyzické SIM s eSIM do jedné částky v EUR, ačkoli
  eSIM ceníky jsou v USD. Druhý nález vznikl už v `research/rozpocet.md`, opraven proto i tam.
  **Pozor: záměna EUR/USD je jediná chyba, která v projektu vznikla dvakrát nezávisle na sobě.**
- **Konkrétní podniky podle recenzí (2026-07-29):** kapitoly 03, 04 a 05 nově jmenují konkrétní
  hotely, restaurace a atrakce vybrané podle doložené metody
  (`01-tvorba-textu/docs/metodika-hodnoceni.md` — dvě nezávislé platformy, prahy na počet recenzí,
  povinný dodatek „nikdo si tady umístění nezaplatil"). Data v research souborech dané kapitoly.
  **Žebříčky se přeověřují před každým vydáním** — podniky zavírají a známky se mění.
- **Modernistický hřbitov (2026-07-29):** doplněný do kapitoly 06. Vyplynul ze sběru hodnocení jako
  nejlépe hodnocené místo, které v průvodci chybělo. Jediná část kapitoly postavená na oficiálních
  městských zdrojích (lloretdemar.org, patrimoni.lloret.cat), ne na blozích.
- **Otevřené otázky pro QA:** `01-tvorba-textu/docs/open-questions-lloret-de-mar.md` (2026-07-29,
  aktuální). Pozor, sekce 1 (ceny dopravy, ubytování, vstupné) se má doověřovat **až těsně před
  vydáním**, ne dopředu — jinak čísla znovu zastarají. Nová sekce 1b (žebříčky podle recenzí) je
  opakovaná položka pro každé vydání, ne jednorázová.
- **Chybí:** design brief pro Lloret. Vizuální styl je společný a definovaný
  v `02-tvorba-vizualu/docs/design-brief-albanie.md` — pro Lloret stačí doplnit barevný akcent
  a fotky, až padne rozhodnutí #1.
- **Fáze 3 a dál:** nezačato.

### 🆕 Barcelona — text hotový, čeká na rozhodnutí

Založena 2026-08-02 na přímé zadání, **vedle běžícího pilota**. Text prošel celou Fází 2 —
8 kapitol se `Stav: OK` a 8 krátkých verzí.

- **Fáze 0:** `01-tvorba-textu/docs/brief-barcelona.md` — persona „Nezávislý plánovač" (u městské
  destinace pobyt 3–5 dní, ne pobytová dovolená), cena 199 Kč, osnova 8 kapitol.
  **Brief má nezaškrtnutá rozhodnutí** — destinace, persona, cena a osnova čekají na potvrzení.
- **Fáze 1:** research hotový, 8 souborů, datum sběru 2026-07-31.
- **Fáze 2:** 8/8 kapitol `Stav: OK`, 8/8 krátkých verzí. Kapitola 01 prošla dvěma koly + inline
  ověřením, kapitola 07 (Rozpočet) třemi koly — nálezy: chybný poměr „pětinásobný" u ceny dopravy
  z letiště, srovnání „tři vstupy do Sagrady Famílie" platné jen pro nejlevnější vstupenku
  a nesouhlasící součet u Montserratu (36,80 EUR počítá s Cremallerou za 15 EUR, ne 14,50 EUR).
- **🔴 Blokující otevřená otázka: není jisté, jestli je Sagrada Família otevřená.** Oficiální web
  hlásí dočasné uzavření, cenová stránka téhož webu funguje normálně, jiné zdroje mluví o běžném
  provozu. Text to nikde netvrdí a nabízí náhradu (Sant Pau), ale před vydáním se to musí vyřešit —
  ovlivňuje kapitoly 05, 07, 08 a oba itineráře.
- **Rozdíl proti Lloretu: žádné jmenované podniky.** Sběr podle
  `01-tvorba-textu/docs/metodika-hodnoceni.md` se pro hotely ani restaurace nepodařilo doložit
  (chybějící data z Google Maps, nízké počty recenzí). Kapitoly 03, 04 a 06 to čtenáři otevřeně
  vysvětlují. Doplnit žebříčky = samostatný sběr, viz sekce 5 v open questions.
- **Otevřené otázky:** `01-tvorba-textu/docs/open-questions-barcelona.md`.
- **Fáze 3 a dál:** nezačato.

**Pozor — pravidlo pilota.** Kořenový `CLAUDE.md` říká, že se další destinace rozjíždějí až po
vyhodnocení pilota (Fáze 9). Barcelona vznikla mimo tohle pravidlo. Než se do ní investuje dál
(vizuál, web, PPC), je potřeba vědomě rozhodnout, jestli má běžet souběžně s Lloretem, nebo se
zmrazit jako Albánie.

### 🆕 Kréta — rozpracovaná (Fáze 1)

Založena 2026-08-06 na přímé zadání, vybraná z top destinací českých turistů (Řecko je trvale
v první pětici). Vědomě běží souběžně s pilotem — viz sekce nahoře.

- **Fáze 0:** `01-tvorba-textu/docs/brief-kreta.md` — brief potvrzený 2026-08-06. Persona
  „Nezávislý plánovač" (stejná jako u ostatních, pro konzistenci řady), cena 199 Kč, osnova
  8 kapitol, pobyt 7–10 dní.
- **Strukturální odlišnost od Lloretu i Barcelony:** Kréta je 260 km dlouhá, takže „jedna základna,
  výlety odtud" nefunguje jako u kompaktních destinací. Kapitola 02 proto není jen „doprava po
  okolí", ale **výběr základny** (Chania / Rethymno / Heraklion / Agios Nikolaos) plus rozhodnutí
  auto vs. autobus vs. organizovaný výlet. Itineráře v kapitole 05 se tím pádem musí lišit podle
  zvolené základny — to je nejnáročnější část celého textu.
- **Fáze 1:** research spuštěn 2026-08-06, 8 témat paralelně.
- **Fáze 2 a dál:** nezačato.

### 🆕 Marsa Alam — text hotový (Fáze 0–2 dokončeny)

Založena 2026-08-26 na přímé zadání. Vědomě běží souběžně s pilotem — viz sekce nahoře.

- **Fáze 0:** `01-tvorba-textu/docs/brief-marsa-alam.md` — brief potvrzený 2026-08-26. Persona
  „Nezávislý plánovač" (stejná jako u ostatních), cena 199 Kč, osnova 8 kapitol.
- **Strukturální odlišnost od dosavadních destinací:** není to město k procházení, ale ~200km pás
  pobřeží kolem resortů a dive campů. Kapitola 05 (potápění a šnorchlování) je proto vlastní
  kapitola, ne podkapitola výletů — u ostatních destinací tenhle typ rozhodování neexistuje.
- **Fáze 1+2:** proběhly v jednom běhu `/destinace-text marsa-alam` — `fakta.md` (6,4 KB), 8 kapitol
  + 8 rychlotaháčků, `kontrola.md` na 25/30 položek.
- **Ruční kontrola:** hotová 2026-08-26 (`content/marsa-alam/kontrola.md`, stav zapsaný v hlavičce
  souboru). Konkrétní podniky nejmenované — pro Marsa Alam zatím nejsou sesbíraná recenzní data
  podle `docs/metodika-hodnoceni.md`.
- **Otevřené:** 5 nedohledaných čísel ve `fakta.md` (cena e-visa, přímé lety PRG–RMF, pronájem
  auta, cena OW potápěčského kurzu, cestovní pojištění s krytím potápění) — v textu označené jako
  „ověř na místě", nejsou blokující, ale stojí za doplnění před vydáním.
- **Fáze 3 a dál:** nezačato.

### 🆕 Malta — text hotový, čeká na ruční kontrolu

Založena 2026-08-26 na přímé zadání, **vedle běžícího pilota** (viz sekce nahoře). Prošla celou
Fází 0–2 v jednom sezení, novým levným postupem `/destinace-text` (jeden soubor `fakta.md` místo
osmi research souborů, kontrolu dělá člověk místo fact-checker agenta).

- **Fáze 0:** `01-tvorba-textu/docs/brief-malta.md` — persona „Nezávislý plánovač", cena 199 Kč,
  pobyt 5–8 dní, osnova 8 kapitol.
- **Odchylka osnovy proti Krétě:** „off the beaten path" není samostatná kapitola (na malém území
  nedává smysl) a je vtažená do kapitoly 06. Zato je samostatná a silná kapitola 05 o koupání —
  hlavní zdroj zklamání z Malty je, že většina pobřeží nejsou písčité pláže, ale skály.
- **Fáze 1:** `content/malta/fakta.md`, sběr 2026-08-26, spotřeba 8 hledání + 3 načtené stránky
  (strop nepřekročen). Soubor má 100 řádků / ~9 KB v bajtech (~8,3 tis. znaků) — mírně nad
  doporučeným stropem 8 KB, protože česká diakritika váží dva bajty.
- **Fáze 2:** 8/8 kapitol + 8/8 rychlotaháčků. Žádný podnik se nejmenuje — sběr podle
  `docs/metodika-hodnoceni.md` neproběhl, kapitoly 03 a 04 to čtenáři říkají otevřeně.
- **🔴 Nejdůležitější k ověření: vstupné.** Oficiální ceník Heritage Malta server při sběru
  odmítl načíst (HTTP 403), takže Hypogeum, Ħaġar Qim, Ġgantija i multi-site pass stojí na
  druhotných zdrojích. Položky 8–12 v `content/malta/kontrola.md`.
- **Druhý rozpor:** ceny rychlotrajektu Valletta–Gozo si napříč zdroji odporují (od ~7,50 EUR vs.
  12–40 EUR). Text uvádí spodní hranici s výslovnou výhradou, že se zdroje rozcházejí.
- **Časová past:** ekologický poplatek za ubytování se mění **1. 7. 2026** (0,50 → 1,50 EUR za
  osobu a noc, strop 5 → 22,50 EUR). Text nese obě sazby; po tomhle datu se dá první z nich
  vypustit.
- **Fáze 3 a dál:** nezačato.

### 🆕 Kypr — text hotový, čeká na ruční kontrolu

Založen 2026-08-26 na přímé zadání, **vedle běžícího pilota** (viz sekce nahoře). Prošel celou
Fází 0–2 v jednom sezení postupem `/destinace-text` (jeden `fakta.md`, kontrolu dělá člověk).

- **Fáze 0:** `01-tvorba-textu/docs/brief-kypr.md` — persona „Nezávislý plánovač", cena 199 Kč,
  pobyt 7–10 dní, osnova 8 kapitol.
- **Hlavní odlišnost od ostatních destinací: rozdělený ostrov.** Je to nosná mezera celého
  produktu a promítá se do tří kapitol — do 01 (měna, legální vstupní body, varování Republiky
  Kypr před ubytováním na severu), do 02 (jižní pojištění auta na severu neplatí, výjezd se hlásí
  půjčovně už při rezervaci) a do 06 (přejezd jako výlet). Druhá odlišnost je délka koupací
  sezóny — moře nad 20 °C zhruba květen–listopad, což rozšiřuje prodejní okno mimo letní špičku.
- **Odchylka osnovy:** „off the beaten path" není samostatná kapitola (jako u Malty), je vtažená
  do kapitoly 06, která výlety dělí podle typu — hory / antika / sever.
- **Fáze 1:** `content/kypr/fakta.md`, sběr 2026-08-26. Rozpočet webu **vyčerpán přesně**
  (8 hledání + 5 stránek). Soubor vyšel na 10,2 KB a byl ručně zhuštěn na 8,1 KB, aby nezdražoval
  každý další běh.
- **Fáze 2:** 8/8 kapitol + 8/8 rychlotaháčků, všechny v limitech (max. 1 900 znaků, 22 odrážek,
  6 podsekcí, 100 znaků na odrážku). Žádný podnik se nejmenuje — sběr podle
  `docs/metodika-hodnoceni.md` neproběhl, kapitoly 03 a 04 to čtenáři říkají otevřeně.
- **🔴 Nejdůležitější k ověření: jízdné.** Ceník Cyprus Public Transport (platný od 3. 8. 2026)
  si odporuje s agregátorem i dalšími zdroji (1,50 vs. 1,80 vs. 2,40 vs. 2,70 EUR), takže text
  všude píše rozptyl „zhruba 1,50–2,70 EUR podle okresu a způsobu platby". Stejný rozpor je
  u letištního expresu a u vstupného na Královské hrobky.
- **Neověřeno vůbec:** vstupné do Kourionu, Amathusu, hradu Kolossi a klášterů v Troodosu
  (rozpočet webu došel) — text je uvádí bez cen. Dál poplatek půjčovny za výjezd na sever
  (100–200 EUR) pochází z komerčních blogů, ne od půjčoven, a pitnost vody z kohoutku se
  nepodařilo doložit oficiálním zdrojem.
- **Ruční kontrola:** `content/kypr/kontrola.md`, 30 položek (15 A + 15 B) — **čeká na člověka.**
- **Fáze 3 a dál:** nezačato.

### 🆕 Antálie (Turecko) — text hotový a zkontrolovaný

Založena 2026-08-28 na přímé zadání, **vedle běžícího pilota** (viz sekce nahoře). Prošla celou
Fází 0–2 v jednom sezení postupem `/destinace-text` (jeden `fakta.md`, kontrolu dělá člověk).

- **Fáze 0:** `01-tvorba-textu/docs/brief-antalie.md` — persona „Nezávislý plánovač", cena 199 Kč,
  pobyt 7–10 dní, osnova 8 kapitol.
- **Hlavní odlišnost od ostatních destinací: turecká lira.** Je to nejrychleji se znehodnocující
  měna v celé řadě — jakékoli absolutní číslo v TRY zastará během sezóny. Kapitola 07 (Rozpočet)
  je proto postavená na **poměrech a rozhodovacích prazích**, ne na částkách; to je odchylka od
  ostatních destinací a je potřeba ji posoudit při sazbě. Druhá odlišnost: Turecko se v ČR prodává
  skoro výhradně jako all-inclusive balíček, takže nosná mezera produktu je „jak vyjet z resortu
  ven", ne „jak si naplánovat celý pobyt".
- **Fáze 1:** `content/antalie/fakta.md`, sběr 2026-08-28. Rozpočet webu **vyčerpán přesně**
  (8 hledání + 5 stránek), soubor 8,2 KB.
- **Fáze 2:** 8/8 kapitol + 8/8 rychlotaháčků, všechny v limitech. Žádný podnik se nejmenuje —
  sběr podle `docs/metodika-hodnoceni.md` neproběhl.
- **🔴 Nejdůležitější k ověření: doprava z letiště.** Zdroje si výrazně protiřečí u taxi do centra
  (600–700 vs. 200–800 TRY) i u autobusu Havaş (80 vs. 220 TRY) a primární zdroj (havas.net) se
  nepodařilo načíst. Text proto všude píše jen řádovou orientaci s doporučením trvat na taxametru
  nebo předem sjednané fixní ceně.
- **Neověřeno vůbec:** jízdné dolmuş a meziměstských autobusů Antálie–Kemer/Side/Alanya (text
  uvádí jen princip, žádné číslo), otevírací doby památek, sezónnost raftingu na Köprülü, cena
  CDW/den u půjčoven a detaily požadovaného cestovního pojištění (EHIC v Turecku neplatí).
  Vstupné do památek je jen ze sekundárního zdroje v EUR — primární `muze.gov.tr` / Müzekart
  nebyl dostupný.
- **Ruční kontrola:** `content/antalie/kontrola.md`, 27 položek (15 A + 12 B) — **prošlá 2026-09-02,
  bez oprav v kapitolách.** Rychlotaháčky tím zůstávají platné (nemusely se generovat znovu).
  Nedohledané údaje výše kontrolou nezmizely — text je obchází, ale pro QA ve Fázi 4 zůstávají.
- **Fáze 3 a dál:** nezačato.

### ❄️ Albánie — zmrazená

Původní pilotní destinace, research i všech 8 kapitol existuje.

**Blíž k hotovu, než vypadá.** Sedm z osmi fact-check záznamů sice hlásí `Stav: NALEZENY PROBLÉMY`,
ale nálezy už jsou v textu opravené (ověřeno namátkou u kapitol 4, 5 a 7 — sporné formulace jsou
přeformulované) — jen se pak fact-check nespustil znovu, takže záznamy zůstaly viset na starém
výsledku. Právě proto nemá Albánie ani krátké verze kapitol (ty čekají na `Stav: OK`) a destinace
není formálně připravená pro Fázi 3.

Rozpracovaný vizuální proof (obálka + kapitola 1 v Canvě) je taky zmrazený — viz
`docs/project-split-plan.md`.

**Nerozšiřovat.** Až bude čas se k ní vrátit, stačí pravděpodobně přeověřit 7 kapitol
(`01-tvorba-textu/content/albanie/text/*.md`) — pokud vyjdou na `Stav: OK`, krátké verze se
vygenerují samy a Albánie je na stejné startovní čáře jako Lloret.

---

## Co je z automatizace reálně postavené

Detail vždy v `<projekt>/docs/automation-registry.md`. Hrubý přehled:

- **Projekt 1:** funguje dobře — 3 skills (`/research-topic`, `/write-chapter`, `/tahacek`),
  4 subagenti (researcher, writer, fact-checker, tahacek-creator), hook, který po uložení kapitoly
  hlídá fact-check a po jejím uzavření krátkou verzi.
- **Projekt 2:** 1 skill + 1 agent, oba 🟡 pozastavené (popisují starý Canva postup).
- **Projekt 3:** nic — všech 6 skills a 4 subagenti jsou zatím jen záměr (⚪).
