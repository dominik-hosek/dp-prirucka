---
title: Vizuální proces – hluboký brief a doporučení
datum: 2026-07-17
status: návrh k rozhodnutí (navazuje na pozastavení procesu v `docs/design-brief-albanie.md` a `docs/automation-registry.md`)
---

# Vizuální proces: hluboký brief a doporučení

## Shrnutí

Dosavadní pokus (Canva MCP, `poster`/`doc` design_type, Canva vlastní stock knihovna) narazil na dva
druhy problémů a oba jsou vidět přímo na proofu kapitoly 1: **technické** (needitovatelná hero sekce,
nefunkční `merge-designs` na unbounded designy, nejde upravit letter-spacing přes API) a **obsahové**
(fotka na hero straně kapitoly 1 je generický flat-lay – pas, peníze, brýle, telefon na stole – nemá
nic společného s Albánií konkrétně; totéž riziko hrozí u každé další auto-vygenerované fotky). Druhý
problém je vážnější, protože se netýká jen Canvy – týká se **jakéhokoli** nástroje, který si fotku
vybere nebo vygeneruje sám bez cíleného zadání.

Moje doporučení: rozdělit fotky v celém průvodci na dvě kategorie, ke kterým se chováte úplně jinak –
**místopisné** (reálná pojmenovaná místa z textu – pláž, hora, historické centrum) se **nikdy
negenerují AI**, ale kupují/licencují jako skutečný stock cíleně dohledaný pro dané místo; **náladové/
generické** (flat-lay rekvizit, detail jídla bez vazby na konkrétní podnik, ikonky, textury) se naopak
klidně generují AI, protože tam žádná faktická přesnost nehrozí a získáte přesnou kontrolu nad stylem
a paletou. Tohle rozdělení řeší kořen problému, který se na kapitole 1 projevil, a je nezávislé na tom,
který konkrétní nástroj nakonec použijete pro sazbu.

K tomu doporučuju **oddělit wireframe od sazby** – nejdřív pevně definovat, kam přesně fotka a text na
stránce padnou (bezpečné zóny pro délku textu, přesný poměr stran fotky), a teprve do hotové kostry
dosazovat konkrétní materiál. Přetečení textu a kolize boxů na proofu kapitoly 1 vznikly přesně proto,
že se stalo naopak – layout vygenerovala Canva sama k neznámému textu a pak se muselo ručně dolaďovat.

## 1. Co přesně na dosavadním výstupu nefunguje

Z `docs/design-brief-albanie.md` a vizuální kontroly `design/albanie/proof-v2/`:

Obálka (`cover-p1.png`) je ve skutečnosti v pořádku – skutečná fotka albánského pobřeží, čitelný serif
nadpis, teplá paleta. Tam Canva `poster` generování zafungovalo, protože obálka je jedna jasně
zadaná věc ("fotka albánského pobřeží + název") a kandidátů šlo vizuálně vybrat.

Hero strana kapitoly 1 (`fresh-p1.png`) má tři samostatné problémy:

Fotka je generický "cestovatelský flat-lay" (pas, eura, sluneční brýle, telefon na dřevěném stole) –
mohla by být z jakéhokoli průvodce na světě, s Albánií ji spojuje jen podpis. Pro kapitolu "Praktické
základy" to technicky sedí tematicky (doklady, peníze), ale nepůsobí to jako průvodce postavený na
reálné destinaci, což je přesně to, co má odlišovat prémiový produkt od genericého PDF.

Text úvodního odstavce zasahuje pod horní hranu obou barevných boxů (vidět i na čerstvém exportu) –
podle briefu to bylo řešeno posunem boxů o 80 px, ne úpravou textového rámu, což je záplata na
symptom, ne na příčinu (rámeček neměl od začátku definovanou pevnou výšku vůči délce textu).

Terakotový "Pozor" box má znatelně širší rozestupy mezi písmeny než olivový "Insider tip" box vedle
něj – podle briefu jde o tvrdý limit nástroje (`format_text` nemá parametr pro tracking/letter-spacing
a font se nedá přes API měnit), zdědilo se to z přebytečného patičkového textového pole, které bylo
napůl narychlo přetvořené na obsah boxu.

Společný jmenovatel všech tří: **layout a obsah vznikaly najednou, automaticky, bez kontroly předem**
nad tím, jak dlouhý bude text, jaká přesně bude fotka, a jaké textové elementy má šablona k dispozici.
Wireframe-first proces to řeší strukturálně, ne záplatami po vygenerování.

## 2. Nástroje, které máte k dispozici – aktuální stav (červenec 2026)

