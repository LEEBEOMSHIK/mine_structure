"""Generate the three unicorn sink models.

For each sink shape this emits, from a single source of truth:
  - resource_pack/models/entity/<id>.geo.json   (Bedrock geometry, per-face UV)
  - resource_pack/textures/entity/unicorn_sink/<id>_atlas.png  (its OWN themed atlas)
  - blockbench/<id>.bbmodel                      (editable Blockbench source)

Why one generator:
  The three sinks share the exact same part vocabulary (counter body, top slab,
  basin rim/walls, faucet, unicorn horn, water). Authoring 3 multi-cube models by
  hand invites per-face UV mistakes (which made the blade render white) and the
  Blockbench save-codec "flatten all faces to one texture" bug. Generating geo +
  bbmodel together from one layout keeps them in lockstep, and each bbmodel embeds
  exactly ONE texture so the flatten bug cannot corrupt anything.

Each sink gets its OWN colourful theme (kid-friendly), while the unicorn signature
(rainbow horn + pastel + sparkles) is kept on all three:
  unicorn_sink_l      strawberry  (pink body, heart sparkles)
  unicorn_sink_island mint        (mint body, star sparkles)
  unicorn_sink_u      lemon       (butter-yellow body, bubble sparkles)

Footprints (1 = block present, row 0 = back):
  unicorn_sink_l      [[1,1,1],[0,0,1]]            basin = back-centre (faucet centred across the 3-wide)
  unicorn_sink_island [[1,1,1],[1,0,1],[1,0,1]]    ring, front-centre is the entrance, basin = back-centre
  unicorn_sink_u      [[1,1,1],[0,0,1],[1,1,1]]    C/U open on the left, basin = back-centre

Each cell is one Minecraft block (16 units). Water is two bones (water_stream,
basin_pool) that the resource animation controller scales 0<->1 on q.variant.

Atlas cells (64x64, 16px cells):
  body (0,0)  top (16,0)  rim (32,0)  wall (48,0)
  faucet (0,16)  horn (16,16)  water (32,16)
"""
import base64
import json
import os
import random
import uuid

from PIL import Image

HERE = os.path.dirname(__file__)
RP = os.path.normpath(os.path.join(HERE, "..", "addon", "resource_pack"))
ATLAS_DIR_REL = os.path.join("textures", "entity", "unicorn_sink")

CELLS = {
    "body": (0, 0),
    "top": (16, 0),
    "rim": (32, 0),
    "wall": (48, 0),
    "faucet": (0, 16),
    "horn": (16, 16),
    "water": (32, 16),
}

SHAPES = {
    "unicorn_sink_l": {"grid": [[1, 1, 1], [0, 0, 1]], "basin": (0, 1)},
    "unicorn_sink_island": {"grid": [[1, 1, 1], [1, 0, 1], [1, 0, 1]], "basin": (0, 1)},
    "unicorn_sink_u": {"grid": [[1, 1, 1], [0, 0, 1], [1, 1, 1]], "basin": (0, 1)},
}

WHITE = (255, 255, 255, 255)
HORN_RAINBOW = [
    (255, 150, 176),
    (255, 190, 120),
    (255, 234, 138),
    (150, 224, 176),
    (140, 198, 246),
    (196, 158, 240),
    (246, 160, 220),
]

# distinct kid-friendly themes (still pastel + rainbow horn = unicorn)
THEMES = {
    "unicorn_sink_l": {
        "label": "strawberry",
        "body": (247, 162, 208),
        "top": (255, 224, 240),
        "rim": (247, 206, 108),
        "wall": (255, 208, 230),
        "faucet": (236, 200, 220),
        "water": (150, 214, 242),
        "speckle": (255, 246, 252),
        "motif": "heart",
        "seed": 5101,
    },
    "unicorn_sink_island": {
        "label": "mint",
        "body": (146, 222, 198),
        "top": (216, 246, 236),
        "rim": (184, 160, 230),
        "wall": (200, 240, 228),
        "faucet": (198, 220, 214),
        "water": (118, 196, 236),
        "speckle": (245, 255, 252),
        "motif": "star",
        "seed": 5102,
    },
    "unicorn_sink_u": {
        "label": "lemon",
        "body": (250, 222, 132),
        "top": (255, 244, 198),
        "rim": (244, 152, 196),
        "wall": (252, 236, 190),
        "faucet": (230, 218, 192),
        "water": (150, 226, 220),
        "speckle": (255, 252, 236),
        "motif": "bubble",
        "seed": 5103,
    },
}

