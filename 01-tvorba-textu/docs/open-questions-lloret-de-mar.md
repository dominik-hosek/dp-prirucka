# Otevřené otázky z Fáze 1 (research) — Lloret de Mar

Souhrn napříč všemi research soubory (`content/lloret-de-mar/research/`), co se rozcházelo mezi
zdroji nebo se nepodařilo spolehlivě ověřit. Před vydáním produktu (Fáze 4 QA) je potřeba tyto body
proklepnout — buď doověřit, nebo zkontrolovat, že je text formuluje dostatečně opatrně.

Seskupeno podle toho, co s tím má QA udělat, ne podle research souborů.

Stav k 2026-07-29 (aktualizováno po doplnění žebříčků podle recenzí a modernistického hřbitova).

## 1. Ceny a jízdní řády — doověřit těsně před vydáním

Tohle jsou konkrétní čísla, která v produktu zůstanou vytištěná. Všechna jsou z podstaty proměnlivá
a research je má jen orientačně.

- **Autobus Girona (letiště) → Lloret de Mar** — zdroje uvádí rozmezí 10–23 EUR podle dopravce.
  Kapitola 01 to už formuluje s výhradou, ale konkrétní číslo doověřit u Sagalés / Moventis Sarfa /
  Flixbus.
- **Autobus Lloret → Girona** (na letiště i do centra) — jízdní řád ani cenu pro sezónu 2026 se
  nepodařilo dohledat; zdroje pokrývaly hlavně linku na Barcelonu. Doověřit na webu Moventis Sarfa.
- **Loď Lloret de Mar – Tossa de Mar** — existence spojení a délka plavby (~30 min) potvrzené,
  aktuální ceník ne.
- **Ubytování za noc** (hotel 3*/4*, aparthotel, apartmán) — jen orientační průměr. V sezóně se ceny
  mění týden od týdne, doověřit na rezervačních portálech těsně před vydáním. Blokuje i rozpočtovou
  kapitolu, protože bez nocležného nejde sestavit denní rozpočet.
- **Jídlo** — menu del día a hlavní jídla jen v orientačním rozmezí 20–25 EUR, bez konkrétních
  podniků.
- **Vstupné Water World a Marineland** — mění se každoročně. Kontrolovat při každém vydání
  i aktualizaci, ne jen teď.
- **Vstupné do zahrad Santa Clotilde** — doložených 6,10 / 3,10 EUR platí k létu 2026. Doověřit
  spolu s ostatním vstupným.
- **Vstupné na modernistický hřbitov** — oficiální zdroje města žádnou cenu neuvádějí, agregátory
  tvrdí, že je zdarma. Text proto cenu neuvádí. Doověřit u města (+34 972 349 573,
  patrimonicultural@lloret.cat) — pokud je vstup opravdu zdarma, stojí za to to do textu doplnit,
  je to silný argument.
- **Mimosezónní otevírací doba zahrad Santa Clotilde** — doložená je jen doba duben–říjen
  (10:00–20:00). Text má výhradu, ale konkrétní zimní doba chybí.

## 1b. Žebříčky podle recenzí — přeověřit před KAŽDÝM vydáním

Kapitoly 03, 04 a 05 jmenují konkrétní hotely, restaurace a atrakce vybrané podle
`docs/metodika-hodnoceni.md`. Data pocházejí ze sběru **2026-07-29** a jsou z podstaty pomíjivá —
podnik může zavřít, změnit majitele nebo se mu propadne známka.

- **Přeověřit celý žebříček**, ne jen namátkou. U restaurací zvlášť — zavírají častěji než hotely.
- **Zkontrolovat, že žádný jmenovaný podnik nezavřel.** *Alva Park Costa Brava* je varovný příklad:
  na seznamech „nejlepších hotelů" se držel i po svém trvalém zavření.
- **Doplnit chybějící druhou platformu, nebo podnik vyřadit:**
  - *ALEGRIA Fenals Mar* — hodnocení na Google Maps se nepodařilo dohledat. Kvůli tomu jsou ve Fenals
    v textu jen dva hotely místo tří. Pokud se doplní, přibude třetí; pokud ne, zůstává to tak.
  - *Hotel Santa Marta* — chybí hodnocení na Booking.com. Je to jediný doporučený hotel v klidné
    oblasti, takže by si plné doložení zasloužil.
- **Hodnocení hlavní pláže Platja de Lloret** — v datech chybí, takže srovnání pláží v kapitole 05
  není úplné a text to musí přiznávat. Doplnit.

## 2. Nedoložená tvrzení — v textu držet opatrnou formulaci

Tady nejde o čísla k doplnění, ale o tvrzení, která by se **neměla** dostat do textu jako fakt
o Lloretu. Úkol QA je ověřit, že se tam nevloudila.

