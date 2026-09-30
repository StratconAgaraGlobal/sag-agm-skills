#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rebuild examples/agm-brand-example.html from the bundled assets.

Fully self-contained (fonts, emblems and both editions' graphics are embedded
as data: URIs), so the page opens anywhere with no downloads. Run again only
if the assets or example_template.html change:

    python build_example_html.py [--out path/to/agm-brand-example.html]

Requires Pillow. woff2 compression needs `fonttools` + `brotli`; without them
fonts are embedded as plain TTF (bigger file, same result).
"""
import argparse
import base64
import io
import json
import os
import tempfile

from PIL import Image

import graphics
from brands import BRANDS

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ASSETS = os.path.join(ROOT, "assets")

FONTS = {400: "PlusJakartaSans-Regular.ttf", 500: "PlusJakartaSans-Medium.ttf",
         600: "PlusJakartaSans-SemiBold.ttf", 700: "PlusJakartaSans-Bold.ttf",
         800: "PlusJakartaSans-ExtraBold.ttf"}


def b64(data):
    return base64.b64encode(data).decode("ascii")


def png_uri(im, max_w=None):
    if max_w and im.size[0] > max_w:
        im = im.resize((max_w, round(im.size[1] * max_w / im.size[0])),
                       Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "PNG", optimize=True)
    return "data:image/png;base64," + b64(buf.getvalue())


def file_uri(rel, max_w=None):
    return png_uri(Image.open(os.path.join(ASSETS, rel)), max_w)


def font_face(weight, fname):
    raw = open(os.path.join(ASSETS, "fonts", fname), "rb").read()
    fmt, mime = "truetype", "font/ttf"
    try:
        from fontTools.ttLib import TTFont
        f = TTFont(io.BytesIO(raw))
        f.flavor = "woff2"
        out = io.BytesIO()
        f.save(out)
        raw, fmt, mime = out.getvalue(), "woff2", "font/woff2"
    except Exception:
        pass
    return ("@font-face{font-family:'Plus Jakarta Sans';font-weight:%d;font-style:normal;"
            "font-display:swap;src:url(data:%s;base64,%s) format('%s')}"
            % (weight, mime, b64(raw), fmt))


def edition_images(brand):
    tmp = tempfile.mkdtemp()
    m = brand.masthead(os.path.join(tmp, "m.png"), "24 SEPTEMBER 2026")
    c = brand.closing(os.path.join(tmp, "c.png"))
    d = brand.deck_band(os.path.join(tmp, "d.png"))
    return {"masthead": png_uri(Image.open(m), 1700),
            "closing": png_uri(Image.open(c), 1700),
            "deckband": png_uri(Image.open(d), 1920)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(ROOT, "examples", "agm-brand-example.html"))
    out = ap.parse_args().out
    imgs = {"common": {
        "emblem_navy": file_uri("logo/agm-emblem-navy.png", 480),
        "emblem_green": file_uri("logo/agm-emblem-green.png", 480),
        "emblem_white": file_uri("logo/agm-emblem-white.png", 480)}}
    for key, brand in BRANDS.items():
        imgs[key] = edition_images(brand)
    html = open(os.path.join(HERE, "example_template.html"), encoding="utf-8").read()
    html = html.replace("/*__FONT_FACES__*/", "\n".join(font_face(w, f) for w, f in FONTS.items()))
    html = html.replace("__IMG_JSON__", json.dumps(imgs))
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(html)
    print(out, "%.1f MB" % (os.path.getsize(out) / 1e6))


if __name__ == "__main__":
    main()
