# A4 cheatsheet page generation

## Use case
Jedna fyzická A4 strana taháčku k turistickému průvodci, kompaktní a rychle skenovatelná.

## Identity
- Destinace: `Barcelona`
- Země: `Španělsko`
- Oddíl: `Kdy se jí`
- Strana taháčku: `cheatsheet-04`

## Exact content contract
Použij výhradně tento text:

# Rychlotaháček 4 — Jídlo a pití

## Kdy se jí
- Oběd 13:30–16:00 (špička ~14:00) · Večeře od 20:30, běžně do 22:00+
- Nedělní vermut 12:00–14:00 — nejvíc „místní" chvíle, bez rezervace, zdarma
- Kdo přijde na večeři v 19:00 → hlavně turistické podniky

## Menú del día
- Orientačně 10–15 € (jiné zdroje 8–15 € nebo 13–20 €) — předkrm, hlavní, dezert, nápoj
- Večerní set menu vzácnější a dražší než polední → **hlavní jídlo v poledne**
- V turistických oblastech dražší než ve čtvrtích s místními

## Co ochutnat
- Pa amb tomàquet, Escalivada, Fideuà (rýže→nudle + plody moře)
- Calçots → sezóna konec prosince–březen, ne v létě
- Katalánská jídla vázaná na katalánský sváteční kalendář
- Čtvrti: tapas/vermut Gotická+El Born · plody moře Barceloneta · moderní kuchyně Gràcia/Eixample

## Jak poznat past
- La Rambla = opakovaně varováno (ohřívaná paella, mražené plody za čerstvé, kola +3→11 USD)
- Signály: nahaněč, foto-menu, „sangria a paella", paella pod lampou/fotka na fasádě
- Zářivě žlutá paella = varování, pravý šafrán barví jemně
- Dobré znamení: paella/fideuà na objednávku → čekání 20+ min
- Nezaměnit La Rambla a Rambla de Catalunya (ta druhá klidnější, lepší podniky)

## Ceny (orientační, agregátory)
- Espresso 1,20–1,80 € (turisticky až 2,50 €), cappuccino ~2,30 €
- Pivo v baru ~2,50 € (jinde zdroj uvádí až 7 € — nedoloženo, ber 2,50 jako spodní hranici)
- Pivo ze supermarketu 1,23–1,25 €/0,5l · 2l Coca-Cola 2,09 € · rychlé jídlo 4–8 €

## Spropitné a chleba
- Spropitné se běžně nedává, jen zaokrouhlení nahoru (~5 %); v dražších podnicích 5–10 %, nepovinné
- Chleba na stole = couvert až 2,50 €/os. — odmítnutím se neplatí, mlčením ano

Konkrétní restaurace zde nejsou — dostupné seznamy nesplňovaly metodiku (2 platformy + počet recenzí).

Chráněné tokeny: `["10–15 €","8–15 €","13–20 €","1,20–1,80 €","2,50 €","2,30 €","7 €","2,09 €","4–8 €","5 %","5–10 %","13:30","16:00","14:00","20:30","22:00","12:00","19:00","4","13","30–16","00","14","20","30","22","12","00–14","19","10–15","8–15","13–20","3","11","1,20–1,80","2,50","2,30","7","1,23–1,25","0","2,09","4–8","5","5–10","2","ne","jen","Rychlotaháček","Jídlo","Kdy","Oběd","Večeře","Nedělní","Kdo","Menú","Orientačně","Večerní","Co","Pa","Escalivada","Katalánská","Čtvrti","Gotická","El Born","Barceloneta","Eixample","Jak","La Rambla","Signály","Zářivě","Dobré","Nezaměnit La Rambla","Rambla","Catalunya","Ceny","Espresso","Pivo","Coca-","Cola","Spropitné","Chleba","Konkrétní","hlavní jídlo v poledne","místní","sangria a paella"]`

## Design
Použij stabilní A4 mřížku všech osmi stran: nadpis oddílu, krátké obsahové bloky a jasně odlišené praktické body. Přizpůsob pouze barvy, typografický pocit, motivy a fotografie systému země: `{"palette":{"background":["#F3ECE0","#F7F0E6"],"primary":"#C1502E","secondary":"#5E6D32","text":"#21150F","sand":"#E4D1B7","border":"#D8BC91"},"heading_fonts":["Cormorant Garamond","Bodoni Moda","Playfair Display","Prata"],"body_fonts":["Inter","Manrope","Source Sans 3","IBM Plex Sans"],"motifs":["středomořská architektura","olivy","keramika","pobřeží"],"photo_style":"teplé přirozené světlo, autentická místa, krémové a terakotové tóny","character":"prémiový středomořský editorial"}`.

## Constraints
- Přesný A4 poměr 1:1.41421356237, bezpečné okraje, žádné přetečení.
- Všechna fakta, čísla, měny, časy, data, vlastní jména, negace a varování zachovej přesně.
- Všechen text česky; žádné smyšlené názvy, loga, watermarky, cedule ani anglické popisky.
- Vytvoř jednu jedinou finální variantu.
