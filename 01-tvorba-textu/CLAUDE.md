# 01-tvorba-textu

Projekt 1 ze 3 (viz `../docs/project-split-plan.md` v rootu `dp-prirucka`) — pokrývá Fáze 0, 1 a 2
celého procesu tvorby digitálního turistického průvodce: výběr/validace destinace, research
"deep knowledge" dat a psaní kapitol. Tento kus procesu funguje dobře a je referenční pro to, jak
by měly fungovat i další dva projekty.

**Výstupem každé kapitoly jsou vždy dvě verze textu, ne jedna:**

| Verze | Kde | Co to je |
|---|---|---|
| **dlouhá** | `content/<destinace>/text/<kapitola>.md` | plná kapitola příručky, 2–3 KB |
| **krátká** | `content/<destinace>/text/_tahacek/<kapitola>.md` | destilát pro rychlotaháček, max. 1 strana A4 |

Krátká verze se vždy odvozuje z dlouhé, nikdy nevzniká samostatně — a nesmí obsahovat nic, co
v dlouhé není. Kapitola se považuje za hotovou, teprve když má obě.

Celý fázový proces je popsaný v `../plan.md`. Živý stav skills/agentů/hooků/loopů patřících sem je
v `docs/automation-registry.md`.

## Struktura

```
content/
  _template/                   # šablona pro novou destinaci (jen research+text, assets jsou v Projektu 2)
    README.md                  # postup založení nové destinace
  <destinace>/
    fakta.md                   # Fáze 1 – JEDEN soubor tvrdých dat na celou destinaci (max. 150 řádků)
    kontrola.md                # seznam k ruční kontrole člověkem (sekce A čísla, sekce B znalost)
    text/                      # Fáze 2 – hotové kapitoly, 2–3 KB každá
    text/_tahacek/             # krátká verze – rychlotaháček (1 A4 na kapitolu), z Tahacek-Creator agenta
docs/
  brief-<destinace>.md             # Fáze 0 výstup – persona, cena, osnova, rozsah produktu
  style-guide.md                   # tone-of-voice a šablona kapitoly, platí napříč destinacemi
  metodika-hodnoceni.md            # jak se vybírají jmenované podniky podle recenzí, platí napříč destinacemi
.claude/
  agents/                      # fakta-collector, chapter-writer, tahacek-creator
  skills/                      # destinace-text, tahacek
```

## Konvence

- **Tokeny nežerou agenti ani psaní — žere je čtení webu.** Jedno načtení stránky je 5–15 tis.
  tokenů. Celý proces je postavený tak, aby se web četl **jednou na destinaci** pod tvrdým stropem
  (8 hledání + 5 stránek), ne jednou na kapitolu. Viz `/destinace-text`.
- **Text stojí na dvou vrstvách a je potřeba vědět, ve které se zrovna píše.** Vrstva A jsou tvrdá
  data (čísla, ceny, úřední informace) — ta pocházejí **výhradně z `fakta.md`**. Vrstva B je
  stabilní znalost destinace (charakter místa, jak se rozhodovat, kulturní kontext) — ta se píše
  z obecné znalosti modelu.
- **Číslo, které není ve `fakta.md`, se do textu nesmí dostat v žádné podobě** — ani opsané slovy,
  ani schované ve srovnání („dvakrát dražší", „za zlomek ceny"). Srovnávací obrat je skryté číselné
  tvrzení.
- **Ceny se píšou jako rozptyly s odkazem na oficiální zdroj**, ne jako přesné hodnoty. Přesná čísla
  jsou drahá na sběr, rychle zastarají a byla zdrojem skoro všech nálezů ve fact-checku. Hodnota
  produktu je v rozhodovacích rámcích („jestli chceš X, zvol Y a počítej se Z"), ne ve výčtu cen.
- Nová destinace se zakládá zkopírováním `content/_template/` — postup v jeho `README.md`.
- **Kontrolu dělá člověk, ne agent.** `content/<destinace>/kontrola.md` je očíslovaný seznam
  k proklikání, **max. 30 položek na celou destinaci** (sekce A tvrdá čísla s odkazem + sekce B
  tvrzení z obecné znalosti, dohromady). Fact-checker agent byl zrušen 2026-08-06 — stál víc než
  celý zbytek procesu.
- **Když se dlouhá verze změní, krátká je tím zastaralá.** Neopravuj taháček ručně po kouskách —
  nech ho vytvořit znovu z upravené kapitoly, jinak se obě verze rozejdou.
- **Konkrétní podnik se smí jmenovat jen podle `docs/metodika-hodnoceni.md`** — dvě nezávislé
  platformy, prahy na počet recenzí, povinný dodatek v textu, že si výběr nikdo nezaplatil. Bez
  doložení metodikou se píšou typy a oblasti, ne jména. Dodatek musí přežít i do taháčku.
- **Rychlotaháček je destilát kapitoly, ne druhý text.** Tahacek-Creator čerpá výhradně z hotové
  kapitoly (ne z research souboru) a smí pouze ubírat a přeformulovávat — žádné nové číslo, jméno
  ani místo. Strop je 1 strana A4 (limity v `.claude/agents/tahacek-creator.md`). Nejrizikovější je,
  že se zkrácením ztratí opatrnost („ověř před cestou", rozptyly cen) nebo se zamění měna; obojí
  se kontroluje zvlášť.
- **Subagenty pouštěj dávkově, ne po jedné kapitole.** Chapter-Writer i Tahacek-Creator zvládnou
  v jednom běhu 4 kapitoly. Osm samostatných spuštění zaplatí tentýž vstupní kontext osmkrát.
- **Zadání pro subagenta drž do 120 slov.** Přešvih 2026-08-06 vznikl přesně tím, že každý agent
  dostal ~600slovný nákupní seznam a odpracoval ho na 30 voláních webu a 34KB souboru (proti
  3–7 KB u Lloretu). Osnovu si agent přečte v briefu sám — nevypisuj mu, co má hledat.
- **Drobnou opravu po ruční kontrole přepiš rovnou v kapitole.** Jedna změněná hodnota nepotřebuje
  nový běh agenta; ten by stál řádově víc než oprava sama.

## Napojení na ostatní projekty

- **Výstup pro Projekt 2** (`../02-tvorba-vizualu/`): obě verze textu — dlouhá v
  `content/<destinace>/text/*.md` a krátká v `content/<destinace>/text/_tahacek/*.md`. Dokud jsou
  projekty v jednom repu, Projekt 2 na tyto cesty odkazuje relativně; ani jedna verze se tu nikdy
  nepřepisuje kvůli sazbě.
- **Výstup pro Projekt 3** (`../03-komercializace/`): `content/<destinace>/kontrola.md` je vstup pro
  QA checklist (Fáze 4) — nahradil dřívější `docs/open-questions-<destinace>.md`.
  `docs/brief-<destinace>.md` (persona/cena) je vstup pro landing page a ads.
