# Digitální produkt: turistický průvodce destinací (PDF) + PPC prodej

> Tento dokument popisuje **proces** (co se v které fázi dělá a co z toho lze automatizovat), ne
> aktuální stav. Kde přesně teď jsme, co je hotové a co je další krok → `docs/stav-projektu.md`.

## Kontext

Cílem je vytvořit produktovou řadu digitálních turistických průvodců (PDF e-booky s tipy a "deep knowledge" ke konkrétní destinaci), kde každá destinace = samostatný prodejný produkt. Start je jako **pilot na 1 destinaci** (proces se ověří, pak replikuje), prodej přes **vlastní web + Meta/Google Ads**, obsah i data se sbírají **od nuly** (žádné vlastní zdroje zatím nejsou). Interaktivní webová/app verze průvodce je zaznamenaná jako **budoucí koncept**, teď se nestaví.

Účelem tohoto plánu je rozepsat celý proces – od výběru destinace po běžící PPC kampaň – na fáze, a u každého kroku vyznačit, co lze automatizovat pomocí nástrojů Claude Code (Skills, Loops, MCP servery, Hooks, tým agentů/subagentů), a co musí zůstat na člověku (rozhodnutí, právní/finanční kroky, kvalitativní schválení).

Legenda automatizace:
- 🤖 **Skill** – opakovaně použitelný balíček promptu/nástrojů (např. `/generate-guide-chapter`)
- 🔁 **Loop** – běží na interval / dokud není splněna podmínka (`/loop`)
- 🔌 **MCP** – napojení na externí systém (Notion, Google Drive, Canva, Gmail…)
- 🪝 **Hook** – reakce na událost (např. po uložení souboru spustit kontrolu faktů)
- 👥 **Agent tým** – více specializovaných subagentů paralelně/v pipeline
- 🙋 **Člověk** – vyžaduje lidské rozhodnutí/schválení, nejde (rozumně) automatizovat

---

## Fáze 0 – Validace & strategie produktu

**Cíl:** Vybrat destinaci, definovat personu, cenu a osnovu 8 kapitol, než se spustí sběr dat a psaní.

Kroky:
1. Výběr kandidáta destinace (poptávka u českých/slovenských turistů, konkurence existujících
   průvodců, mezera na trhu – CK prodávají hotel a pláž, ne "deep knowledge" a rozhodovací rámce).
2. Návrh cílové persony a ceny – u dosavadních destinací se drží konzistentní napříč řadou
   (stejný typ cestovatele, 199 Kč), mění se jen tam, kde si to destinace vyloženě žádá.
3. Návrh osnovy 8 kapitol – jediné místo, kde je napsané, co se má v dalších fázích sbírat a psát.
4. Zápis do `01-tvorba-textu/docs/brief-<destinace>.md`.
5. Rozhodnutí: jde se do přípravy textu na vybranou destinaci.

Automatizace:
- 🙋 Celá fáze je rozhovor s člověkem, bez dedikovaného skillu. Návrh persony/ceny/osnovy vychází
  z předchozích destinací, ale destinaci, cenu a osnovu vždy potvrzuje člověk před spuštěním Fáze 1.

Výstup: `docs/brief-<destinace>.md` (proč destinace, persona, cena, osnova), potvrzený člověkem.

---

## Fáze 1 – Research & sběr "deep knowledge" dat

**Cíl:** Nasbírat tvrdá data (čísla, ceny, otevírací doby, úřední informace) do jednoho souboru,
který je jediným zdrojem čísel pro psaní kapitol.

Kroky:
1. Sběr faktických dat podle osnovy z briefu – pod tvrdým stropem hledání na webu (jednou na
   destinaci, ne jednou na kapitolu; cena je ve čtení stránek, ne v psaní).
