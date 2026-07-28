#!/usr/bin/env python3
"""Vygeneruje náhradní obrázky, aby šlo vysázet zkušební PDF dřív,
než existují skutečné assety.

Použití:
    python design/templates/make-placeholders.py lloret-de-mar

Náhrady se generují do content/<slug>/assets/ a jsou určené k přepsání
skutečnými obrázky. Nikdy je necommituj jako hotové assety.
"""

import os
import sys

from PIL import Image, ImageDraw

BARVY = {
    "primarni": (14, 58, 83),
    "sekundarni": (27, 154, 170),
    "zelen": (63, 107, 79),
    "akcent": (231, 111, 81),
}

SOUBORY = [
    ("cover/00-obalka.png", (1240, 1754), "primarni"),
    ("illustrations/01-cami-de-ronda-utes.png", (1240, 1754), "sekundarni"),
    ("illustrations/02-cala-boadella.png", (1200, 800), "zelen"),
    ("illustrations/03-zatoka.png", (1240, 1754), "akcent"),
]


def main(slug: str) -> None:
    zaklad = os.path.join("content", slug, "assets")
    for cesta, rozmer, barva in SOUBORY:
        cil = os.path.join(zaklad, cesta)
        os.makedirs(os.path.dirname(cil), exist_ok=True)
        im = Image.new("RGB", rozmer, BARVY[barva])
        ImageDraw.Draw(im).text((40, 40), f"NÁHRADA — {os.path.basename(cil)}", fill=(250, 247, 240))
        im.save(cil)
        print("vytvořeno:", cil)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "lloret-de-mar")
