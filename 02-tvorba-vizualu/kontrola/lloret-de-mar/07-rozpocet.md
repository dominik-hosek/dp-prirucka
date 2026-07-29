# Kontrolní list — kapitola 07: Rozpočet

Zdroj: `../../../01-tvorba-textu/content/lloret-de-mar/text/07-rozpocet.md`

Postup generování je v `../../docs/prompt-guide.md`. Tenhle list slouží ke **kontrole vygenerovaných
stránek proti zdroji**.

> **Kapitola je z 90 % čísla.** U ostatních kapitol se hlídají tvrzení a čísla jsou vedlejší produkt —
> tady jsou čísla obsah. Jediné špatně opsané číslo znehodnotí celou stránku, protože přesně kvůli
> těmhle číslům si čtenář průvodce koupil. Kontroluj **položku po položce proti tabulce níž**, ne
> čtením.

## Sekce (počet, pořadí, nadpisy)

Kapitola má **7 podsekcí** v tomto pořadí:

1. Jídlo a pití
2. Doprava
3. Ubytování
4. Atrakce
5. SIM/eSIM
6. Orientační denní rozpočet na osobu (mimo ubytování)
7. Tip navíc

Plus úvodní odstavec pod nadpisem kapitoly, bez vlastního podnadpisu.

Sekce **Jídlo a pití**, **Doprava**, **Atrakce**, **SIM/eSIM** a **Orientační denní rozpočet** jsou
odrážkové seznamy. Sekce **Ubytování** a **Tip navíc** jsou souvislé odstavce. Za seznamem v sekci
Jídlo a pití stojí ještě samostatná věta o cenách u pláže — nesmí se ztratit ani vtáhnout do
poslední odrážky.

## Čísla — musí sedět přesně

| Údaj | Správně |
|---|---|
| Espresso | orientačně **1,40 EUR** |
| Cappuccino | kolem **2 EUR** |
| Litr běžného ležáku | v průměru kolem **2,10 EUR**, nejlevnější od **1,60 EUR** |
| Fast food menu | cca **9 EUR** |
| Cheeseburger samotný | cca **2,70 EUR** |
| Menu del día | **20-25 EUR**/osobu |
| Taxi — nástupní sazba | cca **3,50 EUR** |
| Taxi — sazba za kilometr | cca **1,30 EUR/km** |
| Taxi z letiště Girona | cca **50 EUR** |
| Autobus z letiště Girona | orientačně **10 EUR**, zdroje se rozcházejí, objevují se i částky **až kolem 23 EUR** |
| Půjčení auta | od cca **18 EUR/den** v mimosezóně (listopad, březen) |
| All-inclusive ubytování | kolem **141 USD/noc** v průměru — **USD, ne EUR!** |
| Water World | **37,20 EUR**/osoba (nad **1,2 m** výšky) |
| Marineland | **23 EUR** dospělý / **16,5 EUR** dítě do 12 let / zdarma do 4 let |
| Fyzická SIM | cca **10 EUR** i s velkým balíčkem dat na měsíc |
| eSIM | cca **4-12 USD** — **USD, ne EUR!** |
| Úsporný den | cca **35-45 EUR** |
| Střední den | cca **55-70 EUR** |
| Den s výletem/atrakcí | **+23-40 EUR** k výše uvedeným částkám |

### Měny — dvě místa, kde se to už jednou pokazilo

V kapitole se míchají **EUR i USD** a je to správně, ne překlep: ubytování i eSIM ceníky jsou
ve zdrojích vedené v dolarech.

Přesně tahle záměna se opravovala u eSIM v kapitole 01 (fact-check 2026-07-28) a znovu tady
(2026-07-29, kdy kapitola slučovala fyzickou SIM a eSIM do jediné částky „10-12 EUR"). Je to jediná
chyba v projektu, která vznikla dvakrát nezávisle na sobě.

**Když na stránce uvidíš u ubytování nebo eSIM euro, je to nález — i kdyby to číslo sedělo.**

### Desetinné čárky

**1,40 · 2,10 · 1,60 · 2,70 · 3,50 · 1,30 · 37,20 · 16,5** — osm čísel s desetinnou čárkou. Model má
tendenci je zaokrouhlovat („1,4", „37,2", „16,50"). Kontroluj i počet desetinných míst, nejen
hodnotu.

## Opatrné formulace — nesmí se z nich stát tvrzení najisto

- U autobusu z letiště musí zůstat, že se **zdroje rozcházejí** a objevují se částky až kolem
  23 EUR. Doplněno 2026-07-29 — bez toho kapitola 07 tvrdila o stejném autobusu něco jiného než
  kapitola 01.
- U ubytování musí zůstat, že **141 USD je průměr, ne cena**, a že si má čtenář ověřit aktuální ceny
  na rezervačním portálu.
- U eSIM musí zůstat, že se **ceníky mění častěji než u klasických SIM** a je potřeba je ověřit před
  cestou.
- U půjčení auta musí zůstat, že v hlavní sezóně je **výrazně dráž** — ne jen těch 18 EUR.
- U denních rozpočtů musí zůstat, že jde o **odhad pro plánování, ne garantovanou částku**, a že
  čísla jsou **ověřená k létu 2026**.
- V úvodu musí zůstat, že **červenec a srpen jsou citelně dražší** než zbytek léta. Research to
  výslovně vyžaduje — jedno číslo bez sezónnosti je zavádějící.
- V Tipu navíc **záměrně není konkrétní cena autobusu**, jen „jízdenka v řádu jednotek eur" proti
  taxíku kolem 50 EUR. Když tam model doplní „10 EUR", vrací se tím opravená chyba.

## Fotky

Kapitola je z velké části infografiky a ikony, fotek je málo — o to důležitější je, co v nich stojí.

- **Žádné vymyšlené ceníky, účtenky, jídelní lístky ani cedule s cenou.** Číslo, které vznikne
  v obrázku, neprošlo fact-checkem — a přitom vypadá stejně věrohodně jako ta ověřená.
- Water World a Marineland: žádné čitelné logo ani cedule (reálné firmy).
- U záběru terasy kavárny nesmí být čitelný název podniku ani ceny v menu.
- Infografiky s cenami kontroluj **stejně přísně jako text** — jsou to táž čísla, jen ve větším
  písmu, takže případná chyba je o to viditelnější.

## Poznámka k obsahu

Fact-check kapitoly je `Stav: OK`, přeověřeno 2026-07-29 — při tom se našly a opravily 2 nálezy
(cena autobusu, měna u SIM/eSIM), detail v
`../../../01-tvorba-textu/content/lloret-de-mar/text/_fact-check/07-rozpocet.md`.

**Tahle kapitola zastará ze všech nejdřív.** Skoro každé číslo v ní je v sekci 1 otevřených otázek
(`../../../01-tvorba-textu/docs/open-questions-lloret-de-mar.md`), která se má doověřovat **až těsně
před vydáním**. Když se sazba téhle kapitoly udělá moc brzy, bude se s aktualizovanými čísly dělat
znovu — proto ji nech na konec, až budou ostatní kapitoly hotové.