2. Uložení do jednoho souboru `content/<destinace>/fakta.md`, max. ~150 řádků / 8 KB.
3. Výběr konkrétních hotelů/restaurací/atrakcí, které smí být v textu jmenované, jen podle
   doložené metodiky – dvě nezávislé platformy s hodnocením a prahem na počet recenzí (Google Maps
   + Tripadvisor u restaurací a atrakcí, Google Maps + Booking.com u hotelů) – detail v
   `01-tvorba-textu/docs/metodika-hodnoceni.md`.

Automatizace:
- 🤖 **Skill** `/destinace-text <destinace>` (první běh jeho sekvence) – agent `fakta-collector`
  sesbírá fakta v jednom běhu pod rozpočtem (8 hledání + 5 stránek).
- 🙋 Věrohodnost dat kontroluje člověk ručně (Fáze 2 kontrolní list) – samostatný fact-check agent
  se ukázal dražší než zbytek procesu a byl zrušen.

Výstup: `content/<destinace>/fakta.md` – jediný zdroj čísel pro Fázi 2.

---

## Fáze 2 – Tvorba obsahu (psaní)

**Cíl:** Z `fakta.md` a stabilní obecné znalosti napsat 8 kapitol ve dvou verzích (dlouhá příručka
+ krátký rychlotaháček) a připravit podklad pro ruční kontrolu.

Kroky:
1. Kapitoly píše agent `chapter-writer` v dávkách po 4 (dva běhy na destinaci) – bez přístupu na
   web, čísla výhradně z `fakta.md`, hodnota textu je v rozhodovacích rámcích, ne ve výčtu faktů.
2. Rychlotaháček (max. 1 A4 na kapitolu) destiluje z hotové kapitoly agent `tahacek-creator` –
   nikdy nepřidává nic nového, jen ubírá a přeformulovává.
3. Každá dávka zapisuje položky do `content/<destinace>/kontrola.md` – číslovaný seznam k ruční
   kontrole, **max. 30 položek na celou destinaci** (sekce A tvrdá čísla s odkazem na zdroj, sekce
   B tvrzení z obecné znalosti bez zdroje).
4. Člověk kontrolu projde; drobné opravy se píšou rovnou do kapitoly (nový běh agenta se kvůli
   jedné hodnotě nevyplatí). Po úpravě kapitoly se musí přegenerovat i její taháček, ne opravovat
   ručně, jinak se obě verze rozejdou.

Automatizace:
- 🤖 **Skill** `/destinace-text <destinace>` – zastřešuje celou Fázi 1+2 ve 4–5 bězích (fakta →
  kapitoly 01–04 → kapitoly 05–08 → taháček) pod kontrolou nákladů.
- 👥 **Agent tým** – `chapter-writer` (text) a `tahacek-creator` (destilát); žádný samostatný
  fact-checker agent.
- 🙋 Ruční kontrolu `kontrola.md` a finální schválení tónu dělá vždy člověk.

Výstup: 8 kapitol ve dvou verzích (`text/` + `text/_tahacek/`) a `kontrola.md` prošlý člověkem –
destinace je tím hotová pro Fázi 3.

---

## Fáze 3 – Vizuál & produkce PDF

**Cíl:** Proměnit text ve vizuálně kvalitní, prodejný PDF produkt.

Kroky:
1. Návrh grafického stylu/šablony (brand, barvy, fonty, layout kapitol).
2. Zdroj obrázků – licencované/AI-generované ilustrace nebo fotky (žádné vlastní fotky zatím nejsou).
3. Sazba obsahu do šablony (layout, mapy, tabulky, ikony).
4. Tvorba obálky produktu.
5. Export a technická kontrola PDF (velikost souboru, čitelnost na mobilu/tabletu, klikatelný obsah/odkazy).