| Nástroj | Nejlepší využití v tomto projektu | Na co si dát pozor |
|---|---|---|
| **Claude Design / visualize** (tenhle chat) | Wireframe stránky – HTML/SVG mockup s přesnými rozměry, text-safe zónami a placeholder rámečky pro fotky, než se cokoli řeší v Canvě. Umím i navrhnout rozložení opakujících se prvků (insider tip, pozor box) tak, aby se nikdy nepřekrývaly bez ohledu na délku textu. | Nejde jím exportovat hotový PDF ani nahrávat fotky do Canvy – je to čistě návrhová/kontrolní vrstva před sazbou. |
| **Gemini Nano Banana Pro** (Gemini 3 Pro Image) | Generický/náladový obsah: flat-lay rekvizity, detail jídla bez vazby na konkrétní podnik, textury, ikonky. Aktuálně nejlepší fotorealismus ze srovnávaných nástrojů a umí si při generování "podepřít" konkrétní motiv vyhledáváním na webu, takže riziko úplně smyšlené scény je nižší než u staršího Nano Banana. | I s webovým groundingem jde o AI odhad, ne fotografii – pro pojmenovaná místa v textu (Berat, Modré oko, konkrétní pláž) bych to nepoužíval jako hlavní zdroj, jen jako záložní variantu, pokud reálná fotka daného místa není k sehnání. |
| **ChatGPT Images 2.0 (GPT Image 2, ChatGPT Pro)** | Série vzájemně konzistentních generovaných obrázků v jednom promptu (až 8 najednou se zachovanou kontinuitou stylu/rekvizit/světla) – ideální na sadu ikon nebo food-detailů, které mají vypadat, jako by vznikly na jednom "focení". Také nejlepší ze srovnávaných nástrojů na text uvnitř obrázku (např. ručně psané "cestovatelské" popisky na fotce). | Slabší přímá znalost konkrétního geografického místa než Nano Banana Pro – pro generický/náladový obsah je to jedno, pro místopisný obsah bych to nepoužíval vůbec. |
| **Canva Plus (Magic Media + editor)** | Finální sazba a export: brand kit pro konzistentní barvy/fonty napříč kapitolami, ruční umístění hotových fotek do připravených rámečků, PDF export. Magic Media uvnitř Canvy je fajn na rychlé zaplnění malého detailu, ale recenze ho řadí za Nano Banana Pro / Midjourney na fotorealismu a obličejích. | MCP (automatizované) API má prokázané tvrdé limity – needitovatelná hero sekce u `doc` typu, `merge-designs` nefunguje na unbounded designy, `format_text` nemá tracking. Řešení: fotky a text se do Canvy vkládají **ručně v editoru** podle hotového wireframu, ne přes plně automatické `generate-design`. |

