# dp-prirucka

Produktová řada digitálních turistických průvodců (PDF e-booky s tipy a "deep knowledge"). Každá destinace = samostatný prodejný produkt. Prodej přes vlastní web + Meta/Google Ads.

Kompletní fázový proces (research → psaní → design → QA → prodej → PPC → škálování), včetně toho, co je automatizované skills/loops/MCP/hooks/agenty a co zůstává na člověku, je popsaný v plánu:
`C:\Users\42073\.claude\plans\chci-vytvo-it-digi-ln-produkt-rosy-yeti.md`

Živý přehled toho, co z automatizace už reálně existuje (vs. je jen naplánováno) a kde přesně leží, je v `docs/automation-registry.md` — tam se dívej, pokud potřebuješ najít konkrétní skill/agenta/hook/loop.

Aktuálně: pilot na 1 destinaci, PDF formát, obsah i data od nuly.

## Struktura repozitáře

```
content/
  _template/          # šablona struktury pro novou destinaci (research/text/assets)
  <destinace>/         # jedna složka = jedna destinace/produkt
    research/          # Fáze 1 – surová strukturovaná data (fakta, tipy, zdroje, datum ověření)
    text/               # Fáze 2 – hotové kapitoly průvodce (markdown)
    assets/             # Fáze 3 – obrázky/ilustrace použité v PDF

design/                # Fáze 3 – design šablony, brand kit reference (Canva), export skripty
landing-page/          # Fáze 5 – copy a struktura prodejní stránky
ads/                    # Fáze 6 – reklamní kreativy a texty pro Meta/Google Ads
docs/                   # Fáze 0/4/8/9 – briefy destinací, QA checklisty, pilot log, vyhodnocení
.claude/skills/         # projektové skills (research, psaní, QA, ads, evaluace pilotu...)
```

## Konvence

- `research/` je zdroj pravdy pro `text/` — kapitoly se píšou z dat, ne z volné paměti modelu (mitigace halucinací).
- Každý research záznam má zdroj a datum ověření (ceny/otevírací doby se mění).
- Nová destinace se zakládá zkopírováním `content/_template/`.
- Vygenerované binárky (PDF exporty, obrázky z designu) se negitují — zdroj pravdy je text + design zdroje, PDF je build output.
