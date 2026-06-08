"""Generate 64x64 Bedrock player skins: pastel unicorn one-piece dress.

Spec (from reference 001.png, rewritten):
  - lavender hair + small gold unicorn-horn mark, simple cute face (purple eyes)
  - white one-piece bodice, small rainbow + cloud motif on the chest, pastel trim
  - white sleeves with lavender frill cuffs + one yellow star on an arm
  - pastel-rainbow frill skirt (pink->yellow->mint->blue->lavender, top to bottom)
    across the lower body and the top of the legs, using the jacket/leg overlay layers
  - back: a big heart + a vertical rainbow ribbon, skirt frill continues
  - skin-tone legs, white knee socks with a heart/star, lavender shoes

Outputs PNG skins + front/back/side previews + manifest/skins.json/texts.
"""
import json
import os
import uuid

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.join(HERE, "skin_pack")

# palette (spec)
WHITE = (255, 248, 255)
LAV = (205, 180, 246)
PINK = (247, 167, 200)
BLUE = (169, 216, 255)
MINT = (185, 242, 208)
YEL = (255, 233, 154)
PURP = (169, 135, 217)     # soft purple shadow
GOLD = (255, 215, 90)
SKIN = (255, 220, 200)
SKIN_SH = (240, 198, 178)


def rect(img, x0, y0, w, h, c):
    for yy in range(y0, y0 + h):
        for xx in range(x0, x0 + w):
            if 0 <= xx < img.width and 0 <= yy < img.height:
                img.putpixel((xx, yy), c)


def px(img, x, y, c):
    if 0 <= x < img.width and 0 <= y < img.height:
        img.putpixel((x, y), c)


# ---- 64x64 UV: base + overlay (hat / jacket / sleeves / pants) ----
FACES = {
    "head_top": (8, 0, 8, 8), "head_bottom": (16, 0, 8, 8),
    "head_right": (0, 8, 8, 8), "head_front": (8, 8, 8, 8),
    "head_left": (16, 8, 8, 8), "head_back": (24, 8, 8, 8),
    "hat_top": (40, 0, 8, 8), "hat_front": (40, 8, 8, 8),
    "hat_right": (32, 8, 8, 8), "hat_left": (48, 8, 8, 8), "hat_back": (56, 8, 8, 8),
    "body_top": (20, 16, 8, 4), "body_bottom": (28, 16, 8, 4),
    "body_right": (16, 20, 4, 12), "body_front": (20, 20, 8, 12),
    "body_left": (28, 20, 4, 12), "body_back": (32, 20, 8, 12),
    "jacket_top": (20, 32, 8, 4), "jacket_bottom": (28, 32, 8, 4),
    "jacket_right": (16, 36, 4, 12), "jacket_front": (20, 36, 8, 12),
    "jacket_left": (28, 36, 4, 12), "jacket_back": (32, 36, 8, 12),
    "rarm_top": (44, 16, 4, 4), "rarm_right": (40, 20, 4, 12),
    "rarm_front": (44, 20, 4, 12), "rarm_left": (48, 20, 4, 12), "rarm_back": (52, 20, 4, 12),
    "rarmo_top": (44, 32, 4, 4), "rarmo_right": (40, 36, 4, 12),
    "rarmo_front": (44, 36, 4, 12), "rarmo_left": (48, 36, 4, 12), "rarmo_back": (52, 36, 4, 12),
    "larm_top": (36, 48, 4, 4), "larm_right": (32, 52, 4, 12),
    "larm_front": (36, 52, 4, 12), "larm_left": (40, 52, 4, 12), "larm_back": (44, 52, 4, 12),
    "larmo_top": (52, 48, 4, 4), "larmo_right": (48, 52, 4, 12),
    "larmo_front": (52, 52, 4, 12), "larmo_left": (56, 52, 4, 12), "larmo_back": (60, 52, 4, 12),
    "rleg_top": (4, 16, 4, 4), "rleg_right": (0, 20, 4, 12),
    "rleg_front": (4, 20, 4, 12), "rleg_left": (8, 20, 4, 12), "rleg_back": (12, 20, 4, 12),
    "rlego_top": (4, 32, 4, 4), "rlego_right": (0, 36, 4, 12),
    "rlego_front": (4, 36, 4, 12), "rlego_left": (8, 36, 4, 12), "rlego_back": (12, 36, 4, 12),
    "lleg_top": (20, 48, 4, 4), "lleg_right": (16, 52, 4, 12),
    "lleg_front": (20, 52, 4, 12), "lleg_left": (24, 52, 4, 12), "lleg_back": (28, 52, 4, 12),
    "llego_top": (4, 48, 4, 4), "llego_right": (0, 52, 4, 12),
    "llego_front": (4, 52, 4, 12), "llego_left": (8, 52, 4, 12), "llego_back": (28, 52, 4, 12),
}