MOTIFS = {
    "heart": [(0, 0), (-1, -1), (1, -1), (-2, 0), (2, 0), (-1, 1), (1, 1), (0, 2)],
    "star": [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1), (2, 0), (-2, 0), (0, 2), (0, -2)],
    "bubble": [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (1, -1), (-1, 1)],
}


def clamp(v):
    return max(0, min(255, int(round(v))))


def shade(c, amt):
    return (clamp(c[0] + amt), clamp(c[1] + amt), clamp(c[2] + amt), 255)


def mix(c, other, t):
    return (
        clamp(c[0] * (1 - t) + other[0] * t),
        clamp(c[1] * (1 - t) + other[1] * t),
        clamp(c[2] * (1 - t) + other[2] * t),
        255,
    )


def put_motif(img, px, py, cx, cy, motif, color):
    for dx, dy in MOTIFS[motif]:
        x, y = cx + dx, cy + dy
        if 0 <= x < 16 and 0 <= y < 16:
            img.putpixel((px + x, py + y), color)


def fill_cell(img, px, py, base, theme, rng, kind="solid"):
    light = shade(base, 16)
    dark = shade(base, -20)
    for y in range(16):
        col = light if y <= 2 else dark if y >= 13 else base
        for x in range(16):
            img.putpixel((px + x, py + y), col)
    if kind == "trim":
        for x in range(16):
            img.putpixel((px + x, py + 14), theme["rim"])
            img.putpixel((px + x, py + 15), shade(theme["rim"], -28))
    # cute droplet speckles
    droplet = mix(base, theme["water"], 0.45)
    for _ in range(rng.randint(4, 6)):
        img.putpixel((px + rng.randint(2, 13), py + rng.randint(2, 12)), droplet)
    # themed motif sparkles
    for _ in range(rng.randint(2, 3)):
        put_motif(img, px, py, rng.randint(3, 12), rng.randint(3, 11),
                  theme["motif"], theme["speckle"])


def fill_horn(img, px, py, rng):
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


def fill_water(img, px, py, theme, rng):
    hi = shade(theme["water"], 50)
    for y in range(16):
        for x in range(16):
            col = mix(hi, theme["water"], y / 15.0)
            if (x + y) % 5 == 0:
                col = mix(col, WHITE, 0.4)
            img.putpixel((px + x, py + y), col)
    for _ in range(6):
        img.putpixel((px + rng.randint(1, 14), py + rng.randint(1, 14)), hi)


def build_atlas(sid, theme):
    img = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    rng = random.Random(theme["seed"])
    fill_cell(img, *CELLS["body"], base=theme["body"], theme=theme, rng=rng)
    fill_cell(img, *CELLS["top"], base=theme["top"], theme=theme, rng=rng, kind="trim")
    fill_cell(img, *CELLS["rim"], base=theme["rim"], theme=theme, rng=rng)
    fill_cell(img, *CELLS["wall"], base=theme["wall"], theme=theme, rng=rng)
    fill_cell(img, *CELLS["faucet"], base=theme["faucet"], theme=theme, rng=rng)
    fill_horn(img, *CELLS["horn"], rng=rng)
    fill_water(img, *CELLS["water"], theme=theme, rng=rng)
    rel = os.path.join(ATLAS_DIR_REL, sid + "_atlas.png")
    out = os.path.join(RP, rel)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    img.save(out)
    print("wrote", out)
    with open(out, "rb") as fh:
        return rel, "data:image/png;base64," + base64.b64encode(fh.read()).decode("ascii")


def cell_center(r, c, nrows):
    xc = (c - 1) * 16.0
    zc = ((nrows - 1) / 2.0 - r) * 16.0
    return xc, zc


def new_uuid():
    return str(uuid.uuid4())