Automatizace:
- 🙋 **Generování stránek** – stránky vyrábí člověk v Nano Banana 2 / GPT Image (viz `02-tvorba-vizualu/docs/prompt-guide.md`). Původní záměr automatizovat sazbu přes Canva MCP se neosvědčil a je odstavený; agent do generování nevstupuje, dodává text a kontrolní podklady.
- 🙋 **Kontrola proti zdroji** – povinný krok. Model si text potichu krátí a mění, což na stránce není vidět; bez porovnání s kapitolou se to neodhalí.
- 👥 **Agent tým** – "Design" subagent připravující požadavky na obrázky/ilustrace (prompty pro generování nebo výběr) odděleně od textového agenta.
- 🙋 Finální vizuální schválení a licenční kontrola obrázků (autorská práva!) dělá člověk.

Výstup: hotový PDF produkt + zdrojový design (šablona pro další destinace).

---

## Fáze 4 – QA & finalizace produktu

**Cíl:** Ujistit se, že produkt je kvalitní a prodejný, než se pustí do prodeje.

Kroky:
1. Kompletní read-through (obsah, chyby, konzistence).
2. Testování PDF na různých zařízeních/čtečkách.
3. Sestavení "value proof" – proč tento produkt stojí za peníze (shrnutí přidané hodnoty pro marketing).
4. Právní náležitosti (autorská práva na obrázky/mapy, prohlášení o odpovědnosti za aktuálnost cen/otevíracích dob, obchodní podmínky, GDPR).
5. Finální verzování a pojmenování produktu.

Automatizace:
- 👥 **Agent tým** – QA subagent projde checklist (chybějící odkazy, nekonzistentní formátování, chybějící alt texty, rozbité obrázky) automaticky.
- 🤖 **Skill** `/qa-checklist` – standardizovaný kontrolní seznam spouštěný před každým vydáním (opakovatelné pro každou další destinaci).
- 🙋 Právní náležitosti a finální "go/no-go" k prodeji dělá člověk.

Výstup: finální prodejná verze PDF, připravená ke spuštění prodeje.

---

## Fáze 5 – Prodejní infrastruktura (web)

**Cíl:** Postavit vlastní web, kde lze produkt koupit a automaticky doručit.

Kroky:
1. Volba platformy (např. Shoptet/WordPress+WooCommerce/vlastní řešení) – u digitálních produktů řešit hlavně automatické doručení souboru po platbě.
2. Návrh a tvorba landing page produktu (prodejní copy, ukázky obsahu, recenze/social proof, FAQ).
3. Napojení platební brány.
4. Automatické doručení PDF po platbě (e-mail/ke stažení).
5. Nastavení fakturace a účetních náležitostí (živnost/DPH pravidla pro digitální produkty prodávané do EU – MOSS/OSS režim).
6. Nastavení analytiky a měření konverzí (GA4, Meta Pixel, Google Ads tag) – nutné dřív, než se pustí PPC.

Automatizace:
- 🤖 **Skill** `/build-landing-page` – vygeneruje strukturu a copy prodejní stránky z contentového briefu produktu.
- 👥 **Agent tým** – "Copywriter" subagent napíše prodejní texty (headline, benefity, FAQ) na základě "value proof" z Fáze 4.
- 🔌 **MCP (Gmail)** – automatizace transakčních/support e-mailů (draft odpovědí na dotazy zákazníků).
- 🙋 Výběr platformy, napojení platební brány, účetní/daňové nastavení (OSS, faktury) – vyžaduje lidské/odborné (účetní) rozhodnutí, nejde delegovat na agenta.

Výstup: funkční e-shop s jedním produktem, měřením konverzí a automatickým doručením.

---

## Fáze 6 – Příprava PPC kampaní

**Cíl:** Připravit vše potřebné pro spuštění placené reklamy dřív, než se rozjede útrata.

Kroky:
1. Definice kampaňové struktury a cílů (prodej vs. traffic vs. remarketing).
2. Cílení – výběr publik (zájmy, geo, lookalike – až bude pixel data).
3. Tvorba reklamních kreativ (vizuály, video/carousel, texty pro Meta a Google Ads).
4. Copywriting variant reklam pro A/B testování (více headline/CTA variant).
5. Nastavení konverzních událostí a atribuce (návaznost na Fázi 5 – pixel/GA4).
6. Rozpočet a bidding strategie.

