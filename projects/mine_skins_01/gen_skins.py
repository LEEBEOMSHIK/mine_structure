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
import math
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


def frill(img, name, start, bands):
    """Draw a layered ruffle into a face starting at row `start`. Each colour in
    `bands` takes 2 rows: a bright highlight on top + the base colour below, and a
    scalloped (alternating dark) hem at the bottom of each band -> a 3D frill look."""
    x0, y0, w, h = FACES[name]
    y = start
    for c in bands:
        if y >= h:
            break
        rect(img, x0, y0 + y, w, 1, shade(c, 20))            # lit top of the ruffle
        if y + 1 < h:
            rect(img, x0, y0 + y + 1, w, 1, c)               # body of the ruffle
            for xx in range(x0 + 1, x0 + w, 2):              # scalloped shadow hem
                px(img, xx, y0 + y + 1, shade(c, -34))
        y += 2
    return y


# ---------------------------------------------------------------- head
def hair_shade(img, name, base):
    """Fill a head face with hair + a few darker streaks for a shaded look."""
    x0, y0, w, h = FACES[name]
    rect(img, x0, y0, w, h, base)
    dk = shade(base, -34)
    for yy in range(y0, y0 + h):
        for xx in range(x0, x0 + w):
            if (xx + yy) % 4 == 0:
                px(img, xx, yy, dk)


def draw_head(img, p):
    hair = p["hair"]
    dk = shade(hair, -34)
    for f in ("head_top", "head_back", "head_right", "head_left"):
        hair_shade(img, f, hair)
    fx, fy, _, _ = FACES["head_front"]
    fill(img, "head_front", SKIN)
    # M-shaped bangs: top hair with the forehead centre peeking out, long side locks
    rect(img, fx, fy, 8, 2, hair)
    px(img, fx, fy, dk); px(img, fx + 7, fy, dk)
    rect(img, fx, fy + 2, 1, 6, hair); rect(img, fx + 7, fy + 2, 1, 6, hair)  # side locks
    px(img, fx + 1, fy + 2, hair); px(img, fx + 6, fy + 2, hair)
    px(img, fx + 1, fy + 6, hair); px(img, fx + 6, fy + 6, hair)              # locks reach cheeks
    # big sparkly eyes (2 wide x 3 tall): dark top, white shine, purple lower
    for ex in (fx + 1, fx + 5):
        rect(img, ex, fy + 3, 2, 1, shade(p["eye"], -70))   # dark upper lid
        rect(img, ex, fy + 4, 2, 1, (255, 255, 255))        # bright shine
        rect(img, ex, fy + 5, 2, 1, p["eye"])               # iris lower
    # blush + tiny mouth
    px(img, fx + 1, fy + 6, PINK); px(img, fx + 6, fy + 6, PINK)
    rect(img, fx + 3, fy + 7, 2, 1, shade(PINK, -24))
    # hat layer: fuller framing hair + a bigger gold horn + heart hair clips
    for f in ("hat_top", "hat_back", "hat_right", "hat_left"):
        hair_shade(img, f, hair)
    hx, hy, _, _ = FACES["hat_front"]
    rect(img, hx, hy, 8, 2, hair)
    rect(img, hx, hy + 2, 1, 5, hair); rect(img, hx + 7, hy + 2, 1, 5, hair)
    # gold horn rising from the forehead (front + top)
    rect(img, hx + 3, hy, 2, 2, GOLD); px(img, hx + 3, hy, shade(GOLD, 22))
    tx, ty, _, _ = FACES["hat_top"]
    rect(img, tx + 3, ty + 5, 2, 3, GOLD); px(img, tx + 3, ty + 5, shade(GOLD, 24))
    # heart hair clips on the top, either side of the horn
    px(img, tx + 1, ty + 6, PINK); px(img, tx + 6, ty + 6, PINK)


# ---------------------------------------------------------------- body
def rainbow_arch(img, fx, fy):
    """A clear rainbow semicircle (pink/yellow/mint/blue rings) on a small white
    cloud. fx,fy = top-left of body_front; motif sits high on the chest."""
    ax = fx + 4                                   # arch centre x
    by = fy + 5                                   # arch baseline y
    for r, c in [(4, PINK), (3, YEL), (2, MINT), (1, BLUE)]:
        for a in range(0, 181, 8):
            rad = math.radians(a)
            px(img, ax + int(round(r * math.cos(rad))), by - int(round(r * math.sin(rad))), c)
    # small white cloud under the arch
    rect(img, ax - 3, by + 1, 7, 1, WHITE)
    px(img, ax - 2, by, WHITE); px(img, ax + 1, by, WHITE)
    px(img, ax - 4, by + 2, WHITE); px(img, ax + 4, by + 2, WHITE)
    rect(img, ax - 3, by + 2, 7, 1, shade(WHITE, -12))


