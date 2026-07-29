# Kontrolní list — kapitola 02: Doprava po okolí

Zdroj: `../../../01-tvorba-textu/content/lloret-de-mar/text/02-doprava-po-okoli.md`

Postup generování je v `../../docs/prompt-guide.md`. Tenhle list slouží ke **kontrole vygenerovaných
stránek proti zdroji**.

## Sekce (počet, pořadí, nadpisy)

Kapitola má **4 podsekce** v tomto pořadí:

1. Autobusy
2. Auto a parkování
3. Tip navíc
4. Rychlé shrnutí

Plus úvodní odstavec pod nadpisem kapitoly, bez vlastního podnadpisu.

Pozor: sekce **Autobusy** obsahuje odrážkový seznam dvou cen — ten musí zůstat seznamem, ne se
rozpustit do odstavce.

## Čísla — musí sedět přesně

| Údaj | Správně |
|---|---|
| Barcelona → Lloret de Mar | od cca **13–16 EUR** jednosměrně |
| Barcelona → Tossa de Mar | od cca **17 EUR** jednosměrně |
| Zavazadla v ceně jízdenky | 25 kg zdarma |
| Vrácení běžného tarifu | až do **2 hodin** před odjezdem |
| Pronájem auta, nejlevnější měsíce | listopad a březen, od cca **18 EUR/den** |
| Bezplatné hlídané parkoviště | Avinguda Alegries, jen v sezóně **červen–září**, 24 h denně |
| Frekvence spojů Barcelona–Lloret | desítky denně |

**Nejrizikovější je 13–16 EUR** — rozsah uvnitř věty s dalším číslem hned pod ním. Přesně ten typ
konstrukce, na které model klopýtal v kapitole 01.

## Opatrné formulace — nesmí se z nich stát tvrzení najisto

- U **lodní linky Lloret–Tossa** musí zůstat, že se **spolehlivý aktuální zdroj online nepodařilo
  dohledat** a jízdní řád i cenu si má čtenář ověřit na místě nebo v infocentru. Tohle je otevřená
  otázka z Fáze 1 — když to model „uhladí" na konkrétní cenu nebo čas, vznikne tvrzení, které nemá
  oporu v researchi.
- U cen jízdenek musí zůstat, že se **liší podle předstihu nákupu a sezóny**.
- U pronájmu auta musí zůstat, že v hlavní sezóně ceny **výrazně rostou** — ne jen ta levná čísla.

## Vlastní jména — musí být přesně

Zkomolené jméno dopravce nebo ulice je horší než chybějící údaj, protože podle něj čtenář hledá.

- **Moventis Sarfa** (dopravce)
- **Avinguda Alegries** (parkoviště)
- **Tossa de Mar**, **Blanes**, **Sant Feliu de Guíxols**, **Palamós**, **Cadaqués**
- **Water World** (orientační bod u parkoviště)

## Fotky

- Žádná čitelná cedule s názvem konkrétního podniku, půjčovny nebo hotelu.
- Autobus Moventis Sarfa je reálná značka — pokud bude na fotce, musí být napsaná správně, jinak
  raději bez čitelného loga.
- Parkoviště na Avinguda Alegries nepodepisovat — model konkrétní místo nevygeneruje věrně.
- Zelená a modrá zóna: pokud je vidět dopravní značení, nesmí obsahovat vymyšlené české nápisy.

## Poznámka k obsahu

Fact-check kapitoly je `Stav: OK` bez nálezů. Dvě otevřené otázky z Fáze 1, které se týkají téhle
kapitoly (cena a jízdní řád linky na Gironu; jestli modrá zóna funguje celoročně), jsou vedené
v `../../../01-tvorba-textu/docs/open-questions-lloret-de-mar.md` a řeší se **až před vydáním**,
ne teď.
