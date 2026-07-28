---
name: map-infographic
description: Vyrábí mapy, itinerářové schémata a infografiky s přesným českým textem. Použij, když průvodce potřebuje mapu regionu nebo trasy, rozpočtovou tabulku, časovou osu itineráře nebo srovnávací grafiku. Text se do nich nikdy negeneruje obrázkovým modelem — sází se jako skutečná vektorová typografie.
---

# map-infographic

Mapy a infografiky jsou jediná část průvodce, kde na obrázku **musí** být text —
a zároveň je to místo, kde generátory obrázků selhávají nejvíc. Česká diakritika
se v generovaných obrázcích komolí prakticky vždy (`Camí de Ronda` → `Cami de
Roncla`, `Zátoka` → `Zátaka`), a chyba v mapě je v placeném produktu neomluvitelná.

## Základní princip: rozděl obraz a text

**Nikdy negeneruj text obrázkovým modelem.** Každá mapa a infografika se skládá
ze dvou vrstev:

| Vrstva | Čím se dělá | Co obsahuje |
|---|---|---|
| **Podklad** | generátor obrázků nebo vektorová kresba | terén, moře, pobřeží, textura, ilustrativní prvky |
| **Popisky** | HTML/SVG se skutečnými fonty | všechny názvy, čísla, legenda, měřítko, popisky bodů |

Výsledek se skládá až v sazbě (`layout`), takže text v PDF zůstane **ostrý,
vyhledatelný a s korektní diakritikou**. Zároveň jde opravit překlep bez
přegenerování obrázku.

## Typy výstupů

### 1. Přehledová mapa regionu

- Podklad: stylizovaná mapa bez popisků (pobřeží, terén, zeleň) v paletě destinace.
- Popisky: názvy míst, značky bodů zájmu, měřítko, směrovka.
- Prompt pro podklad používá 5-komponentovou formuli, ale v komponentě SUBJECT
  se výslovně říká **„mapa bez jakýchkoli popisků a názvů"**.

### 2. Mapa trasy / itineráře

- Podklad jako výše, navíc vyznačená linie trasy.
- Popisky: čísla zastávek, názvy, vzdálenosti, převýšení.
- Trasu kresli **vektorově v SVG**, ne generátorem — musí přesně sedět na body.

### 3. Infografika (rozpočet, časová osa, srovnání)

- **Žádný generovaný podklad.** Dělá se celá vektorově v HTML/SVG z palety
  a fontů destinace. Generátor obrázků tu nemá co dělat.
- Pravidla vizualizace dat: jedna barva = jeden význam napříč celým průvodcem,
  žádné 3D, žádné koláčové grafy s víc než 4 díly, popisky přímo u dat místo
  legendy, kde to jde.

## Struktura souborů

```
content/<slug>/assets/maps/
  NN-nazev/
    prompt.md          prompt pro podklad (jen u map s generovaným podkladem)
    podklad.png        vygenerovaný nebo kreslený podklad
    popisky.svg        vrstva s texty a body
    NN-nazev.html      složená mapa pro sazbu
    data.md            zdroj pravdy pro texty a souřadnice
```

`data.md` je důležitý: obsahuje **seznam všech popisků a jejich pozic**. Z něj se
generuje SVG a proti němu kontroluje `text-qa`. Nikdy nepiš texty přímo do SVG
bez záznamu v `data.md`.

## Typografie v mapách

Podle `guide-style`:

- **Inter** pro všechny popisky — je čitelný i v 7 pt a má plnou diakritiku.
- Názvy míst: 9–11 pt, 600, barva Text (`#1C2321`).
- Vodní plochy: 9 pt, 400, kurzíva, barva Primární.
- Čísla zastávek: v kolečku, 8 pt, 700, na akcentní barvě.
- Legenda a měřítko: 7–8 pt, 400.
- **Popisek nikdy nesmí přeběhnout přes hranu nebo přes jiný popisek.**
  Když se nevejde, přesuň bod, ne velikost písma.

## Kontrola přesnosti

Než se mapa označí za hotovou:

1. **Diakritika** — každý popisek znak po znaku proti `data.md`. Dělá `text-qa`.
2. **Geografie** — sedí vzájemná poloha bodů? Mapa nemusí být kartograficky
   přesná, ale nesmí být zavádějící (zátoka na špatné straně mysu je chyba).
3. **Úplnost** — jsou na mapě všechny orientační body vyžadované profilem destinace?
4. **Čitelnost** — otevři výstup ve 100 % velikosti A4. Co není čitelné na papíře,
   není čitelné.
5. **Podklad neobsahuje žádný generovaný text** — pokud model přesto nějaký
   protlačil, podklad jde přegenerovat.

## Když podklad opravdu musí mít text

Výjimečně (stylizovaná dobová mapa, cedule jako součást scény) může být text
součástí obrazu. Pak:

- generuj přes model s nejlepší podporou diakritiky (GPT Image 2),
- text drž na minimu a v krátkých slovech,
- **vždy** protáhni `text-qa`,
- počítej s několika pokusy; když se po třech nepovede, přepni na vektorovou vrstvu.
