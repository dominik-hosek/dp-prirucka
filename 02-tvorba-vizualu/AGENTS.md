# Hranice vizuální fáze

- `01-tvorba-textu` je pouze read-only vstup. Nikdy v něm neupravuj, nepřesouvej ani nemaž soubory.
- Zdroj pravdy pro vizuální systém je v `config/*.yaml`; původní DOCX zůstávají beze změny jako dokumentace.
- Obrázky generuj výhradně vestavěným `$imagegen`, vždy jedním voláním pro jednu stránku. Nepoužívej vlastní API klient ani API klíč.
- Španělské PNG v `šablony/Španělsko/` jsou neměnný vizuální baseline.
- Schválené PNG, manifesty, finální prompt packets a QA reporty verzuj. Drafty, zamítnuté varianty, rendery PDF a soubory v `dist/` neuchovávej v Gitu.
- Existující schválený soubor nikdy nepřepisuj. Pro novou verzi použij verzovaný název.
- Textový obsah musí zachovat fakta, čísla, měny, časy, data, vlastní jména, negace a opatrné formulace. Marketingový podtitul nikdy nevymýšlej.
- Po 14 country šablonách a po první kompletní kapitole destinace vždy zastav na lidském checkpointu.
- Stránku regeneruj nejvýše dvakrát. Po třetím celkovém pokusu ji označ `needs-human-review` a PDF nesestavuj.

