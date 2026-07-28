# 5-komponentová promptová formule

Závazný způsob, jak se v tomhle projektu staví prompt pro generátor obrázků. Vychází z doporučené struktury Google pro Gemini image modely a je rozšířená o kontrolu značky.

## Komponenty

Prompt se vždy skládá v tomhle pořadí. Žádná komponenta se nevynechává — když k ní není co říct, doplní se výchozí hodnota z jádra `guide-style`.

| # | Komponenta | Co obsahuje | Odkud se bere |
|---|---|---|---|
| 1 | **Subject** | Co je na obrázku — konkrétní místo, objekt, děj | scéna z kapitoly + fotografický slovník destinace |
| 2 | **Composition** | Rámování, ohnisko, úhel, kam se dívá oko, kde je prázdné místo na text | typ assetu (obálka / celostrana / pás) |
| 3 | **Style** | Fotografický žánr, referenční estetika, grading | invarianty jádra + paleta destinace |
| 4 | **Lighting** | Denní doba, směr a kvalita světla, atmosféra | profil destinace (sezóna, světlo) |
| 5 | **Technical** | Poměr stran, rozlišení, hloubka ostrosti, zrno, negativní prompt | tabulka formátů v jádru + zákazy |

## Šablona

```
[SUBJECT] — <konkrétní scéna, místo, děj, roční doba>.
[COMPOSITION] — <ohnisko>, <úhel>, <rámování>, <kde je klidná plocha pro text>.
[STYLE] — <žánr>, barevný grading do <hex/slovní popis palety>, <referenční estetika>.
[LIGHTING] — <denní doba>, <směr světla>, <atmosféra>.
[TECHNICAL] — poměr <X:Y>, <hloubka ostrosti>, jemné filmové zrno.
NEGATIVE — <seznam zákazů>.
```

## Příklad (Lloret de Mar, celostránková ilustrace)

```
[SUBJECT] — Skalnatý výběžek pobřežní stezky Camí de Ronda nad skrytou zátokou
Cala Boadella, borovice nakloněné nad útesem, jediný turista s batohem daleko
v záběru jako měřítko, pozdní jaro.
[COMPOSITION] — 24 mm širokoúhlý objektiv, pohled z vyvýšeného bodu podél
pobřeží, stezka vede oko zleva dolů k zátoce, horní třetina je klidná obloha
a moře — volná plocha pro titulek.
[STYLE] — cestovatelská reportážní fotografie, barevný grading do hluboké
mořské modři #0E3A53 a tyrkysu #1B9AAA s korálovým akcentem #E76F51,
estetika magazínu Sidetracked, filmový kontrast se zavřenými stíny.
[LIGHTING] — zlatá hodina krátce před západem, boční světlo zprava, teplý
nádech na skále, moře v chladném kontrastu.
[TECHNICAL] — poměr 1:1.414 na výšku, velká hloubka ostrosti, jemné filmové zrno.
NEGATIVE — text, písmena, nápisy, watermark, logo, rozpoznatelné tváře,
lidé v popředí, stock estetika, přesycené barvy, HDR halo, koláž, rámeček,
davy turistů, párty, neón.
```

## Negativní prompt — výchozí sada

Kopíruj do každé generace, pak doplň zákazy z profilu destinace:

```
text, písmena, nápisy, cedule s textem, watermark, logo, podpis,
rozpoznatelné tváře, portrét, lidé v popředí,
stock photo estetika, přesycené barvy, HDR halo, plastová kůže,
koláž, více panelů, rámeček, okraj, ořezové značky,
deformované ruce, zdvojené horizonty, nelogická perspektiva
```

## Přizpůsobení podle modelu

Systém je psaný tak, aby fungoval bez ohledu na to, čím se obrázek nakonec vyrobí.

### Nano Banana Pro v appce Gemini (aktuální pilotní režim)

Ruční cesta — prompt se vkládá do appky, obrázek se stahuje zpět do repa.

- Appka nemá pole pro negativní prompt. Zákazy se proto formulují **pozitivně nebo jako věta na konci**: „Bez jakéhokoli textu, nápisů a log. Bez rozpoznatelných tváří."
- Poměr stran se v appce nastavuje volbou, ne v textu — vyber ho ručně podle komponenty TECHNICAL.
- **Konzistence série** se drží tak, že se k promptu **přiloží kotevní obrázek** (viz skill `illustration`) a dopíše se: „Zachovej stejný fotografický styl, grading a atmosféru jako v přiloženém obrázku."
- Generuj na 1K/2K, ne 4K.

### Gemini API / banana-claude (kdyby se přešlo na automatizaci)

- Negativní prompt jde do samostatného parametru.
- Poměr stran jako `aspect_ratio`.
- Kotva se předává jako referenční obrázek ve vstupu.

### GPT Image 2 (jen když je potřeba text v obrázku)

Používej **jen výjimečně** — v tomhle projektu text do obrázků nepatří, řeší ho `layout` jako skutečnou typografii. Kdyby přesto bylo potřeba (např. stylizovaná cedule jako součást scény), GPT Image 2 zvládá českou diakritiku nejlépe z dostupných modelů. Text pak vždy zkontroluj subagentem `text-qa`.

### Flux 2 Pro (kdyby bylo potřeba tvrdší brandová konzistence)

- Paletu předávej jako explicitní seznam hex kódů v komponentě STYLE.
- Drž stejný seed napříč sérií, měň jen komponentu SUBJECT.

## Časté chyby

- **Příliš dlouhý Subject.** Model rozmělní pozornost. Jedna scéna, jeden děj.
- **Chybějící klidná plocha.** Když se zapomene v Composition říct, kde bude text, titulek pak nemá kam sednout a obálka se musí předělat.
- **Míchání sezón.** Série, kde půl obrázků je letní a půl podzimní, se rozpadá — sezóna patří do profilu destinace a drží se.
- **Popis textu ve scéně.** Jakmile se v promptu objeví „cedule s nápisem…", model začne generovat zkomolená písmena. Takové prvky popisuj bez obsahu: „dřevěná směrovka".
