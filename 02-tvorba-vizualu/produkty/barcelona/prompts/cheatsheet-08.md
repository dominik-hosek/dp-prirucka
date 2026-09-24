# A4 cheatsheet page generation

## Use case
Jedna fyzická A4 strana taháčku k turistickému průvodci, kompaktní a rychle skenovatelná.

## Identity
- Destinace: `Barcelona`
- Země: `Španělsko`
- Oddíl: `Doklady`
- Strana taháčku: `cheatsheet-08`

## Exact content contract
Použij výhradně tento text:

# Rychlotaháček 08 — Checklist před odjezdem

## Doklady
- [ ] OP nebo pas — EU/Schengen, nic víc
- [ ] ETIAS se tě netýká (jen třetí země) — nekupuj si „vyřízení ETIAS"
- [ ] Spuštění ETIAS nejisté, možný odklad na 2027; EES se v ES už zavádí (jen 3. země)

## Pojištění
- [ ] EHIC platí jen ve veřejných zdravotnických zařízeních
- [ ] EHIC NEKRYJE: repatriaci, spoluúčast při hospitalizaci, spoluúčast na lécích
- [ ] Sjednej i cestovní pojištění (záchrana, asistence, tlumočení) — konkrétní produkt je na tobě

## DROZD a konzulát
- [ ] Zaregistruj se do DROZD (MZV) — zdarma, pár minut
- [ ] Konzulát ČR Barcelona: Carrer de Mallorca 272, 9-1, 08037 BCN
- [ ] Tel. +34 933 128 044 · nouzová linka MZV +420 222 420 222
- [ ] Úřední hodiny po/st/pá 10:00–12:00 — s náhradním dokladem nepočítej „hned"
- [ ] Kontakty na internetu se liší — ověř na mzv.gov.cz před cestou

## Rezervovat dopředu
- [ ] Ubytování 3–6 měsíců dopředu na léto
- [ ] Registrační číslo apartmánu (NRU/HUT/NIRTC) — bez čísla je varovný signál
- [ ] Park Güell — časový slot, po čase 30 min na vstup
- [ ] Museu Picasso zdarma — sloty 4 dny dopředu v 10:00 (BCN čas), rychle mizí
- [ ] Sagrada Família — ověř, zda je otevřená; informacio@sagradafamilia.org, +34 932 080 414
- [ ] Montserrat, pokud plánuješ — hůř spontánní než Sitges

## Doma + s sebou
- [ ] eSIM aktivovat před odletem, zkontroluj ceník (EUR i USD)
- [ ] MHD jízdenka: T-casual vs. Hola Barcelona (zlom ~21 jízd/3 dny), T-casual neplatí na letišti
- [ ] Turistická daň do rozpočtu: 6–12 EUR/os./noc
- [ ] Zkontrolovat doporučení MZV na mzv.gov.cz
- [ ] Pohodlná obuv (Bunkers) + drobná hotovost

Chráněné tokeny: `["30 min","4 dny","3 dny","10:00","12:00","08","2027","3","272","9-1","08037","34","933","128","044","420","222","10","00–12","00","3–6","30","4","932","080","414","21","6–12","jen","Rychlotaháček","Checklist","Doklady","Schengen","Spuštění","Pojištění","Sjednej","Zaregistruj","Konzulát","Barcelona","Carrer","Mallorca","Tel","Úřední","Kontakty","Rezervovat","Ubytování","Registrační","Park","Museu Picasso","Sagrada Família","Montserrat","Sitges","Doma","T-casual","Hola Barcelona","Turistická","Zkontrolovat","Pohodlná","Bunkers","vyřízení ETIAS","hned"]`

## Design
Použij stabilní A4 mřížku všech osmi stran: nadpis oddílu, krátké obsahové bloky a jasně odlišené praktické body. Přizpůsob pouze barvy, typografický pocit, motivy a fotografie systému země: `{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`.

## Constraints
- Přesný A4 poměr 1:1.41421356237, bezpečné okraje, žádné přetečení.
- Všechna fakta, čísla, měny, časy, data, vlastní jména, negace a varování zachovej přesně.
- Všechen text česky; žádné smyšlené názvy, loga, watermarky, cedule ani anglické popisky.
- Vytvoř jednu jedinou finální variantu.
