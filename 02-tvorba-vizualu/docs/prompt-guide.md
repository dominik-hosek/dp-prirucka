# Prompt guide — generování stránek PDF přes Nano Banana 2 / GPT Image

Rozhodnuto 2026-07-29. Nahrazuje dosavadní Canva MCP postup (viz `docs/design-brief-albanie.md`,
`.claude/skills/layout-guide/`, `.claude/agents/design.md` — všechno pozastavené).

**Jak to funguje:** já připravím prompty, ty je vkládáš do Nano Banana 2 nebo GPT Image (obojí máš
předplacené) a generuješ jednotlivé stránky. Hotové stránky se pak spojí do PDF.

Vizuální styl (paleta, typografie, opakující se prvky) se **nemění** — dál platí
`docs/design-brief-albanie.md`, mění se jen způsob výroby.

---

## Formát stránky

**2:3 na výšku, 2048 × 3072 px.** Není to A4 (ta má 1:1,41), ale pro čistě digitální produkt čtený
na mobilu a tabletu je 2:3 lepší — vyplní displej telefonu skoro přesně a nevznikají prázdné pruhy.
Všechny stránky musí mít stejný poměr, jinak bude PDF „skákat".

Pokud ti nástroj nabídne vyšší rozlišení při stejném poměru, ber ho — zmenšit jde vždycky.

---

## Styl blok (vlož před KAŽDÝ prompt)

Tohle je to, co drží všechny stránky pohromadě. Kopíruj beze změny, mění se až text pod ním.

```
STYLE (apply to every page, keep absolutely consistent across the whole series):
Editorial travel-guide page design, premium print magazine aesthetic. Warm, calm, uncluttered,
generous margins and white space. Flat matte print look — no glossy 3D, no heavy drop shadows,
no stock-photo collage feel.

Color palette (use exactly these):
- background: warm cream #F3ECE0
- body text: warm dark brown #3A2E27
- primary accent: terracotta #C1502E (headings, chapter numbers, "warning" cards)
- secondary accent: olive green #6B7A3A (tips, icon badges)
- card surface: off-white #FFFDF9

Typography: elegant high-contrast serif for headings (Playfair Display style), clean geometric
sans-serif for body text. Generous line spacing. Never use condensed or decorative display fonts
for body text.

Recurring elements: soft rounded-corner cards for tips and warnings, numbered circular badges in
olive or terracotta, thin dotted connector lines as decoration, simple line icons in a single
consistent stroke weight.

Page format: 2:3 portrait aspect ratio, 2048x3072 px, designed as one page of a printed guidebook.

NEVER include: watermarks, logos, page furniture in English, lorem ipsum, placeholder gibberish,
random letterforms, stock-photo watermarks, borders around the entire page.
```

---

## Dva druhy stránek — a proč na tom záleží

### Typ V — vizuální stránka (text generuj rovnou)

Obálka, otevírací strana kapitoly, infografika, ikonová stránka. Textu je málo (nadpis, pár slov,
čísla), takže riziko, že ho model zkomolí, je zvládnutelné — a hlavně to na první pohled poznáš.

### Typ T — textová stránka (text NEgeneruj)

Stránky s odstavci souvislé prózy. Tam se generuje **jen pozadí a rám s prázdnými plochami** a
skutečný text se vloží až potom (Canva, Word, Affinity — cokoli, kde jde psát).

**Proč:** obrázkové modely sázejí delší českou prózu s diakritikou nespolehlivě — komolí slova,
vynechávají háčky a čárky, občas vloží neexistující slovo. Tvoje kapitoly prošly čtyřmi koly
fact-checku; nechat je přepsat obrázkovým modelem znamená tu práci potichu zahodit. Navíc text
v obrázku nejde vyhledat, zkopírovat ani zvětšit na mobilu.

U každé stránky níže je proto napsané, jestli je typ **V** nebo **T**, a u typu T dostaneš dvě věci:
prompt na prázdný rám a k němu přesný text, který do něj patří.

---

## Který nástroj na co

| Potřebuješ | Použij | Proč |
|---|---|---|
| Fotografii reálné scény (pláž, ulice, autobus) | **Nano Banana 2** | Lepší fotorealismus a při generování si motiv podepře vyhledáváním, takže scéna méně „ujede" |
| Stránku s nadpisy a krátkými popisky | **GPT Image** | Zdaleka nejlepší ze všech na text uvnitř obrázku |
| Sadu ikon nebo prvků, které musí vypadat jednotně | **GPT Image** | Umí vygenerovat víc kusů v jednom promptu se zachovaným stylem |
| Infografiku s čísly | **GPT Image** | Čísla jsou text — platí totéž |
| Prázdný rám/pozadí bez textu (typ T) | Kterýkoli | Bez textu je to jedno, ber ten, co ti dá hezčí podklad |

---

## Postup na jednu stránku

1. Zkopíruj **styl blok** (nahoře) do nástroje.
2. Pod něj vlož **prompt konkrétní stránky** ze složky `prompts/<destinace>/`.
3. Vygeneruj 3–4 varianty, ne jednu — první nález bývá průměrný.
4. Projdi **kontrolní seznam** níže.
5. Vyber vítěze, ulož jako `design/<destinace>/pages/<číslo>-<název>.png`.
6. U stránek typu T vlož text podle přiloženého znění.

**Postupuj po jedné kapitole**, ne všechno najednou. Když se ukáže, že něco ve stylu nesedí,
předěláváš 5 stránek, ne 40.

---

## Kontrolní seznam — než stránku přijmeš

- [ ] **Text slovo po slovu.** Přečti každé slovo nahlas. Háčky, čárky, koncovky. Jediná chyba =
      generuj znovu, neopravuj to ručně přemalováním.
- [ ] **Čísla sedí na text kapitoly.** Model si rád „zaokrouhlí" cenu nebo teplotu.
- [ ] **Paleta odpovídá.** Žádná stránka nesmí být studeně bílá ani mít cizí barvu navíc.
- [ ] **Nic anglicky.** Modely rády propašují anglické slovo do patičky nebo popisku.
- [ ] **Poměr stran 2:3** a stejná velikost jako ostatní stránky.
- [ ] **Žádné vymyšlené logo, cedule s nesmyslným nápisem, zdvojené prsty na rukou.**

---

## Jedno riziko, které prompt nevyřeší

U fotek **konkrétních pojmenovaných míst** (Cala Boadella, Fenals, hrad Sant Joan, Tossa de Mar)
platí, že model vygeneruje *věrohodně vypadající, ale smyšlené* místo. Nebude to ta zátoka.
Pro placený produkt, který slibuje „deep knowledge", je to slabina — a je to přesně ten problém,
na kterém ztroskotal předchozí pokus s Albánií.

Praktické řešení: u pojmenovaných míst buď použij licencovanou fotku (Adobe Stock, Shutterstock),
nebo místo v popisku **nepojmenovávej** a nech fotku fungovat jako náladovou. Generické scény
(pláž obecně, detail jídla, rekvizity, ikony) tímhle netrpí — tam AI generování problém nemá.

Prompty níže jsou proto psané tak, aby si nevymýšlely konkrétní identifikovatelná místa, pokud to
není výslovně napsané.
