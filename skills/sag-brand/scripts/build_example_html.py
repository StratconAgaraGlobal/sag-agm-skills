#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rebuild examples/sag-brand-example.html from the bundled assets.

The page is fully self-contained (fonts, logos and graphics are embedded as
data: URIs), so it opens anywhere with no downloads. Run this again only if the
assets or example_template.html change:

    python build_example_html.py [--out path/to/sag-brand-example.html]

Requires Pillow. woff2 font compression needs `fonttools` + `brotli`; without
them the fonts are embedded as plain TTF (bigger file, same result).
"""
import argparse
import base64
import io
import os

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ASSETS = os.path.join(ROOT, "assets")

# font-weight -> file
FONTS = {400: "PlusJakartaSans-Regular.ttf", 500: "PlusJakartaSans-Medium.ttf",
         600: "PlusJakartaSans-SemiBold.ttf", 700: "PlusJakartaSans-Bold.ttf",
         800: "PlusJakartaSans-ExtraBold.ttf"}

# token -> (relative path, max width px)  (downscaled for the page; the files
# in assets/ stay full resolution)
IMAGES = {
    "__IMG_LOGO__": ("logo/sag-logo.png", 471),
    "__IMG_LOGO_PLATED__": ("logo/sag-logo-plated.png", 471),
    "__IMG_MASTHEAD__": ("graphics/masthead_blue.png", 1700),
    "__IMG_CLOSING__": ("graphics/closing_blue.png", 1700),
    "__IMG_DECKBAND__": ("graphics/deck_band_blue.png", 1920),
}


def b64(data):
    return base64.b64encode(data).decode("ascii")


def image_uri(rel, max_w):
    im = Image.open(os.path.join(ASSETS, rel))
    if im.size[0] > max_w:
        im = im.resize((max_w, round(im.size[1] * max_w / im.size[0])), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "PNG", optimize=True)
    return "data:image/png;base64," + b64(buf.getvalue())


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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(ROOT, "examples", "sag-brand-example.html"))
    out = ap.parse_args().out
    html = open(os.path.join(HERE, "example_template.html"), encoding="utf-8").read()
    html = html.replace("/*__FONT_FACES__*/", "\n".join(font_face(w, f) for w, f in FONTS.items()))
    for token, (rel, w) in IMAGES.items():
        html = html.replace(token, image_uri(rel, w))
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(html)
    print(out, "%.1f MB" % (os.path.getsize(out) / 1e6))


if __name__ == "__main__":
    main()
