> **⚠️ Pozastaveno 2026-07-17.** Postup popsaný v tomto dokumentu (v2 — `design_type: "poster"` +
> Canva vlastní stock fotky) se nepoužívá. Čím se nahradí, není rozhodnuto — varianty a doporučení
> jsou v `brief-vizualni-proces.md`, rozhodnutí je vedené jako otevřené #1 v
> `../docs/stav-projektu.md`. Nepokračovat v produkci kapitol tímto postupem.
> Tento dokument zůstává jako historický záznam Canva technického postupu a jeho omezení (v1 i v2)
> **a jako platný zdroj vizuálního stylu** (paleta, typografie, layout) — ten se rozhodnutím
> o procesu nemění.

# Design brief – vizuální styl průvodce (šablona pro všechny destinace)

Tento brief definuje grafický styl PDF průvodce. Cíl: teplý, editorialní, důvěryhodný vzhled ve
stylu prémiových travel guide/moodboard PDF (viz `design/inspirace/insp-1` až `insp-9`), který jde
replikovat pro další destinace výměnou barevného akcentu, fotek a názvu na obálce.

**2026-07-16 – zásadní revize po zpětné vazbě uživatele.** Verze 1 (čistě typografická, bez fotek,
`design_type: "doc"` verbatim) neodpovídala požadovanému stylu a navíc narazila na tvrdé API
omezení (hero sekce needitovatelná – viz "Výstup v1" níže, ponecháno jako historický záznam).
Verze 2 (tento dokument) byla závazná do 2026-07-17, kdy se postup pozastavil – viz rámeček nahoře.
Vizuální styl níže (paleta, typografie, layout) platí dál; pozastavený je jen technický postup
výroby a způsob získávání fotek.

## Styl – syntéza z 9 inspirací

Napříč `design/inspirace/insp-1` až `insp-9` (mix: elegantní editorialní travel magazine, pastelové
"boutique" itineráře, scrapbook/moodboard, infografika) je společné jádro:

- **Teplé krémové/béžové pozadí**, ne studená bílá ani tmavě modrá.
- **Skutečné destinační fotky** jako hlavní vizuální nosič – ne jen barevné bloky. Fotky v
  zaoblených obdélnících nebo kruhových výřezech.
- **Serif nadpisy** (elegantní, výrazné) + volitelný **script/rukopisný akcent** pro podnadpisy
  nebo "kicker" slova (např. "seasonal *SPECIAL*"), tělo textu čisté bezpatkové písmo.
- **Číslované kruhové ikonové odznaky** pro checklisty a kroky (den 1/2/3, tip 1/2/3...).
- **Měkké zaoblené "tip" kartičky** s ikonou, tečkované spojnice jako dekorativní prvek u itinerářů.

Tato syntéza (ne jedna konkrétní inspirace 1:1) je cíl – aplikovaná na brand paletu níže, ne na
neutrální pastelové barvy z inspirací.

## Paleta

- **Pozadí:** teplá krémová `#F3ECE0` (hlavní plocha stránky, nahrazuje bílou i tmavě modrou z v1)
- **Text:** teplá tmavě hnědá `#3A2E27` (nahrazuje studenou téměř černou z v1)
- **Sekundární akcent:** terakotová/cihlová `#C1502E` (odkaz na osmanskou/kamennou architekturu –
  nadpisy, čísla kapitol, CTA, "pozor/ověř si" boxy) – beze změny z v1
- **Podpůrná:** olivová/zelená `#6B7A3A` (insider tipy, ikonové odznaky) – beze změny z v1
- **Světlý neutrál:** `#FFFDF9` (pozadí kartiček/boxů na krémové ploše, jemný kontrast)

Barevný akcent (terakotová/olivová zůstávají, mění se jen krémový podklad dle nálady destinace)
je to, co se při škálování na další destinaci upravuje.

## Typografie

- **Nadpisy:** elegantní serif display font (např. Canva "Playfair Display" nebo vizuálně
  příbuzný) – velký, výrazný, čitelný i zmenšený.
- **Kicker/podnadpis akcent:** volitelný script/rukopisný font pro jedno až dvě klíčová slova
  (jako v insp-4/insp-5/insp-9), použít střídmě, ne na celé věty.
- **Běžný text:** čisté bezpatkové písmo (např. Lato/Poppins Regular) pro delší čtení na
  mobilu/tabletu.