Automatizace:
- 👥 **Agent tým** – "Ads Copywriter" subagent generuje sadu variant textů/headlinů podle cílové persony z Fáze 0.
- 🔌 **MCP (Canva)** – generování reklamních vizuálů/creative sad (formáty pro Meta feed/story, Google Display) ze stejného brand kitu jako PDF.
- 🤖 **Skill** `/generate-ad-variants` – standardizovaný výstup: sada headlinů + textů + CTA pro A/B test, napojená na produktový brief.
- 🙋 Samotné založení kampaně v Ads Manageru/Google Ads, nastavení rozpočtu a spuštění útraty musí schválit a spustit člověk (finanční riziko + platformy nemají obecně dostupné MCP pro přímý zápis, jde spíš o připravené podklady ke vložení).

Výstup: kompletní sada reklamních kreativ, textů a kampaňové struktury připravené k nahrání do Ads Manageru.

---

## Fáze 7 – Spuštění a optimalizace PPC

**Cíl:** Rozjet kampaně a průběžně je zlepšovat na základě dat.

Kroky:
1. Spuštění kampaní s malým rozpočtem (test fáze).
2. Sledování klíčových metrik (CTR, CPC, ROAS, konverzní poměr).
3. A/B testování kreativ a cílení.
4. Škálování úspěšných sad, vypínání neúspěšných.
5. Retargeting kampaně na návštěvníky, kteří nekoupili.
6. Pravidelný reporting výkonu.

Automatizace:
- 🔁 **Loop** – pravidelný (např. denní/týdenní) report výkonu kampaní – pokud/až bude k dispozici MCP napojení na Meta/Google Ads API, subagent stáhne metriky a vygeneruje shrnutí + doporučení (co vypnout/škálovat).
- 👥 **Agent tým** – "Campaign Analyst" subagent interpretuje čísla a navrhuje konkrétní úpravy (ne jen dashboard, ale doporučení).
- 🤖 **Skill** `/weekly-ads-report` – standardizovaný výstup reportu k rychlému rozhodování.
- 🙋 Reálné škálování rozpočtu a vypínání/zapínání kampaní zůstává na člověku (finanční riziko, platformy to typicky vyžadují manuální/API zásah mimo dnešní dostupné nástroje).

Poznámka: Přímé MCP napojení na Meta Ads / Google Ads API dnes není v dostupné sadě nástrojů – pokud objem kampaní časem ospravedlní investici, dává smysl nechat postavit vlastní MCP server nad Ads API (čtení metrik, případně i zápis) jako samostatný krok až po pilotu.

Výstup: běžící, průběžně optimalizovaná kampaň s pravidelným reportingem.

---

## Fáze 8 – Post-launch péče a iterace

**Cíl:** Udržet produkt aktuální a zákaznickou zkušenost dobrou.

Kroky:
1. Zákaznická podpora (dotazy, reklamace, technické problémy se stažením).
2. Sběr zpětné vazby/recenzí.
3. Pravidelná aktualizace faktických dat (ceny, otevírací doby – viz Fáze 1 revalidace).
4. Vydávání drobných verzí/aktualizací produktu.

Automatizace:
- 🔌 **MCP (Gmail)** – návrhy odpovědí na support dotazy k lidskému schválení.
- 🔁 **Loop** – čtvrtletní revalidace dat destinace (návaznost na Fázi 1) → automaticky navrhne, které pasáže textu potřebují update.
- 🙋 Odesílání odpovědí zákazníkům a rozhodnutí o refundacích dělá člověk.

---

## Fáze 9 – Škálování na další destinace

**Cíl:** Jakmile pilot ověří proces a prodejnost, replikovat ho efektivně na další destinace.

