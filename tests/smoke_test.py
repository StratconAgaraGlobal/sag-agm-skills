#!/usr/bin/env python3
"""Build every reference output for both brands and check the files exist.

    python tests/smoke_test.py

Needs python-docx, python-pptx and Pillow. Fonts are not required to build
(they are embedded / only matter for rendering).
"""
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SK = os.path.join(ROOT, "skills")

JOBS = [
    ("sag-brand", ["build_doc.py", "--out", "{t}/sag_doc.docx"]),
    ("sag-brand", ["build_mom.py", "--out", "{t}/sag_mom.docx"]),
    ("sag-brand", ["build_deck.py", "--out", "{t}/sag_deck.pptx"]),
    ("sag-brand", ["build_example_html.py", "--out", "{t}/sag.html"]),
]
for ed in ("seafood", "marine"):
    JOBS += [
        ("agm-brand", ["build_doc.py", "--edition", ed, "--out", "{t}/agm_doc_%s.docx" % ed]),
        ("agm-brand", ["build_mom.py", "--brand", ed, "--out", "{t}/agm_mom_%s.docx" % ed]),
        ("agm-brand", ["build_deck.py", "--edition", ed, "--out", "{t}/agm_deck_%s.pptx" % ed]),
    ]
JOBS.append(("agm-brand", ["build_example_html.py", "--out", "{t}/agm.html"]))


def main():
    fails = 0
    with tempfile.TemporaryDirectory() as t:
        for skill, args in JOBS:
            args = [a.replace("{t}", t) for a in args]
            cwd = os.path.join(SK, skill, "scripts")
            r = subprocess.run([sys.executable] + args, cwd=cwd, capture_output=True, text=True)
            out = args[args.index("--out") + 1]
            ok = r.returncode == 0 and os.path.getsize(out) > 5000
            print("%-4s %s %s" % ("ok" if ok else "FAIL", skill, " ".join(args[:1] + args[1:-1:2][:0])))
            if not ok:
                fails += 1
                print(r.stdout[-500:], r.stderr[-1500:])
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
