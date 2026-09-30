# -*- coding: utf-8 -*-
"""The Complexity Line.

Many tangled strands travelling left to right, converging into one clean line,
carrying the tagline in the middle. Seeded, so every render is identical.
Horizontal only -- there is no vertical form of this device.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FD = os.path.join(os.path.dirname(HERE), "assets", "fonts")


def seeded(a):
    """mulberry32 -- same sequence in JS and Python, so renders match."""
    st = {"a": a & 0xFFFFFFFF}

    def rnd():
        st["a"] = (st["a"] + 0x6D2B79F5) & 0xFFFFFFFF
        a0 = st["a"]
        t = ((a0 ^ (a0 >> 15)) * (1 | a0)) & 0xFFFFFFFF
        t = (t + (((t ^ (t >> 7)) * (61 | t)) & 0xFFFFFFFF)) & 0xFFFFFFFF
        t ^= a0
        return ((t ^ (t >> 14)) & 0xFFFFFFFF) / 4294967296.0
    return rnd


def hexc(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def blend(fg, bg, o):
    return tuple(int(round(f * o + b * (1 - o))) for f, b in zip(fg, bg))


def build(path, ground, pale, cap, tag1, tag2, dot,
          seed=7, strands=56, fs=30, S=4, tagline=True, cross=300):
    L, C = 1600, cross
    W, H = L, C
    cx, mid = 600, C / 2.0
    spread = C * 0.40
    bg, PALE, CAP = hexc(ground), hexc(pale), hexc(cap)

    img = Image.new("RGB", (W * S, H * S), bg)
    d = ImageDraw.Draw(img)
    rnd = seeded(seed)

    textW = 22 * fs * 0.70
    stubEnd = cx + 92
    mCentre = stubEnd + 46 + textW / 2
    tailStart = (mCentre + textW / 2 + 46) if tagline else stubEnd
    tailEnd = L - 56

    dots = []
    for i in range(strands):
        t0 = rnd() * rnd() * 0.44
        off = ((i / (strands - 1)) * 2 - 1) * spread + (rnd() * 2 - 1) * 24
        f1, ph1, a1 = 1.3 + rnd() * 3.6, rnd() * 6.283, 24 + rnd() * 60
        f2, ph2, a2 = 3.0 + rnd() * 5.4, rnd() * 6.283, 10 + rnd() * 28
        xf, xph, xa = 0.9 + rnd() * 2.4, rnd() * 6.283, 16 + rnd() * 36
        K, pts = 30, []
        for k in range(K + 1):
            t = t0 + (1 - t0) * (k / K)
            env = pow(1 - t, 1.45)
            al = t * cx + env * math.sin(t * xf * 6.283 + xph) * xa
            cr = mid + env * (off + math.sin(t * f1 * 6.283 + ph1) * a1
                              + math.sin(t * f2 * 6.283 + ph2) * a2)
            pts.append((al, cr))
        op, wd = 0.20 + rnd() * 0.5, 0.6 + rnd() * 0.9
        d.line([(x * S, y * S) for x, y in pts], fill=blend(PALE, bg, op),
               width=max(1, int(round(wd * S))), joint="curve")
        if rnd() < 0.4:
            dots.append((pts[int(rnd() * K * 0.78)], 1.2 + rnd() * 1.9))
    for (qx, qy), r in dots:
        d.ellipse([(qx - r) * S, (qy - r) * S, (qx + r) * S, (qy + r) * S],
                  fill=blend(PALE, bg, 0.6))

    def seg(a, b, col, w):
        d.line([(a * S, mid * S), (b * S, mid * S)], fill=col,
               width=max(1, int(round(w * S))))
    seg(cx, stubEnd, blend(PALE, bg, 0.95), 2.2)
    seg(tailStart, tailEnd, CAP, 2.2)
    r = 4.5
    d.ellipse([(tailEnd - r) * S, (mid - r) * S, (tailEnd + r) * S,
               (mid + r) * S], fill=hexc(dot))

    if tagline:
        f = ImageFont.truetype(
            os.path.join(FD, "PlusJakartaSans-ExtraBold.ttf"), int(fs * S))
        ls = fs * 0.085 * S

        def track(txt, cxp, cyp, col):
            ws = [d.textlength(c, font=f) for c in txt]
            x = cxp - (sum(ws) + ls * (len(txt) - 1)) / 2
            for c, w in zip(txt, ws):
                d.text((x, cyp), c, font=f, fill=col, anchor="ls")
                x += w + ls
        track("NAVIGATING COMPLEXITY,", mCentre * S, (mid - fs * 0.26) * S,
              hexc(tag1))
        track("DELIVERING SIMPLICITY", mCentre * S, (mid + fs * 1.06) * S,
              hexc(tag2))

    img.resize((W * 2, H * 2), Image.LANCZOS).save(path, "PNG")
    return path