Zdroje k aktuálnímu stavu nástrojů: [Nano Banana Pro – Google DeepMind](https://blog.google/innovation-and-ai/products/nano-banana-pro/), [Nano Banana 2 – Gemini image generation](https://gemini.google/overview/image-generation/), [ChatGPT Images 2.0 – OpenAI](https://openai.com/index/introducing-chatgpt-images-2-0/), [Canva Magic Media – Help Center](https://www.canva.com/help/using-magic-media/), [Canva AI 2026 přehled funkcí](https://pasqualepillitteri.it/en/news/601/canva-ai-magic-studio-guide).

## 3. Doporučený proces (na kapitolu)

Prvně shot list, pak wireframe, teprve pak materiál – v tomto pořadí, ne obráceně:

**Krok 1 – shot list z textu.** Pro každou kapitolu vypsat ze schváleného textu (`../01-tvorba-textu/content/<destinace>/text/*.md`) konkrétní seznam potřebných fotek se štítkem kategorie: místopisná (konkrétní pojmenované místo) vs. náladová (cokoli generické). U kapitoly 1 Albánie by to bylo např. "hero: cokoli náladové (doklady/cestování)" = náladová, ale u kapitoly "Regiony a itineráře" už by šlo o "Berat – kamenné domy nad řekou Osum" = místopisná.

**Krok 2 – wireframe stránky.** Než existuje jediná finální fotka, postavit prázdnou kostru stránky (přesný poměr stran fotky, maximální počet znaků pro každý textový blok při dané velikosti písma, pevná vzájemná pozice boxů s dostatečnou rezervou) – to je přesně to, co jsem teď udělal jako demo níže. Tahle kostra se dá znovu použít pro všechny kapitoly stejného typu stránky (hero strana, čistě textová strana, stránka s tabulkou).

**Krok 3 – sourcing/generování podle kategorie.** Místopisné fotky: cílené hledání podle přesného názvu místa v placené stock knihovně (Adobe Stock/Shutterstock – viz licence níže), případně přímo poskytnuté vlastní fotky, pokud někdo v týmu v destinaci byl. Náladové fotky: generování v Nano Banana Pro nebo ChatGPT Images 2.0 s promptem, který cíleně necílí na konkrétní reálné místo, a s barevnou paletou briefu v promptu (krémová `#F3ECE0`, terakotová `#C1502E`, olivová `#6B7A3A`).

**Krok 4 – ruční sazba v Canvě.** Do wireframu z kroku 2 (převedeného na Canva šablonu) se fotky a text vkládají ručně přes editor, ne přes `generate-design` na celou stránku najednou – tím padá důvod, proč vznikaly needitovatelné hero sekce a nekonzistentní tracking.

**Krok 5 – QA průchod.** Před exportem kapitoly zkontrolovat tři věci zvlášť: (a) sedí každá místopisná fotka fakticky na popsané místo, (b) nikde nepřetéká text mimo svůj rámeček, (c) žádný box/nadpis nemá zbytkové artefakty ze šablony (anglický text, cizí ikony, nekonzistentní rozestupy).

## 4. Tři varianty – upřímně, s kompromisy

**Varianta A – pokračovat v automatizaci přes Canva MCP** (např. zkusit `generate-design-structured`
nebo `search-brand-templates`, jak plán briefu naznačoval). *Nedoporučuju.* Dosavadní proof už narazil
na zdokumentované tvrdé limity (needitovatelná hero sekce, chybějící tracking parametr) a nejde o
náhodu jednoho pokusu – je to vlastnost typu designu, ne prompt, který by šlo doladit. I kdyby se
podařilo najít typ designu bez těchto konkrétních limitů, problém generických/nesouvisejících fotek
zůstává, protože je to důsledek toho, že si nástroj fotku vybírá sám bez cíleného zadání pro dané
místo.

**Varianta B – hybridní proces popsaný výše (doporučuju).** Wireframe odděleně od sazby, místopisné
fotky jako skutečný cílený stock, náladové fotky jako AI generace, finální sazba ručně v Canva Plus
editoru. Nejvyváženější poměr kvalita/čas – většina automatizace (wireframe, generování náladových
fotek, psaní textu) zůstává rychlá, ruční práce se soustředí jen tam, kde na ní záleží (výběr
místopisné fotky, finální vizuální polish v Canvě). Tohle přesně odpovídá směru, který už je
naznačený v `docs/project-split-plan.md` (wireframe → Nano Banana fotky nahrané člověkem → assembly
v Canvě) – tenhle brief ho jen rozpracovává do konkrétního postupu a přidává rozlišení
místopisné/náladové fotky, které v původní poznámce chybělo.

**Varianta C – opustit Canvu a udělat sazbu ručně v opravdovém DTP nástroji** (Affinity Publisher,
Adobe InDesign) s master stránkami postavenými na stejném wireframu. Nejvyšší dosažitelný strop
kvality – skutečná kontrola nad trackingem, vodicími linkami, tiskovým PDF/X exportem – ale bez
možnosti, aby cokoli automatizoval tenhle chat (nejde ovládat DTP nástroj přes MCP) a s výrazně delší
křivkou učení, pokud v takovém nástroji nemáte zkušenost. Dává smysl jako další krok, pokud po
zkušenosti s variantou B zjistíte, že vás pořád limituje typografická kontrola v Canvě (např. právě
ten neopravitelný tracking) – ne jako startovní bod.

## 5. Licencování fotek – protože se produkt prodává

Protože jde o placený produkt (viz `../03-komercializace/`), bych se u místopisných fotek vyhnul čistě
volným CC0 zdrojům (Unsplash, Pixabay) jako hlavnímu zdroji – jsou zdarma přesně proto, že je může
použít kdokoli, takže hrozí, že stejnou fotku pláže uvidí zákazník i v deseti jiných blozích, což
nepůsobí prémiově. Pro placený produkt dává větší smysl standardní licence z Adobe Stock nebo
Shutterstock (obě běžně pokrývají e-booky/digitální publikace v základní komerční licenci) – nejde o
velký náklad na fotku a odlišuje to vzhled od zdarma dostupných zdrojů. U AI generovaných (náladových)
fotek žádná licence třetí strany nehrozí, ale stojí za to mít v `docs/design-brief-<destinace>.md`
poznámku, čím byla fotka vytvořená, pro budoucí konzistenci.

## 6. Demo wireframe

Postavil jsem konkrétní ukázku – opravenou verzi hero strany kapitoly 1 (ta s přetékajícím textem a
kolidujícími boxy) jako wireframe s vyznačenými bezpečnými zónami. Zobrazený v konverzaci a uložený
jako `design/albanie/wireframes/ch01-hero-wireframe.svg`. Princip: fotka má pevný rámeček nahoře
(místo, kam patří místopisná NEBO náladová fotka podle kroku 1), úvodní text má vyznačený maximální
bezpečný prostor s rezervou, a oba boxy (insider tip / pozor) mají fixní odsazení od tohoto prostoru
bez ohledu na to, jak moc se text nakonec přiblíží limitu. Tohle je kostra, kterou by šlo v Canvě
znovu použít pro hero stranu každé další kapitoly každé destinace.

## 7. Co dál

Pokud varianta B dává smysl, dalším krokem by bylo: rozdělit fotky celé kapitoly 1 (nebo klidně celého
Albánie průvodce) na místopisné/náladové podle textu, postavit zbývající typy wireframu stránky
(čistě textová strana, strana s tabulkou rozpočtu), a teprve pak začít sourcing/generování skutečného
materiálu. Ráda bych věděla, jestli chcete jít touto cestou, než na to půjdu navázat.