def draw_body(img, p):
    # The waist/skirt line sits at the HAND line (bottom of the body = where the
    # arms end). So the white one-piece bodice fills most of the body (rows 0-9),
    # and the rainbow skirt frill flares from the hem (body bottom) down onto the
    # legs -> the skirt is centred on the hand line, not halfway up the torso.
    for f in ("body_front", "body_back", "body_right", "body_left"):
        x0, y0, w, h = FACES[f]
        rect(img, x0, y0, w, 2, SKIN)              # bare shoulders / chest top (off-shoulder)
        rect(img, x0, y0 + 1, w, 1, p["trim"])     # dress neckline band
        rect(img, x0, y0 + 2, w, 8, WHITE)         # white bodice
        rect(img, x0, y0 + 9, w, 1, p["trim"])     # waistband at the hand line
        frill(img, f, 10, [SKIRT[0]])              # first frill (pink) at the hem
    fill(img, "body_top", SKIN)
    fill(img, "body_bottom", SKIRT[0])
    fx, fy, _, _ = FACES["body_front"]
    rainbow_arch(img, fx, fy + 1)                   # chest rainbow + cloud
    # back: collar + heart + ribbon bow
    bx, by, _, _ = FACES["body_back"]
    rect(img, bx, by, 8, 1, p["trim"])
    heart(img, bx + 4, by + 3, PINK)
    px(img, bx + 2, by + 2, PINK); px(img, bx + 5, by + 2, PINK)   # bow loops
    # jacket overlay: skirt frill tiers (yellow, mint) flaring out at the hem
    for f in ("jacket_front", "jacket_back", "jacket_right", "jacket_left"):
        frill(img, f, 8, [SKIRT[1], SKIRT[2]])
    # long side hair draping over the shoulders (front + back), with a dark streak
    dk = shade(p["hair"], -34)
    for f in ("body_front", "body_back"):
        x0, y0, w, h = FACES[f]
        rect(img, x0, y0, 1, 5, p["hair"]); rect(img, x0 + w - 1, y0, 1, 5, p["hair"])
        px(img, x0, y0 + 2, dk); px(img, x0 + w - 1, y0 + 3, dk)


# ---------------------------------------------------------------- arms
def draw_arm(img, side, p):
    # off-shoulder: bare shoulder/upper arm, puffed sleeve lower down, then hand
    pre = "rarm" if side == "r" else "larm"
    for f in ("front", "back", "right", "left"):
        x0, y0, w, h = FACES[pre + "_" + f]
        rect(img, x0, y0, w, 3, SKIN)              # bare shoulder (off-shoulder)
        px(img, x0, y0 + 1, SKIN_SH); px(img, x0 + w - 1, y0 + 1, SKIN_SH)
        rect(img, x0, y0 + 3, w, 4, WHITE)         # puffed white sleeve
        rect(img, x0, y0 + 3, w, 1, p["trim"])     # sleeve top trim
        rect(img, x0, y0 + 7, w, 1, p["trim"])     # cuff line
        rect(img, x0, y0 + 8, w, 4, SKIN)          # forearm/hand
    fill(img, pre + "_top", SKIN)
    # frill cuff via the sleeve overlay (rows 6..8)
    preo = "rarmo" if side == "r" else "larmo"
    for f in ("front", "back", "right", "left"):
        x0, y0, w, h = FACES[preo + "_" + f]
        rect(img, x0, y0 + 6, w, 1, shade(LAV, 18))
        rect(img, x0, y0 + 7, w, 1, LAV)
        for xx in range(x0 + 1, x0 + w, 2):
            px(img, xx, y0 + 7, shade(LAV, -28))
    # one yellow star on the sleeve
    sx, sy, _, _ = FACES[pre + "_front"]
    star(img, sx + 2, sy + 5, YEL)


# ---------------------------------------------------------------- legs
def draw_leg(img, side, p):
    pre = "rleg" if side == "r" else "lleg"
    for f in ("front", "back", "right", "left"):
        x0, y0, w, h = FACES[pre + "_" + f]
        frill(img, pre + "_" + f, 0, [SKIRT[3], SKIRT[4]])  # skirt frill onto upper leg
        rect(img, x0, y0 + 4, w, 2, SKIN)              # bare leg
        px(img, x0, y0 + 4, SKIN_SH); px(img, x0 + w - 1, y0 + 4, SKIN_SH)
        rect(img, x0, y0 + 6, w, 3, WHITE)             # white knee sock
        rect(img, x0, y0 + 6, w, 1, p["trim"])         # sock cuff
        rect(img, x0, y0 + 9, w, 3, LAV)               # lavender shoe
        rect(img, x0, y0 + 9, w, 1, shade(LAV, 22))    # shoe highlight
    fill(img, pre + "_top", SKIRT[3])
    # heart + star on the front of the sock
    fx, fy, _, _ = FACES[pre + "_front"]
    px(img, fx + 1, fy + 7, PINK)
    star(img, fx + 2, fy + 7, YEL)


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
