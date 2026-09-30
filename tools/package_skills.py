#!/usr/bin/env python3
"""Zip each skill in skills/ into dist/<name>.skill (installable in Claude).

    python tools/package_skills.py            # all skills
    python tools/package_skills.py sag-brand  # one skill
"""
import os
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
DIST = os.path.join(ROOT, "dist")
SKIP_DIRS = {"__pycache__", ".git"}
SKIP_FILES = {".DS_Store", "Thumbs.db"}


def package(name):
    src = os.path.join(SKILLS, name)
    if not os.path.isfile(os.path.join(src, "SKILL.md")):
        sys.exit("%s: no SKILL.md" % name)
    os.makedirs(DIST, exist_ok=True)
    out = os.path.join(DIST, name + ".skill")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for base, dirs, files in os.walk(src):
            dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
            for f in sorted(files):
                if f in SKIP_FILES or f.endswith(".pyc"):
                    continue
                p = os.path.join(base, f)
                z.write(p, os.path.relpath(p, SKILLS))
    print("%s  %.1f MB" % (out, os.path.getsize(out) / 1e6))


if __name__ == "__main__":
    names = sys.argv[1:] or sorted(d for d in os.listdir(SKILLS)
                                   if os.path.isdir(os.path.join(SKILLS, d)))
    for n in names:
        package(n)
