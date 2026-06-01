"""Re-skin the furniture entity atlases with the "cute" toilet-atlas style.

Problem:
  Each furniture entity ships its own 64x64 atlas, but the dining/chair/barrel/
  doll atlases were mostly flat solid-color cells. The models therefore render
  as plain blocks of colour. The toilet atlas, by contrast, fills every 16x16
  cell with a pastel base PLUS little sparkles / droplet speckles / soft shading,
  which reads as cute and varied.

Fix:
  For every 16x16 cell we KEEP that cell's existing base colour (so each part of
  every model stays the colour it already is) and overlay the toilet-style
  detail: vertical shading, scattered sparkles, and pale droplet speckles. Cells
  that are essentially empty/transparent are left untouched.

  Because furniture UVs map full 16x16 cells, the detail lands exactly where the
  model samples it -> editor preview AND in-game both look cute.

Run:
  python blockbench/gen_cute_furniture_atlases.py
"""
import os
import random
from collections import Counter

from PIL import Image

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "addon", "resource_pack"))

ATLASES = [
    "unicorn_dining_table/unicorn_dining_table_atlas.png",
    "unicorn_chair/unicorn_chair_atlas.png",
    "unicorn_barrel_cabinet/unicorn_barrel_cabinet_atlas.png",
    "decorative_unicorn_doll/decorative_unicorn_doll_atlas.png",
]

CELL = 16
GRID = 64 // CELL


def clamp(v):
    return max(0, min(255, int(round(v))))


def lighten(c, amt):
    return (clamp(c[0] + amt), clamp(c[1] + amt), clamp(c[2] + amt), c[3])


def mix(c, other, t):
    return (
        clamp(c[0] * (1 - t) + other[0] * t),
        clamp(c[1] * (1 - t) + other[1] * t),
        clamp(c[2] * (1 - t) + other[2] * t),
        c[3],
    )


def luminance(c):
    return 0.299 * c[0] + 0.587 * c[1] + 0.114 * c[2]


def cell_base_color(img, cx, cy):
    """Most common fully-opaque colour in a cell; None if cell is ~empty."""
    counts = Counter()
    for y in range(cy, cy + CELL):
        for x in range(cx, cx + CELL):
            r, g, b, a = img.getpixel((x, y))
            if a >= 250:
                counts[(r, g, b, 255)] += 1
    if not counts:
        return None
    color, n = counts.most_common(1)[0]
    if n < (CELL * CELL) * 0.15:
        return None
    return color


PINK = (244, 158, 214)
LAVENDER = (176, 158, 222)
WHITE = (255, 255, 255)


def decorate_cell(img, cx, cy, base, rng):
    light = lighten(base, 16)
    shade = lighten(base, -18)

    # base fill + soft vertical shading (top lighter, bottom darker)
    for y in range(cy, cy + CELL):
        row = y - cy
        if row <= 2:
            col = light
        elif row >= CELL - 3:
            col = shade
        else:
            col = base
        for x in range(cx, cx + CELL):
            img.putpixel((x, y), col)

    is_light = luminance(base) > 175
    # droplet speckle colour: pale accent on light cells, white-ish on saturated
    if is_light:
        droplet = mix(base, PINK if rng.random() < 0.5 else LAVENDER, 0.55)
        sparkle = lighten(base, -22)
    else:
        droplet = lighten(base, 40)
        sparkle = (255, 255, 255, 255)

    # scattered droplet speckles ("방울")
    for _ in range(rng.randint(4, 6)):
        px = cx + rng.randint(2, CELL - 3)
        py = cy + rng.randint(2, CELL - 3)
        img.putpixel((px, py), droplet)
        if rng.random() < 0.4:
            img.putpixel((px, min(cy + CELL - 1, py + 1)), mix(droplet, base, 0.4))

    # a couple of plus-shaped sparkles
    for _ in range(rng.randint(1, 2)):
        px = cx + rng.randint(3, CELL - 4)
        py = cy + rng.randint(3, CELL - 4)
        img.putpixel((px, py), sparkle)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            img.putpixel((px + dx, py + dy), mix(sparkle, base, 0.45))


def process(path, seed):
    full = os.path.join(BASE, "textures", "entity", path)
    img = Image.open(full).convert("RGBA")
    if img.size != (64, 64):
        raise SystemExit(f"{path} is {img.size}, expected (64,64)")
    rng = random.Random(seed)
    decorated = 0
    for gy in range(GRID):
        for gx in range(GRID):
            cx, cy = gx * CELL, gy * CELL
            base = cell_base_color(img, cx, cy)
            if base is None:
                continue
            decorate_cell(img, cx, cy, base, rng)
            decorated += 1
    img.save(full)
    print(f"decorated {decorated} cells -> {path}")


def main():
    for i, path in enumerate(ATLASES):
        process(path, seed=1000 + i)


if __name__ == "__main__":
    main()
