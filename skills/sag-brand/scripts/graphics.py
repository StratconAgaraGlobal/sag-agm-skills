# -*- coding: utf-8 -*-
"""The two banner graphics: the masthead lockup and the closing band.

Word cannot round a table corner, so these ship as images with the rounding
baked in. Corners are filled with the page colour rather than left
transparent, so they survive printing and viewers that drop the page ground.
"""
import os
import tempfile

from PIL import Image, ImageDraw, ImageFont

import cline
from palette import BLUE

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(HERE), "assets")
FD = os.path.join(ASSETS, "fonts")
OUT = os.path.join(ASSETS, "graphics")

PX = 20                # px per mm
W_MM = 170.0           # A4 content measure
TOP_MM = 25.1          # logo / wordmark zone
BAND_MM = 30.9         # complexity line zone
RAD_MM = 2.5

DEVICE = dict(ground=BLUE["PANEL"], pale=BLUE["PALE"], cap=BLUE["PAPER"],
              tag1="FFFFFF", tag2=BLUE["ACCENT"], dot=BLUE["ACCENT"])


def hexc(h):
    return cline.hexc(h)


def font(name, pt, px=PX):
    return ImageFont.truetype(os.path.join(FD, name),
                              int(round(pt * 0.3528 * px)))


def track(d, txt, f, x, y, fill, em, anchor="ls"):
    ls = f.size * em
    ws = [d.textlength(c, font=f) for c in txt]
    if anchor == "rs":
        x -= sum(ws) + ls * (len(txt) - 1)
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


def band(w_px, h_px, square=False):
    # temp file, not the skill folder: the skill directory may be read-only
    fd, tmp = tempfile.mkstemp(suffix=".png")
    os.close(fd)
    cline.build(tmp, cross=int(round(1600.0 * h_px / w_px)), S=4, **DEVICE)
    im = Image.open(tmp).convert("RGB").resize((w_px, h_px), Image.LANCZOS)
    os.remove(tmp)
    return im


def masthead(out, date="24 SEPTEMBER 2026", w_mm=W_MM, px=PX):
    w, top, bnd = int(w_mm * px), int(TOP_MM * px), int(BAND_MM * px)
    img = Image.new("RGB", (w, top + bnd), hexc(BLUE["PANEL"]))
    img.paste(band(w, bnd), (0, top))
    d = ImageDraw.Draw(img)

    logo = Image.open(os.path.join(ASSETS, "logo", "sag-logo-plated.png")).convert("RGBA")
    lh = int(11.5 * px)
    logo = logo.resize((int(round(lh * logo.size[0] / logo.size[1])), lh),
                       Image.LANCZOS)
    img.paste(logo, (int(5 * px), (top - lh) // 2), logo)

    x = int(26 * px)
    track(d, "PT STRATCON AGARA GLOBAL", font("PlusJakartaSans-ExtraBold.ttf", 10.5, px),
          x, int(12.6 * px), hexc(BLUE["PAPER"]), 0.10)
    track(d, "Strategic advisory  ·  Regulatory affairs  ·  ESG",
          font("PlusJakartaSans-Regular.ttf", 7.2, px), x, int(15.2 * px),
          hexc(BLUE["PALE"]), 0.09)
    track(d, date, font("PlusJakartaSans-SemiBold.ttf", 7.5, px),
          int((w_mm - 5) * px), int(13.5 * px), hexc(BLUE["PALE"]), 0.16,
          anchor="rs")

    d.line([(int(5 * px), top), (int((w_mm - 5) * px), top)],
           fill=cline.blend(hexc(BLUE["PALE"]), hexc(BLUE["PANEL"]), 0.16),
           width=2)

    rounded(img, int(RAD_MM * px), BLUE["PAPER"]).save(out, "PNG")
    return out


def closing(out, w_mm=W_MM, px=PX):
    w, h = int(w_mm * px), int(BAND_MM * px)
    rounded(band(w, h), int(RAD_MM * px), BLUE["PAPER"]).save(out, "PNG")
    return out


def deck_band(out, w_mm, h_mm, px=10):
    """Full-bleed band for slides -- square corners, it runs to the edges."""
    band(int(w_mm * px), int(h_mm * px)).save(out, "PNG")
    return out


if __name__ == "__main__":
    print(masthead(os.path.join(OUT, "masthead_blue.png")))
    print(closing(os.path.join(OUT, "closing_blue.png")))
    print(deck_band(os.path.join(OUT, "deck_band_blue.png"), 338.667, 52.0))
