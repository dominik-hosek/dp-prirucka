# Kontrolní list — kapitola 06: Off the beaten path

Zdroj: `../../../01-tvorba-textu/content/lloret-de-mar/text/06-off-the-beaten-path.md`

Postup generování je v `../../docs/prompt-guide.md`. Tenhle list slouží ke **kontrole vygenerovaných
stránek proti zdroji**.

## Sekce (počet, pořadí, nadpisy)

Kapitola má **5 podsekcí** v tomto pořadí:

1. Skryté zátoky
2. Pobřežní stezka
3. Zahrady Santa Clotilde navečer
4. Sousední města mimo hlavní trasu
5. Tip navíc

Plus úvodní odstavec pod nadpisem kapitoly, bez vlastního podnadpisu.

Struktura, která musí zůstat:

- **Skryté zátoky** — odrážkový seznam **4 zátok** s tučnými názvy. Poslední odrážka (Cala Forcanera)
  je výrazně delší než ostatní, protože nese celou opatrnou formulaci — nesmí se zkrátit na úroveň
  předchozích tří.
- **Sousední města** — odrážkový seznam **3 měst** s tučnými názvy, a **za ním samostatný odstavec**
  s výčtem dalších městeček. Ten odstavec není součástí seznamu.

Název kapitoly je anglický („Off the beaten path") — je to záměr, tak je to i v osnově. Nepřekládat.

## Dlouhý výčet městeček — nejrizikovější místo kapitoly

V odstavci pod odrážkami stojí **12 jmen v závorce za sebou**:

> Pals, Begur, Tamariu, S'Agaró, Empuriabrava, Llafranc, L'Estartit, Aigua Blava, Fornells,
> Calella de Palafrugell, Calonge, Palamós

Dvanáct cizích jmen bez kontextu je přesně to, u čeho model tiše vypustí jednu položku nebo dvě
slepí dohromady — a při čtení stránky to nikdo nepozná, protože seznam vypadá pořád stejně
věrohodně. **Počítej je.** Musí jich být 12 a v tomhle pořadí.

Pozor na apostrofy: **S'Agaró** a **L'Estartit**. Apostrof i čárka nad „o" musí zůstat.
**Calella de Palafrugell** jsou tři slova, ne jedno.

Rámec věty: městečka leží **mezi Rosas a Tossa de Mar** — v textu je tvar „Rosas" (ne „Roses"),
drž se textu.

## Čísla — musí sedět přesně

| Údaj | Správně |
|---|---|
| Cala Sa Boadella — délka | cca **250 m** |
| Tossa de Mar — stálí obyvatelé | jen kolem **6 200** mimo sezónu |

Číslo 6 200 se píše s mezerou jako oddělovačem tisíců. Model rád doplní tečku nebo čárku.

## Opatrné formulace — nesmí se z nich stát tvrzení najisto

- U **Cala Forcanera** musí zůstat, že se **trasu ani vzdálenost nepodařilo ověřit z víc zdrojů**
  a že se bude potřeba doptat na místě (v půjčovně paddleboardů nebo v infocentru). Tohle je
  otevřená otázka z Fáze 1 — když z toho model udělá návod, vznikne tvrzení bez opory a čtenář
  vyrazí hledat cestu, která možná neexistuje.
- U **Cala dels Frares** musí zůstat, že je **bez základních služeb** (bez baru, sprch) — to je
  důvod, proč je prázdná, a zároveň praktické varování.
- U Tossa de Mar musí zůstat, že jde o **počet stálých obyvatel mimo sezónu** — bez toho by 6 200
  vypadalo jako počet lidí ve městě v létě, což je nesmysl.
- V Tipu navíc musí zůstat, že si má čtenář **vzdálenost a dobu cesty ověřit podle aktuálního
  jízdního řádu** — je to druhá otevřená otázka z Fáze 1.

## Vlastní jména — musí být přesně

- **Cala Sa Boadella**, **Cala Banys**, **Cala dels Frares**, **Cala Forcanera**
- **Camí de Ronda** (pobřežní stezka — `í` s čárkou)
- **Cala Canyelles**, **Santa Cristina** (zmíněné jako navazující trasa)
- **Santa Clotilde** (zahrady)
- **Blanes**, **Sant Feliu de Guíxols** (`í` s čárkou), **Tossa de Mar**
- plus 12 městeček z výčtu výše

## Fotky

- Zátoky **nepodepisovat**. Cala Banys, Cala dels Frares a Cala Forcanera jsou reálná, málo známá
  místa — model si je vymyslí a nikdo to nepozná, dokud tam čtenář nedojede.
- U zahrad Santa Clotilde nesmí být čitelná informační cedule ani vstupné.
- V Blanes: záběr rybářského přístavu bez čitelných jmen lodí a bez cedulí podniků.
- Fotka paddleboardu / lodi u Cala Forcanera nesmí obsahovat logo půjčovny.

## Poznámka k obsahu

Fact-check kapitoly je `Stav: OK`, přeověřeno 2026-07-29. Obě otevřené otázky z Fáze 1 (přístup ke
Cala Forcanera a Cala dels Frares, vzdálenosti do Blanes a Sant Feliu de Guíxols) jsou vedené
v `../../../01-tvorba-textu/docs/open-questions-lloret-de-mar.md` a **v textu jsou už ošetřené
opatrnou formulací** — tady jde jen o to, aby je model nesetřel.
