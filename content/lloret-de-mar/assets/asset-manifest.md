# Manifest vizuálů — Lloret de Mar

Přehled obrazové série. Udržuje skill `illustration`.

Stavy: ⚪ čeká na vygenerování · 🟡 vygenerováno, nezkontrolováno · 🟢 schváleno · 🔴 vráceno k přegenerování

**Kotva série:** `01-cami-de-ronda-utes.png` — na ni se kotví každý další obrázek.

| # | Soubor | Kapitola | Formát | Poznámka | Stav |
|---|---|---|---|---|---|
| 00 | `cover/00-obalka.png` | obálka | 1:1.414 | volná plocha v horní třetině pro titulek | ⚪ |
| 01 | `illustrations/01-cami-de-ronda-utes.png` | 1 | 1:1.414 | **kotva série** — generovat jako první | ⚪ |

Shot list se doplní, jakmile bude hotová osnova kapitol v `content/lloret-de-mar/text/`.
Cílový rozsah: obálka + 8–12 celostránkových + 4–6 doplňkových.

## Postup v ručním režimu

1. Otevři prompt v `prompts/NN-<popis>.md`.
2. Vlož do appky Gemini (Nano Banana Pro), nastav poměr stran podle promptu.
3. U všeho kromě `01` přilož kotevní obrázek a použij kotvicí větu z promptu.
4. Stáhni výsledek jako `illustrations/NN-<popis>.png` — **stejné číslo i slug**.
5. Změň stav v tabulce na 🟡 a nech projít kontrolou konzistence.
