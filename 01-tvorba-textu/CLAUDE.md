# 01-tvorba-textu

Projekt 1 ze 3 (viz `../docs/project-split-plan.md` v rootu `dp-prirucka`) — pokrývá Fáze 0, 1 a 2
celého procesu tvorby digitálního turistického průvodce: výběr/validace destinace, research
"deep knowledge" dat a psaní kapitol. Tento kus procesu funguje dobře a je referenční pro to, jak
by měly fungovat i další dva projekty.

Celý fázový proces je popsaný v `../plan.md`. Živý stav skills/agentů/hooků/loopů patřících sem je
v `docs/automation-registry.md`.

## Struktura

```
content/
  _template/                   # šablona pro novou destinaci (jen research+text, assets jsou v Projektu 2)
    README.md                  # postup založení nové destinace
  <destinace>/
    research/                  # Fáze 1 – surová strukturovaná data (fakta, tipy, zdroje, datum ověření)
    text/                      # Fáze 2 – hotové fact-checked kapitoly (markdown)
    text/_fact-check/          # záznamy z Fact-Checker agenta
    text/_shot-list/           # shot listy vizuálů pro Projekt 2, z Shot-List-Creator agenta
docs/
  brief-<destinace>.md             # Fáze 0 výstup – persona, cena, osnova
  open-questions-<destinace>.md    # Fáze 1 výstup – co doověřit před vydáním (čte i Projekt 3 v QA)
  style-guide.md                   # tone-of-voice a šablona kapitoly, platí napříč destinacemi
.claude/
  agents/                      # researcher, writer, fact-checker, shot-list-creator
  skills/                      # research-topic, write-chapter
  hooks/                       # fact-check-on-save.js – navazuje fact-check a shot-list na uložení kapitoly
```

## Konvence

- `content/<destinace>/research/` je zdroj pravdy pro `content/<destinace>/text/` — kapitoly se
  píšou z dat, ne z volné paměti modelu (mitigace halucinací).
- Každý research záznam má zdroj a datum ověření (ceny/otevírací doby se mění).
- Nová destinace se zakládá zkopírováním `content/_template/` — postup v jeho `README.md`.
- **Kapitola je hotová až s `Stav: OK` ve fact-checku.** Nálezy z fact-checku se opravují v textu
  a fact-check se pouští znovu; nechat kapitolu ve stavu "NALEZENY PROBLÉMY" znamená, že destinace
  není připravená pro Projekt 2 (a shot listy se pro ni ani nevygenerují).
- Fact-checker běží nezávisle na Writeru — kontroluje tvrzení v textu zpět proti research datům.
- Shot-List-Creator běží nezávisle na Writeru i Fact-Checkerovi — čerpá výhradně z hotového textu
  kapitoly (ne z research souboru), aby shot list nikdy neobsahoval víc, než co se čtenář v
  kapitole skutečně dočte.
- Fact-check i navazující shot list se pro danou kapitolu/destinaci spouští automaticky po uložení
  souboru (hook `.claude/hooks/fact-check-on-save.js`), ne jen na ruční vyžádání — viz
  `docs/automation-registry.md`.

## Napojení na ostatní projekty

- **Výstup pro Projekt 2** (`../02-tvorba-vizualu/`): hotové kapitoly v `content/<destinace>/text/*.md`
  a k nim odpovídající shot listy v `content/<destinace>/text/_shot-list/*.md` (vznikají automaticky,
  jakmile jsou všechny kapitoly destinace fact-checked na `Stav: OK`). Dokud jsou projekty v jednom
  repu, Projekt 2 na tyto cesty odkazuje relativně; text ani shot list se tu nikdy nepřepisují kvůli
  vizuální sazbě.
- **Výstup pro Projekt 3** (`../03-komercializace/`): `docs/open-questions-<destinace>.md` je vstup
  pro QA checklist (Fáze 4), `docs/brief-<destinace>.md` (persona/cena) je vstup pro landing page
  a ads.
