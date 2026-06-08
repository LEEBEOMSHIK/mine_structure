"""Custom 3D A-line rainbow skirt worn over a skin: mine_structure:unicorn_rainbow_skirt.

A wearable (legs slot) attachable whose geometry is a real A-line tutu: stacked
tiers that get WIDER toward the bottom (narrow waist -> wide knee hem), each tier a
pastel-rainbow frill colour with light-top / dark-hem shading. Parented to the
player 'body' bone so it sits at the waist and flares over the legs.

NOTE: armor-slot attachables + custom geometry are version-sensitive; verify in-game.
"""
import base64
import json
import os
import uuid

from PIL import Image

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
RP = os.path.join(BASE, "addon", "resource_pack")
BP_ITEMS = os.path.join(BASE, "addon", "behavior_pack", "items")
HERE = os.path.dirname(__file__)
SID = "unicorn_rainbow_skirt"
IDENT = "mine_structure:" + SID
ATLAS_REL = os.path.join("textures", "entity", SID, SID + ".png")

# pastel rainbow frill, waist -> hem
RAINBOW = [(255, 184, 206), (255, 228, 168), (190, 240, 206), (174, 214, 250), (206, 182, 244)]
CELL = 12  # texture block size per tier

# A-line tiers: (y_from, height, half_width, half_depth, colour_index) -> widens downward
TIERS = [
    (10.0, 2.0, 4.6, 3.0, 0),   # waist (pink)
    (8.0, 2.5, 5.6, 3.6, 1),    # yellow
    (5.5, 2.6, 6.7, 4.2, 2),    # mint
    (3.0, 2.6, 7.8, 4.8, 3),    # blue
    (1.0, 2.2, 9.0, 5.4, 4),    # hem (lavender)
]


def write_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent="\t")
    print("wrote", path)


def shade(c, amt):
    return tuple(max(0, min(255, v + amt)) for v in c)


def textures():
    atlas = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    for i, c in enumerate(RAINBOW):
        x0 = i * CELL
        for yy in range(CELL):
            # light top -> base -> dark scalloped hem within each tier block
            if yy < 2:
                col = shade(c, 22)
            elif yy >= CELL - 3:
                col = shade(c, -30)
            else:
                col = c
            for xx in range(CELL):
                col2 = col
                if yy >= CELL - 3 and xx % 2 == 0:     # scallop dots on the hem
                    col2 = shade(c, -50)
                atlas.putpixel((x0 + xx, yy), col2 + (255,))
    out = os.path.join(RP, ATLAS_REL)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    atlas.save(out)
    print("wrote", out)
    # 16x16 inventory icon: a little A-line rainbow skirt
    icon = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    for i, c in enumerate(RAINBOW):
        y = 3 + i * 2
        half = 2 + i
        for yy in (y, y + 1):
            for xx in range(8 - half, 8 + half):
                icon.putpixel((xx, yy), (shade(c, 18) if yy == y else c) + (255,))
    icon.save(os.path.join(RP, "textures", "items", SID + ".png"))
    print("wrote icon")


def cube_uv(ci):
    u = ci * CELL
    return {f: {"uv": [u, 0], "uv_size": [CELL, CELL]}
            for f in ("north", "south", "east", "west", "up", "down")}


def geometry():
    cubes = []
    for (y, h, hw, hd, ci) in TIERS:
        cubes.append({"origin": [-hw, y, -hd], "size": [hw * 2, h, hd * 2], "uv": cube_uv(ci)})
    geo = {
        "format_version": "1.12.0",
        "minecraft:geometry": [{
            "description": {"identifier": "geometry." + SID,
                            "texture_width": 64, "texture_height": 64,
                            "visible_bounds_width": 4, "visible_bounds_height": 3,
                            "visible_bounds_offset": [0, 1, 0]},
            "bones": [{"name": "body", "pivot": [0, 24, 0], "cubes": cubes}],
        }],
    }
    write_json(os.path.join(RP, "models", "entity", SID + ".geo.json"), geo)


def bbmodel():
    with open(os.path.join(RP, ATLAS_REL), "rb") as fh:
        src = "data:image/png;base64," + base64.b64encode(fh.read()).decode("ascii")

    def uid():
        return str(uuid.uuid4())

    def bb_faces(ci):
        u = ci * CELL
        return {f: {"uv": [u, 0, u + CELL, CELL], "texture": 0}
                for f in ("north", "south", "east", "west", "up", "down")}

    els = []
    for (y, h, hw, hd, ci) in TIERS:
        frm = [-hw, y, -hd]
        to = [hw, y + h, hd]
        els.append({"name": "tier%d" % ci, "box_uv": False, "from": frm, "to": to,
                    "autouv": 0, "color": ci % 8, "origin": [0, 24, 0], "uv_offset": [0, 0],
                    "faces": bb_faces(ci), "type": "cube", "uuid": uid(), "export": True})
    u_body = uid()
    group = {"name": "body", "uuid": u_body, "export": True, "origin": [0, 24, 0],
             "rotation": [0, 0, 0], "color": 0, "children": [e["uuid"] for e in els],
             "isOpen": True, "visibility": True}
    texture = {"name": SID + ".png", "width": 64, "height": 64, "uv_width": 64, "uv_height": 64,
               "particle": False, "render_mode": "default", "id": "0", "uuid": uid(), "source": src}
    bb = {"meta": {"format_version": "5.0", "model_format": "bedrock", "box_uv": False},
          "name": SID, "resolution": {"width": 64, "height": 64},
          "elements": els, "groups": [group],
          "outliner": [{"uuid": u_body, "name": "body", "isOpen": True,
                        "children": [e["uuid"] for e in els]}],
          "textures": [texture]}
    with open(os.path.join(HERE, SID + ".bbmodel"), "w", encoding="utf-8") as fh:
        json.dump(bb, fh, ensure_ascii=False, separators=(",", ":"))
    print("wrote", SID + ".bbmodel")


def item():
    write_json(os.path.join(BP_ITEMS, SID + ".item.json"), {
        "format_version": "1.20.10",
        "minecraft:item": {
            "description": {"identifier": IDENT, "menu_category": {"category": "equipment"}},
            "components": {
                "minecraft:display_name": {"value": "무지개 프릴 스커트"},
                "minecraft:icon": {"texture": SID},
                "minecraft:max_stack_size": 1,
                "minecraft:wearable": {"slot": "slot.armor.legs"},
                "minecraft:durability": {"max_durability": 240},
            },
        },
    })


def attachable():
    write_json(os.path.join(RP, "attachables", SID + ".attachable.json"), {
        "format_version": "1.10.0",
        "minecraft:attachable": {
            "description": {
                "identifier": IDENT,
                "materials": {"default": "entity_alphatest"},
                "textures": {"default": "textures/entity/" + SID + "/" + SID},
                "geometry": {"default": "geometry." + SID},
                "render_controllers": ["controller.render.armor"],
            }
        },
    })


def main():
    textures()
    geometry()
    bbmodel()
    item()
    attachable()


if __name__ == "__main__":
    main()