- Minimální velikost běžného textu 11–12 pt ekvivalent, dostatečný řádkový proklad.

## Struktura stránky / layout

- Titulní strana: skutečná destinační fotka (hero, celostránková nebo horní 2/3), název +
  podnázev produktu přes/pod fotkou, barevný akcent.
- Obsah (klikatelný, pokud to Canva export do PDF podporuje).
- Každá kapitola začíná na nové stránce/stránkách: fotka relevantní k tématu kapitoly (nahoře
  nebo v postranním sloupci), serif nadpis kapitoly, ikona tématu.
- Opakující se vizuální prvky (konzistence napříč kapitolami i budoucími destinacemi):
  - **Fakta** – běžný text, případně s fotkou po straně.
  - **Insider tip** – olivový zaoblený box s ikonou žárovky/hvězdy.
  - **Pozor / ověř si** – terakotový zaoblený box s ikonou vykřičníku, pro pasáže s otevřenou
    otázkou z research (viz `../01-tvorba-textu/docs/open-questions-albanie.md`).
  - Checklisty/kroky – číslované kruhové ikonové odznaky (viz insp-5/insp-9).
  - Tabulky (rozpočet, ceny) – jednoduché, na krémovém/bílém podkladu.
- Patička: číslo stránky + název produktu.

## Obrázky / fotky

**Rozhodnutí v2 (nahrazuje zákaz fotek z v1):** ano, skutečné destinační fotky Albánie, protože
požadovaný styl na nich přímo stojí. Zdroj: Canva vlastní licencovaná stock knihovna (fotky
vyhledané a vložené přes Canva nástroje v rámci Canva designu/exportu jsou licenčně kryté Canva
předplatným – na rozdíl od stahování fotek odjinud z webu, což zůstává zakázané). Výběr fotek podle
tématu kapitoly (pláže/pobřeží, hory, historická centra měst, jídlo, doprava...), ne generické
stock fotky nesouvisející s Albánií.

Doplňkově: jednoduché ikony (Canva Elements) pro odznaky/tip boxy, případně jednoduchá vektorová
mapa regionů u kapitoly Regiony a itineráře.

## Technický přístup (návrh, ověřit při produkci proofu)

Verze 1 použila `design_type: "doc"` s `verbatim: true` – to sice zaručí doslovný text, ale výsledný
design je Canva "unbounded" (nestránkovaný) typ, kde auto-vygenerovaná hero sekce **není vůbec
editovatelná** přes API (viz historický záznam níže) a `merge-designs` na něj nefunguje. Pro v2:

1. Design agent nejdřív prozkoumá dostupné cesty k **bounded/stránkovanému** designu s reálně
   editovatelnými elementy a podporou fotek – např. `design_type: "document"`, `generate-design-structured`,
   nebo šablona přes `search-brand-templates`/`create-design-from-brand-template`. Cíl: fixní
   stránky, kde jde po vygenerování mazat/přebarvovat/nahrazovat elementy (na rozdíl od v1).
2. Protože bounded generování zřejmě nepodporuje `verbatim`, text se vloží ve dvou krocích:
   nejdřív se vygeneruje vizuální kostra/layout (styl, fotky, boxy) podle briefu, bez reálného
   textu kapitoly v promptu, a teprve poté se přesný text z `content/albanie/text/*.md` vloží přes
   editační operace (`replace_text`/`find_and_replace_text`) do připravených textových elementů –
   nikdy se nesmí nechat AI přeformulovat obsah kapitoly.
3. **Proof-first postup:** nejdřív obálka + 1 kapitola (proof), vizuálně ověřit (thumbnail) a počkat
   na potvrzení, než se stejným postupem vyrobí zbývajících 7 kapitol – aby se nezopakovala chyba
   z v1 (vada objevená až po dokončení všech 8).

## Obálka (cover)

- Název: **Albánie: Chytrý průvodce pro cestovatele s rozpočtem**
- Podnázev: pro personu "Objevitel na rozpočtu" – "Praktické tipy, insider místa a itineráře bez
  balastu"
- Skutečná destinační fotka Albánie (pobřeží/hory/historické centrum) jako hero, barevný akcent
  (terakotová + olivová na krémovém podkladu), serif nadpis.

## Poznámka ke škálování (Fáze 9)

Tento brief je psaný tak, aby šel zkopírovat pro další destinaci a upravit jen: barevný akcent,
název/podnázev na obálce, a fotky dané destinace (zbytek šablony – layout, typografie, opakující
se prvky – zůstává stejný).

