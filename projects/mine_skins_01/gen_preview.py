"""Re-runnable full-character preview for Blockbench.

Builds `_preview.bbmodel` (gitignored) = the player skin on a humanoid model PLUS
the rainbow A-line skirt costume, so you can eyeball the whole character (skin +
worn skirt) at once. Run it any time after regenerating the skin/skirt:

    python gen_preview.py [skin_sid]        # default: unicorn_pastel

Then open `_preview.bbmodel` in Blockbench. Two textures are embedded: the skin
(id 0) and the skirt atlas (id 1, from mine_furniture_01).
"""
import base64
import json
import os
import sys
import uuid

HERE = os.path.dirname(os.path.abspath(__file__))
SKIN_PNG = os.path.join(HERE, "skin_pack")
SKIRT_PNG = os.path.normpath(os.path.join(
    HERE, "..", "mine_furniture_01", "addon", "resource_pack",
    "textures", "entity", "unicorn_rainbow_skirt", "unicorn_rainbow_skirt.png"))

# Player body parts (skin texture, id 0): (name, from, size, uv_offset, inflate)
PARTS = [
    ("head", [-4, 24, -4], [8, 8, 8], [0, 0], 0),
    ("body", [-4, 12, -2], [8, 12, 4], [16, 16], 0),
    ("rArm", [-8, 12, -2], [4, 12, 4], [40, 16], 0),
    ("lArm", [4, 12, -2], [4, 12, 4], [32, 48], 0),
    ("rLeg", [-4, 0, -2], [4, 12, 4], [0, 16], 0),
    ("lLeg", [0, 0, -2], [4, 12, 4], [16, 48], 0),
    ("hat", [-4, 24, -4], [8, 8, 8], [32, 0], 0.6),
    ("rsleeve", [-8, 12, -2], [4, 12, 4], [40, 32], 0.4),
    ("lsleeve", [4, 12, -2], [4, 12, 4], [48, 48], 0.4),
]
# Skirt tiers (skirt texture, id 1) -- keep in sync with mine_furniture_01/gen_skirt.py
CELL = 12
TIERS = [
    (11.0, 1.5, 4.6, 3.0, 0), (9.8, 1.5, 5.6, 3.6, 1), (8.6, 1.5, 6.7, 4.2, 2),
    (7.4, 1.5, 7.8, 4.8, 3), (6.0, 1.8, 9.0, 5.4, 4),
]


def uid():
    return str(uuid.uuid4())


def player_faces(ox, oy, sx, sy, sz, tex):
    return {
        "north": {"uv": [ox + sz, oy + sz, ox + sz + sx, oy + sz + sy], "texture": tex},
        "south": {"uv": [ox + 2 * sz + sx, oy + sz, ox + 2 * sz + 2 * sx, oy + sz + sy], "texture": tex},
        "east": {"uv": [ox, oy + sz, ox + sz, oy + sz + sy], "texture": tex},
        "west": {"uv": [ox + sz + sx, oy + sz, ox + 2 * sz + sx, oy + sz + sy], "texture": tex},
        "up": {"uv": [ox + sz, oy, ox + sz + sx, oy + sz], "texture": tex},
        "down": {"uv": [ox + sz + sx, oy, ox + sz + 2 * sx, oy + sz], "texture": tex},
    }


def data_url(path):
    with open(path, "rb") as fh:
        return "data:image/png;base64," + base64.b64encode(fh.read()).decode("ascii")


def main():
    sid = sys.argv[1] if len(sys.argv) > 1 else "unicorn_pastel"
    skin = data_url(os.path.join(SKIN_PNG, sid + ".png"))
    skirt = data_url(SKIRT_PNG)

    els = []
    for name, frm, size, uvoff, inflate in PARTS:
        to = [frm[i] + size[i] for i in range(3)]
        els.append({"name": name, "box_uv": False, "from": frm, "to": to, "inflate": inflate,
                    "autouv": 0, "color": 0, "origin": [0, 0, 0], "uv_offset": [0, 0],
                    "faces": player_faces(uvoff[0], uvoff[1], size[0], size[1], size[2], 0),
                    "type": "cube", "uuid": uid(), "export": True})
    for (y, h, hw, hd, ci) in TIERS:
        u = ci * CELL
        faces = {f: {"uv": [u, 0, u + CELL, CELL], "texture": 1}
                 for f in ("north", "south", "east", "west", "up", "down")}
        els.append({"name": "skirt%d" % ci, "box_uv": False, "from": [-hw, y, -hd],
                    "to": [hw, y + h, hd], "inflate": 0, "autouv": 0, "color": ci % 8,
                    "origin": [0, 24, 0], "uv_offset": [0, 0], "faces": faces,
                    "type": "cube", "uuid": uid(), "export": True})

    def tex(name, tid, src):
        return {"name": name, "width": 64, "height": 64, "uv_width": 64, "uv_height": 64,
                "particle": False, "render_mode": "default", "id": tid, "uuid": uid(), "source": src}

    bb = {"meta": {"format_version": "5.0", "model_format": "free", "box_uv": False},
          "name": sid + "_preview", "resolution": {"width": 64, "height": 64},
          "elements": els, "outliner": [e["uuid"] for e in els],
          "textures": [tex("skin.png", "0", skin), tex("skirt.png", "1", skirt)]}
    out = os.path.join(HERE, "_preview.bbmodel")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(bb, fh, ensure_ascii=False, separators=(",", ":"))
    print("wrote", out)
    print("Open _preview.bbmodel in Blockbench to view the full character (skin + skirt).")


if __name__ == "__main__":
    main()
