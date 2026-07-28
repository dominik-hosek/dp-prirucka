# Stav projektu

Jediné místo, kde je vidět, kde v procesu jsme a co je další krok. Aktualizuje se po každém
dokončeném kroku. Popis samotného procesu (co se v které fázi dělá) je v `plan.md`, sem patří
jen stav.

**Poslední aktualizace: 2026-07-28**

---

## 👉 Další kroky (v tomto pořadí)

1. **Znovu spustit fact-check na `01-tvorba-textu/content/lloret-de-mar/text/01-prakticke-zaklady.md`.** Kapitola byla
   upravená až po svém fact-checku (13:33 vs. 02:06), takže její záznam už neplatí pro aktuální
   znění. Zbylých 7 kapitol je ověřených a aktuálních.
2. **Doplnit `01-tvorba-textu/docs/open-questions-lloret-de-mar.md`** — soupis toho, co se
   v researchu Lloretu nepodařilo spolehlivě ověřit nebo si zdroje odporovaly. Pro Albánii takový
   soubor existuje a Fáze 4 (QA) z něj čerpá; pro pilot chybí, takže by se do QA vstupovalo bez
   seznamu rizikových tvrzení.
3. **Rozhodnout #1 níže** — bez něj se Fáze 3 nepohne a produkt nemůže vzniknout.

---

## Otevřená rozhodnutí (blokují postup)

### #1 — Jakým procesem vyrobit vizuální PDF? ⛔ blokuje celou Fázi 3

Dosavadní plně automatický postup přes Canva MCP je pozastavený (limity API + generické fotky,
které s destinací nemají nic společného). Tři varianty jsou rozepsané v
`02-tvorba-vizualu/docs/brief-vizualni-proces.md`:

| Varianta | Podstata | Poznámka |
|---|---|---|
| A | Dál automatizovat přes Canva MCP | Autor analýzy nedoporučuje — narazí na stejné limity |
| B | Hybrid: shot list → wireframe → fotky (reálná místa = placený stock, náladové = AI) → ruční sazba v Canvě | **Doporučeno** |
| C | Opustit Canvu, sázet v DTP nástroji (Affinity/InDesign) | Nejvyšší kvalita, nejde automatizovat |

Dokud rozhodnutí nepadne, v žádné variantě se nepokračuje.

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
| 2 | Psaní kapitol + fact-check | 01 | ◐ Lloret (8/8 `Stav: OK`, shot listy hotové; kapitola 01 upravená po fact-checku → potřebuje přeověřit) · ◐ Albánie (text opravený, ale fact-check nespuštěný znovu) |
| 3 | Vizuál a sazba PDF | 02 | ⛔ blokováno rozhodnutím #1 |
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
- **Fáze 1:** research hotový, 8 souborů, datum sběru 2026-07-17.
- **Fáze 2:** všech 8 kapitol napsaných a fact-checknutých na `Stav: OK`, shot listy vygenerované.
  Jediná výhrada: kapitola 01 byla po svém fact-checku ještě upravená, takže její záznam se
  nevztahuje k aktuálnímu znění — viz krok 1 nahoře.
- **Chybí:** `01-tvorba-textu/docs/open-questions-lloret-de-mar.md` (viz Další kroky), design brief pro Lloret
  (vizuální styl je společný a definovaný v `02-tvorba-vizualu/docs/design-brief-albanie.md` —
  pro Lloret stačí doplnit barevný akcent a fotky, až padne rozhodnutí #1).
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
