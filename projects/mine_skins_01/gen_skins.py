"""Generate 64x64 Bedrock player skins for the pastel-unicorn character set.

Reference: ../../game/mine_reference/001.png (pastel unicorn girl: lavender hair,
rainbow dress, star/heart accents, horn). These are procedural *approximations*
on the classic 64x64 humanoid UV (4px arms).

Outputs PNG skins + a flat front-facing preview (for eyeballing) into skin_pack/.
manifest.json / skins.json / texts are written here too.
"""
import json
import os
import uuid

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.join(HERE, "skin_pack")


def rect(img, x0, y0, w, h, c):
    for yy in range(y0, y0 + h):
        for xx in range(x0, x0 + w):
            if 0 <= xx < img.width and 0 <= yy < img.height:
                img.putpixel((xx, yy), c)


def px(img, x, y, c):
    if 0 <= x < img.width and 0 <= y < img.height:
        img.putpixel((x, y), c)


# Classic 64x64 UV face origins (x, y) for 8x8 head / body / 4-wide limbs.
# Each entry: (x0, y0, width, height) of the FRONT face unless noted.
FACES = {
    "head_top": (8, 0, 8, 8), "head_bottom": (16, 0, 8, 8),
    "head_right": (0, 8, 8, 8), "head_front": (8, 8, 8, 8),
    "head_left": (16, 8, 8, 8), "head_back": (24, 8, 8, 8),
    "hat_top": (40, 0, 8, 8), "hat_front": (40, 8, 8, 8),
    "hat_right": (32, 8, 8, 8), "hat_left": (48, 8, 8, 8), "hat_back": (56, 8, 8, 8),
    "body_front": (20, 20, 8, 12), "body_back": (32, 20, 8, 12),
    "body_right": (16, 20, 4, 12), "body_left": (28, 20, 4, 12),
    "body_top": (20, 16, 8, 4), "body_bottom": (28, 16, 8, 4),
    "rarm_front": (44, 20, 4, 12), "rarm_back": (52, 20, 4, 12),
    "rarm_right": (40, 20, 4, 12), "rarm_left": (48, 20, 4, 12),
    "rarm_top": (44, 16, 4, 4),
    "larm_front": (36, 52, 4, 12), "larm_back": (44, 52, 4, 12),
    "larm_right": (32, 52, 4, 12), "larm_left": (40, 52, 4, 12),
    "larm_top": (36, 48, 4, 4),
    "rleg_front": (4, 20, 4, 12), "rleg_back": (12, 20, 4, 12),
    "rleg_right": (0, 20, 4, 12), "rleg_left": (8, 20, 4, 12),
    "rleg_top": (4, 16, 4, 4),
    "lleg_front": (20, 52, 4, 12), "lleg_back": (28, 52, 4, 12),
    "lleg_right": (16, 52, 4, 12), "lleg_left": (24, 52, 4, 12),
    "lleg_top": (20, 48, 4, 4),
}


def fill_face(img, name, c):
    x0, y0, w, h = FACES[name]
    rect(img, x0, y0, w, h, c)


def draw_head(img, p):
    # hair on top / back / sides, skin on the lower front
    for f in ("head_top", "head_back", "head_right", "head_left"):
        fill_face(img, f, p["hair"])
    fx, fy, _, _ = FACES["head_front"]
    fill_face(img, "head_front", p["skin"])
    # bangs across the top two rows of the face + side strands
    rect(img, fx, fy, 8, 2, p["hair"])
    rect(img, fx, fy + 2, 1, 6, p["hair"])
    rect(img, fx + 7, fy + 2, 1, 6, p["hair"])
    px(img, fx + 1, fy + 2, p["hair"]); px(img, fx + 6, fy + 2, p["hair"])
    # eyes (2x2) with a white highlight + dark top
    for ex in (fx + 2, fx + 5):
        rect(img, ex, fy + 4, 1, 3, p["eye"])
        px(img, ex, fy + 4, p["eye_dk"])
        px(img, ex, fy + 6, (255, 255, 255))
    # blush + mouth
    px(img, fx + 1, fy + 5, p["blush"]); px(img, fx + 6, fy + 5, p["blush"])
    px(img, fx + 3, fy + 6, p["mouth"]); px(img, fx + 4, fy + 6, p["mouth"])
    # hat layer: fuller hair + a little horn nub on the forehead
    for f in ("hat_top", "hat_back", "hat_right", "hat_left"):
        fill_face(img, f, p["hair_dk"])
    hx, hy, _, _ = FACES["hat_front"]
    rect(img, hx, hy, 8, 2, p["hair_dk"])      # bangs overlay
    rect(img, hx, hy + 2, 1, 5, p["hair_dk"])
    rect(img, hx + 7, hy + 2, 1, 5, p["hair_dk"])
    # horn nub: small gold mark on the hat top, front-centre
    tx, ty, _, _ = FACES["hat_top"]
    rect(img, tx + 3, ty + 1, 2, 2, p["horn"])
    px(img, tx + 3, ty + 1, (255, 245, 200))


