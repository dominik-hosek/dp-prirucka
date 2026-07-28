# Obálka — Lloret de Mar

Typ **V** (text se generuje). Nástroj: **GPT Image** — je jediný, kterému se dá věřit text na obálce.

## Název produktu — návrh k potvrzení

- **Hlavní název:** Lloret de Mar a okolí
- **Podnázev:** Chytrý průvodce pro ty, kdo si dovolenou plánují sami
- **Kicker (malý text nahoře):** Costa Brava · 2026

Vychází z persony „Nezávislý plánovač" a z diferenciace v `../../01-tvorba-textu/docs/brief-lloret-de-mar.md`
(vytěžit z destinace víc než jen hotel a pláž před ním). **Než začneš generovat, potvrď mi znění** —
přegenerovat obálku kvůli změněnému podtitulku je zbytečná práce.

---

## Prompt

Vlož před něj styl blok z `../../docs/prompt-guide.md`.

```
Front cover of a premium printed travel guidebook, 2:3 portrait.

Layout:
- Full-bleed photograph filling the upper two thirds: a warm Mediterranean coastal scene at golden
  hour — turquoise cove water, pine-covered cliffs dropping to the sea, a crescent of sand. Shot
  from an elevated viewpoint looking down and out to sea. Warm late-afternoon light. Do NOT depict a
  specific recognizable landmark; this is an evocative Costa Brava scene, not a documented place.
- The photograph's bottom edge curves gently into the cream area below.
- Lower third: flat warm cream #F3ECE0 with generous margins, carrying the title block.

Text on the cover, rendered EXACTLY as written, in Czech, with all diacritics correct:
- Small uppercase kicker above the title, letter-spaced, in olive green: "COSTA BRAVA · 2026"
- Main title in large elegant high-contrast serif, warm dark brown #3A2E27, two lines:
  "Lloret de Mar"
  "a okolí"
- Below it, a short terracotta #C1502E horizontal rule
- Subtitle in clean sans-serif, smaller, warm dark brown:
  "Chytrý průvodce pro ty, kdo si dovolenou plánují sami"

Typography must be impeccable — this is the first thing a paying customer sees. Czech diacritics
(í, á, é, ů, ý) must be correctly formed and consistent.

No logos, no watermarks, no author name, no publisher marks, no barcode, no English text anywhere.
```

## Kontrola po vygenerování

Kromě obecného seznamu z prompt guide zkontroluj hlavně:

- [ ] „okolí" má **í** s čárkou, ne i
- [ ] „plánují" má **á** i **í**
- [ ] Nikde nepřibylo slovo navíc (modely rády doplní „GUIDE", „TRAVEL", „2026" podruhé)
- [ ] Fotka nevypadá jako konkrétní slavné místo, které by šlo identifikovat a vyvrátit
