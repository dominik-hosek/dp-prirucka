# Kontrolní list — kapitola 01: Praktické základy

**✅ Hotovo 2026-07-29** — všech 6 sekcí vygenerovaných, text ověřený proti zdroji, bez nálezů.
Trvalo to 3 běhy (historie níže). Jediná zbylá odchylka: slovo „nemusí" v sekci Peníze ztratilo
tučné zvýraznění, které zdroj má — ponecháno, přegenerování kvůli tomu nestojí za riziko.

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

## Riziková věta — kontrolovat při každém běhu

Jedna věta v sekci Peníze se rozbila ve **dvou** po sobě jdoucích bězích. Správné znění:

> Ve Španělsku se platí eurem. Kartou zaplatíš ve městech prakticky všude a do 50 EUR bezkontaktně
> i bez PINu — ale nespoléhej na to úplně: podnik **ve** Španělsku kartu přijmout nemusí, cash-only
> bar nebo obchod je tu **naprosto legální a hotovostí pořád projde víc než polovina plateb
> v kamenných obchodech**.

Historie:

| Běh | Co vyšlo |
|---|---|
| 1 | „podnik **se** Španělsku" + celá část o polovině plateb vypadla |
| 2 | předložka opravena, ale doplňovaná část se slepila do nesmyslu: „je tu **naprosti** plateb v kamenných obchodech" |
| 3 | ✅ správně a kompletně |

Ponaučení: prosté přegenerování stačilo, zdrojovou kapitolu nebylo nutné zkracovat. Jde o loterii,
ne o systematickou neschopnost modelu — ale u téhle věty počítej s víc pokusy.

Proč zrovna tahle: je dlouhá, má vloženou vedlejší větu a nese číselný údaj (podíl hotovostních
plateb podle Banco de España), kvůli kterému se dělal doplňkový research.

## Pravidlo pro opravy

**Každé přegenerování je nový hod kostkou.** Model neopraví jen chybné místo — sází stránku znovu
celou a může rozbít i to, co bylo v pořádku. Po opravě proto kontroluj:

1. opravované místo,
2. **celý odstavec kolem něj**,
3. zbytek stránky proti tabulce čísel výše.

Když se stejná věta rozbije dvakrát po sobě, zvaž její zkrácení ve zdrojové kapitole
(`../../../01-tvorba-textu/content/lloret-de-mar/text/01-prakticke-zaklady.md`) — rozdělit na dvě
kratší věty a nechat kapitolu znovu fact-checknout je spolehlivější než dokola generovat stránku.

## Fotky

- Žádná čitelná cedule s názvem konkrétního podniku. V prvních dvou bězích vznikla vymyšlená
  „CHIRINGUITO SA BOADELLA", ve třetím už jen generické „CHIRINGUITO" — tak je to správně.
- Pojmenovaná místa (Cala Boadella, hrad Sant Joan) nepodepisovat — model je nevygeneruje věrně.