def draw_body(img, p):
    # bodice (upper) + rainbow skirt (lower); back/sides follow the dress
    for f in ("body_front", "body_back"):
        x0, y0, w, h = FACES[f]
        rect(img, x0, y0, w, 6, p["dress"])           # bodice
        for i in range(6):                            # skirt stripes
            rect(img, x0, y0 + 6 + i, w, 1, p["rainbow"][i % len(p["rainbow"])])
    for f in ("body_right", "body_left"):
        x0, y0, w, h = FACES[f]
        rect(img, x0, y0, w, 6, p["dress"])
        for i in range(6):
            rect(img, x0, y0 + 6 + i, w, 1, p["rainbow"][i % len(p["rainbow"])])
    fill_face(img, "body_top", p["dress"])
    fill_face(img, "body_bottom", p["rainbow"][3])
    # chest heart + collar trim
    fx, fy, _, _ = FACES["body_front"]
    px(img, fx + 3, fy + 2, p["heart"]); px(img, fx + 4, fy + 2, p["heart"])
    rect(img, fx + 2, fy + 3, 4, 1, p["heart"])
    rect(img, fx + 3, fy + 4, 2, 1, p["heart"])
    rect(img, fx, fy, 8, 1, p["trim"])                # collar


def draw_arm(img, prefix, p):
    # puffed dress sleeve (upper) + skin hand (lower)
    for side in ("front", "back", "right", "left"):
        x0, y0, w, h = FACES[prefix + "_" + side]
        rect(img, x0, y0, w, 8, p["dress"])           # sleeve
        rect(img, x0, y0 + 8, w, 4, p["skin"])        # hand
        rect(img, x0, y0 + 7, w, 1, p["trim"])        # cuff
    fill_face(img, prefix + "_top", p["dress"])


def draw_leg(img, prefix, p):
    # rainbow stocking (upper) + shoe (lower)
    for side in ("front", "back", "right", "left"):
        x0, y0, w, h = FACES[prefix + "_" + side]
        for i in range(9):
            rect(img, x0, y0 + i, w, 1, p["rainbow"][i % len(p["rainbow"])])
        rect(img, x0, y0 + 9, w, 3, p["shoe"])        # shoe
        rect(img, x0, y0 + 9, w, 1, p["trim"])        # shoe strap
    fill_face(img, prefix + "_top", p["rainbow"][0])


def build_skin(palette):
    img = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    draw_head(img, palette)
    draw_body(img, palette)
    draw_arm(img, "rarm", palette)
    draw_arm(img, "larm", palette)
    draw_leg(img, "rleg", palette)
    draw_leg(img, "lleg", palette)
    return img


