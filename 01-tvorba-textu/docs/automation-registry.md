# Registr automatizace — Projekt 1: Tvorba textu (Fáze 0+1+2)

Živý přehled Skills a subagentů tohoto projektu. Celkový přehled napříč všemi 3 projekty je
v `../docs/project-split-plan.md` (root). Zdroj procesu: `../plan.md` (root, Fáze 0/1/2).

Legenda stavu: 🟢 vytvořeno · ⚪ naplánováno (zatím neexistuje)

## Přestavba 2026-08-06 — proč to vypadá jinak než dřív

Původní proces (8× research + 8× psaní + fact-check + taháček ≈ 32 běhů subagentů) stál zhruba
1,2 mil. tokenů na destinaci a **nevešel se do jednoho sezení** — sběr dat pro Krétu spadl na limitu
po třech z osmi kapitol.

První diagnóza zněla „žere to čtení webu" a **byla chybná**. Přestavěný proces vyrobil celou Krétu
při **nula voláních webu** — a přesto stál 460 tis. tokenů, protože každý z pěti běhů vyšel na
84–102 tis. bez ohledu na to, co dělal. Taháček přečte 17 KB textu a stojí 87 tis.

Skutečný vzorec je: **cena běhu ≈ počet volání nástrojů × velikost kontextu.** Při každém volání
nástroje se agentovi přeúčtuje celý dosavadní kontext, takže 18 volání × ~5 tis. ≈ 90 tis. Web to
jen zhoršoval, kořen to nebyl.

Páky podle síly: (1) míň běhů — každý má fixní režii ~80 tis.; (2) míň volání nástrojů v běhu —
dávat agentovi přesné cesty, ať nehledá; (3) kratší vstupy — definice agentů se přeposílají při
každém volání, proto jsou držené na ~2,5 KB.

Nový proces: **5 běhů, ~460 tis. tokenů na destinaci** (naměřeno na Krétě 2026-08-06).

| Co se změnilo | Z | Na |
|---|---|---|
| Běhů subagentů | ~32 | 5 |
| Sběr dat | 8 research souborů, ~240 volání webu | 1 `fakta.md`, strop 8 hledání + 5 stránek |
| Psaní | 8 běhů, agent s webem | 2 běhy po 4 kapitolách, agent **bez webových nástrojů** |
| Čísla v textu | přesné hodnoty | rozptyly + odkaz na oficiální zdroj |
| Kontrola | Fact-Checker subagent | **člověk** nad `kontrola.md` |
| Délka kapitoly | 2,4–5,4 KB | 2–3 KB |

**Co se tím vědomě obětovalo:** padla záruka „každá věta má zdroj". Nově ji má jen číselná a úřední
část textu (vrstva A z `fakta.md`); zbytek se píše z obecné znalosti modelu (vrstva B) a jeho
kontrola leží na člověku. Je to vědomý kompromis mezi cenou a doložitelností, ne přehlédnutí.

## Skills

Umístění: `.claude/skills/<název>/SKILL.md`

| Skill | Účel | Fáze | Stav |
|---|---|---|---|
| `/validate-destination` | Research poptávky/konkurence pro výběr destinace | 0 | ⚪ |
| `/destinace-text` | Celý text destinace ve 4 bězích — fakta, 8 kapitol, kontrolní list, taháček | 1+2 | 🟢 |
| `/tahacek` | Rychlotaháček do kapsy — 1stránkový destilát hotových kapitol | 2 | 🟢 |

## Subagenti

Umístění: `.claude/agents/<název>.md`

| Agent | Účel | Fáze | Stav |
|---|---|---|---|
| Market Research | Prohledá web, shrne poptávku/konkurenci/mezery na trhu | 0 | ⚪ |
| Fakta-Collector | JEDEN soubor tvrdých dat na celou destinaci. Tvrdý strop 8 hledání + 5 stránek. | 1 | 🟢 |
| Chapter-Writer | Píše kapitoly z `fakta.md` a obecné znalosti. **Bez webových nástrojů.** Dávkově 4 kapitoly. | 2 | 🟢 |
| Tahacek-Creator | Destiluje kapitoly do krátké verze na max. 1 A4. Dávkově 4 kapitoly. | 2 | 🟢 |

