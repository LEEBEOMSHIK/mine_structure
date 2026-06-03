"""Generate four kid-friendly unicorn furniture models.

For each model this emits, from one source of truth:
  - resource_pack/models/entity/<id>.geo.json   (Bedrock geometry, per-face full-cell UV)
  - resource_pack/textures/entity/<id>/<id>_atlas.png  (its own themed 64x64 atlas)
  - blockbench/<id>.bbmodel                      (editable Blockbench source, single texture)

Models / mechanics (mechanics are wired in gen_kids_wiring.py):
  unicorn_rocking_horse      rideable + always-on "rock" animation bone
  unicorn_night_lamp         variant on/off toggle, "glow" bone shown/hidden
  unicorn_ice_cream_machine  Script API gives a treat on interact (static model)
  unicorn_cloud_bunk_bed     rideable, two bunks

Conventions match the rest of the project: 16 units = 1 block, feet at y=0, footprint
centred on origin, no rotated cubes, per-face UV pinned to full 16x16 atlas cells.
Each bbmodel embeds exactly ONE texture so the save-codec face-flatten bug stays local.
"""
import base64
import json
import os
import random
import uuid

from PIL import Image

HERE = os.path.dirname(__file__)
RP = os.path.normpath(os.path.join(HERE, "..", "addon", "resource_pack"))

WHITE = (255, 255, 255, 255)
HORN_RAINBOW = [
    (255, 150, 176), (255, 190, 120), (255, 234, 138), (150, 224, 176),
    (140, 198, 246), (196, 158, 240), (246, 160, 220),
]


def clamp(v):
    return max(0, min(255, int(round(v))))


def shade(c, amt):
    return (clamp(c[0] + amt), clamp(c[1] + amt), clamp(c[2] + amt), 255)


def mix(c, other, t):
    return tuple(clamp(c[i] * (1 - t) + other[i] * t) for i in range(3)) + (255,)


def draw_solid(img, px, py, base, rng, trim=None):
    light, dark = shade(base, 16), shade(base, -20)
    for y in range(16):
        col = light if y <= 2 else dark if y >= 13 else base
        for x in range(16):
            img.putpixel((px + x, py + y), col)
    if trim:
        for x in range(16):
            img.putpixel((px + x, py + 14), trim)
            img.putpixel((px + x, py + 15), shade(trim, -28))
    spark = shade(base, 40)
    for _ in range(rng.randint(3, 5)):
        img.putpixel((px + rng.randint(2, 13), py + rng.randint(2, 12)), shade(base, 30))
    for _ in range(rng.randint(1, 2)):
        cx, cy = rng.randint(3, 12), rng.randint(3, 11)
        img.putpixel((px + cx, py + cy), spark)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            img.putpixel((px + cx + dx, py + cy + dy), mix(spark, base, 0.5))