def geo_face_uv(cell):
    px, py = cell
    return {f: {"uv": [px, py], "uv_size": [16, 16]}
            for f in ("north", "east", "south", "west", "up", "down")}


def bb_face_uv(cell):
    px, py = cell
    return {f: {"uv": [px, py, px + 16, py + 16], "texture": 0}
            for f in ("north", "east", "south", "west", "up", "down")}


class Builder:
    def __init__(self):
        self.bones = {}
        self.children = {}
        self.elements = []
        self._color = 0

    def bone(self, name):
        self.bones.setdefault(name, [])
        self.children.setdefault(name, [])

    def add(self, bone, name, frm, size, cell):
        self.bone(bone)
        px, py = CELLS[cell]
        self.bones[bone].append({
            "origin": [round(frm[0], 3), round(frm[1], 3), round(frm[2], 3)],
            "size": [round(size[0], 3), round(size[1], 3), round(size[2], 3)],
            "uv": geo_face_uv((px, py)),
        })
        to = [frm[0] + size[0], frm[1] + size[1], frm[2] + size[2]]
        center = [(frm[0] + to[0]) / 2, (frm[1] + to[1]) / 2, (frm[2] + to[2]) / 2]
        cid = new_uuid()
        self.elements.append({
            "name": name, "box_uv": False, "render_order": "default", "locked": False,
            "export": True, "scope": 0, "allow_mirror_modeling": True,
            "from": [round(v, 3) for v in frm], "to": [round(v, 3) for v in to],
            "autouv": 0, "color": self._color % 8,
            "origin": [round(v, 3) for v in center], "uv_offset": [0, 0],
            "faces": bb_face_uv((px, py)), "type": "cube", "uuid": cid,
        })
        self._color += 1
        self.children[bone].append(cid)
        return cid


