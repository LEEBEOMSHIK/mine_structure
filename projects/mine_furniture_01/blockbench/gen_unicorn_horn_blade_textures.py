"""Generate textures for mine_structure:unicorn_horn_blade.

Outputs:
  - 16x16 inventory icon: textures/items/unicorn_horn_blade.png
  - 64x64 3D attachable atlas: textures/entity/unicorn_horn_blade/unicorn_horn_blade.png

The 3D model uses EXPLICIT PER-FACE UV (not box UV): the blade cubes are small
(0.5-2.6 units) and box UV collapses to near-zero-width regions, which made the
horn render white. Instead every face points at a flat colour swatch, so each
part shows a clear solid colour. Swatch rectangles in the atlas (must match the
per-face uv in unicorn_horn_blade.geo.json):
  horn (segments + tip) -> [0,0]  size 16x16  (rainbow pearl spiral, NOT white)
  grip                  -> [16,0] size 8x8    (lavender)
  pommel                -> [24,0] size 8x8    (gold)
  base_glow             -> [32,0] size 8x8    (cyan)
  guard (rainbow, per face):
    north [40,0] south [48,0] east [56,0] west [40,8] up [48,8] down [56,8]  size 8x8
"""
import os
import random
import base64
import json
from PIL import Image

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "addon", "resource_pack"))
BBMODEL = os.path.join(os.path.dirname(__file__), "unicorn_horn_blade.bbmodel")

HORN = (236, 130, 200, 255)
HORN_DK = (198, 92, 168, 255)
HORN_HI = (255, 226, 246, 255)
LAVENDER = (176, 158, 222, 255)
GOLD = (247, 214, 110, 255)
CYAN = (150, 232, 244, 255)
WHITE = (255, 255, 255, 255)
CLEAR = (0, 0, 0, 0)
PINK = (244, 158, 214, 255)
PINK_DK = (216, 112, 184, 255)
LAVENDER_DK = (138, 120, 188, 255)
GOLD_DK = (206, 165, 70, 255)
RAINBOW = [
    (244, 120, 120, 255),  # north red
    (247, 184, 110, 255),  # south orange
    (247, 233, 120, 255),  # east yellow
    (150, 224, 150, 255),  # west green
    (140, 196, 244, 255),  # up blue
    (186, 150, 232, 255),  # down purple
]
HORN_RAINBOW = [
    (255, 116, 151, 255),
    (255, 177, 92, 255),
    (255, 232, 104, 255),
    (126, 222, 167, 255),
    (111, 193, 255, 255),
    (181, 136, 244, 255),
    (246, 136, 215, 255),
]
HORN_SHADOW = [
    (219, 78, 128, 255),
    (222, 132, 48, 255),
    (218, 190, 62, 255),
    (76, 171, 122, 255),
    (64, 143, 218, 255),
    (132, 91, 204, 255),
    (203, 87, 179, 255),
]


def fill(img, x0, y0, x1, y1, color):
    for y in range(y0, y1):
        for x in range(x0, x1):
            img.putpixel((x, y), color)


# ---------------------------------------------------------------- 3D atlas
atlas = Image.new("RGBA", (64, 64), HORN)  # opaque base so nothing reads white