def draw_horn(img, px, py, rng):
    for y in range(16):
        for x in range(16):
            col = HORN_RAINBOW[((x + y) // 3) % len(HORN_RAINBOW)]
            if (x - y) % 6 == 0:
                col = shade(col, -34)
            elif (x + y) % 7 == 1:
                col = shade(col, 30)
            img.putpixel((px + x, py + y), col)
    for _ in range(8):
        img.putpixel((px + rng.randint(1, 14), py + rng.randint(1, 14)), (255, 248, 200, 255))


def draw_glow(img, px, py, base, rng):
    hi = shade(base, 60)
    for y in range(16):
        for x in range(16):
            d = abs(x - 7.5) + abs(y - 7.5)
            img.putpixel((px + x, py + y), mix(hi, base, min(1.0, d / 14.0)))
    for _ in range(10):
        img.putpixel((px + rng.randint(1, 14), py + rng.randint(1, 14)), WHITE)


def draw_water(img, px, py, base, rng):
    hi = shade(base, 50)
    for y in range(16):
        for x in range(16):
            col = mix(hi, base, y / 15.0)
            if (x + y) % 5 == 0:
                col = mix(col, WHITE, 0.4)
            img.putpixel((px + x, py + y), col)


def draw_face(img, px, py, base, rng):
    """A cute sleepy unicorn face: happy closed eyes, blush, little smile."""
    draw_solid(img, px, py, base, random.Random(1))
    dark = (140, 120, 170, 255)
    cheek = (255, 168, 200, 255)
    # happy closed eyes (gentle smile-shaped arcs)
    for x, y in [(3, 7), (4, 6), (5, 6), (6, 7), (9, 7), (10, 6), (11, 6), (12, 7)]:
        img.putpixel((px + x, py + y), dark)
    # rosy cheeks
    for x in range(3, 5):
        for y in range(9, 11):
            img.putpixel((px + x, py + y), cheek)
    for x in range(11, 13):
        for y in range(9, 11):
            img.putpixel((px + x, py + y), cheek)
    # small smile
    for x, y in [(6, 10), (7, 11), (8, 11), (9, 10)]:
        img.putpixel((px + x, py + y), dark)


def draw_cone(img, px, py, base, rng):
    """Waffle cone: tan with a crosshatch pattern."""
    dark = shade(base, -34)
    for y in range(16):
        for x in range(16):
            col = dark if ((x + y) % 4 == 0 or (x - y) % 4 == 0) else base
            img.putpixel((px + x, py + y), col)


def draw_sign(img, px, py, rng):
    """Menu sign showing a little ice-cream-cone icon."""
    bg = (255, 230, 242, 255)
    tan = (230, 196, 140, 255)
    scoop = (250, 150, 192, 255)
    cherry = (228, 72, 86, 255)
    for y in range(16):
        for x in range(16):
            img.putpixel((px + x, py + y), bg if (x + y) % 7 else shade(bg, -10))
    # scoop (pink blob)
    for y in range(3, 10):
        for x in range(16):
            if (x - 8) ** 2 + (y - 7) ** 2 <= 12:
                img.putpixel((px + x, py + y), scoop)
    img.putpixel((px + 6, py + 5), WHITE)
    # cone (tan triangle, point down)
    for y in range(10, 15):
        half = max(0, 5 - (y - 10))
        for x in range(8 - half, 8 + half + 1):
            img.putpixel((px + x, py + y), tan)
    # cherry
    img.putpixel((px + 8, py + 2), cherry)
    img.putpixel((px + 8, py + 3), cherry)


def draw_capsule(img, px, py, base, rng):
    """Gachapon globe: light base full of colourful capsule dots."""
    draw_solid(img, px, py, base, random.Random(2))
    dots = [(255, 150, 176), (255, 200, 120), (150, 224, 176),
            (140, 198, 246), (200, 158, 240), (250, 230, 130)]
    for _ in range(14):
        cx, cy = rng.randint(1, 13), rng.randint(1, 13)
        col = dots[rng.randint(0, len(dots) - 1)] + (255,)
        img.putpixel((px + cx, py + cy), col)
        img.putpixel((px + cx + 1, py + cy), col)
        img.putpixel((px + cx, py + cy + 1), col)
        img.putpixel((px + cx + 1, py + cy + 1), shade(col, -25))


def make_atlas(sid, specs, seed):
    """specs: ordered list of (name, color, style). Returns (rel_path, base64, cellmap)."""
    img = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    rng = random.Random(seed)
    cellmap = {}
    for i, (name, color, style) in enumerate(specs):
        px, py = 16 * (i % 4), 16 * (i // 4)
        if style == "horn":
            draw_horn(img, px, py, rng)
        elif style == "glow":
            draw_glow(img, px, py, color, rng)
        elif style == "water":
            draw_water(img, px, py, color, rng)
        elif style == "trim":
            draw_solid(img, px, py, color, rng, trim=specs_trim(specs))
        elif style == "face":
            draw_face(img, px, py, color, rng)
        elif style == "cone":
            draw_cone(img, px, py, color, rng)
        elif style == "sign":
            draw_sign(img, px, py, rng)
        elif style == "capsule":
            draw_capsule(img, px, py, color, rng)
        else:
            draw_solid(img, px, py, color, rng)
        cellmap[name] = (px, py)
    rel = os.path.join("textures", "entity", sid, sid + "_atlas.png")
    out = os.path.join(RP, rel)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    img.save(out)
    print("wrote", out)
    with open(out, "rb") as fh:
        return rel, "data:image/png;base64," + base64.b64encode(fh.read()).decode("ascii"), cellmap


def specs_trim(specs):
    for name, color, style in specs:
        if name == "_trimcolor":
            return color
    return (244, 210, 120, 255)


def new_uuid():
    return str(uuid.uuid4())


class Builder:
    def __init__(self, cellmap):
        self.cellmap = cellmap
        self.bones = {}
        self.children = {}
        self.elements = []
        self._color = 0

    def bone(self, name):
        self.bones.setdefault(name, [])
        self.children.setdefault(name, [])

    def add(self, bone, name, frm, size, cell, face_cells=None):
        self.bone(bone)
        face_cells = face_cells or {}
        geo_uv, bb_uv = {}, {}
        for f in ("north", "east", "south", "west", "up", "down"):
            px, py = self.cellmap[face_cells.get(f, cell)]
            geo_uv[f] = {"uv": [px, py], "uv_size": [16, 16]}
            bb_uv[f] = {"uv": [px, py, px + 16, py + 16], "texture": 0}
        self.bones[bone].append({
            "origin": [round(v, 3) for v in frm],
            "size": [round(v, 3) for v in size],
            "uv": geo_uv,
        })
        to = [frm[0] + size[0], frm[1] + size[1], frm[2] + size[2]]
        center = [(frm[i] + to[i]) / 2 for i in range(3)]
        cid = new_uuid()
        self.elements.append({
            "name": name, "box_uv": False, "render_order": "default", "locked": False,
            "export": True, "scope": 0, "allow_mirror_modeling": True,
            "from": [round(v, 3) for v in frm], "to": [round(v, 3) for v in to],
            "autouv": 0, "color": self._color % 8,
            "origin": [round(v, 3) for v in center], "uv_offset": [0, 0],
            "faces": bb_uv, "type": "cube", "uuid": cid,
        })
        self._color += 1
        self.children[bone].append(cid)
        return cid


def assemble(sid, builder, bone_defs, atlas_rel, atlas_source):
    """bone_defs: ordered list of dicts {name, parent, pivot}. Parents must precede children."""
    coords = []
    for cubes in builder.bones.values():
        for cube in cubes:
            o, s = cube["origin"], cube["size"]
            coords.append((o[0], o[1], o[2], o[0] + s[0], o[1] + s[1], o[2] + s[2]))
    max_h = max((abs(v) for c in coords for v in (c[0], c[2], c[3], c[5])), default=8)
    max_y = max((c[4] for c in coords), default=16)
    vb_w = round((max_h * 2) / 16 + 1, 1)
    vb_h = round(max_y / 16 + 0.6, 1)

    geo_bones = []
    for bd in bone_defs:
        bone = {"name": bd["name"], "pivot": bd["pivot"]}
        if bd["parent"]:
            bone["parent"] = bd["parent"]
        cubes = builder.bones.get(bd["name"], [])
        if cubes:
            bone["cubes"] = cubes
        geo_bones.append(bone)

    geo = {
        "format_version": "1.12.0",
        "minecraft:geometry": [{
            "description": {
                "identifier": "geometry." + sid,
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": vb_w, "visible_bounds_height": vb_h,
                "visible_bounds_offset": [0, round(max_y / 32, 2), 0],
            },
            "bones": geo_bones,
        }],
    }
    geo_path = os.path.join(RP, "models", "entity", sid + ".geo.json")
    os.makedirs(os.path.dirname(geo_path), exist_ok=True)
    with open(geo_path, "w", encoding="utf-8") as fh:
        json.dump(geo, fh, ensure_ascii=False, indent="\t")
    print("wrote", geo_path)

    uuids = {bd["name"]: new_uuid() for bd in bone_defs}
    groups = []
    for bd in bone_defs:
        groups.append({
            "name": bd["name"], "uuid": uuids[bd["name"]], "export": True, "locked": False,
            "scope": 0, "selected": False, "_static": {"properties": {}, "temp_data": {}},
            "origin": bd["pivot"], "rotation": [0, 0, 0], "bedrock_binding": "", "color": 0,
            "children": [], "reset": False, "shade": False, "mirror_uv": False,
            "visibility": True, "autouv": 0, "isOpen": True, "primary_selected": False,
        })

    kids = {}
    for bd in bone_defs:
        kids.setdefault(bd["parent"], []).append(bd["name"])

    def node(name):
        children = list(builder.children.get(name, []))
        for child in kids.get(name, []):
            children.append(node(child))
        return {"uuid": uuids[name], "name": name, "isOpen": True, "children": children}

    roots = [node(bd["name"]) for bd in bone_defs if bd["parent"] is None]

    texture = {
        "name": sid + "_atlas.png",
        "relative_path": "../addon/resource_pack/" + atlas_rel.replace(os.sep, "/"),
        "folder": "", "namespace": "", "id": "0", "group": "", "scope": 0,
        "width": 64, "height": 64, "uv_width": 64, "uv_height": 64,
        "particle": False, "use_as_default": False, "layers_enabled": False,
        "sync_to_project": "", "file_format": "png", "render_mode": "default",
        "render_sides": "auto", "wrap_mode": "limited", "pbr_channel": "color",
        "fps": 7, "frame_time": 1, "frame_order_type": "loop", "frame_order": "",
        "frame_interpolate": False, "visible": True, "internal": True, "saved": True,
        "uuid": new_uuid(), "source": atlas_source,
    }
    bb = {
        "meta": {"format_version": "5.0", "model_format": "bedrock", "box_uv": False},
        "name": sid, "model_identifier": "", "visible_box": [vb_w, vb_h, vb_w],
        "variable_placeholders": "", "multi_file_ruleset": "",
        "variable_placeholder_buttons": [], "bedrock_animation_mode": "entity",
        "timeline_setups": [], "unhandled_root_fields": {},
        "resolution": {"width": 64, "height": 64},
        "elements": builder.elements, "groups": groups, "outliner": roots,
        "textures": [texture], "animations": [],
    }
    with open(os.path.join(HERE, sid + ".bbmodel"), "w", encoding="utf-8") as fh:
        json.dump(bb, fh, ensure_ascii=False, separators=(",", ":"))
    print("wrote", os.path.join(HERE, sid + ".bbmodel"))


# ----------------------------------------------------------------- models
def build_rocking_horse():
    sid = "unicorn_rocking_horse"
    specs = [
        ("body", (242, 238, 250), "solid"),
        ("legs", (198, 184, 230), "solid"),
        ("rocker", (246, 168, 206), "solid"),
        ("saddle", (245, 210, 120), "solid"),
        ("muzzle", (250, 204, 226), "solid"),
        ("rainbow", None, "horn"),
    ]
    atlas_rel, src, cm = make_atlas(sid, specs, 6001)
    b = Builder(cm)
    R = "rock"
    # rockers (two side rails) + cross braces
    b.add(R, "rocker_l", [-7, 0, -13], [2, 2, 26], "rocker")
    b.add(R, "rocker_r", [5, 0, -13], [2, 2, 26], "rocker")
    b.add(R, "brace_front", [-7, 1.5, 8], [14, 1.5, 2], "rocker")
    b.add(R, "brace_back", [-7, 1.5, -10], [14, 1.5, 2], "rocker")
    # legs
    for lx, lz, nm in [(-5, 6, "leg_fl"), (3, 6, "leg_fr"), (-5, -8, "leg_bl"), (3, -8, "leg_br")]:
        b.add(R, nm, [lx, 3, lz], [2, 4, 2], "legs")
    # barrel body
    b.add(R, "body", [-5, 6, -9], [10, 7, 16], "body")
    b.add(R, "chest", [-4.5, 6.5, 5], [9, 6.5, 2], "body")
    # neck + head + muzzle
    b.add(R, "neck", [-2.5, 12, 3], [5, 6, 4], "body")
    b.add(R, "head", [-2.5, 16, 4.5], [5, 4, 6], "body")
    b.add(R, "muzzle", [-2, 16.5, 10], [4, 3, 3], "muzzle")
    # ears
    b.add(R, "ear_l", [-2.2, 20, 5], [1.4, 2, 1.4], "body")
    b.add(R, "ear_r", [0.8, 20, 5], [1.4, 2, 1.4], "body")
    # horn (3-seg taper)
    b.add(R, "horn1", [-1, 20, 7], [2, 2.4, 2], "rainbow")
    b.add(R, "horn2", [-0.7, 22.2, 7.3], [1.4, 2, 1.4], "rainbow")
    b.add(R, "horn3", [-0.45, 24, 7.55], [0.9, 1.8, 0.9], "rainbow")
    # mane along neck/head (rainbow strips)
    for i, zz in enumerate([3.2, 4.6, 6.0]):
        b.add(R, "mane%d" % i, [-3, 13 + i * 0.3, zz], [1.2, 6 - i, 1.2], "rainbow")
    # tail (back, -Z)
    b.add(R, "tail1", [-1.5, 7, -10.5], [3, 7, 1.5], "rainbow")
    b.add(R, "tail2", [-1.2, 4, -10.8], [2.4, 4, 1.2], "rainbow")
    # saddle
    b.add(R, "saddle", [-5.5, 13, -3], [11, 1.5, 8], "saddle")
    b.add(R, "saddle_horn", [-1, 14.3, 2.5], [2, 1.5, 1.5], "saddle")

    bone_defs = [
        {"name": sid, "parent": None, "pivot": [0, 0, 0]},
        {"name": R, "parent": sid, "pivot": [0, 1, 0]},
    ]
    assemble(sid, b, bone_defs, atlas_rel, src)


def build_night_lamp():
    """A chubby sleepy cloud-unicorn night light. Front = -Z (north face)."""
    sid = "unicorn_night_lamp"
    specs = [
        ("base", (202, 188, 234), "solid"),
        ("cloud", (250, 250, 255), "solid"),
        ("face", (250, 250, 255), "face"),
        ("star", (247, 212, 120), "solid"),
        ("rainbow", None, "horn"),
        ("glow", (255, 226, 168), "glow"),
    ]
    atlas_rel, src, cm = make_atlas(sid, specs, 6002)
    b = Builder(cm)
    C = "cabinet"
    # little pedestal
    b.add(C, "base", [-3.5, 0, -3.5], [7, 1.5, 7], "base")
    b.add(C, "base_top", [-3, 1.5, -3], [6, 1, 6], "base")
    # chubby cloud body (rounded silhouette via stacked puffs); face on the front (north)
    b.add(C, "cloud_core", [-5, 2.5, -3.5], [10, 7, 7], "cloud", face_cells={"north": "face"})
    b.add(C, "puff_left", [-7, 3.5, -3], [3, 4.5, 6], "cloud")
    b.add(C, "puff_right", [4, 3.5, -3], [3, 4.5, 6], "cloud")
    b.add(C, "puff_top", [-3.5, 9, -3], [7, 3, 6], "cloud")
    # ears + unicorn horn on top
    b.add(C, "ear_left", [-3, 11.5, -1], [1.6, 2, 1.6], "cloud")
    b.add(C, "ear_right", [1.4, 11.5, -1], [1.6, 2, 1.6], "cloud")
    b.add(C, "horn1", [-0.8, 11.5, -1], [1.6, 2.2, 1.6], "rainbow")
    b.add(C, "horn2", [-0.5, 13.5, -0.7], [1, 1.8, 1], "rainbow")
    # tiny gold star topper (always on)
    b.add(C, "star_top", [-1.4, 14.5, -0.5], [2.8, 2.8, 0.6], "star")
    # glow twinkles (toggled, hidden by default; appear around the cloud when on)
    G = "glow"
    b.add(G, "tw_l", [-9, 7, -0.8], [2, 2, 0.6], "glow")
    b.add(G, "tw_r", [7, 8, -0.8], [1.8, 1.8, 0.6], "glow")
    b.add(G, "tw_bl", [-8, 2.5, -0.8], [1.4, 1.4, 0.6], "glow")
    b.add(G, "tw_br", [6.4, 3, -0.8], [1.4, 1.4, 0.6], "glow")
    b.add(G, "tw_top", [-2.5, 16, -0.8], [1.8, 1.8, 0.6], "glow")

    bone_defs = [
        {"name": sid, "parent": None, "pivot": [0, 0, 0]},
        {"name": C, "parent": sid, "pivot": [0, 0, 0]},
        {"name": G, "parent": sid, "pivot": [0, 8, 0]},
    ]
    assemble(sid, b, bone_defs, atlas_rel, src)


def build_ice_cream_machine():
    """Soft-serve machine: two-tone body, a hero cone with white/pink swirl + cherry
    on the serving tray, and a cone-icon menu sign. Front = -Z (north face)."""
    sid = "unicorn_ice_cream_machine"
    specs = [
        ("body_white", (248, 244, 250), "solid"),
        ("body_pink", (248, 178, 214), "solid"),
        ("tray", (196, 224, 240), "solid"),
        ("cone", (230, 196, 140), "cone"),
        ("swirl_white", (255, 250, 250), "solid"),
        ("swirl_pink", (250, 182, 210), "solid"),
        ("cherry", (228, 72, 86), "solid"),
        ("sign", None, "sign"),
        ("lever", (247, 212, 120), "solid"),
        ("rainbow", None, "horn"),
    ]
    atlas_rel, src, cm = make_atlas(sid, specs, 6003)
    b = Builder(cm)
    M = "machine"
    # two-tone rounded body
    b.add(M, "body_lower", [-5, 0, -5], [10, 7, 9], "body_white")
    b.add(M, "body_upper", [-5, 7, -5], [10, 6, 9], "body_pink")
    b.add(M, "body_cap", [-5.5, 13, -4.5], [11, 2.5, 8], "body_pink")
    # serving tray sticking out the front (-Z)
    b.add(M, "tray", [-3.5, 6, -8], [7, 1, 3], "tray")
    # the hero cone (waffle, point down) sitting on the tray
    b.add(M, "cone_tip", [-1, 7, -7], [2, 2, 2], "cone")
    b.add(M, "cone_mid", [-2, 9, -7.5], [4, 2, 4], "cone")
    b.add(M, "cone_rim", [-2.5, 11, -8], [5, 1.5, 5], "cone")
    # soft-serve swirl (alternating white/pink, tapering to a point)
    b.add(M, "swirl1", [-2.2, 12.5, -7.8], [4.4, 2, 4.4], "swirl_white")
    b.add(M, "swirl2", [-1.8, 14.5, -7.4], [3.6, 2, 3.6], "swirl_pink")
    b.add(M, "swirl3", [-1.3, 16.5, -6.9], [2.6, 2, 2.6], "swirl_white")
    b.add(M, "swirl4", [-0.8, 18.5, -6.4], [1.6, 1.8, 1.6], "swirl_pink")
    b.add(M, "swirl_tip", [-0.4, 20, -6], [0.8, 1.2, 0.8], "swirl_white")
    b.add(M, "cherry", [-0.6, 21, -6], [1.2, 1.2, 1.2], "cherry")
    # menu sign on top, cone icon facing the front (north)
    b.add(M, "sign_post", [-0.6, 15.5, -1], [1.2, 2, 1.2], "body_white")
    b.add(M, "sign_board", [-4, 17, -1.4], [8, 5, 0.8], "body_pink", face_cells={"north": "sign"})
    # side lever
    b.add(M, "lever", [4.8, 6, -1], [1, 5, 1], "lever")
    b.add(M, "lever_knob", [4.6, 10.5, -1.2], [1.4, 1.4, 1.4], "rainbow")
    # small unicorn touch on the back top
    b.add(M, "ear_l", [-4.5, 15.5, 2.5], [1.4, 2, 1.4], "body_pink")
    b.add(M, "ear_r", [3.1, 15.5, 2.5], [1.4, 2, 1.4], "body_pink")
    b.add(M, "horn", [-0.7, 15.5, 3], [1.4, 2.2, 1.4], "rainbow")

    bone_defs = [
        {"name": sid, "parent": None, "pivot": [0, 0, 0]},
        {"name": M, "parent": sid, "pivot": [0, 0, 0]},
    ]
    assemble(sid, b, bone_defs, atlas_rel, src)


def build_cloud_bunk_bed():
    sid = "unicorn_cloud_bunk_bed"
    specs = [
        ("cloud", (246, 246, 252), "solid"),
        ("mattress", (190, 214, 245), "solid"),
        ("pillow", (248, 196, 224), "solid"),
        ("post", (200, 186, 232), "solid"),
        ("ladder", (245, 210, 120), "solid"),
        ("rainbow", None, "horn"),
    ]
    atlas_rel, src, cm = make_atlas(sid, specs, 6004)
    b = Builder(cm)
    F = "frame"
    # 4 posts (length x ~24, depth z ~14)
    for px, pz, nm in [(-12, -7, "post_a"), (10, -7, "post_b"), (-12, 5, "post_c"), (10, 5, "post_d")]:
        b.add(F, nm, [px, 0, pz], [2, 26, 2], "post")
    # star toppers
    for px, pz, nm in [(-12.4, -7.4, "star_a"), (9.6, -7.4, "star_b"), (-12.4, 4.6, "star_c"), (9.6, 4.6, "star_d")]:
        b.add(F, nm, [px, 26, pz], [2.8, 2.8, 2.8], "rainbow")
    # bottom bunk
    b.add(F, "bot_mat", [-11, 4, -6], [22, 3, 12], "mattress")
    b.add(F, "bot_pillow", [-11, 7, -5], [5, 2, 10], "pillow")
    b.add(F, "bot_blanket", [-5.5, 7, -6], [16, 1, 12], "rainbow")
    b.add(F, "bot_rail", [-12, 7, 5.5], [24, 1.5, 1], "cloud")
    # top bunk
    b.add(F, "top_mat", [-11, 16, -6], [22, 3, 12], "mattress")
    b.add(F, "top_pillow", [-11, 19, -5], [5, 2, 10], "pillow")
    b.add(F, "top_blanket", [-5.5, 19, -6], [16, 1, 12], "rainbow")
    b.add(F, "top_rail", [-12, 19, 5.5], [24, 1.5, 1], "cloud")
    # cloud puffs along the sides
    for i, xx in enumerate([-9, -3, 3, 9]):
        b.add(F, "puff_b%d" % i, [xx - 2, 2.5, -7.5], [4, 3, 2], "cloud")
        b.add(F, "puff_t%d" % i, [xx - 2, 14.5, -7.5], [4, 3, 2], "cloud")
    # ladder on right end
    b.add(F, "ladder_l", [11, 4, -2], [1, 14, 1], "ladder")
    b.add(F, "ladder_r", [11, 4, 2], [1, 14, 1], "ladder")
    for i, yy in enumerate([6, 9, 12, 15]):
        b.add(F, "rung%d" % i, [11, yy, -2], [1, 1, 4], "ladder")

    bone_defs = [
        {"name": sid, "parent": None, "pivot": [0, 0, 0]},
        {"name": F, "parent": sid, "pivot": [0, 0, 0]},
    ]
    assemble(sid, b, bone_defs, atlas_rel, src)


def main():
    build_rocking_horse()
    build_night_lamp()
    build_ice_cream_machine()
    build_cloud_bunk_bed()


if __name__ == "__main__":
    main()
