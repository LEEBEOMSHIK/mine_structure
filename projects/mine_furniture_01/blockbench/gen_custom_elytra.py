"""Custom elytra-based wings: mine_structure:unicorn_elytra (vanilla elytra untouched).

Worn in the chest slot, glides via minecraft:glider, folds/spreads on q.is_gliding.

Smoothness: instead of a staircase of cubes, each wing is a single THIN FLAT quad
whose shape is painted into the texture with transparency (alpha cutout) -- exactly
how the vanilla elytra is built. The cube outline is a rectangle but the visible
wing is the painted feathered shape, so the silhouette is smooth.

Emits item.json, attachable.json, geo.json, animation.json, animation_controllers.json,
the 64x64 entity atlas, a 16x16 icon, and an editable Blockbench .bbmodel.

NOTE: custom gliders + player-attached animation are version-sensitive; verify in-game.
"""
import base64
import json
import math
import os
import uuid

from PIL import Image

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
RP = os.path.join(BASE, "addon", "resource_pack")
BP_ITEMS = os.path.join(BASE, "addon", "behavior_pack", "items")
HERE = os.path.dirname(__file__)
SID = "unicorn_elytra"
IDENT = "mine_structure:" + SID
RAINBOW = [
    (255, 150, 176), (255, 190, 120), (255, 232, 138), (150, 224, 176),
    (140, 198, 246), (196, 158, 240), (246, 160, 220),
]
ATLAS_REL = os.path.join("textures", "entity", SID, SID + ".png")
# wing painted into a WWxWH region of the 64x64 atlas (1:2, elytra-like proportions)
WW, WH = 16, 32


def write_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent="\t")
    print("wrote", path)


def shade(c, amt):
    return tuple(max(0, min(255, v + amt)) for v in c)


