# -*- coding: utf-8 -*-
"""AGM palettes by role, fonts and geometry.

AGM uses the SAG component system (same geometry, type, components and
restraint) with its own colours. The eleven roles are the same as SAG's;
ACCENT_ON_DARK is the accent as it appears on PANEL (brass and ocean blue
both need a lighter/other value on light grounds).

Colours are named for the job they do, not for what they look like, so the
same build code re-skins by swapping the dict.
"""

SEAFOOD = {                      # default: sea cucumber, processing, export
    "PAPER":  "F5F9FD",          # page ground; text on dark panels
    "PANEL":  "052240",          # deep navy: masthead, bands, contact, dark slides
    "INK":    "012864",          # titles, item text, slide headlines
    "BODY":   "3F4F63",          # body copy
    "META":   "3980C3",          # eyebrows, item numbers, page number
    "MUTED":  "55657A",          # small labels, counts, footers
    "TINT":   "EAF3FB",          # callouts, response boxes, slide cards
    "RULE":   "8FB4DA",          # hairlines, bullet dashes
    "PALE":   "C9DCEF",          # text on PANEL; header hairline
    "ACCENT": "3980C3",          # ocean blue
    "ACCENT_ON_DARK": "8FB4DA",  # accent on PANEL (tagline line 2, dots)
}

MARINE = {                       # FRP shipbuilding, Harvester vessels, charter
    "PAPER":  "F6F8F7",
    "PANEL":  "0D2A2B",          # harbour green
    "INK":    "0D2A2B",
    "BODY":   "3E5754",
    "META":   "2D5352",
    "MUTED":  "526C68",
    "TINT":   "EAF0EE",
    "RULE":   "A3B9B5",
    "PALE":   "C9D6D3",
    "ACCENT": "C4A56A",          # brass - never as text on a light ground
    "ACCENT_ON_DARK": "C4A56A",
}

EDITIONS = {"seafood": SEAFOOD, "marine": MARINE}

# Plus Jakarta Sans ships each weight as its own Windows family, so weight is
# selected by family name -- not by the bold flag, except for 700.
F400 = "Plus Jakarta Sans"
F500 = "Plus Jakarta Sans Medium"
F600 = "Plus Jakarta Sans SemiBold"
F800 = "Plus Jakarta Sans ExtraBold"

EMBED = [(F400, "PlusJakartaSans-Regular.ttf", "PlusJakartaSans-Bold.ttf"),
         (F500, "PlusJakartaSans-Medium.ttf", None),
         (F600, "PlusJakartaSans-SemiBold.ttf", None),
         (F800, "PlusJakartaSans-ExtraBold.ttf", None)]

# ---------------------------------------------------------------- geometry --
PAGE = dict(w=210.0, h=297.0, ml=20.0, mr=20.0, mt=14.0, mb=16.0,
            header=9.0, footer=9.0)
W = PAGE["w"] - PAGE["ml"] - PAGE["mr"]      # 170mm content measure
GUTTER = 15.0                                # item-number column
RADIUS = 2.5                                 # panel corner radius

SLIDE = dict(w=338.667, h=190.5, ml=18.0, mr=18.0)   # 16:9, mm
