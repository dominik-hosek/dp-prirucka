# Stav projektu

Jediné místo, kde je vidět, kde v procesu jsme a co je další krok. Aktualizuje se po každém
dokončeném kroku. Popis samotného procesu (co se v které fázi dělá) je v `plan.md`, sem patří
jen stav.

**Poslední aktualizace: 2026-07-29**

---

## 👉 Další krok

**Vygenerovat obálku a 5 stránek kapitoly 01 Lloretu** podle promptů v
`02-tvorba-vizualu/prompts/lloret-de-mar/`. Postup, styl blok a kontrolní seznamy jsou
v `02-tvorba-vizualu/docs/prompt-guide.md`, prázdné šablony textových stránek
v `02-tvorba-vizualu/prompts/_sablony-stranek.md`.

Než se pojede dál, projít první kapitolu společně — když bude potřeba doladit styl nebo postup,
je lepší předělat 5 stránek než 40.

**Nejdřív ale dvě drobnosti:**
- Potvrdit název a podnázev produktu (návrh je v `prompts/lloret-de-mar/00-obalka.md`) — obálka se
  generuje s ním a přegenerovávat ji kvůli změněnému podtitulku je zbytečné.
- Ověřit si na jednom odstavci, jak si tvůj nástroj poradí s českou diakritikou — na tom stojí
  rozdělení stránek na vizuální a textové.

✅ *Hotovo 2026-07-28: přeověření kapitoly 01 Lloretu (viz Fáze 2 níže).*
✅ *Hotovo 2026-07-29: `01-tvorba-textu/docs/open-questions-lloret-de-mar.md` — 18 otevřených otázek
z 8 research souborů seskupených podle toho, co s nimi má udělat QA ve Fázi 4.*

---

## Otevřená rozhodnutí

### ✅ #1 — Jakým procesem vyrobit vizuální PDF? *(rozhodnuto 2026-07-29)*

Stránky generuje člověk v **Nano Banana 2 / GPT Image** podle promptů připravených agentem. Canva
se nepoužívá (skill i agent odstavené). Stránky se dělí na vizuální (text se generuje) a textové
(generuje se jen prázdný rám, fact-checked text se vkládá až potom) — důvod je nespolehlivá sazba
české diakritiky obrázkovými modely.

Detail: `02-tvorba-vizualu/docs/prompt-guide.md`. Rozhodnutí a jeho kontext:
`docs/project-split-plan.md`.

**Známé riziko, se kterým se do toho jde:** u fotek konkrétních pojmenovaných míst model vygeneruje
věrohodné, ale smyšlené místo. Řešení v prompt guide — buď licencovaná fotka, nebo místo
v popisku nepojmenovávat.

### #2 — Notion jako centrální databáze destinací? (neblokuje)

`plan.md` (technická příprava, bod 2) s ním počítá. Zatím nezaložený — repo pro dvě destinace
stačí. Rozhodnout, až bude destinací víc.

---

## Stav podle fází

Legenda: ✅ hotovo · ◐ rozpracováno · ⛔ blokováno · ⬜ nezačato

| Fáze | Co | Projekt | Stav |
|---|---|---|---|
| 0 | Validace destinace, persona, cena, osnova | 01 | ✅ pro Lloret i Albánii |
| 1 | Research "deep knowledge" dat | 01 | ✅ pro Lloret (8 témat) · ✅ pro Albánii |
| 2 | Psaní kapitol + fact-check | 01 | ✅ Lloret (8/8 `Stav: OK` a aktuální, 8/8 shot listů aktuálních) · ◐ Albánie (text opravený, ale fact-check nespuštěný znovu) |
| 3 | Vizuál a sazba PDF | 02 | ◐ postup rozhodnutý, prompty pro obálku + kap. 01 Lloretu hotové, generování nezačalo |
| 4 | QA a finalizace produktu | 03 | ⬜ čeká na PDF z Fáze 3 |
| 5 | Prodejní web | 03 | ⬜ |
| 6 | Příprava PPC kampaní | 03 | ⬜ |
| 7 | Spuštění a optimalizace PPC | 03 | ⬜ |
| 8 | Post-launch péče | 03 | ⬜ |
| 9 | Škálování na další destinace | 03 | ⬜ až po vyhodnocení pilotu |

