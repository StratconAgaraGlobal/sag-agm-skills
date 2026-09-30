#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Install Plus Jakarta Sans (the SAG brand typeface) if it is not already there.

    python install_fonts.py            # install whatever is missing, skip the rest
    python install_fonts.py --check    # only report, change nothing

For each of the five weights the design uses (Regular, Medium, SemiBold, Bold,
ExtraBold) the script first checks whether the font is already installed and
skips it if so. Anything missing is fetched from Google Fonts, and if Google
Fonts cannot be reached (offline, firewall) it falls back to the copies bundled
in ../assets/fonts, so it always finishes. The typeface is SIL OFL 1.1, which
allows redistribution (licence in ../assets/fonts/OFL.txt).

Installs are per-user and need no admin rights:
  Windows  %LOCALAPPDATA%\\Microsoft\\Windows\\Fonts  (+ HKCU registry entry)
  macOS    ~/Library/Fonts
  Linux    ~/.local/share/fonts/PlusJakartaSans  (+ fc-cache)

Standard library only. Exit code 0 = all five weights available afterwards.
"""
import argparse
import glob
import io
import os
import platform
import shutil
import subprocess
import sys
import urllib.request
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
BUNDLED = os.path.join(os.path.dirname(HERE), "assets", "fonts")

FAMILY = "Plus Jakarta Sans"
# style -> (file name, Windows registry / full font name)
WEIGHTS = {
    "Regular":   ("PlusJakartaSans-Regular.ttf",   "Plus Jakarta Sans"),
    "Medium":    ("PlusJakartaSans-Medium.ttf",    "Plus Jakarta Sans Medium"),
    "SemiBold":  ("PlusJakartaSans-SemiBold.ttf",  "Plus Jakarta Sans SemiBold"),
    "Bold":      ("PlusJakartaSans-Bold.ttf",      "Plus Jakarta Sans Bold"),
    "ExtraBold": ("PlusJakartaSans-ExtraBold.ttf", "Plus Jakarta Sans ExtraBold"),
}

# The family zip behind the "Download family" button on fonts.google.com; its
# static/ folder holds one TTF per weight.
GOOGLE_ZIP = "https://fonts.google.com/download?family=Plus%20Jakarta%20Sans"


def log(msg):
    print(msg, flush=True)


# ------------------------------------------------------------------ paths --
def system():
    return {"Windows": "windows", "Darwin": "mac"}.get(platform.system(), "linux")


def user_font_dir():
    s = system()
    if s == "windows":
        base = os.environ.get("LOCALAPPDATA") or os.path.expanduser(r"~\AppData\Local")
        return os.path.join(base, "Microsoft", "Windows", "Fonts")
    if s == "mac":
        return os.path.expanduser("~/Library/Fonts")
    return os.path.expanduser("~/.local/share/fonts/PlusJakartaSans")


def search_dirs():
    s = system()
    if s == "windows":
        return [os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts"),
                user_font_dir()]
    if s == "mac":
        return ["/Library/Fonts", "/System/Library/Fonts",
                os.path.expanduser("~/Library/Fonts")]
    return ["/usr/share/fonts", "/usr/local/share/fonts",
            os.path.expanduser("~/.local/share/fonts"),
            os.path.expanduser("~/.fonts")]


# -------------------------------------------------------------- detection --
def _file_present(fname):
    """Same file name anywhere in the font folders (case-insensitive)."""
    want = fname.lower()
    for d in search_dirs():
        if not os.path.isdir(d):
            continue
        for root, _dirs, files in os.walk(d):
            if any(f.lower() == want for f in files):
                return True
    return False


def _fontconfig_styles():
    """Styles fontconfig knows for the family (covers variable-font installs)."""
    if not shutil.which("fc-list"):
        return set()
    try:
        out = subprocess.run(["fc-list", FAMILY, "style"], capture_output=True,
                             text=True, timeout=30).stdout
    except Exception:
        return set()
    found = set()
    for line in out.splitlines():
        for part in line.replace(":style=", ",").split(","):
            found.add(part.strip().replace(" ", "").lower())
    return found


def _registry_names():
    if system() != "windows":
        return set()
    try:
        import winreg
    except ImportError:
        return set()
    names = set()
    for hive in (winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE):
        try:
            key = winreg.OpenKey(
                hive, r"Software\Microsoft\Windows NT\CurrentVersion\Fonts")
        except OSError:
            continue
        i = 0
        while True:
            try:
                names.add(winreg.EnumValue(key, i)[0].lower())
            except OSError:
                break
            i += 1
    return names


def installed_status():
    """{style: True/False} for the five weights."""
    fc = _fontconfig_styles()
    reg = _registry_names()
    status = {}
    for style, (fname, full) in WEIGHTS.items():
        ok = _file_present(fname)
        if not ok and fc:
            ok = style.lower() in fc
        if not ok and reg:
            ok = any(n.startswith(full.lower() + " (") for n in reg)
        status[style] = ok
    return status


# ------------------------------------------------------------------ fetch --
def _get(url, timeout=40):
    req = urllib.request.Request(url, headers={"User-Agent": "sag-brand-skill/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def _looks_like_ttf(data):
    return len(data) > 50_000 and data[:4] in (b"\x00\x01\x00\x00", b"true", b"OTTO")


def fetch_from_google(missing, zip_url=GOOGLE_ZIP):
    """Return ({style: bytes}, source label) for the missing styles."""
    got = {}
    try:
        z = zipfile.ZipFile(io.BytesIO(_get(zip_url, timeout=90)))
        by_base = {os.path.basename(n): n for n in z.namelist()}
        for style in missing:
            fname = WEIGHTS[style][0]
            if fname in by_base:
                data = z.read(by_base[fname])
                if _looks_like_ttf(data):
                    got[style] = data
        if got:
            log("  source: Google Fonts (family download)")
    except Exception as e:  # network blocked, endpoint changed, bad zip ...
        log("  Google Fonts zip not available (%s)" % _short(e))
    return got


def _short(e):
    return str(e).splitlines()[0][:90]


def fetch_bundled(styles):
    got = {}
    for style in styles:
        p = os.path.join(BUNDLED, WEIGHTS[style][0])
        if os.path.isfile(p):
            got[style] = open(p, "rb").read()
            log("  source: bundled copy (%s)" % WEIGHTS[style][0])
    return got


# ---------------------------------------------------------------- install --
def install(style, data):
    fname, full = WEIGHTS[style]
    dest_dir = user_font_dir()
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, fname)
    with open(dest, "wb") as f:
        f.write(data)
    if system() == "windows":
        try:
            import winreg
            key = winreg.CreateKey(
                winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows NT\CurrentVersion\Fonts")
            winreg.SetValueEx(key, full + " (TrueType)", 0, winreg.REG_SZ, dest)
        except Exception as e:
            log("  could not register %s in the registry (%s)" % (fname, _short(e)))
    return dest


def refresh_caches():
    s = system()
    if s == "linux" and shutil.which("fc-cache"):
        subprocess.run(["fc-cache", "-f", user_font_dir()],
                       capture_output=True, timeout=120)
    elif s == "windows":
        try:  # ask running apps to re-read the font table
            import ctypes
            ctypes.windll.user32.SendMessageTimeoutW(
                0xFFFF, 0x001D, 0, 0, 0x0002, 1000, None)
        except Exception:
            pass


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="report only, install nothing")
    ap.add_argument("--force", action="store_true", help="reinstall even if present")
    ap.add_argument("--offline", action="store_true",
                    help="skip Google Fonts, use the bundled copies")
    ap.add_argument("--url", help=argparse.SUPPRESS)  # test hook: alternate zip URL
    args = ap.parse_args()

    status = installed_status()
    for style, ok in status.items():
        log("  %-9s %s" % (style, "installed" if ok else "missing"))
    missing = [s for s, ok in status.items() if args.force or not ok]

    if not missing:
        log("Plus Jakarta Sans is already installed - nothing to do.")
        return 0
    if args.check:
        log("Missing weights: %s" % ", ".join(missing))
        return 1

    log("Installing: %s" % ", ".join(missing))
    got = {} if args.offline else fetch_from_google(missing, args.url or GOOGLE_ZIP)
    rest = [s for s in missing if s not in got]
    if rest:
        if not args.offline:
            log("Falling back to the copies bundled with the skill for: %s" % ", ".join(rest))
        got.update(fetch_bundled(rest))

    for style, data in got.items():
        log("  installed %s -> %s" % (style, install(style, data)))
    refresh_caches()

    final = installed_status()
    bad = [s for s, ok in final.items() if not ok]
    if bad:
        log("STILL MISSING: %s" % ", ".join(bad))
        return 1
    log("Done - all five weights of Plus Jakarta Sans are installed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
