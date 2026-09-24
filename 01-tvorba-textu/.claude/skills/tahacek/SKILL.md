---
name: tahacek
description: Vytvoří nebo obnoví krátkou verzi kapitol — rychlotaháček do kapsy, max. 1 strana A4 na kapitolu, odvozený výhradně z hotové dlouhé verze. Fáze 2. Volání: `/tahacek <destinace>` pro celou destinaci nebo `/tahacek <destinace> <kapitola>` pro jednu.
---

# Krátká verze kapitol — rychlotaháček do kapsy

Každá kapitola má dvě verze: **dlouhou** (`content/<destinace>/text/<kapitola>.md`) a **krátkou**
(`content/<destinace>/text/_tahacek/<kapitola>.md`). Tenhle skill vyrábí a udržuje tu krátkou.

Krátká verze je destilát, ne druhý text — jen to, co se rozhoduje na místě (čísla, směry, otevírací
doby, rozhodovací pravidla). Nesmí obsahovat nic, co v dlouhé verzi není.

## Předpoklad

Kapitola musí existovat v `content/<destinace>/text/<kapitola>.md` (napsaná chapter-writerem).
Samostatný fact-check gate od 2026-08-06 neexistuje — kontrolu dělá člověk nad `kontrola.md`, ne
agent před vydáním. Z toho plyne jediné riziko: když člověk po kontrole kapitolu opraví, existující
taháček je tím zastaralý a musí se vyrobit znovu (viz krok 3 níže) — nekontroluj tedy „je hotovo",
ale „je aktuální".

## Postup

1. **Zjisti, co je rozsypané.** Projdi `content/<destinace>/text/*.md` a porovnej s `_tahacek/`:
   chybí krátká verze, nebo je její soubor starší než dlouhá verze? To jsou kapitoly ke zpracování.
   Bez argumentu `<kapitola>` ber všechny takové, s argumentem jen zadanou.
2. **Spusť Tahacek-Creator subagenta** (`.claude/agents/tahacek-creator.md`) **dávkově — po max.
   4 kapitolách na jeden běh**, ne po jedné. Každé spuštění subagenta se platí znovu, a přitom je
   práce nad jednou kapitolou krátká; osm samostatných běhů je proti dvěma dávkovým čistá ztráta.
   Agent čte jen dlouhé verze, ne research, a pro každou kapitolu zapíše samostatný soubor.
3. **Neopravuj existující taháček po kouskách.** Když se kapitola změnila, nech krátkou verzi
   vytvořit znovu celou — jinak se obě verze pomalu rozejdou.
4. Zkontroluj výsledek **jedním průchodem přes celou destinaci** (skript níže), ne po kapitolách.
   Co je přes strop, nech přepsat znovu s pokynem, co vypustit — a i tyhle opravy shlukni do jedné
   dávky.

## Kontrola

Zkracování neztrácí fakta, ale **ztrácí opatrnost** — z „od 10 €, podle dopravce až 23 €" se snadno
stane „10 €" a z poctivé výhrady je rázem tvrdé tvrzení. Projeď proto u každé krátké verze:

| Co | Jak |
|---|---|
| Rozsah | ≤ 1 900 znaků, ≤ 22 odrážek, ≤ 6 sekcí, ≤ 100 znaků na odrážku |
| Čísla | každé číslo v krátké verzi musí být i v dlouhé — žádné nové |
| Měny | co je v dlouhé verzi v USD, je v USD i v krátké |
| Opatrnost | „ověř před cestou", „orientačně", rozptyly cen musí přežít |
| Žebříčky | dodatek „nikdo si tady umístění nezaplatil" musí přežít (`docs/metodika-hodnoceni.md`) |

**Délku měř nástrojem, který umí UTF-8** (Node `[...text].length`). `wc -m` i `awk length` tady
vracejí bajty, a české diakritice zabírá dva — délky pak vyjdou zhruba o třetinu vyšší, než jsou.

Kontrolní průchod přes všechny kapitoly destinace najednou:

```bash
node -e 'const fs=require("fs"),p=require("path"),d=process.argv[1],t=p.join("01-tvorba-textu/content",d,"text");for(const f of fs.readdirSync(t).filter(f=>f.endsWith(".md")&&fs.statSync(p.join(t,f)).isFile()).sort()){const tp=p.join(t,"_tahacek",f);if(!fs.existsSync(tp)){console.log("CHYBI  "+f);continue}const src=fs.readFileSync(p.join(t,f),"utf8"),full=fs.readFileSync(tp,"utf8"),tah=full.split("\n").slice(1).join("\n"),bl=tah.split("\n").filter(l=>l.startsWith("- ")),e=[];if([...tah].length>1900)e.push("ZNAKY");if(bl.length>22)e.push("ODRAZKY");if(bl.some(l=>[...l].length>100))e.push("DELKA");const m=[...new Set(tah.match(/\d+(?:[.,]\d+)?/g)||[])].filter(n=>!src.includes(n));if(m.length)e.push("CISLA NAVIC: "+m.join(","));if(/USD/.test(src)&&!/USD/.test(tah))e.push("ZTRACENO USD");if(/ověř|orientačn|rozcház/i.test(src)&&!/ověř|orientačn|zkontroluj|mrkni|doptej/i.test(tah))e.push("ZTRACENA OPATRNOST");if(/nezaplatil/.test(src)&&!/nezaplatil/.test(tah))e.push("ZTRACEN DODATEK");console.log((e.length?"X  ":"ok ")+f+" "+e.join(" | "))}' <destinace>
```

## Návaznost

- Vstup: dlouhé verze `content/<destinace>/text/*.md`, pravidla pro žebříčky `docs/metodika-hodnoceni.md`.
- Výstup: `content/<destinace>/text/_tahacek/*.md` — vedle dlouhé verze druhý vstup pro Projekt 2.
  Taháček se sází jako samostatný produkt, ne jako kapitola příručky.
- Žádný hook to nespouští automaticky — `/destinace-text` zahrne taháček do své vlastní sekvence
  (poslední 1–2 běhy) a mimo ni se spouští ručně přes `/tahacek`. Detail v
  `docs/automation-registry.md`.
