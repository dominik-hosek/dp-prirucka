---
name: write-chapter
description: Napíše jednu kapitolu turistického průvodce z research dat dané destinace (nikdy z volné paměti modelu). Fáze 2 procesu. Volání: `/write-chapter <destinace> <kapitola>`.
---

# Psaní kapitoly průvodce

Cíl: proměnit strukturovaná research data (Fáze 1) v čtivou kapitolu v jednotném stylu produktové řady — bez přidávání faktů, které nejsou v podkladu.

## Postup

1. Přečti `docs/style-guide.md` (tone-of-voice, struktura, formát) — závazné pro každou kapitolu.
2. Přečti `docs/brief-<destinace>.md` pro personu a místo kapitoly v osnově.
3. Přečti odpovídající `content/<destinace>/research/<téma>.md` — to je JEDINÝ zdroj faktů. Pokud kapitola potřebuje info, které tam není, buď to vynech, nebo to explicitně označ jako nutné doověřit — nevymýšlej si to.
4. Napiš kapitolu podle šablony ze style guide, ulož do `content/<destinace>/text/<pořadové-číslo>-<téma-slug>.md`.
5. Otevřené otázky z research souboru (nejisté/rozporné údaje) promítni do textu jako opatrnou formulaci ("k létu 2026...", "ověř si před cestou"), ne jako tvrdé tvrzení.

## Návaznost

- Vstup: `docs/style-guide.md`, `docs/brief-<destinace>.md`, `content/<destinace>/research/*.md`.
- Výstup ověřuje: Fact-Checker agent (`.claude/agents/fact-checker.md`) — porovná kapitolu zpět proti research souboru a hlásí nepodložená tvrzení.
- Stav automatizace: `docs/automation-registry.md`.
