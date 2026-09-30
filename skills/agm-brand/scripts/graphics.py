# -*- coding: utf-8 -*-
"""The AGM device: photography under a flat PANEL veil, with the two-line
tagline and a rule that ends in an accent dot. It replaces SAG's Complexity
Line. Generated, never hand-drawn; the photo is swapped per edition.

Word cannot round a table corner, so the masthead and closing band ship as
images with the rounding baked in.
"""
import os
import tempfile  # noqa: F401  (kept for callers that want temp output)

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(HERE), "assets")
FD = os.path.join(ASSETS, "fonts")

W_MM = 170.0           # A4 content measure
TOP_MM = 25.1          # logo / wordmark zone
BAND_MM = 30.9         # device zone
RAD_MM = 2.5
VEIL = 0.78            # PANEL over the photo (fitted to the reference render)


def hexc(h):
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def font(name, pt, k):
    """k = px per mm at the document scale."""
    return ImageFont.truetype(os.path.join(FD, name),
                              max(4, int(round(pt * 0.3528 * k))))


def track(d, txt, f, x, y, fill, em, anchor="ls"):
    """Letter-spaced text. anchor 'ls' left, 'rs' right, 'ms' centred."""
    ls = f.size * em
    ws = [d.textlength(c, font=f) for c in txt]
    total = sum(ws) + ls * (len(txt) - 1)
    if anchor == "rs":
        x -= total
    elif anchor == "ms":
        x -= total / 2.0
    for c, w in zip(txt, ws):
        d.text((x, y), c, font=f, fill=fill, anchor="ls")
        x += w + ls


def rounded(img, radius_px, bg):
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        [0, 0, img.size[0] - 1, img.size[1] - 1], radius=radius_px, fill=255)
    out = Image.new("RGB", img.size, hexc(bg))
    out.paste(img, (0, 0), mask)
    return out


def band(brand, w_px, h_px):
    """Photo (width-fit, cropped vertically) under the PANEL veil, with the
    tagline and rule drawn on top. Sizes scale with the band width."""
    P = brand.P
    k = w_px / W_MM
    photo = Image.open(brand.photo).convert("RGB")
    sc = w_px / photo.size[0]
    photo = photo.resize((w_px, max(h_px, round(photo.size[1] * sc))),
                         Image.LANCZOS)
    top = int(round((photo.size[1] - h_px) * brand.photo_y))
    photo = photo.crop((0, top, w_px, top + h_px))
    veil = Image.new("RGB", photo.size, hexc(P["PANEL"]))
    img = Image.blend(photo, veil, VEIL)
    d = ImageDraw.Draw(img)

    f = font("PlusJakartaSans-ExtraBold.ttf", 8.6, k)
    cx = int(0.62 * w_px)
    track(d, brand.tagline1, f, cx, int(14.5 / BAND_MM * h_px), (255, 255, 255),
          0.085, "ms")
    track(d, brand.tagline2, f, cx, int(19.2 / BAND_MM * h_px),
          hexc(P["ACCENT_ON_DARK"]), 0.085, "ms")
    y = int(16.0 / BAND_MM * h_px)
    x0, x1 = int(144.2 * k), int(165.6 * k)
    col = hexc(P["ACCENT_ON_DARK"])
    d.line([(x0, y), (x1, y)], fill=col, width=max(2, int(0.17 * k)))
    r = max(3, int(0.5 * k))
    d.ellipse([x1 - r, y - r, x1 + r, y + r], fill=col)
    return img


def masthead(brand, out, date="24 SEPTEMBER 2026", w_mm=W_MM, px=20):
    k = px
    w, top, bnd = int(w_mm * k), int(TOP_MM * k), int(BAND_MM * k)
    P = brand.P
    img = Image.new("RGB", (w, top + bnd), hexc(P["PANEL"]))
    img.paste(band(brand, w, bnd), (0, top))
    d = ImageDraw.Draw(img)

    em = Image.open(brand.emblem_white).convert("RGBA")
    eh = int(15.3 * k)
    em = em.resize((int(round(eh * em.size[0] / em.size[1])), eh), Image.LANCZOS)
    img.paste(em, (int(5.1 * k), (top - eh) // 2), em)

    x = int(25.7 * k)
    track(d, brand.wordmark, font("PlusJakartaSans-ExtraBold.ttf", 10.5, k),
          x, int(12.5 * k), hexc(P["PAPER"]), 0.10)
    track(d, brand.descriptor, font("PlusJakartaSans-Regular.ttf", 6.6, k),
          x, int(15.7 * k), hexc(P["PALE"]), 0.09)
    track(d, date, font("PlusJakartaSans-SemiBold.ttf", 7.5, k),
          int((w_mm - 5) * k), int(13.5 * k), hexc(P["PALE"]), 0.16, "rs")

    rounded(img, int(RAD_MM * k), P["PAPER"]).save(out, "PNG")
    return out


def closing(brand, out, w_mm=W_MM, px=20):
    w, h = int(w_mm * px), int(BAND_MM * px)
    rounded(band(brand, w, h), int(RAD_MM * px), brand.P["PAPER"]).save(out, "PNG")
    return out


def deck_band(brand, out, w_mm=338.667, h_mm=52.0, px=10):
    """Full-bleed band for slides: square corners, runs to the edges."""
    band(brand, int(w_mm * px), int(h_mm * px)).save(out, "PNG")
    return out


if __name__ == "__main__":
    import argparse
    from brands import BRANDS
    ap = argparse.ArgumentParser(description="Regenerate the banner images")
    ap.add_argument("--edition", default="seafood", choices=sorted(BRANDS))
    ap.add_argument("--date", default="24 SEPTEMBER 2026")
    a = ap.parse_args()
    b = BRANDS[a.edition]
    out = os.path.join(ASSETS, "graphics")
    print(masthead(b, os.path.join(out, "masthead_%s.png" % a.edition), a.date))
    print(closing(b, os.path.join(out, "closing_%s.png" % a.edition)))
    print(deck_band(b, os.path.join(out, "deck_band_%s.png" % a.edition)))
