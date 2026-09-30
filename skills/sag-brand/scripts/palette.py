# -*- coding: utf-8 -*-
"""SAG Graphite & Slate ("Blue") palette, by role.

Colours are named for the job they do, not for what they look like, so the
same build code can be re-skinned. Yellow is an accent only -- it appears on
the Complexity Line tagline and nowhere else by default.
"""

BLUE = {
    "PAPER":  "EFF3F4",   # page ground
    "PANEL":  "1B3038",   # dark panels: masthead, section bands, contact
    "INK":    "16181A",   # document title, question text
    "BODY":   "2C4550",   # body copy
    "META":   "3A5560",   # eyebrows, item numbers, page number
    "MUTED":  "63696C",   # small labels, counts
    "TINT":   "E2E6E7",   # fill for response boxes and the callout
    "RULE":   "8FA3AB",   # hairline on TINT
    "PALE":   "B8C6CC",   # text on PANEL, header hairline
    "ACCENT": "F9C939",   # SAG Yellow -- tagline and single accents only
    "GOLD":   "C9A227",   # deep gold, sparing
}

SAG = BLUE   # alias: older notes/scripts say `from palette import SAG as P`

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