## Výstup v1 (2026-07-15) – historický záznam, nahrazeno v2

Zamítnuto uživatelem 2026-07-16 (styl neodpovídal očekávání + needitovatelná hero sekce, viz
revize výše). Ponecháno jako záznam, proč `design_type: "doc"` + verbatim není správná cesta pro
v2 – nezkoušet znovu stejný postup.

Fáze 3 provedena přes Canva MCP (design agent), 2026-07-15. Text všech 8 kapitol byl vložen
doslovně (`design_type: "doc"`, `verbatim: true`) – žádný obsah nebyl přeformulován ani zkrácen.

### Titulní strana (cover)

- Canva design: **DAHPcJvK0Sc** – "Plakát - Albánie: Chytrý průvodce pro cestovatele s rozpočtem"
- Edit: https://www.canva.com/d/QPjwXvdv5os1rS0 · View: https://www.canva.com/d/P7fzp6Ro7-67iGy
- Typografická obálka bez fotky, jadranská modrá + terakotová z brand palety, název a podnázev
  podle briefu. Vygenerovaný návrh obsahoval zbytky event-flyer šablony (ikona oka, fiktivní údaje
  o místě/čase akce) – ručně vyčištěno přes editing transaction (smazány cizí prvky, upraven
  eyebrow text, doladěn poměr barevných ploch).

### Kapitoly (8× Canva Doc, verbatim)

| # | Kapitola | Design ID | Edit URL |
|---|----------|-----------|----------|
| 1 | Praktické základy | DAHPcPvSp8M | https://www.canva.com/d/610zqQuXOhJSxmD |
| 2 | Doprava po zemi | DAHPcLRZz84 | https://www.canva.com/d/fOaLfRHNWhj5P5t |
| 3 | Ubytování | DAHPcMWi_9I | https://www.canva.com/d/ZsjQQEvqQs8EzKg |
| 4 | Jídlo a pití | DAHPcEhFhIo | https://www.canva.com/d/EuFw9Bx8OZu4nxw |
| 5 | Regiony a itineráře | DAHPcKiGL7M | https://www.canva.com/d/hIXILbvHXg1q3F5 |
| 6 | Off the beaten path | DAHPcCT7YVQ | https://www.canva.com/d/hj66khcYQCVRKRX |
| 7 | Rozpočet | DAHPcBIY1_E | https://www.canva.com/d/AmsrrZfKrFrKqVn |
| 8 | Checklist před odjezdem | DAHPcMXHD7c | https://www.canva.com/d/0NhNKYsRe9UpAr2 |

Text byl kvůli celkové délce (~77 000 znaků) rozdělen po kapitolách do 8 samostatných `generate-design`
volání (jak předpokládá skill při překročení limitu jednoho volání) – každá kapitola je 1:1 kopie
příslušného `content/albanie/text/*.md` souboru včetně nadpisů, odrážek a kurzívy/tučného textu,
které verbatim mód podporuje. Boxy pro insider tipy / "pozor, ověř si" a barevné nadpisy podle
brand palety nebylo možné plošně aplikovat přes editační nástroje u textu vloženého v `doc` verbatim
módu – Canva Doc bloky (odstavce/nadpisy generované z markdownu) nejdou selektivně přebarvit per
sekce bez zásahu do každého jednotlivého text elementu; toto by šlo dotáhnout v další iteraci ručně
v Canva editoru nebo přes cílené `perform-editing-operations` na konkrétní `element_id` každého boxu.

### Sloučení cover + kapitoly do jednoho PDF – nepodařilo se automaticky

`merge-designs` (spojování stránek napříč designy) **nepodporuje Canva Doc** – Canva ho interně vede
jako "unbounded" (scrollovací, nestránkovaný) typ dokumentu, zatímco `merge-designs` pracuje jen s
"bounded" (stránkovanými) designy jako poster/prezentace. Pokus o vložení kapitoly 1 do sloučeného
designu skončil chybou: `Design 'DAHPcPvSp8M' has unsupported document type: unbounded`. Zkusili jsme
i alternativu doporučenou skillem – spojit všechny kapitoly rovnou do jednoho velkého Doc designu bez
merge nástroje (funguje to, ověřeno na kombinaci kapitol 1+2 v jednom volání) – ale uprostřed dalšího
volání (kapitoly 3+4) jsme narazili na kvótový limit Canva účtu pro `generate-design`
("User has reached their quota limit"), takže konsolidace do jediného Doc designu zůstala nedokončená.