## Hooks

**Žádné.** Hook `fact-check-on-save.js` byl 2026-08-06 zrušen spolu s Fact-Checker agentem, kterého
volal. Sekvenci nově drží skill `/destinace-text`. Definice zmizely z `.claude/settings.json` tohoto
projektu i z `../.claude/settings.json` (root).

## Známá omezení

Většina vznikla za starého procesu, ale platí dál — jen je teď hlídá **člověk při kontrole**, ne
Fact-Checker.

- **Superlativy jsou u řadicích sekcí systémové riziko, ne náhoda.** Při doplňování žebříčků podle
  recenzí (2026-07-29, Lloret) byly 4 z 5 nálezů neopodstatněné superlativy vzniklé při psaní:
  „nejlepší v celém Lloretu", „nejlépe hodnocené s odstupem". Data byla správná, závěr o nich ne —
  vzorek nepokrýval celé město. U každé sekce, která něco řadí, kontroluj superlativy zvlášť.
- **Srovnávací obraty jsou skryté číselné tvrzení.** „Za zlomek peněz", „mnohonásobně dražší"
  vypadají jako stylistika, ale tvrdí poměr. Proto je `chapter-writer` má zakázané stejně jako čísla.
- **Záměna měn (EUR/USD) je jediná chyba, která v projektu vznikla dvakrát nezávisle na sobě** —
  u Lloretu i u Barcelony, obakrát přes ceníky eSIM uváděné v USD. Proto `fakta-collector` nikdy
  nepřevádí mlčky a zdroj v USD nechává v USD.
- **Zkracování do taháčku ubírá opatrnost dřív než fakta.** Při destilaci se snadno ztratí „ověř
  před cestou" a rozptyly cen (`od 10 €, až 23 €` → `10 €`) — a z opatrné formulace je rázem tvrdé
  tvrzení. S přechodem na rozptyly je tohle riziko **větší, ne menší**: rozptyl je teď hlavní forma
  ceny v textu. Kontroluj u každého taháčku zvlášť.
- **Rozsah taháčku se nedá měřit přes `wc -m` ani `awk length`.** Oboje tady vrací bajty, ne znaky,
  a české diakritice zabírá v UTF-8 dva bajty — délky vycházejí zhruba o třetinu vyšší (ověřeno
  2026-07-30: `printf 'ěščř' | wc -m` vrátí 8). Měř nástrojem, který UTF-8 umí (Node
  `[...text].length`).
- **Dlouhé zadání pro subagenta je nejdražší chyba, kterou lze udělat.** Přešvih 2026-08-06 vznikl
  tím, že každý research agent dostal ~600slovný nákupní seznam a odpracoval ho na 30 voláních webu
  a 34KB souboru — proti 3–7 KB u Lloretu, kde byla zadání krátká. Strop: **120 slov na zadání.**

## Loops

| Loop | Interval | Účel | Fáze | Stav |
|---|---|---|---|---|
| Revalidace cen/otevíracích dob | čtvrtletně | Kontrola, že vydaný obsah nezastarává | 1 / 8 | ⚪ |

Poznámka: s přechodem na rozptyly a odkazy je revalidace **výrazně méně naléhavá** — text neuvádí
hodnoty, které by se den ode dne rozcházely se skutečností.

## Výstup tohoto projektu

Ke každé kapitole **dvě verze textu**: dlouhá (2–3 KB) v `content/<destinace>/text/*.md` a krátká
(rychlotaháček, max. 1 A4) v `content/<destinace>/text/_tahacek/*.md`. Obojí je vstup pro Projekt 2;
taháček se sází jako samostatný produkt vedle příručky, ne jako její kapitola.

Navíc `content/<destinace>/kontrola.md` — vstup pro QA v Projektu 3 (Fáze 4), nahradil dřívější
`docs/open-questions-<destinace>.md`.

## Jak s tímto registrem pracovat

- Než se něco z výše uvedeného skutečně vytvoří, je to jen záměr (⚪) — neexistuje žádný soubor.
- Jakmile něco vznikne, změní se stav na 🟢 a doplní se poznámka, pokud se od návrhu odchýlí.
