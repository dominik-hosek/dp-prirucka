# Jak se vyrábějí stránky PDF

Ověřeno 2026-07-29 na obálce a kapitole 01 Lloretu. Nahrazuje Canva postup
(`design-brief-albanie.md`, `.claude/skills/layout-guide/`, `.claude/agents/design.md` — odstavené).

Vizuální styl definuje `design-brief-albanie.md` (paleta, typografie, opakující se prvky) a platí
dál. Tenhle dokument popisuje jen výrobu.

---

## Postup, který funguje

Stránky negeneruje agent — generuje je člověk v předplacených nástrojích. Agent dodává text
a kontrolní podklady.

| Co | Nástroj |
|---|---|
| Obálka a fotky | **Nano Banana 2** |
| Textové stránky kapitol | **GPT Image** |

### Zadání pro textové stránky (GPT Image)

Přílohy:
1. **4 vzorové inspirace** — konkrétně `design/inspirace/inspirace1.png` až `inspirace4.png`
   (ne starší sada `insp-1` až `insp-9`, ta sloužila pro Canva pokus)
2. **Zdrojový text** — hotová kapitola z Fáze 2 (`../01-tvorba-textu/content/<destinace>/text/`)

Prompt:

> Máš přiložené 4 vzorové inspirace. Podle délky, rozložení textu a možné grafiky se rozhodni,
> kterou použiješ.

To je celé. Model si rozvrh stránky zvolí sám podle toho, kolik textu dostane — a dělá to dobře.
Nemá smysl mu layout předepisovat.

**Důležité:** drž se **stejných 4 inspirací** po celou destinaci. Když je vyměníš uprostřed, změní
se vzhled a kapitoly přestanou vypadat jako jedna kniha.

---

## Co model dělá dobře (ověřeno, nemusíš hlídat)

- **Českou diakritiku.** Napříč stovkami slov bez chyby — háčky, čárky, kroužky. Původní obava, že
  tohle bude problém, se nepotvrdila.
- **Typografii a paletu.** Drží krémové pozadí, terakotové nadpisy, olivové akcenty, serif nadpisy
  a bezpatkové tělo textu — bez toho, aby se to muselo v promptu vyjmenovávat.
- **Rozvržení stránky.** Sám vytváří „Rychlý přehled" boxy, tipové karty, číslované odznaky
  a ikonové pásy, a rozhoduje se rozumně podle délky textu.

---

## Co model dělá špatně — tohle hlídat musíš

Tady je veškerá zbývající práce. Nejde o překlepy, které praští do očí, ale o **tiché změny
obsahu**. Stránka vypadá hotově a chyba je vidět, až když ji čteš proti originálu.

Zjištěno na kapitole 01 (~600 slov, dvě změny):

1. **Zaměněná předložka.** „podnik **ve** Španělsku" → „podnik **se** Španělsku". Gramaticky špatně,
   ale v odstavci to oko přeskočí.
2. **Vypadlá věta.** Zmizelo „a hotovostí pořád projde víc než polovina plateb v kamenných
   obchodech" — zrovna údaj od Banco de España, kvůli kterému se dělal doplňkový research.

Ke stejné kategorii patří i **dokreslené nápisy na fotkách**: na fotce u chiringuita vznikla cedule
„CHIRINGUITO SA BOADELLA". Sa Boadella je reálná pláž v Lloretu, ale jestli takový podnik existuje,
nevíme — a research říká nejmenovat konkrétní chiringuita bez ověření z víc zdrojů.

---

## Kontrola stránky — než ji přijmeš

**Čti stránku vedle zdrojového textu, ne samotnou.** Bez porovnání se tyhle chyby nenajdou.

- [ ] **Věta po větě proti zdroji.** Nevypadl odstavec nebo jeho konec? Nezměnila se předložka,
      spojka, koncovka?
- [ ] **Čísla.** Ceny, teploty, časy, měna (EUR vs. USD) — model rád zaokrouhlí.
- [ ] **Opatrné formulace zůstaly.** „až kolem 23 EUR", „ověř si před cestou", „nenašli jsme
      spolehlivá data" — tohle jsou místa, která prošla fact-checkem a nesmí se z nich stát
      tvrzení najisto.
- [ ] **Nápisy a cedule na fotkách.** Žádný čitelný název konkrétního podniku, ulice nebo
      provozovny, pokud není ověřený. Generická cedule nebo žádná.
- [ ] **Sekce sedí** — počet, pořadí a nadpisy podle zdrojové kapitoly.
- [ ] **Nic anglicky** v patičce ani popiscích.

Když najdeš chybu v textu, **nech stránku přegenerovat**, neopravuj ji retušováním.

### Pozor na opravné běhy

Přegenerování kvůli jedné chybě je **nový hod kostkou pro celou stránku** — model nesází jen
opravované místo. Ověřeno na kapitole 01: oprava zaměněné předložky sice prošla, ale ve stejné větě
se zároveň slepilo doplňované znění do nesmyslu, takže druhý běh dopadl hůř než první.

Po opravě proto projdi celý odstavec kolem opravovaného místa, ne jen to slovo. A když se stejná
věta rozbije dvakrát po sobě, je rychlejší **zkrátit ji ve zdrojové kapitole** (a nechat znovu
fact-checknout) než ji dokola generovat — dlouhé věty s vloženou vedlejší větou a číslem jsou to,
na čem model klopýtá.

---

## Formát a ukládání

- Stránky na výšku, **stejný poměr stran u všech** — jinak bude PDF „skákat".
- Hotové stránky: `design/<destinace>/pages/<číslo>-<název>-pN.png`
- **Stránky se verzují do gitu.** Nejsou build output — stejný prompt podruhé vrátí jiný obrázek,
  takže schválená stránka je nenahraditelná.

---

## Postupuj po kapitolách

Nejdřív jedna kapitola celá, projít, teprve pak další. Kdyby se ukázalo, že něco ve vzhledu nesedí,
předěláváš pět stránek, ne čtyřicet.
