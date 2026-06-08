"""Custom butterfly wings: mine_structure:unicorn_elytra (vanilla elytra untouched).

Worn in the chest slot, glides via minecraft:glider, folds/spreads on q.is_gliding.

Ref game/mine_reference/005.png: a real BUTTERFLY worn on the back -- a large
rounded FOREWING up top and a smaller HINDWING below, spread out to each side.
So each side is built from TWO thin flat lobes (forewing + hindwing) parented to
the wing bone, fanning up/down and outward, rather than one tall elytra plane.

Each lobe is a flat quad whose butterfly shape is painted with alpha cutout, with
a pastel gradient, dark veins, an edge band with dots, and an eyespot.

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

# pastel RAINBOW butterfly palette: each wing graded through the rainbow inner->outer,
# divided by white veins/edges (stained-glass look) with a dark body.
RAINBOW = [
    (255, 158, 176),   # pink-red
    (255, 196, 150),   # orange
    (255, 240, 158),   # yellow
    (168, 226, 168),   # green
    (150, 202, 246),   # blue
    (202, 166, 240),   # violet
]
LINE = (255, 255, 255)       # white veins / edge band (stained-glass dividers)
BODY = (96, 64, 142)         # dark body / inner spine
EYE_C = (236, 120, 190)      # eyespot centre (pink)


def rainbow(t):
    t = max(0.0, min(1.0, t)) * (len(RAINBOW) - 1)
    i = int(t)
    if i >= len(RAINBOW) - 1:
        return RAINBOW[-1]
    return lerp(RAINBOW[i], RAINBOW[i + 1], t - i)

ATLAS_REL = os.path.join("textures", "entity", SID, SID + ".png")
ATLAS_SIZE = 128
# UV regions (u0, v0, w, h) for the forewing and hindwing lobes
FORE_UV = (0, 0, 32, 40)
HIND_UV = (0, 44, 28, 34)


def write_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent="\t")
    print("wrote", path)


def lerp(a, b, t):
    t = max(0.0, min(1.0, t))
    return tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))


def spot(img, cx, cy, r):
    """Eyespot: pink centre + white ring + dark rim, clipped to painted pixels."""
    for yy in range(int(cy - r), int(cy + r + 1)):
        for xx in range(int(cx - r), int(cx + r + 1)):
            if not (0 <= xx < ATLAS_SIZE and 0 <= yy < ATLAS_SIZE):
                continue
            if img.getpixel((xx, yy))[3] == 0:
                continue
            d = math.hypot(xx - cx, yy - cy)
            if d <= r * 0.45:
                img.putpixel((xx, yy), EYE_C + (255,))
            elif d <= r * 0.78:
                img.putpixel((xx, yy), LINE + (255,))
            elif d <= r:
                img.putpixel((xx, yy), BODY + (255,))


def draw_lobe(img, ox, oy, rw, rh, mode):
    """Paint one RAINBOW butterfly lobe into the (ox,oy,rw,rh) region. Inner edge
    (x=ox) is the straight body attachment; the outer edge is a rounded butterfly
    curve. Colour runs through the rainbow inner->outer, split by white veins and a
    white edge band (stained-glass look). 'fore' = broad rounded top; 'hind' =
    rounded lobe."""
    veins = 4
    for vy in range(rh):
        tv = vy / (rh - 1)                              # 0 = top .. 1 = bottom(root)
        if mode == "fore":
            peak = max(0.0, 1.0 - abs(tv - 0.30) / 0.74)
            redge = rw * (0.16 + 0.82 * peak ** 0.55)
        else:
            dy = (tv - 0.45) * 2.0
            redge = rw * math.sqrt(max(0.0, 1.0 - dy * dy * 0.82))
        redge = max(0.0, min(rw - 1, redge))
        for vx in range(rw):
            if vx > redge:
                continue
            tip = vx / redge if redge > 0 else 0.0
            col = rainbow(tip)                          # rainbow inner -> outer
            ang = math.atan2((rh - vy) + 1.0, vx + 1.0)  # veins fan from the root
            fi = (ang / (math.pi / 2)) * veins
            fr = fi - math.floor(fi)
            if fr < 0.07 or fr > 0.93:
                col = LINE                              # white vein dividers
            if tip > 0.9:                               # white outer edge band
                col = LINE
            if vx < 1:                                  # dark body edge
                col = BODY
            img.putpixel((ox + vx, oy + vy), col + (255,))
    spot(img, ox + int(rw * 0.42), oy + int(rh * 0.40), max(2.5, rw * 0.17))


def textures():
    atlas = Image.new("RGBA", (ATLAS_SIZE, ATLAS_SIZE), (0, 0, 0, 0))
    draw_lobe(atlas, FORE_UV[0], FORE_UV[1], FORE_UV[2], FORE_UV[3], "fore")
    draw_lobe(atlas, HIND_UV[0], HIND_UV[1], HIND_UV[2], HIND_UV[3], "hind")
    out = os.path.join(RP, ATLAS_REL)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    atlas.save(out)
    print("wrote", out)

    # icon: a pair of rainbow butterfly wings (forewing + hindwing) + dark body
    icon = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    cx = 8
    for y in range(1, 9):                               # forewing pair (upper)
        u = (y - 1) / 7
        half = 1 + int(5.5 * math.sin((1 - u) * math.pi * 0.62))
        for dx in range(1, half + 1):
            col = LINE if dx >= half else rainbow(dx / max(1, half))
            icon.putpixel((cx - 1 - dx, y), col + (255,))
            icon.putpixel((cx + dx, y), col + (255,))
    for y in range(8, 15):                              # hindwing pair (lower)
        u = (y - 8) / 6
        half = 1 + int(4.5 * math.sin((1 - abs(u - 0.4)) * math.pi * 0.5))
        for dx in range(1, half + 1):
            col = LINE if dx >= half else rainbow(dx / max(1, half))
            icon.putpixel((cx - 1 - dx, y), col + (255,))
            icon.putpixel((cx + dx, y), col + (255,))
    for by in range(1, 15):                             # dark body down the middle
        icon.putpixel((cx - 1, by), BODY + (255,))
        icon.putpixel((cx, by), BODY + (255,))
    icon_out = os.path.join(RP, "textures", "items", SID + ".png")
    icon.save(icon_out)
    print("wrote", icon_out)


# Four thin lobes (flat in Z). Forewing up + out, hindwing down + out; spine inner.
FORE_R = {"from": [0.5, 18, 2.35], "size": [16, 20, 0.05], "pivot": [1, 24, 2.375], "uv": FORE_UV}
HIND_R = {"from": [0.5, 3, 2.35], "size": [14, 16, 0.05], "pivot": [1, 24, 2.375], "uv": HIND_UV}
FORE_L = {"from": [-16.5, 18, 2.35], "size": [16, 20, 0.05], "pivot": [-1, 24, 2.375], "uv": FORE_UV}
HIND_L = {"from": [-14.5, 3, 2.35], "size": [14, 16, 0.05], "pivot": [-1, 24, 2.375], "uv": HIND_UV}


def geo_faces(uv, mirror):
    u0, v0, uw, vh = uv
    big = {"uv": [u0 + uw, v0] if mirror else [u0, v0],
           "uv_size": [-uw, vh] if mirror else [uw, vh]}
    edge = {"uv": [ATLAS_SIZE - 2, ATLAS_SIZE - 2], "uv_size": [1, 1]}  # transparent corner
    return {"north": dict(big), "south": dict(big), "east": dict(edge),
            "west": dict(edge), "up": dict(edge), "down": dict(edge)}


def geometry():
    def gcube(spec, mirror):
        return {"origin": spec["from"], "size": spec["size"], "uv": geo_faces(spec["uv"], mirror)}
    geo = {
        "format_version": "1.12.0",
        "minecraft:geometry": [{
            "description": {
                "identifier": "geometry." + SID,
                "texture_width": ATLAS_SIZE, "texture_height": ATLAS_SIZE,
                "visible_bounds_width": 8, "visible_bounds_height": 5,
                "visible_bounds_offset": [0, 1.5, 0],
            },
            "bones": [
                {"name": "body", "pivot": [0, 24, 0]},
                {"name": "right_wing", "parent": "body", "pivot": [1, 24, 2.375],
                 "cubes": [gcube(FORE_R, False), gcube(HIND_R, False)]},
                {"name": "left_wing", "parent": "body", "pivot": [-1, 24, 2.375],
                 "cubes": [gcube(FORE_L, True), gcube(HIND_L, True)]},
            ],
        }],
    }
    write_json(os.path.join(RP, "models", "entity", SID + ".geo.json"), geo)


def bbmodel():
    with open(os.path.join(RP, ATLAS_REL), "rb") as fh:
        src = "data:image/png;base64," + base64.b64encode(fh.read()).decode("ascii")

    def uid():
        return str(uuid.uuid4())

    def bb_faces(uv, mirror):
        u0, v0, uw, vh = uv
        u = [u0 + uw, v0, u0, v0 + vh] if mirror else [u0, v0, u0 + uw, v0 + vh]
        big = {"uv": u, "texture": 0}
        edge = {"uv": [ATLAS_SIZE - 2, ATLAS_SIZE - 2, ATLAS_SIZE - 1, ATLAS_SIZE - 1], "texture": 0}
        return {"north": dict(big), "south": dict(big), "east": dict(edge),
                "west": dict(edge), "up": dict(edge), "down": dict(edge)}

    def element(spec, mirror, name):
        frm = spec["from"]
        to = [frm[i] + spec["size"][i] for i in range(3)]
        return {
            "name": name, "box_uv": False, "render_order": "default", "locked": False,
            "export": True, "scope": 0, "allow_mirror_modeling": True,
            "from": frm, "to": to, "autouv": 0, "color": 0,
            "origin": spec["pivot"], "uv_offset": [0, 0], "faces": bb_faces(spec["uv"], mirror),
            "type": "cube", "uuid": uid(),
        }

    fr = element(FORE_R, False, "right_forewing")
    hr = element(HIND_R, False, "right_hindwing")
    fl = element(FORE_L, True, "left_forewing")
    hl = element(HIND_L, True, "left_hindwing")
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
              group("right_wing", u_r, [1, 24, 2.375], []),
              group("left_wing", u_l, [-1, 24, 2.375], [])]
    outliner = [{"uuid": u_body, "name": "body", "isOpen": True, "children": [
        {"uuid": u_r, "name": "right_wing", "isOpen": True, "children": [fr["uuid"], hr["uuid"]]},
        {"uuid": u_l, "name": "left_wing", "isOpen": True, "children": [fl["uuid"], hl["uuid"]]},
    ]}]
    texture = {
        "name": SID + "_atlas.png", "relative_path": "../addon/resource_pack/" + ATLAS_REL.replace(os.sep, "/"),
        "folder": "", "namespace": "", "id": "0", "group": "", "scope": 0,
        "width": ATLAS_SIZE, "height": ATLAS_SIZE, "uv_width": ATLAS_SIZE, "uv_height": ATLAS_SIZE,
        "particle": False, "use_as_default": False, "layers_enabled": False,
        "sync_to_project": "", "file_format": "png", "render_mode": "default",
        "render_sides": "auto", "wrap_mode": "limited", "pbr_channel": "color",
        "fps": 7, "frame_time": 1, "frame_order_type": "loop", "frame_order": "",
        "frame_interpolate": False, "visible": True, "internal": True, "saved": True,
        "uuid": uid(), "source": src,
    }
    bb = {
        "meta": {"format_version": "5.0", "model_format": "bedrock", "box_uv": False},
        "name": SID, "model_identifier": "", "visible_box": [8, 5, 2],
        "variable_placeholders": "", "multi_file_ruleset": "",
        "variable_placeholder_buttons": [], "bedrock_animation_mode": "entity",
        "timeline_setups": [], "unhandled_root_fields": {},
        "resolution": {"width": ATLAS_SIZE, "height": ATLAS_SIZE},
        "elements": [fr, hr, fl, hl], "groups": groups, "outliner": outliner,
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
                "minecraft:display_name": {"value": "나비 날개"},
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
            # resting: wings angled back a touch
            "animation." + SID + ".folded": {
                "loop": "hold_on_last_frame", "animation_length": 0.25,
                "bones": {"right_wing": {"rotation": [0, -12, 0]}, "left_wing": {"rotation": [0, 12, 0]}},
            },
            # gliding: butterfly wings spread wide AND flap up/down in a loop
            "animation." + SID + ".spread": {
                "loop": True, "animation_length": 0.7,
                "bones": {
                    "right_wing": {"rotation": {
                        "0.0": [0, -50, -2], "0.35": [0, -38, -30], "0.7": [0, -50, -2]}},
                    "left_wing": {"rotation": {
                        "0.0": [0, 50, 2], "0.35": [0, 38, 30], "0.7": [0, 50, 2]}},
                },
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