# pastel rainbow frill, top -> bottom
SKIRT = [PINK, YEL, MINT, BLUE, LAV]


def fill(img, name, c):
    x0, y0, w, h = FACES[name]
    rect(img, x0, y0, w, h, c)


def shade(c, amt):
    return tuple(max(0, min(255, v + amt)) for v in c)


def heart(img, cx, cy, c):
    rect(img, cx - 2, cy, 2, 1, c); rect(img, cx + 1, cy, 2, 1, c)
    rect(img, cx - 2, cy + 1, 5, 1, c)
    rect(img, cx - 1, cy + 2, 3, 1, c)
    px(img, cx, cy + 3, c)


def star(img, cx, cy, c):
    px(img, cx, cy - 1, c); px(img, cx, cy + 1, c)
    px(img, cx - 1, cy, c); px(img, cx + 1, cy, c); px(img, cx, cy, c)


def skirt_face(img, name, n=6):
    """Fill a 4- or 8-wide body/leg face with the rainbow frill, with a soft
    scalloped shade at the bottom of each colour band for a frill look."""
    x0, y0, w, h = FACES[name]
    for i in range(h):
        c = SKIRT[(i * len(SKIRT)) // h]
        rect(img, x0, y0 + i, w, 1, c)
    # subtle frill scallops: darken every other column at band edges
    for i in range(h):
        c = SKIRT[(i * len(SKIRT)) // h]
        if i > 0 and SKIRT[((i - 1) * len(SKIRT)) // h] != c:
            for xx in range(x0, x0 + w, 2):
                px(img, xx, y0 + i, shade(c, -22))


# ---------------------------------------------------------------- head
def draw_head(img, p):
    for f in ("head_top", "head_back", "head_right", "head_left"):
        fill(img, f, p["hair"])
    fx, fy, _, _ = FACES["head_front"]
    fill(img, "head_front", SKIN)
    # bangs (3 rows) + side locks (2 cols) -> small cute face
    rect(img, fx, fy, 8, 3, p["hair"])
    rect(img, fx, fy + 3, 2, 5, p["hair"]); rect(img, fx + 6, fy + 3, 2, 5, p["hair"])
    px(img, fx + 2, fy + 3, p["hair"]); px(img, fx + 5, fy + 3, p["hair"])
    # purple eyes (2 tall) + shine, blush, small smile
    for ex in (fx + 2, fx + 5):
        rect(img, ex, fy + 4, 1, 2, p["eye"])
        px(img, ex, fy + 4, shade(p["eye"], -40))
        px(img, ex, fy + 5, (255, 255, 255))
    px(img, fx + 2, fy + 6, PINK); px(img, fx + 5, fy + 6, PINK)
    rect(img, fx + 3, fy + 6, 2, 1, shade(PINK, -30))
    # hat layer: fuller framing hair + a small gold horn mark on the forehead
    for f in ("hat_top", "hat_back", "hat_right", "hat_left"):
        fill(img, f, p["hair"])
    hx, hy, _, _ = FACES["hat_front"]
    rect(img, hx, hy, 8, 3, p["hair"])
    rect(img, hx, hy + 3, 2, 4, p["hair"]); rect(img, hx + 6, hy + 3, 2, 4, p["hair"])
    # small gold horn: a short triangle on the forehead/hat top, front-centre
    px(img, hx + 4, hy + 2, GOLD)
    tx, ty, _, _ = FACES["hat_top"]
    px(img, tx + 4, ty + 6, GOLD); px(img, tx + 4, ty + 5, GOLD)
    px(img, tx + 4, ty + 4, shade(GOLD, 20))


# ---------------------------------------------------------------- body
def rainbow_arch(img, cx, cy):
    # tiny rainbow arc (5 wide) over a little cloud, centred at (cx, cy)
    arc = [PINK, YEL, MINT, BLUE]
    for k, c in enumerate(arc):
        px(img, cx - 2 + 0, cy + k, c)        # left leg of arch
        px(img, cx + 2 - 0, cy + k, c)        # right leg
    for k, c in enumerate(arc):
        px(img, cx - 2, cy + k, c); px(img, cx + 2, cy + k, c)
    rect(img, cx - 1, cy - 1, 3, 1, PINK)     # top of arch
    px(img, cx - 2, cy, PINK); px(img, cx + 2, cy, PINK)
    # little cloud under the arch
    rect(img, cx - 2, cy + 4, 5, 1, WHITE)
    px(img, cx - 1, cy + 3, WHITE); px(img, cx + 1, cy + 3, WHITE)


def draw_body(img, p):
    # base: white bodice on top, rainbow skirt on the lower rows
    for f in ("body_front", "body_back", "body_right", "body_left"):
        x0, y0, w, h = FACES[f]
        rect(img, x0, y0, w, 6, WHITE)             # bodice (white)
        rect(img, x0, y0 + 5, w, 1, p["trim"])     # waist trim
        for i in range(6):                         # skirt frill (rows 6..11)
            rect(img, x0, y0 + 6 + i, w, 1, SKIRT[(i * len(SKIRT)) // 6])
    fill(img, "body_top", WHITE)
    fill(img, "body_bottom", SKIRT[-1])
    fx, fy, _, _ = FACES["body_front"]
    rect(img, fx, fy, 8, 1, p["trim"])             # neckline
    rainbow_arch(img, fx + 4, fy + 2)              # chest rainbow + cloud
    # back: collar + big heart + vertical rainbow ribbon
    bx, by, _, _ = FACES["body_back"]
    rect(img, bx, by, 8, 1, p["trim"])
    heart(img, bx + 4, by + 2, PINK)
    for i in range(6):                             # ribbon tail down the back skirt
        px(img, bx + 3, by + 5 + i, SKIRT[(i * len(SKIRT)) // 6])
        px(img, bx + 4, by + 5 + i, shade(SKIRT[(i * len(SKIRT)) // 6], -18))
    # jacket overlay: a frill ruffle layer at the skirt hem (front/back/sides)
    for f in ("jacket_front", "jacket_back", "jacket_right", "jacket_left"):
        x0, y0, w, h = FACES[f]
        for i in range(4):                         # bottom 4 rows = frill
            c = SKIRT[min(len(SKIRT) - 1, 1 + (i * len(SKIRT)) // 4)]
            rect(img, x0, y0 + 8 + i, w, 1, c)
        for xx in range(x0, x0 + w, 2):            # scalloped hem shading
            px(img, xx, y0 + 11, shade(SKIRT[-1], -26))


# ---------------------------------------------------------------- arms
def draw_arm(img, side, p):
    pre = "rarm" if side == "r" else "larm"
    for f in ("front", "back", "right", "left"):
        x0, y0, w, h = FACES[pre + "_" + f]
        rect(img, x0, y0, w, 8, WHITE)             # white sleeve
        rect(img, x0, y0 + 7, w, 1, p["trim"])     # lavender cuff line
        rect(img, x0, y0 + 8, w, 4, SKIN)          # hand
    fill(img, pre + "_top", WHITE)
    # frill cuff via the sleeve overlay (rows 7..9)
    preo = "rarmo" if side == "r" else "larmo"
    for f in ("front", "back", "right", "left"):
        x0, y0, w, h = FACES[preo + "_" + f]
        rect(img, x0, y0 + 7, w, 1, LAV)
        for xx in range(x0, x0 + w, 2):
            px(img, xx, y0 + 8, shade(LAV, -26))
    # one yellow star on the outer upper sleeve
    sx, sy, _, _ = FACES[pre + "_front"]
    star(img, sx + 1, sy + 3, YEL)


# ---------------------------------------------------------------- legs
def draw_leg(img, side, p):
    pre = "rleg" if side == "r" else "lleg"
    for f in ("front", "back", "right", "left"):
        x0, y0, w, h = FACES[pre + "_" + f]
        rect(img, x0, y0, w, 2, SKIRT[-1])         # skirt hem continues onto upper leg
        rect(img, x0, y0 + 2, w, 4, SKIN)          # bare leg
        rect(img, x0, y0 + 6, w, 4, WHITE)         # white knee sock
        rect(img, x0, y0 + 6, w, 1, p["trim"])     # sock cuff
        rect(img, x0, y0 + 10, w, 2, LAV)          # lavender shoe
    fill(img, pre + "_top", SKIRT[-1])
    # heart + star on the front of the sock
    fx, fy, _, _ = FACES[pre + "_front"]
    px(img, fx + 1, fy + 7, PINK); px(img, fx + 2, fy + 7, PINK)
    star(img, fx + 2, fy + 8, YEL)


def build_skin(p):
    img = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    draw_head(img, p)
    draw_body(img, p)
    draw_arm(img, "r", p)
    draw_arm(img, "l", p)
    draw_leg(img, "r", p)
    draw_leg(img, "l", p)
    return img


# ---------------------------------------------------------------- previews
def preview(img, view, scale=12):
    """Assemble FRONT/BACK/LEFT/RIGHT body faces into a standing figure."""
    W, H = 16, 32
    cv = Image.new("RGBA", (W, H), (244, 244, 250, 255))

    def blit(face, dx, dy, mirror=False):
        x0, y0, w, h = FACES[face]
        for yy in range(h):
            for xx in range(w):
                c = img.getpixel((x0 + xx, y0 + yy))
                if c[3] > 0:
                    tx = dx + (w - 1 - xx if mirror else xx)
                    cv.putpixel((tx, dy + yy), c)

    def blit_pair(base, over, dx, dy, mirror=False):
        blit(base, dx, dy, mirror)
        blit(over, dx, dy, mirror)

    if view == "front":
        blit_pair("head_front", "hat_front", 4, 0)
        blit_pair("rarm_front", "rarmo_front", 1, 8)
        blit_pair("body_front", "jacket_front", 4, 8)
        blit_pair("larm_front", "larmo_front", 12, 8)
        blit_pair("rleg_front", "rlego_front", 4, 20)
        blit_pair("lleg_front", "llego_front", 8, 20)
    elif view == "back":
        blit_pair("head_back", "hat_back", 4, 0)
        blit_pair("larm_back", "larmo_back", 1, 8, True)
        blit_pair("body_back", "jacket_back", 4, 8)
        blit_pair("rarm_back", "rarmo_back", 12, 8, True)
        blit_pair("lleg_back", "llego_back", 4, 20, True)
        blit_pair("rleg_back", "rlego_back", 8, 20, True)
    else:  # side (right)
        blit_pair("head_right", "hat_right", 4, 0)
        blit_pair("body_right", "jacket_right", 6, 8)
        blit_pair("rarm_right", "rarmo_right", 6, 8)
        blit_pair("rleg_right", "rlego_right", 6, 20)
    return cv.resize((W * scale, H * scale), Image.NEAREST)


PALETTES = {
    "unicorn_pastel": {"hair": LAV, "trim": LAV, "eye": (120, 80, 190)},
    "unicorn_pastel_pink": {"hair": PINK, "trim": MINT, "eye": (150, 90, 170)},
}

SKIN_TITLES = {
    "unicorn_pastel": "Pastel Unicorn Dress",
    "unicorn_pastel_pink": "Pink Unicorn Dress",
}


def write_pack():
    os.makedirs(os.path.join(PACK, "texts"), exist_ok=True)
    for sid, p in PALETTES.items():
        skin = build_skin(p)
        skin.save(os.path.join(PACK, sid + ".png"))
        for view in ("front", "back", "side"):
            preview(skin, view).save(os.path.join(PACK, "preview_%s_%s.png" % (sid, view)))
        print("wrote", sid + ".png")

    serialize = "UnicornPastelGirls"
    with open(os.path.join(PACK, "skins.json"), "w", encoding="utf-8") as fh:
        json.dump({"skins": [{"localization_name": sid, "geometry": "geometry.humanoid.custom",
                              "texture": sid + ".png", "type": "free"} for sid in PALETTES],
                   "serialize_name": serialize, "localization_name": serialize}, fh,
                  ensure_ascii=False, indent=2)
    with open(os.path.join(PACK, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump({"format_version": 2,
                   "header": {"name": "Unicorn Pastel Girls",
                              "uuid": str(uuid.uuid5(uuid.NAMESPACE_DNS, "mine_skins_01.header")),
                              "version": [1, 0, 0]},
                   "modules": [{"type": "skin_pack",
                                "uuid": str(uuid.uuid5(uuid.NAMESPACE_DNS, "mine_skins_01.module")),
                                "version": [1, 0, 0]}]}, fh, ensure_ascii=False, indent=2)
    lines = ["skinpack.%s=Unicorn Pastel Girls" % serialize]
    for sid in PALETTES:
        lines.append("skin.%s.%s=%s" % (serialize, sid, SKIN_TITLES[sid]))
    for lang in ("en_US", "ko_KR"):
        with open(os.path.join(PACK, "texts", lang + ".lang"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
    print("wrote manifest.json / skins.json / texts")


if __name__ == "__main__":
    write_pack()