Kroky:
1. Vyhodnocení pilotu (co fungovalo, co upravit v procesu).
2. Zobecnění šablon (obsahová osnova, design šablona, ads šablony) do znovupoužitelné podoby.
3. Standardizace celého pipeline do sady Skills/subagentů, aby další destinace šla spustit téměř "na jedno tlačítko" (research → psaní → design → QA → landing page → ads).
4. Postupné přidávání destinací, sledování, které agenty/kroky je potřeba dál doladit.

Automatizace:
- 👥 **Agent tým** – celá pipeline z fází 1–6 se zapouzdří do orchestrovaného řetězce subagentů spouštěného jedním příkazem pro novou destinaci.
- 🤖 **Skill** `/new-destination-guide <destinace>` – zastřešující skill, který prochází fáze 1–4 (research → psaní → design → QA) a připraví podklady pro fáze 5–6.
- 🤖 **Skill** `/evaluate-pilot` – po ukončení testovacího období pilotu automaticky posbírá data napříč fázemi (výkon PPC z Fáze 7, konverze/tržby z Fáze 5, support témata z Fáze 8, poznámky z QA z Fáze 4) a vygeneruje strukturované vyhodnocení: co fungovalo, co ne, kde v pipeline vznikaly úzká hrdla.
- 👥 **Agent tým** – "Pilot Analyst" subagent porovná pilot proti cílům z Fáze 0 (persona, cena, poptávka) a navrhne konkrétní úpravy procesu i šablon (obsah, design, ads) před škálováním na další destinace.
- 🔁 **Loop** – v testovacím období pilotu pravidelně (např. týdně) sbírá metriky a doplňuje průběžný "pilot log", aby vyhodnocení na konci nebylo jen jednorázový snímek, ale mělo i trend v čase.
- 🙋 Rozhodnutí, zda a jak škálovat (kolik dalších destinací, jaký rozpočet) na základě vyhodnocení dělá člověk.

---

## Doporučená technická příprava (aby automatizace fungovala)

1. ✅ **Založit git repozitář** pro projekt – hotovo. V repu se drží: research data (Fáze 1), texty (Fáze 2), design zdroje, landing page copy, ads podklady. Vygenerované binárky (PDF, exportované obrázky) se negitují. Repo je zatím jedno společné pro všechny 3 projektové složky – viz `docs/project-split-plan.md`.
2. **Notion jako centrální databáze destinací** – stav každé destinace (nápad → research → psaní → design → QA → live), napojeno přes dostupný Notion MCP.
3. **Canva jako design engine** – brand kit + šablony pro PDF i ads kreativy, napojeno přes dostupný Canva MCP.
4. **Postupně budovat Skills** pro opakující se kroky (research, psaní kapitoly, QA checklist, ads varianty) – vyplatí se hlavně od Fáze 9 (škálování), u pilotu stačí základní verze.
5. Až po ověření pilotu zvážit vlastní MCP server nad Ads API pro čtení/zápis kampaní – u jednoho pilotního produktu se to zatím nevyplatí.

---

## Co dělat hned (pilot – 1 destinace)

Odškrtávaný postup pilotu. Aktuální detailní stav a nejbližší konkrétní úkol je v
`docs/stav-projektu.md`.

1. ✅ Fáze 0: vybrat destinaci a sepsat brief (rozhovor s člověkem, rozhodnutí člověka).
2. ◐ Založit git repo (✅ hotovo) + Notion databázi pro projekt (zatím ne – repo zatím stačí).
3. ✅ Fáze 1–2: sběr faktů a psaní obsahu (`/destinace-text` + ruční kontrola `kontrola.md`).
4. ⬜ Fáze 3–4: design + QA. *Fáze 3 je blokovaná otevřeným rozhodnutím o vizuálním procesu.*
5. ⬜ Fáze 5: postavit minimální prodejní web s jedním produktem a měřením konverzí.
6. ⬜ Fáze 6–7: připravit a spustit první malou PPC kampaň (testovací rozpočet).
7. ⬜ Vyhodnotit pilot → teprve pak Fáze 9 (škálování).