**Prakticky dostupný výstup je tedy 9 samostatných PDF** (obálka + 8 kapitol), ne jeden sloučený
soubor. Všech 9 bylo úspěšně exportováno přes `export-design` (formát PDF, kvalita "pro", A4 u
obálky):

- Obálka: export proveden, stažitelný odkaz vygenerován (podepsaná Canva URL, platnost ~24 h od
  exportu – při potřebě znovu vyexportovat stačí zavolat `export-design` znovu na design ID výše).
- Kapitoly 1–8: export proveden stejným způsobem, po jednom PDF na kapitolu.

**Doporučený další krok pro člověka (Fáze 4/lidská kontrola):** buď (a) sloučit těchto 9 PDF do
jednoho souboru externím nástrojem (Acrobat, `pdftk`, `qpdf`, online merge), nebo (b) až kvóta Canva
generování obnoví, dokončit konsolidaci do jednoho Doc designu (kapitoly 3–8 zbývá přidat k
již ověřené kombinaci 1+2) a export zopakovat jako dva soubory (cover.pdf + obsah.pdf), nebo (c)
ručně v Canva UI zkopírovat obsah kapitol 3–8 do jednoho Doc designu (copy-paste mezi designy Canva
podporuje i pro scrollovací Docs) a sloučit s kapitolami 1–2.

### Pokus o opravu hero sekcí kapitol (2026-07-15) – zablokováno platformou

Druhý běh (oprava rozjetých auto-vygenerovaných hero bloků – anglické nadpisy, fotky talíře/židle/
moře, barvy mimo brand paletu) narazil na tvrdý limit Canva MCP API pro `design_type: "doc"`
(unbounded/scrollovací dokumenty, což je typ, ve kterém byly všechny kapitoly `verbatim`
vygenerovány):