---

## Destinace

Plán počítá s pilotem na jedné destinaci — další se rozjíždějí až po jeho vyhodnocení (Fáze 9).

### 🎯 Lloret de Mar a okolí — **aktuální pilot**

- **Fáze 0:** brief potvrzený (`01-tvorba-textu/docs/brief-lloret-de-mar.md`) — persona "Nezávislý
  plánovač", cena 199 Kč, osnova 8 kapitol.
- **Fáze 1:** research hotový, 8 souborů, datum sběru 2026-07-17. Sekce o penězích v
  `prakticke-zaklady.md` doplněná 2026-07-28 (karty vs. hotovost, chiringuita, limity).
- **Fáze 2:** hotovo — všech 8 kapitol má aktuální fact-check se `Stav: OK` i aktuální shot list.
  Kapitola 01 prošla 2026-07-28 přeověřením (4 kola: neshoda měny u eSIM, ztracená opatrnost u ceny
  autobusu z Girony, nepodložená tvrzení o placení kartou) — všechny nálezy opravené.
- **Otevřené otázky pro QA:** `01-tvorba-textu/docs/open-questions-lloret-de-mar.md` (2026-07-29).
  Pozor, sekce 1 (ceny dopravy, ubytování, vstupné) se má doověřovat **až těsně před vydáním**, ne
  dopředu — jinak čísla znovu zastarají.
- **Chybí:** design brief pro Lloret. Vizuální styl je společný a definovaný
  v `02-tvorba-vizualu/docs/design-brief-albanie.md` — pro Lloret stačí doplnit barevný akcent
  a fotky, až padne rozhodnutí #1.
- **Fáze 3 a dál:** nezačato.

### ❄️ Albánie — zmrazená

Původní pilotní destinace, research i všech 8 kapitol existuje.

**Blíž k hotovu, než vypadá.** Sedm z osmi fact-check záznamů sice hlásí `Stav: NALEZENY PROBLÉMY`,
ale nálezy už jsou v textu opravené (ověřeno namátkou u kapitol 4, 5 a 7 — sporné formulace jsou
přeformulované) — jen se pak fact-check nespustil znovu, takže záznamy zůstaly viset na starém
výsledku. Právě proto se nikdy nespustil ani Shot-List-Creator (ten čeká, až bude všech 8 na
`Stav: OK`) a destinace není formálně připravená pro Fázi 3.

Rozpracovaný vizuální proof (obálka + kapitola 1 v Canvě) je taky zmrazený — viz
`docs/project-split-plan.md`.

**Nerozšiřovat.** Až bude čas se k ní vrátit, stačí pravděpodobně přeověřit 7 kapitol
(`01-tvorba-textu/content/albanie/text/*.md`) — pokud vyjdou na `Stav: OK`, shot listy se
vygenerují samy a Albánie je na stejné startovní čáře jako Lloret.

---

## Co je z automatizace reálně postavené

Detail vždy v `<projekt>/docs/automation-registry.md`. Hrubý přehled:

- **Projekt 1:** funguje dobře — 2 skills (`/research-topic`, `/write-chapter`), 4 subagenti
  (researcher, writer, fact-checker, shot-list-creator), hook, který po uložení kapitoly hlídá
  fact-check a po dokončení destinace shot listy.
- **Projekt 2:** 1 skill + 1 agent, oba 🟡 pozastavené (popisují starý Canva postup).
- **Projekt 3:** nic — všech 6 skills a 4 subagenti jsou zatím jen záměr (⚪).
