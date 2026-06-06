"""Audit .bbmodel models for cubes that look 'detached' (a visible gap to every
other cube). Reports cube NAMES so structural gaps are easy to find/fix.

gap(A,B) = largest per-axis separation needed to make the boxes touch. A cube whose
nearest neighbour gap > THRESHOLD is flagged. Toggle/animation parts (glow, flame,
water, blades, flag, wings, lid, screen, bubble) are expected to float and are skipped.
"""
import glob
import json
import os

HERE = os.path.dirname(__file__)
THRESHOLD = 0.3
SKIP = ("glow", "flame", "water", "basin_pool", "blade", "flag", "wing", "lid",
        "screen", "bubble", "rock", "tw_", "twinkle")


def gap(a, b):
    g = 0.0
    for i in range(3):
        sep = max(a[0][i] - b[1][i], b[0][i] - a[1][i], 0.0)
        g = max(g, sep)
    return g


def audit(path):
    model = json.load(open(path, encoding="utf-8"))
    els = [(e.get("name", "?"), (e["from"], e["to"])) for e in model.get("elements", [])]
    out = []
    for i, (name, box) in enumerate(els):
        best = min((gap(box, other) for j, (_, other) in enumerate(els) if j != i), default=999)
        if best > THRESHOLD and not any(k in name for k in SKIP):
            out.append((name, round(best, 2)))
    return out


def main():
    for path in sorted(glob.glob(os.path.join(HERE, "*.bbmodel"))):
        sid = os.path.basename(path)[:-len(".bbmodel")]
        fl = audit(path)
        if fl:
            print(f"{sid}: " + ", ".join(f"{n}({g})" for n, g in fl))


if __name__ == "__main__":
    main()