def draw_wing(img):
    """Jet / cicada wing into the WWxWH region (transparent outside): narrow at the
    shoulder (top), fanning WIDER toward the bottom, inner edge straight along the
    spine, with a curved swept outer edge, a rounded bottom and a couple of veins.
    Smooth because the silhouette is an alpha cutout."""
    for y in range(WH):
        ty = y / (WH - 1)
        redge = 1.5 + 14.5 * (ty ** 0.85)          # narrow top -> wide bottom
        if ty > 0.86:
            redge -= (ty - 0.86) * 70              # round off the bottom-outer corner
        redge = max(0.0, min(WW - 1, redge))
        for x in range(WW):
            if x <= redge:
                col = RAINBOW[(y // 3) % len(RAINBOW)]
                if redge - x < 1.3:
                    col = shade(col, -45)           # crisp swept outer edge
                elif x < 1:
                    col = shade(col, -22)           # inner spine edge
                elif abs(x - 0.5 * y) < 0.6 or abs(x - 0.28 * y) < 0.6:
                    col = shade(col, -28)           # radiating veins (cicada/jet)
                elif (x + y) % 15 == 0:
                    col = (255, 255, 255)            # sparkle
                img.putpixel((x, y), col + (255,))


def textures():
    atlas = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    draw_wing(atlas)
    out = os.path.join(RP, ATLAS_REL)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    atlas.save(out)
    print("wrote", out)

    icon = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    for y in range(3, 14):
        col = RAINBOW[(y - 3) % len(RAINBOW)] + (255,)
        for x in range(3, 7):
            icon.putpixel((x, y), col)
        for x in range(9, 13):
            icon.putpixel((x, y), col)
    for y in range(3, 14):
        icon.putpixel((7, y), (236, 210, 130, 255))
        icon.putpixel((8, y), (236, 210, 130, 255))
    icon_out = os.path.join(RP, "textures", "items", SID + ".png")
    icon.save(icon_out)
    print("wrote", icon_out)


# flat wing quads sized like the vanilla elytra (narrow + tall, close to the spine);
# thin in Z so the two big faces (north/south) show the painted wing.
RIGHT = {"from": [1, 6, 2.2], "size": [9, 18, 0.3], "pivot": [1, 23, 2.3]}
LEFT = {"from": [-10, 6, 2.2], "size": [9, 18, 0.3], "pivot": [-1, 23, 2.3]}


def geo_faces(mirror):
    big = {"uv": [WW, 0] if mirror else [0, 0], "uv_size": [-WW, WH] if mirror else [WW, WH]}
    edge = {"uv": [62, 62], "uv_size": [1, 1]}  # transparent corner -> invisible thin sides
    return {"north": dict(big), "south": dict(big), "east": dict(edge),
            "west": dict(edge), "up": dict(edge), "down": dict(edge)}


def geometry():
    def gcube(spec, mirror):
        return {"origin": spec["from"], "size": spec["size"], "uv": geo_faces(mirror)}
    geo = {
        "format_version": "1.12.0",
        "minecraft:geometry": [{
            "description": {
                "identifier": "geometry." + SID,
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 5, "visible_bounds_height": 3,
                "visible_bounds_offset": [0, 1.5, 0],
            },
            "bones": [
                {"name": "body", "pivot": [0, 24, 0]},
                {"name": "right_wing", "parent": "body", "pivot": RIGHT["pivot"], "cubes": [gcube(RIGHT, False)]},
                {"name": "left_wing", "parent": "body", "pivot": LEFT["pivot"], "cubes": [gcube(LEFT, True)]},
            ],
        }],
    }
    write_json(os.path.join(RP, "models", "entity", SID + ".geo.json"), geo)


def bbmodel():
    with open(os.path.join(RP, ATLAS_REL), "rb") as fh:
        src = "data:image/png;base64," + base64.b64encode(fh.read()).decode("ascii")

    def bb_faces(mirror):
        u = [WW, 0, 0, WH] if mirror else [0, 0, WW, WH]
        big = {"uv": u, "texture": 0}
        edge = {"uv": [62, 62, 63, 63], "texture": 0}
        return {"north": dict(big), "south": dict(big), "east": dict(edge),
                "west": dict(edge), "up": dict(edge), "down": dict(edge)}

    def uid():
        return str(uuid.uuid4())

    def element(spec, mirror, name):
        frm = spec["from"]
        to = [frm[i] + spec["size"][i] for i in range(3)]
        return {
            "name": name, "box_uv": False, "render_order": "default", "locked": False,
            "export": True, "scope": 0, "allow_mirror_modeling": True,
            "from": frm, "to": to, "autouv": 0, "color": 0,
            "origin": spec["pivot"], "uv_offset": [0, 0], "faces": bb_faces(mirror),
            "type": "cube", "uuid": uid(),
        }

    r = element(RIGHT, False, "right_wing")
    le = element(LEFT, True, "left_wing")
    u_body, u_r, u_l = uid(), uid(), uid()

    def group(name, uuid_, origin, children):
        return {
            "name": name, "uuid": uuid_, "export": True, "locked": False, "scope": 0,
            "selected": False, "_static": {"properties": {}, "temp_data": {}},
            "origin": origin, "rotation": [0, 0, 0], "bedrock_binding": "", "color": 0,
            "children": children, "reset": False, "shade": False, "mirror_uv": False,
            "visibility": True, "autouv": 0, "isOpen": True, "primary_selected": False,
        }

    groups = [group("body", u_body, [0, 24, 0], []),
              group("right_wing", u_r, RIGHT["pivot"], []),
              group("left_wing", u_l, LEFT["pivot"], [])]
    outliner = [{"uuid": u_body, "name": "body", "isOpen": True, "children": [
        {"uuid": u_r, "name": "right_wing", "isOpen": True, "children": [r["uuid"]]},
        {"uuid": u_l, "name": "left_wing", "isOpen": True, "children": [le["uuid"]]},
    ]}]
    texture = {
        "name": SID + "_atlas.png", "relative_path": "../addon/resource_pack/" + ATLAS_REL.replace(os.sep, "/"),
        "folder": "", "namespace": "", "id": "0", "group": "", "scope": 0,
        "width": 64, "height": 64, "uv_width": 64, "uv_height": 64,
        "particle": False, "use_as_default": False, "layers_enabled": False,
        "sync_to_project": "", "file_format": "png", "render_mode": "default",
        "render_sides": "auto", "wrap_mode": "limited", "pbr_channel": "color",
        "fps": 7, "frame_time": 1, "frame_order_type": "loop", "frame_order": "",
        "frame_interpolate": False, "visible": True, "internal": True, "saved": True,
        "uuid": uid(), "source": src,
    }
    bb = {
        "meta": {"format_version": "5.0", "model_format": "bedrock", "box_uv": False},
        "name": SID, "model_identifier": "", "visible_box": [5, 3, 2],
        "variable_placeholders": "", "multi_file_ruleset": "",
        "variable_placeholder_buttons": [], "bedrock_animation_mode": "entity",
        "timeline_setups": [], "unhandled_root_fields": {},
        "resolution": {"width": 64, "height": 64},
        "elements": [r, le], "groups": groups, "outliner": outliner,
        "textures": [texture], "animations": [],
    }
    out = os.path.join(HERE, SID + ".bbmodel")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(bb, fh, ensure_ascii=False, separators=(",", ":"))
    print("wrote", out)


def item():
    write_json(os.path.join(BP_ITEMS, SID + ".item.json"), {
        "format_version": "1.20.10",
        "minecraft:item": {
            "description": {"identifier": IDENT, "menu_category": {"category": "equipment"}},
            "components": {
                "minecraft:display_name": {"value": "유니콘 엘리트라"},
                "minecraft:icon": {"texture": SID},
                "minecraft:max_stack_size": 1,
                "minecraft:wearable": {"slot": "slot.armor.chest"},
                "minecraft:durability": {"max_durability": 432},
                "minecraft:glider": {},
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
                "animations": {
                    "folded": "animation." + SID + ".folded",
                    "spread": "animation." + SID + ".spread",
                    "glide": "controller.animation." + SID + ".glide",
                },
                "scripts": {"animate": ["glide"]},
                "render_controllers": ["controller.render.armor"],
            }
        },
    })


def animations():
    write_json(os.path.join(RP, "animations", SID + ".animation.json"), {
        "format_version": "1.8.0",
        "animations": {
            "animation." + SID + ".folded": {
                "loop": "hold_on_last_frame", "animation_length": 0.25,
                "bones": {"right_wing": {"rotation": [0, -6, 0]}, "left_wing": {"rotation": [0, 6, 0]}},
            },
            "animation." + SID + ".spread": {
                "loop": "hold_on_last_frame", "animation_length": 0.25,
                "bones": {"right_wing": {"rotation": [0, -38, 0]}, "left_wing": {"rotation": [0, 38, 0]}},
            },
        },
    })


def controller():
    write_json(os.path.join(RP, "animation_controllers", SID + ".animation_controllers.json"), {
        "format_version": "1.10.0",
        "animation_controllers": {
            "controller.animation." + SID + ".glide": {
                "initial_state": "folded",
                "states": {
                    "folded": {"animations": ["folded"], "transitions": [{"spread": "q.is_gliding"}]},
                    "spread": {"animations": ["spread"], "transitions": [{"folded": "!q.is_gliding"}]},
                },
            }
        },
    })


def main():
    textures()
    geometry()
    bbmodel()
    item()
    attachable()
    animations()
    controller()


if __name__ == "__main__":
    main()