def build_sink(sid, spec, atlas_rel, atlas_source):
    grid = spec["grid"]
    nrows = len(grid)
    basin = tuple(spec["basin"])
    b = Builder()
    for bone in ("cabinet", "faucet", "water_stream", "basin_pool"):
        b.bone(bone)

    bx, bz = cell_center(basin[0], basin[1], nrows)

    for r in range(nrows):
        for c in range(3):
            if not grid[r][c]:
                continue
            xc, zc = cell_center(r, c, nrows)
            if (r, c) == basin:
                b.add("cabinet", "basin_base", [xc - 8, 0, zc - 8], [16, 8, 16], "body")
                b.add("cabinet", "wall_back", [xc - 8, 8, zc + 5], [16, 4, 3], "wall")
                b.add("cabinet", "wall_front", [xc - 8, 8, zc - 8], [16, 4, 3], "wall")
                b.add("cabinet", "wall_left", [xc - 8, 8, zc - 5], [3, 4, 10], "wall")
                b.add("cabinet", "wall_right", [xc + 5, 8, zc - 5], [3, 4, 10], "wall")
                b.add("cabinet", "rim_back", [xc - 8, 12, zc + 5], [16, 1.5, 3], "rim")
                b.add("cabinet", "rim_front", [xc - 8, 12, zc - 8], [16, 1.5, 3], "rim")
                b.add("cabinet", "rim_left", [xc - 8, 12, zc - 5], [3, 1.5, 10], "rim")
                b.add("cabinet", "rim_right", [xc + 5, 12, zc - 5], [3, 1.5, 10], "rim")
            else:
                b.add("cabinet", "cabinet_body", [xc - 8, 0, zc - 8], [16, 12, 16], "body")
                b.add("cabinet", "counter_top", [xc - 8, 12, zc - 8], [16, 1.5, 16], "top")

    b.add("faucet", "faucet_post", [bx - 1, 13.5, bz + 5.5], [2, 7, 2], "faucet")
    b.add("faucet", "faucet_arm", [bx - 1, 18.5, bz - 0.5], [2, 2, 6.5], "faucet")
    b.add("faucet", "faucet_nozzle", [bx - 0.75, 17, bz - 0.5], [1.5, 1.5, 1.5], "faucet")
    b.add("faucet", "horn_seg1", [bx - 0.9, 20.5, bz + 5.6], [1.8, 2, 1.8], "horn")
    b.add("faucet", "horn_seg2", [bx - 0.7, 22.5, bz + 5.8], [1.4, 1.8, 1.4], "horn")
    b.add("faucet", "horn_tip", [bx - 0.5, 24.3, bz + 6.0], [0.9, 1.8, 0.9], "horn")

    b.add("water_stream", "water_stream", [bx - 0.6, 8.6, bz - 0.5], [1.2, 8.4, 1.2], "water")
    b.add("basin_pool", "basin_pool", [bx - 4.5, 8.4, bz - 4.5], [9, 0.6, 9], "water")

    all_coords = []
    for cubes in b.bones.values():
        for cube in cubes:
            ox, oy, oz = cube["origin"]
            sx, sy, sz = cube["size"]
            all_coords.append((ox, oy, oz, ox + sx, oy + sy, oz + sz))
    max_h = max(abs(v) for c in all_coords for v in (c[0], c[2], c[3], c[5]))
    max_y = max(c[4] for c in all_coords)
    vb_w = round((max_h * 2) / 16 + 1, 1)
    vb_h = round(max_y / 16 + 0.6, 1)

    geo_bones = [
        {"name": sid, "pivot": [0, 0, 0]},
        {"name": "cabinet", "parent": sid, "pivot": [0, 0, 0], "cubes": b.bones["cabinet"]},
        {"name": "faucet", "parent": sid, "pivot": [0, 0, 0], "cubes": b.bones["faucet"]},
        {"name": "water", "parent": sid, "pivot": [bx, 9, bz]},
        {"name": "water_stream", "parent": "water", "pivot": [bx, 8.6, bz - 0.5], "cubes": b.bones["water_stream"]},
        {"name": "basin_pool", "parent": "water", "pivot": [bx, 8.7, bz], "cubes": b.bones["basin_pool"]},
    ]
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

    def group(name, origin, bone_uuid):
        return {
            "name": name, "uuid": bone_uuid, "export": True, "locked": False, "scope": 0,
            "selected": False, "_static": {"properties": {}, "temp_data": {}},
            "origin": origin, "rotation": [0, 0, 0], "bedrock_binding": "", "color": 0,
            "children": [], "reset": False, "shade": False, "mirror_uv": False,
            "visibility": True, "autouv": 0, "isOpen": True, "primary_selected": False,
        }

    u_root, u_cab, u_fau, u_wat, u_str, u_pool = (new_uuid() for _ in range(6))
    groups = [
        group(sid, [0, 0, 0], u_root),
        group("cabinet", [0, 0, 0], u_cab),
        group("faucet", [0, 0, 0], u_fau),
        group("water", [bx, 9, bz], u_wat),
        group("water_stream", [bx, 8.6, bz - 0.5], u_str),
        group("basin_pool", [bx, 8.7, bz], u_pool),
    ]
    outliner = [{
        "uuid": u_root, "name": sid, "isOpen": True,
        "children": [
            {"uuid": u_cab, "name": "cabinet", "isOpen": True, "children": b.children["cabinet"]},
            {"uuid": u_fau, "name": "faucet", "isOpen": True, "children": b.children["faucet"]},
            {"uuid": u_wat, "name": "water", "isOpen": True, "children": [
                {"uuid": u_str, "name": "water_stream", "isOpen": True, "children": b.children["water_stream"]},
                {"uuid": u_pool, "name": "basin_pool", "isOpen": True, "children": b.children["basin_pool"]},
            ]},
        ],
    }]
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
        "elements": b.elements, "groups": groups, "outliner": outliner,
        "textures": [texture], "animations": [],
    }
    bb_path = os.path.join(HERE, sid + ".bbmodel")
    with open(bb_path, "w", encoding="utf-8") as fh:
        json.dump(bb, fh, ensure_ascii=False, separators=(",", ":"))
    print("wrote", bb_path)


def main():
    for sid, spec in SHAPES.items():
        atlas_rel, atlas_source = build_atlas(sid, THEMES[sid])
        build_sink(sid, spec, atlas_rel, atlas_source)


if __name__ == "__main__":
    main()