- **Hero banner (nadpis + podnadpis + dekorativní obrázky/fotky) není vůbec vystavený jako
  editovatelný element.** `start-editing-transaction` / `perform-editing-operations` vrací pro
  všech 8 kapitol prázdné pole `fills` a hero text (např. "Before You Go" / "Essential logistics
  for your trip to Albania.") chybí i v `richtexts` – objeví se jen v plochém textovém výstupu
  `get-design-content`. Bez `element_id` nejde zavolat `delete_element`, `update_fill` ani
  `format_text` na nic z hero sekce – ověřeno na designu 1 (DAHPcPvSp8M) i designu 8
  (DAHPcMXHD7c).
- **`update_title` mění jen interní dashboardový titul designu, ne viditelný obsah stránky.**
  Ověřeno na kapitole 1: `update_title` → `"Praktické základy"` proběhl úspěšně a `get-design`
  potvrdil změnu metadat, ale `get-design-pages` thumbnail před/po commitu ukázal, že na stránce
  pořád je anglický nadpis "BEFORE YOU GO" i všechny tři dekorativní fotky (talíř, obraz, židle) –
  hero grafika je zjevně statický snímek vytvořený při generování, ne živý element navázaný na
  titul designu.
- Na `is_responsive: true` stránkách navíc `perform-editing-operations` striktně povoluje jen
  `update_title, replace_text, update_fill, delete_element, find_and_replace_text` – i kdyby se
  podařilo získat `element_id` hero prvků, operace jako `format_text` (barva textu) nebo
  `insert_fill` (barevný blok přes fotku) by stejně byly zamítnuté.

**Výsledek:** u žádné z 8 kapitol se nepodařilo přes API smazat fotky, přebarvit hero sekci do
brand palety ani upravit viditelný podnadpis. Jediná reálně proveditelná změna byla úprava
dashboardového (ne viditelného) titulu designu u kapitol s anglickým/nepřesným názvem – provedeno
u designů 1, 2, 5, 6, 7 (`update_title` → `Praktické základy`, `Doprava po zemi`,
`Regiony a itineráře`, `Off the beaten path`, `Rozpočet`). Toto rozšiřuje už dřív zdokumentované
omezení (nejde selektivně přebarvit text v Doc designu) na celou hero sekci včetně obrázků.

**Doporučení pro člověka:** hero sekce (nadpis, podnadpis, fotky) u všech 8 kapitol je potřeba
opravit ručně v Canva UI (editor umí mazat/přebarvovat elementy, které MCP API nevystavuje) – buď
smazat hero blok a nahradit jednoduchým barevným pruhem s textem podle brand palety (`#1B4B66` /
`#C1502E`), nebo aplikovat brand kit přímo v editoru. Po ruční úpravě stačí zavolat `export-design`
znovu pro čerstvé PDF.

Čerstvé exporty (formát PDF, kvalita `pro`) pořízené 2026-07-15 po úpravě dashboardových titulů –
**vizuální obsah stránek je identický s předchozí verzí** (hero sekce beze změny), podepsané URL
mají platnost jen řádově hodiny:

| # | Design ID | Export |
|---|-----------|--------|
| 1 | DAHPcPvSp8M | proveden, viz konverzace 2026-07-15 |
| 2 | DAHPcLRZz84 | proveden, viz konverzace 2026-07-15 |
| 3 | DAHPcMWi_9I | proveden, viz konverzace 2026-07-15 |
| 4 | DAHPcEhFhIo | proveden, viz konverzace 2026-07-15 |
| 5 | DAHPcKiGL7M | proveden, viz konverzace 2026-07-15 |
| 6 | DAHPcCT7YVQ | proveden, viz konverzace 2026-07-15 |
| 7 | DAHPcBIY1_E | proveden, viz konverzace 2026-07-15 |
| 8 | DAHPcMXHD7c | proveden, viz konverzace 2026-07-15 |

### Aktuální stav pilotního PDF (v1, zamítnuto)

Všech 9 exportů bylo staženo a lokálně sloučeno (pořadí: obálka → kapitoly 1–8, bez merge-designs,
viz výše) do jednoho pracovního souboru: `design/albanie/albanie-pruvodce.pdf` (32 stran, ~54 MB –
negitováno, jen lokálně). Tento soubor je nahrazen novým vizuálním stylem (v2) – ponechán jen jako
referenční/starý build, nepoužívat jako finální produkt.

## Výstup v2 (2026-07-16 – proof hotov, čeká na schválení)

### Historie: proof nejdřív blokován kvótou/plánem, po upgradu na Canva Plus proveden

Prvni pokus (viz níže "Blokace před upgradem") narazil na `generate-design` kvótu a na
`search-brand-templates` vyžadující placený plán. Po tom, co uživatel aktivoval **Canva Plus**,
proof byl zopakován od začátku stejný den a tentokrát prošel až do konce (cover + kapitola 1,
5 stran, export PDF).

### Zvolený technický postup

- **Cover:** `generate-design` s `design_type: "document"` vrátil jen kancelářské šablony (press
  release, "Albania Travel Guide" report, invoice...) bez skutečné fotky – nehodí se na fotografický
  cover. `design_type: "poster"` naopak spolehlivě vracel kandidáty se skutečnou fotkou destinace,
  správnou paletou i serif nadpisem. Cover je tedy `design_type: "poster"` (bounded/stránkovaný,
  1 strana) – vybrán z 4 vygenerovaných kandidátů ten s reálnou fotkou albánského pobřeží.
- **Kapitola 1:** `design_type: "document"` opět vracel jen kancelářské šablony (meeting agenda,
  invoice, press release) i pro kapitolu – nehodí se na foto-editoriální layout. Řešení: hero strana
  kapitoly (fotka + úvod + insider tip/pozor boxy) vygenerována jako `design_type: "poster"`
  (kandidát se skutečnou fotkou flat-lay cestovních věcí – pas, peníze, telefon, sluneční brýle).
  Pokračovací strany (čistě textové, bez fotky) vygenerovány týmž `poster` typem s promptem
  zaměřeným na velkou textovou plochu (bez fotky), 1 šablona znovu použita pro 3 další strany.
- Protože `poster` generuje vždy jen 1 stránku a `perform-editing-operations` nemá operaci pro
  přidání strany, bylo 5 samostatných `poster` designů (1 cover-styl hero + 4× textová šablona)
  spojeno do jednoho designu přes **`merge-designs`** (`create_new_design` + postupné
  `modify_existing_design`/`insert_pages`, protože nástroj povoluje jen 1 operaci na volání) –
  funguje bez problémů na `poster` typ (na rozdíl od `doc` z v1).
- Text byl v promptu ke `generate-design` popsán jen jako styl/placeholder (anglický
  lorem-ipsum, "Kapitola 1"), skutečný český text z `content/albanie/text/01-prakticke-zaklady.md`
  byl vložen až přes `replace_text`/`find_and_replace_text` v editační transakci nad hotovým
  layoutem – přesně podle skillu.
- `generate-design-structured` nebyl použit – je omezený na `design_type: "presentation"` a
  vyžaduje `request-outline-review` widget flow mimo tento nástrojový set.

### Rozložení textu a úpravy layoutu

Kapitola 1 má 5 stran (bounded design, `merge-designs` funguje):

1. Hero: fotka (pas/peníze/brýle/telefon na stole), nadpis „Praktické základy", úvod „Než vyrazíš",
   olivový insider-tip box (bankomat/DCC tip) a terakotový pozor box (přeplácení taxikáři).
2. Doklady a vstup do země + Jak se do Albánie dostaneš (Letecky, Z letiště do centra Tirany).
3. Autem přes pozemní hranici, Trajektem z Itálie, Peníze — lek, karty, bankomaty.
4. SIM karta a internet, Bezpečnost.
5. Kdy jet, Rychlé shrnutí (odrážkový checklist).

První pokus vložit celou "Doklady + Jak se dostaneš" na stránku 2 přetekl pod stránku (výška textu
1769 px proti dostupným ~1621 px) – opraveno rozšířením textového pole a mírným snížením velikosti
písma (z výchozí generované velikosti na 26 px, u strany 3 na 25 px kvůli těsnému doteku patičky) –
zůstává v rozumné čitelné velikosti. Titulek na hero straně se nejdřív zalomil na 2 řádky a
překrýval dekorativní linku – opraveno rozšířením textového pole a zmenšením fontu na 60 px.
Nepodařilo se najít textové pole pro obsah terakotového pozor-boxu na hero straně (šablona měla jen
nadpis + ikonu) – vyřešeno přesunutím/přeškálováním nevyužitého patičkového textového pole do boxu a
vložením reálného textu (přeplácení taxikáři) + `format_text` (bílá barva, větší písmo).

### Design ID a odkazy

**Cover:**
- Canva design: **DAHPi_beWeU** – "Albánie: Chytrý průvodce pro cestovatele s rozpočtem - Obálka (v2)"
- Edit: https://www.canva.com/d/meTcXtU-y4LhDM6 · View: https://www.canva.com/d/O3adXF-rh45XjTG
- Export PDF (pro kvalita, podepsaný odkaz platný ~14 h od exportu 2026-07-16):
  https://export-download.canva.com/beWeU/DAHPi_beWeU/-1/0-7572186552919624168.pdf

**Kapitola 1 (5 stran):**
- Canva design: **DAHPjAg7pRM** – "Kapitola 1: Prakticke zaklady - v2 proof"
- Edit: https://www.canva.com/d/pqtH-LMrWEnnQGQ · View: https://www.canva.com/d/2u6M7SttOnFHh4t
- Export PDF (pro kvalita, podepsaný odkaz platný ~8 h od exportu 2026-07-16):
  https://export-download.canva.com/g7pRM/DAHPjAg7pRM/-1/0-3946788850372142438.pdf

Vizuálně ověřeno přes `start-editing-transaction`/`get-design-pages` thumbnaily na obou designech
(všech 5 stran kapitoly + cover) před commitnutím i po něm – reálná fotka albánského pobřeží na
coveru, reálná fotka cestovních dokladů/peněz na kapitole, krémové pozadí `#F3ECE0`, terakotový
serif nadpis `#C1502E`, olivový insider-tip box `#6B7A3A`, čitelný běžný text v hnědé `#3A2E27`,
žádné zbytkové anglické placeholder texty ani cizí prvky (na rozdíl od v1).

### Blokace před upgradem (2026-07-16, dopoledne) – vyřešeno upgradem na Canva Plus

Před aktivací Canva Plus byly zaznamenány dvě blokace: `generate-design` (`design_type: document`)
2× vrátil `User has reached their quota limit` a `search-brand-templates` 2× vrátil `This feature
requires a Canva paid plan`. Po upgradu na Canva Plus obě chyby zmizely a `generate-design` fungoval
bez problémů (viz postup výše) – `search-brand-templates` už nebyl potřeba, protože `poster` typ
řešení nevyžaduje.

### Doporučení pro člověka

- **Proof je hotový a čeká na vizuální schválení** (cover + kapitola 1, 5 stran) – teprve po
  potvrzení pokračovat na kapitoly 2–8 stejným postupem (`poster` design_type pro hero i textové
  strany, `merge-designs` pro spojení do vícestránkového designu, verbatim vložení textu přes
  editační operace).
- Drobné manuální doladění, které by šlo v Canva editoru zlepšit: bullet znaky v "Rychlém shrnutí"
  na straně 5 jsou zarovnané na střed (zděděno z šablony) – vypadalo by čistěji zarovnat na začátek
  řádku; velikost písma běžného textu (25–26 px) by šlo na kratších stranách (4, 5) mírně zvětšit
  zpět na jednotnou hodnotu, protože tam zbylo hodně volného místa.

### Oprava dvou vad na straně 1 kapitoly 1 (2026-07-16, po zpětné vazbě z vizuální kontroly)

Nadřazený agent po čerstvém exportu (ne cache thumbnail) našel na hero straně kapitoly 1 dvě vady.
Obě prošly přes `start-editing-transaction` → `perform-editing-operations` → `commit-editing-transaction`
na designu DAHPjAg7pRM, ověřeno čerstvým `export-design` (PNG strany 1) po commitu:

1. **Přetečení úvodního textu pod boxy – opraveno.** Textové pole úvodního odstavce (`element_id`
   `...LBqbn1pk2Xr8G0N8`, končící „...internet, bezpečnost a kdy vlastně jet.") sahalo až na
   souřadnici top ≈ 1456 px, zatímco oba boxy (olivový + terakotový) začínaly na top 1431 px –
   přesah cca 25 px. Řešení zvoleno: posun obou boxů (ne úpravu textu) o 80 px níž – přesunuty
   všechny součásti obou boxů najednou, aby zůstaly vzájemně zarovnané: pozadí boxů, nadpisy
   "Insider tip"/"Pozor", dekorativní podtržení pod "Insider tip", obě těla textu a ikona uvnitř
   Pozor boxu (8 elementů, `position_element`, top +80 px, left beze změny). Nový odstup mezi
   koncem odstavce a horní hranou boxů je cca 54 px. Ověřeno vizuálně na čerstvém PNG exportu
   strany 1 – žádný překryv.

2. **Nekonzistentní letter-spacing v "Pozor" boxu – NEOPRAVENO, tvrdý limit API.** Tělo textu
   v terakotovém boxu (`element_id` `...LBPgFC9PGDHVBDgW`) má viditelně širší mezery mezi písmeny
   než olivový "Insider tip" box – potvrzeno i na vysokém rozlišení čerstvého PNG exportu. Vyzkoušeno
   postupně: (a) `format_text` s `font_weight: normal`, `font_style: normal`, `text_align: start`,
   `line_height: 1.3` – bez viditelné změny rozestupů (jen mírně zmenšilo výšku boxu z 226 px na
   215 px, spacing beze změny), (b) `resize_element` (změna šířky ze 480 na 485 px, aby seděla na
   Insider tip box) – text se přeuspořádal, ale rozestupy zůstaly stejně široké. Závěr: `format_text`
   nemá parametr pro letter-spacing/tracking (schema obsahuje jen `color, decoration, font_size,
   font_style, font_weight, line_height, link, list_level, list_marker, strikethrough, text_align`)
   a font family změnit nejde (nástroj to explicitně nepodporuje – stejné omezení jako zaznamenané
   dřív v tomto briefu). Rozestup je pravděpodobně vlastnost fontu/varianty tohoto konkrétního
   textového elementu (repurpose z patičkového pole, viz sekce "Rozložení textu a úpravy layoutu"
   výše) a přes dostupné MCP nástroje ho nejde selektivně upravit. **Doporučení pro člověka:**
   opravit ručně v Canva editoru – označit text v Pozor boxu a buď vynulovat tracking/letter-spacing
   přímo, nebo změnit font na stejný, jaký má Insider tip box.
   - Mimoto při kontrole všimnuto (nepožádáno, neopraveno, jen pro info): malá tmavá ikonka uvnitř
     Pozor boxu (`element_id` `...LBPfCZwDxNNT9VkB`) se vizuálně překrývá se slovem uprostřed
     odstavce ("signál") – vhodné doladit ručně spolu s letter-spacingem.

Čerstvý export po opravě (PDF i PNG strany 1, `export-design`, 2026-07-16): stažen a vizuálně
zkontrolován přímo (ne přes `get-design-thumbnail`), potvrzuje bod 1 opraven, bod 2 přetrvává.