- **Platba kartou v taxi v Lloretu** — nedoloženo. Dostupné zdroje mluví o Barceloně (kde licencované
  taxíky kartu brát musí) a jsou navíc slabé kvality (SEO weby). Netvrdit, že taxi v Lloretu kartu
  vezme.
- **Platební politika chiringuit v Lloretu** — nedoloženo. Jediný doložený cash-only příklad je
  z jiné obce na Costa Bravě (Sant Pere Pescador). Psát obecně („část plážových barů bere jen
  hotovost"), ne jako fakt o Lloretu.
- **Kapesní krádeže v Lloretu** — specifické zkušenosti se nepodařilo dohledat, zdroje mluví hlavně
  o Barceloně. Psát o obezřetnosti obecně, ne o Lloretu jako rizikovém místě.
- **Konkrétní seznam doporučených chiringuitos s adresami** — nepodařilo se najít aktuální seznam
  nezávislý na sponzorovaných recenzích. Nejmenovat konkrétní podniky bez ověření z více zdrojů.
- **Trasa ke Cala dels Frares a Cala Forcanera** — potvrzeno jen to, že standardní přístup je
  omezený; konkrétní trasa/vzdálenost/způsob (chůze, kolo, loď) ne. Netvrdit konkrétní přístupovou
  cestu.

## 3. Chybějící detaily — doplnit při finalizaci

Drobnosti, které text zpřesní, ale nic neblokují.

- **Doba chůze mezi čtvrtěmi** (Fenals, centrum, Cala Boadella) — zdroje uvádí „asi 1 km" bez
  časů. Doplnit orientační minuty.
- **Vzdálenost a doba cesty do Blanes a Sant Feliu de Guíxols** — doověřit, pokud v guide zůstávají
  jako konkrétní výletní tip.
- **Modrá zóna parkování v centru** — není jasné, jestli funguje celoročně nebo jen v sezóně.
  Doověřit na webu města.

## 4. Kontrolovat při každém vydání (nezastarává jen jednou)

- **Vstupní podmínky do Španělska** — Lloretu jako destinace v EU/Schengenu se EES/ETIAS netýká, ale
  před každým vydáním zkontrolovat aktuální stav na mzv.gov.cz.
- **Sezónnost cen** — ceny se mezi červnem a zářím výrazně liší (nejdražší červenec/srpen). Text
  nesmí uvádět jedno číslo jako platné pro celé léto; ověřit, že to tak kapitoly opravdu mají.

## Doporučení

1. Body ze sekce 1 doověřit **až těsně před vydáním**, ne teď — jinak se do dne vydání stihnou znovu
   změnit. Do textu je do té doby psát s výhradou („k létu 2026", „ověř si před cestou").
2. Sekci 2 projít jako kontrolní seznam proti hotovým kapitolám — jsou to přesně ta místa, kde
   fact-checker při psaní opakovaně chytal ztracenou opatrnost.
3. Chiringuita a taxi se opakují ve víc bodech a týkají se běžné každodenní situace čtenáře. Pokud
   bude příležitost cokoli doověřit u někoho s reálnou znalostí Lloretu, mají tyhle dvě věci
   nejlepší poměr užitku k námaze.
4. Sekci 4 překlopit do QA checklistu (Fáze 4) jako opakovanou položku, ne jednorázovou.
5. **Sekce 1b patří do QA checklistu taky jako opakovaná položka.** Jmenované podniky jsou největší
   přidaná hodnota průvodce a zároveň to, co zastará nejrychleji — zavřená restaurace v placeném
   průvodci poškodí důvěryhodnost víc než chybějící tip.

## Co se mezitím uzavřelo

- **Konkrétní restaurace a hotely** byly původně vedené jako „nejmenovat bez ověření z víc zdrojů".
  Sběrem 2026-07-29 podle `docs/metodika-hodnoceni.md` se to vyřešilo — jména v kapitolách 03 a 04
  teď oporu mají. **Chiringuita zůstávají otevřená** (viz sekce 2), pro ně se použitelná data
  nenašla ani při tomhle sběru.
- **Modernistický hřbitov** — objevil se jako nejlépe hodnocené místo, které v průvodci nebylo.
  Doresearchován 2026-07-29 z oficiálních městských zdrojů a doplněn do kapitoly 06. Otevřené
  zůstává jen vstupné (viz sekce 1).

## Poznámka k researchi

Itineráře („3 dny v Lloretu", „5 dní s výlety") byly v research fázi vedené jako otevřená položka —
research dodal jen stavební kameny (vzdálenosti, otevírací doby). Writer je mezitím poskládal
v kapitole 05, takže tenhle bod už otevřený není; zůstává jen závislost na cenách a otevíracích
dobách ze sekce 1.
