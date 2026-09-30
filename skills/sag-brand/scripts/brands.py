# -*- coding: utf-8 -*-
"""Brand configuration objects consumed by components.BrandDoc."""
import os

import graphics
from palette import BLUE

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(HERE), "assets")


class Brand:
    """Everything BrandDoc needs to know about a brand."""
    key = "sag"
    name = "PT Stratcon Agara Global"
    wordmark = "PT STRATCON AGARA GLOBAL"
    footer_tagline = "Navigating complexity, delivering simplicity"
    P = BLUE
    # Colour for small tracked labels, item numbers and the page number on
    # light grounds. SAG Yellow must never be used as text on light, so META.
    LBL = BLUE["META"]
    header_logo = os.path.join(ASSETS, "logo", "sag-logo.png")
    contact = dict(email="ahmed.khalifa@stratconagaraglobal.com",
                   phone="+62 812 10020646", org="PT Stratcon Agara Global")

    def masthead(self, out, date):
        return graphics.masthead(out, date=date)

    def closing(self, out):
        return graphics.closing(out)


SAG = Brand()
BRANDS = {"sag": SAG}
DEFAULT = "sag"