def front_preview(img, scale=12):
    """Assemble the FRONT faces into a standing character for eyeballing."""
    # canvas in 'pixels': head 8 wide, body 8, arms 4 each side
    W, H = 16, 32
    cv = Image.new("RGBA", (W, H), (245, 245, 250, 255))

    def blit(face, dx, dy):
        x0, y0, w, h = FACES[face]
        for yy in range(h):
            for xx in range(w):
                c = img.getpixel((x0 + xx, y0 + yy))
                if c[3] > 0:
                    cv.putpixel((dx + xx, dy + yy), c)
    blit("head_front", 4, 0)
    # overlay hat front on top of the head
    hx, hy, hw, hh = FACES["hat_front"]
    for yy in range(hh):
        for xx in range(hw):
            c = img.getpixel((hx + xx, hy + yy))
            if c[3] > 0:
                cv.putpixel((4 + xx, 0 + yy), c)
    blit("rarm_front", 1, 8)
    blit("body_front", 4, 8)
    blit("larm_front", 12, 8)
    blit("rleg_front", 4, 20)
    blit("lleg_front", 8, 20)
    return cv.resize((W * scale, H * scale), Image.NEAREST)


PALETTES = {
    "unicorn_pastel": {
        "hair": (200, 180, 234), "hair_dk": (176, 152, 214),
        "skin": (255, 236, 226), "eye": (150, 110, 200), "eye_dk": (110, 76, 160),
        "blush": (250, 180, 200), "mouth": (235, 140, 165),
        "dress": (250, 182, 210), "trim": (150, 230, 200), "heart": (235, 90, 130),
        "shoe": (255, 252, 255), "horn": (255, 224, 130),
        "rainbow": [(255, 182, 193), (255, 220, 160), (255, 246, 170),
                    (180, 236, 190), (176, 216, 246), (208, 186, 240)],
    },
    "unicorn_pastel_mint": {
        "hair": (170, 226, 210), "hair_dk": (140, 200, 188),
        "skin": (255, 236, 226), "eye": (90, 170, 160), "eye_dk": (60, 130, 122),
        "blush": (250, 180, 200), "mouth": (235, 140, 165),
        "dress": (176, 216, 246), "trim": (255, 224, 150), "heart": (235, 110, 150),
        "shoe": (255, 252, 255), "horn": (255, 224, 130),
        "rainbow": [(208, 186, 240), (176, 216, 246), (180, 236, 190),
                    (255, 246, 170), (255, 220, 160), (255, 182, 193)],
    },
}

SKIN_TITLES = {
    "unicorn_pastel": "Pastel Unicorn Girl",
    "unicorn_pastel_mint": "Mint Unicorn Girl",
}


def write_pack():
    os.makedirs(os.path.join(PACK, "texts"), exist_ok=True)
    for sid, palette in PALETTES.items():
        skin = build_skin(palette)
        skin.save(os.path.join(PACK, sid + ".png"))
        front_preview(skin).save(os.path.join(PACK, "preview_" + sid + ".png"))
        print("wrote", sid + ".png")

    serialize = "UnicornPastelGirls"
    skins_json = {
        "skins": [{"localization_name": sid, "geometry": "geometry.humanoid.custom",
                   "texture": sid + ".png", "type": "free"} for sid in PALETTES],
        "serialize_name": serialize, "localization_name": serialize,
    }
    with open(os.path.join(PACK, "skins.json"), "w", encoding="utf-8") as fh:
        json.dump(skins_json, fh, ensure_ascii=False, indent=2)

    manifest = {
        "format_version": 2,
        "header": {"name": "Unicorn Pastel Girls", "uuid": str(uuid.uuid5(uuid.NAMESPACE_DNS, "mine_skins_01.header")),
                   "version": [1, 0, 0]},
        "modules": [{"type": "skin_pack",
                     "uuid": str(uuid.uuid5(uuid.NAMESPACE_DNS, "mine_skins_01.module")),
                     "version": [1, 0, 0]}],
    }
    with open(os.path.join(PACK, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=2)

    lines = ["skinpack.%s=Unicorn Pastel Girls" % serialize]
    for sid in PALETTES:
        lines.append("skin.%s.%s=%s" % (serialize, sid, SKIN_TITLES[sid]))
    for lang in ("en_US", "ko_KR"):
        with open(os.path.join(PACK, "texts", lang + ".lang"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
    print("wrote manifest.json / skins.json / texts")


if __name__ == "__main__":
    write_pack()