# horn swatch [0,0]-[16,16]: rainbow pearl spiral, never white
for y in range(16):
    for x in range(16):
        band = ((x + y) // 3) % len(HORN_RAINBOW)
        if (x - y) % 6 == 0:
            atlas.putpixel((x, y), HORN_SHADOW[band])
        elif (x + y) % 7 == 1:
            atlas.putpixel((x, y), HORN_HI)
        else:
            atlas.putpixel((x, y), HORN_RAINBOW[band])
rng = random.Random(7)
for _ in range(10):
    atlas.putpixel((rng.randint(1, 14), rng.randint(1, 14)), (255, 244, 168, 255))

# grip swatch [16,0]-[24,8]
fill(atlas, 16, 0, 24, 8, LAVENDER)
fill(atlas, 16, 0, 24, 1, LAVENDER_DK)
fill(atlas, 16, 7, 24, 8, LAVENDER_DK)

# pommel swatch [24,0]-[32,8]
fill(atlas, 24, 0, 32, 8, GOLD)
fill(atlas, 24, 7, 32, 8, GOLD_DK)

# base_glow swatch [32,0]-[40,8]
fill(atlas, 32, 0, 40, 8, CYAN)
atlas.putpixel((35, 3), WHITE)
atlas.putpixel((37, 5), WHITE)

# guard rainbow swatches (8x8 each)
guard_pos = [(40, 0), (48, 0), (56, 0), (40, 8), (48, 8), (56, 8)]
for (gx, gy), col in zip(guard_pos, RAINBOW):
    fill(atlas, gx, gy, gx + 8, gy + 8, col)

out_atlas = os.path.join(BASE, "textures", "entity", "unicorn_horn_blade", "unicorn_horn_blade.png")
os.makedirs(os.path.dirname(out_atlas), exist_ok=True)
atlas.save(out_atlas)
print("wrote", out_atlas)

if os.path.isfile(BBMODEL):
    with open(out_atlas, "rb") as file:
        atlas_source = "data:image/png;base64," + base64.b64encode(file.read()).decode("ascii")
    with open(BBMODEL, encoding="utf-8") as file:
        project = json.load(file)
    updated = False
    for texture in project.get("textures", []):
        if texture.get("name") == "unicorn_horn_blade.png":
            texture["source"] = atlas_source
            texture["width"] = 64
            texture["height"] = 64
            texture["uv_width"] = 64
            texture["uv_height"] = 64
            texture["relative_path"] = "../addon/resource_pack/textures/entity/unicorn_horn_blade/unicorn_horn_blade.png"
            texture["saved"] = True
            updated = True
    if updated:
        with open(BBMODEL, "w", encoding="utf-8") as file:
            json.dump(project, file, ensure_ascii=False, separators=(",", ":"))
        print("updated embedded Blockbench texture", BBMODEL)
    else:
        print("warning: unicorn_horn_blade.png texture not found in", BBMODEL)

# ---------------------------------------------------------------- 16x16 icon
icon = Image.new("RGBA", (16, 16), CLEAR)
base = (3.0, 13.0)
tip = (12.0, 2.0)
steps = 40
for i in range(steps + 1):
    t = i / steps
    cx = base[0] + (tip[0] - base[0]) * t
    cy = base[1] + (tip[1] - base[1]) * t
    half = (1.0 - t) * 1.6 + 0.3
    band = int((t * 9)) % 2
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            px = int(round(cx + dx))
            py = int(round(cy + dy))
            if 0 <= px < 16 and 0 <= py < 16:
                dist = (dx * dx + dy * dy) ** 0.5
                if dist <= half:
                    color = HORN_RAINBOW[int(t * len(HORN_RAINBOW)) % len(HORN_RAINBOW)]
                    edge = HORN_SHADOW[int(t * len(HORN_SHADOW)) % len(HORN_SHADOW)]
                    icon.putpixel((px, py), edge if dist > half - 0.9 else color)

gx, gy = 3, 13
for k, c in enumerate(RAINBOW[:4]):
    px = gx - 2 + k
    py = gy + 1
    if 0 <= px < 16 and 0 <= py < 16:
        icon.putpixel((px, py), c)
    if 0 <= px < 16 and 0 <= py - 1 < 16:
        icon.putpixel((px, py - 1), c)

icon.putpixel((2, 14), LAVENDER)
icon.putpixel((2, 15), LAVENDER_DK)
icon.putpixel((1, 15), GOLD)
icon.putpixel((12, 2), HORN_HI)
icon.putpixel((11, 3), HORN)

out_icon = os.path.join(BASE, "textures", "items", "unicorn_horn_blade.png")
os.makedirs(os.path.dirname(out_icon), exist_ok=True)
icon.save(out_icon)
print("wrote", out_icon)
