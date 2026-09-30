# -*- coding: utf-8 -*-
"""AGM brand editions consumed by components.BrandDoc (and the deck builder).

Seafood is the default edition. Marine is for FRP shipbuilding / Harvester
vessels / charter / marine services.
"""
import os

import graphics
from palette import SEAFOOD, MARINE

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(HERE), "assets")
LOGO = os.path.join(ASSETS, "logo")
PHOTO = os.path.join(ASSETS, "photos")

CONTACT = dict(phone="+62 819-231-001", web="www.agmaritim.com",
               email="corporate@stratconagaraglobal.com",
               address="Marunda, North Jakarta, Indonesia")


class Edition:
    key = ""
    name = "PT Agara Global Maritim"
    short = "AGM"
    wordmark = "PT AGARA GLOBAL MARITIM"
    descriptor = ""
    tagline1 = tagline2 = footer_tagline = ""
    P = None
    LBL = None
    header_logo = emblem_white = photo = ""
    photo_y = 0.5           # vertical crop position: 0 = top, 1 = bottom
    contact = CONTACT

    def masthead(self, out, date):
        return graphics.masthead(self, out, date=date)

    def closing(self, out):
        return graphics.closing(self, out)

    def deck_band(self, out, w_mm=338.667, h_mm=52.0):
        return graphics.deck_band(self, out, w_mm, h_mm)


class Seafood(Edition):
    key = "seafood"
    P = SEAFOOD
    LBL = SEAFOOD["ACCENT"]            # ocean blue reads well on light
    descriptor = "Sea Cucumber (Teripang)  ·  Processing & Export  ·  Indonesia"
    tagline1 = "SOURCED AND PROCESSED IN INDONESIA"
    tagline2 = "PROCESSED TO A HIGHER STANDARD"
    footer_tagline = ("Premium Indonesian sea cucumber, processed to a "
                      "higher standard")
    header_logo = os.path.join(LOGO, "agm-emblem-navy.png")
    emblem_white = os.path.join(LOGO, "agm-emblem-white.png")
    photo = os.path.join(PHOTO, "sea-cucumber-warehouse.jpg")
    photo_y = 0.45


class Marine(Edition):
    key = "marine"
    P = MARINE
    LBL = MARINE["META"]               # brass must never be text on light
    descriptor = "FRP Shipbuilding & Marine Services  ·  Jakarta, Indonesia"
    tagline1 = "HARVESTER SERIES  |  MADE IN INDONESIA"
    tagline2 = "BUILT FOR YOUR OPERATIONS"
    footer_tagline = "Fiberglass vessels for commercial marine operations"
    header_logo = os.path.join(LOGO, "agm-emblem-green.png")
    emblem_white = os.path.join(LOGO, "agm-emblem-white.png")
    photo = os.path.join(PHOTO, "harvester-vessel.jpg")
    photo_y = 0.30


SEAFOOD_ED = Seafood()
MARINE_ED = Marine()
BRANDS = {"seafood": SEAFOOD_ED, "marine": MARINE_ED}
DEFAULT = "seafood"
