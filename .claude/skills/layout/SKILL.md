---
name: layout
description: Sazba průvodce do finálního PDF — mřížka, okraje, rytmus textu a obrazu, obsah, číslování stránek. Použij, když se z hotových kapitol a vygenerovaných assetů skládá výsledný PDF e-book, nebo když je potřeba upravit sazební pravidla. Naplňuje roli plánovaného skillu /layout-guide z Fáze 3.
---

# layout

Skládá kapitoly z `content/<slug>/text/` a assety z `content/<slug>/assets/` do
prodejného PDF. Sazební systém je destinačně nezávislý — mění se jen barevné
tokeny.

## Nástroj

**WeasyPrint** (HTML + CSS → PDF). Zvolen proto, že dává plnou kontrolu nad
stránkovou sazbou: `@page`, živá záhlaví přes `string-set`, čísla stránek
v obsahu přes `target-counter`, kontrola sirotků a vdov, dělení slov podle
českých pravidel.

```bash
pip install weasyprint
python -m weasyprint <vstup>.html <výstup>.pdf
```

## Soubory systému

```
design/
  fonts/                        Archivo, Source Serif 4, Inter (variabilní, v repu)
  templates/
    guide.css                   sazební systém — destinačně nezávislý
    tokens-<slug>.css           barvy jedné destinace
    page-skeleton.html          referenční kostra se všemi prvky
    make-placeholders.py        náhradní obrázky pro zkušební render
```

Pořadí linkování je závazné: **nejdřív tokeny, pak `guide.css`.**

## Mřížka a rozměry

| Veličina | Hodnota |
|---|---|
| Formát | A4 na výšku, 210 × 297 mm |
| Okraje | 22 mm nahoře, 20 mm dole, 18 mm po stranách |
| Vnitřní okraj (hřbet) | 22 mm — širší kvůli vazbě |
| Základní písmo | Source Serif 4, 10,5 pt / 1,58 |
| Sazební obrazec | jednosloupcový, ~174 mm široký |

Jednosloupcová sazba je záměr: průvodce se čte i na tabletu, kde dva sloupce
na A4 nutí ke skrolování nahoru a dolů.

## Režim obrazovky vs. tisku

Výchozí je **režim obrazovky** — produkt se prodává jako PDF e-book, takže se
nevynucují začátky kapitol na pravé stránce a nevznikají prázdné vakáty.

Pro tisk přidej na `<body>` třídu `rezim-tisk`: kapitoly, předěly a obsah pak
začínají vždy na liché stránce, jak se sluší na vazbu.

## Rytmus textu a obrazu

Průvodce nesmí být zeď textu ani fotoalbum. Držené pravidlo:

1. **Každá kapitola začíná předělem** — celostránkový obraz s číslem a názvem.
2. **Po předělu následuje textová stránka** s úvodním odstavcem (kapitálky na
   prvním řádku, bez odsazení).
3. **Maximálně 2 stránky souvislého textu za sebou.** Pak přijde obraz, mapa,
   tabulka nebo tipový box.
4. **Celostránkový obraz na spad** se používá 1× za kapitolu, jako oddech.
5. **Tipové boxy** rozbíjejí text průběžně — jsou nosnou hodnotou produktu,
   ne dekorací.

## Prvky sazby

Referenční použití všech prvků je v `design/templates/page-skeleton.html`.

| Třída | Účel |
|---|---|
| `.obalka` | obálka s nadtitulem, titulem a podtitulem |
| `.obsah` | obsah; čísla stránek se doplňují automaticky |
| `.predel` | předěl kapitoly — obraz + číslo + název |
| `.kapitola` | tělo kapitoly |
| `.tip` / `.tip.pozor` | insider tip / varování |
| `.fakta` | blok rychlých údajů (ceny, časy, vzdálenosti) |
| `figure.obraz-cela-strana` | celostránkový obraz na spad |
| `figure.obraz-pas` | pásový obraz přes šířku sazby |
| `figure.obraz-vpravo` | poloviční obraz s obtékáním |
| `.mapa` | mapa nebo infografika s legendou |
| `.tiraz` | tiráž s datem ověření údajů |

Prvek `.stin` uvnitř `.obalka` a `.predel` je ztmavovací přechod pod textem —
bez něj titulek na světlém obraze zmizí. Nevynechávej ho.

## Postup sazby

1. Ověř, že všechny assety mají v manifestu stav 🟢 (viz skill `illustration`).
2. Zkontroluj, že existuje `design/templates/tokens-<slug>.css`. Když ne, vytvoř
   ho podle profilu destinace v `guide-style/destinations/<slug>.md`.
3. Sestav `content/<slug>/<slug>.html` podle kostry — kapitoly v pořadí osnovy.
4. Vygeneruj PDF do `content/<slug>/<slug>.pdf`.
5. Projdi kontrolní seznam níže.

## Kontrolní seznam před vydáním

- [ ] Render proběhl **bez varování** WeasyPrintu.
- [ ] Žádná nechtěná prázdná stránka.
- [ ] Čísla stránek v obsahu odpovídají skutečnosti.
- [ ] Živé záhlaví ukazuje správnou kapitolu (ne zbytek předchozí).
- [ ] Žádný sirotek ani vdova, žádný nadpis na konci stránky bez textu.
- [ ] Diakritika všude správně — kontrolní věta *příliš žluťoučký kůň úpěl
      ďábelské ódy* se sází bez chyb a bez náhradních glyfů.
- [ ] Dělení slov nerozděluje slova nesmyslně.
- [ ] Všechny obrázky mají min. 300 DPI v cílové velikosti.
- [ ] Fonty jsou vložené v PDF (ověř `PyMuPDF`: `page.get_fonts()`).
- [ ] Tiráž obsahuje datum ověření údajů.

## Ověření hotového PDF

```python
import fitz
d = fitz.open("content/<slug>/<slug>.pdf")
print("stránek:", d.page_count)
print("fonty:", {f[3] for p in d for f in p.get_fonts(full=True)})
for i, p in enumerate(d):
    if not p.get_text().strip() and not p.get_images():
        print("PRÁZDNÁ STRÁNKA:", i + 1)
```

## Známá omezení WeasyPrintu

Zjištěno při stavbě systému — nepoužívej, tiše se ignorují:

- rozsah vah v `@font-face` (`font-weight: 100 900`) → řez se vybírá přes
  `font-variation-settings` u prvku
- `font-stretch` v procentech → přes `font-variation-settings: "wdth" …`
- `text-shadow` → nahrazeno přechodovou plochou `.stin`
- `aspect-ratio` → explicitní výška
- `hanging-punctuation`
- seskupené selektory `@page` (`@page :first, @page obalka { … }`) → každý zvlášť

## Výstup

Finální PDF patří do `content/<slug>/<slug>.pdf`. Podle konvence repa se
**negituje** (je v `.gitignore`) — zdrojem pravdy je text, assety a šablony,
PDF je build output. Kopie k doručení jde do `outputs/` (Fáze 5).
