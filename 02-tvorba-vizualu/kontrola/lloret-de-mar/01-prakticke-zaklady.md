# Kontrolní list — kapitola 01: Praktické základy

Zdroj: `../../../01-tvorba-textu/content/lloret-de-mar/text/01-prakticke-zaklady.md`

Postup generování je v `../../docs/prompt-guide.md`. Tenhle list slouží ke **kontrole vygenerovaných
stránek proti zdroji** — bez porovnání se tiché změny textu nenajdou.

## Sekce (počet, pořadí, nadpisy)

Kapitola má **6 podsekcí** v tomto pořadí:

1. Kdy jet
2. Doprava z letiště
3. Peníze
4. SIM a internet
5. Bezpečnost
6. Rychlé shrnutí

Plus úvodní odstavec pod nadpisem kapitoly, bez vlastního podnadpisu.

## Čísla — musí sedět přesně

| Údaj | Správně |
|---|---|
| Denní maximum v červenci/srpnu | kolem 30 °C |
| Teplota moře | 22–26 °C |
| Teplota v květnu/červnu a září | 20–25 °C |
| Girona (GRO) → Lloret | 30–40 minut |
| Barcelona (BCN) → Lloret | 1–1,5 hodiny |
| Autobus Sagalés 613, jízda | cca 35 minut |
| Autobus, jízdenka | orientačně 10 EUR, **až kolem 23 EUR** podle dopravce |
| Bezkontaktní platba bez PINu | do 50 EUR |
| Fyzická SIM | cca 10 EUR / měsíc |
| eSIM | 4–12 **USD** (ne EUR!) |

## Opatrné formulace — nesmí se z nich stát tvrzení najisto

Tohle jsou místa, která prošla fact-checkem. Když je model „uhladí", zmizí přesně ta opatrnost,
kvůli které se dělala čtyři kola kontroly.

- U ceny autobusu musí zůstat, že se **zdroje rozcházejí** a že se objevují částky až kolem 23 EUR.
- U karet musí zůstat, že podnik kartu přijmout **nemusí** a že cash-only je legální.
- U kapesních krádeží musí zůstat, že **jsme nenašli spolehlivá data** přímo pro Lloret a že se
  zdroje týkají hlavně Barcelony — ne že je Lloret bezpečný, ani že je rizikový.
- U eSIM musí zůstat, že se ceny mění a je potřeba je ověřit těsně před cestou.

## Věty, které už jednou vypadly nebo se změnily

Ověřeno na prvním běhu (2026-07-29) — u dalšího generování kontrolovat přednostně:

- „podnik **ve** Španělsku kartu přijmout nemusí" — v prvním běhu vyšlo „podnik **se** Španělsku".
- „…je tu naprosto legální **a hotovostí pořád projde víc než polovina plateb v kamenných
  obchodech**." — zvýrazněná část v prvním běhu úplně vypadla.

## Fotky

- Žádná čitelná cedule s názvem konkrétního podniku. V prvním běhu vznikla vymyšlená
  „CHIRINGUITO SA BOADELLA".
- Pojmenovaná místa (Cala Boadella, hrad Sant Joan) nepodepisovat — model je nevygeneruje věrně.
