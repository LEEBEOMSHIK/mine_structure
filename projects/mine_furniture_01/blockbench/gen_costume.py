"""Generate the wearable unicorn costume: horn headband (head slot) and wings
(chest slot). Each is a wearable item + an attachable whose geometry binds to a
player bone ("head" / "body") so it renders on the player.

Outputs: item icons, entity atlases, geo.json, item.json, attachable.json.

NOTE: custom player-attached cosmetics are the most version-sensitive part of the
add-on and must be verified in-game.
"""
import json
import os

from PIL import Image

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
RP = os.path.join(BASE, "addon", "resource_pack")
BP_ITEMS = os.path.join(BASE, "addon", "behavior_pack", "items")

DIRS = ("north", "east", "south", "west", "up", "down")
RAINBOW = [
    (255, 150, 176, 255), (255, 190, 120, 255), (255, 232, 138, 255),
    (150, 224, 176, 255), (140, 198, 246, 255), (196, 158, 240, 255), (246, 160, 220, 255),
]


def write_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent="\t")
    print("wrote", path)


def faces(px, py):
    return {f: {"uv": [px, py], "uv_size": [16, 16]} for f in DIRS}


def cube(origin, size, cell):
    return {"origin": [round(v, 3) for v in origin], "size": [round(v, 3) for v in size], "uv": faces(*cell)}


def fill_cell(img, px, py, base):
    light = tuple(min(255, c + 16) for c in base[:3]) + (255,)
    dark = tuple(max(0, c - 20) for c in base[:3]) + (255,)
    for y in range(16):
        col = light if y <= 2 else dark if y >= 13 else base
        for x in range(16):
            img.putpixel((px + x, py + y), col)


def fill_horn(img, px, py):
    for y in range(16):
        for x in range(16):
            img.putpixel((px + x, py + y), RAINBOW[((x + y) // 3) % len(RAINBOW)])



def save_png(path, img):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path)
    print("wrote", path)


def item_json(sid, name, slot):
    return {
        "format_version": "1.20.10",
        "minecraft:item": {
            "description": {"identifier": "mine_structure:" + sid, "menu_category": {"category": "equipment"}},
            "components": {
                "minecraft:display_name": {"value": name},
                "minecraft:icon": {"texture": sid},
                "minecraft:max_stack_size": 1,
                "minecraft:wearable": {"slot": slot, "protection": 0},
            },
        },
    }


def attachable_json(sid):
    return {
        "format_version": "1.10.0",
        "minecraft:attachable": {
            "description": {
                "identifier": "mine_structure:" + sid,
                "materials": {"default": "entity_alphatest"},
                "textures": {"default": "textures/entity/" + sid + "/" + sid},
                "geometry": {"default": "geometry." + sid},
                "render_controllers": ["controller.render.armor"],
            }
        },
    }


def geo_json(sid, bone_name, pivot, cubes):
    return {
        "format_version": "1.12.0",
        "minecraft:geometry": [{
            "description": {
                "identifier": "geometry." + sid,
                "texture_width": 64, "texture_height": 64,
                "visible_bounds_width": 3, "visible_bounds_height": 4,
                "visible_bounds_offset": [0, 1.5, 0],
            },
            "bones": [{"name": bone_name, "pivot": pivot, "cubes": cubes}],
        }],
    }


def build_headband():
    sid = "unicorn_horn_headband"
    # entity atlas: band(0,0) gold, horn(16,0) rainbow, ear(32,0) white
    atlas = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    fill_cell(atlas, 0, 0, (245, 210, 120, 255))
    fill_horn(atlas, 16, 0)
    fill_cell(atlas, 32, 0, (250, 250, 255, 255))
    save_png(os.path.join(RP, "textures", "entity", sid, sid + ".png"), atlas)
    # icon
    icon = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    for x in range(3, 13):
        icon.putpixel((x, 11), (245, 210, 120, 255))
        icon.putpixel((x, 12), (210, 174, 90, 255))
    for i, (x, y) in enumerate([(8, 9), (8, 7), (8, 5), (8, 3)]):
        icon.putpixel((x, y), RAINBOW[i % len(RAINBOW)])
    icon.putpixel((5, 10), (250, 250, 255, 255))
    icon.putpixel((11, 10), (250, 250, 255, 255))
    save_png(os.path.join(RP, "textures", "items", sid + ".png"), icon)
    # geometry on the player's "head" bone (head cube spans y24..32)
    cubes = [
        cube([-4.5, 25.5, -4.5], [9, 2, 9], (0, 0)),       # band
        cube([-1, 32, -1], [2, 2.4, 2], (16, 0)),          # horn seg 1
        cube([-0.7, 34.2, -0.7], [1.4, 2, 1.4], (16, 0)),  # horn seg 2
        cube([-0.45, 35.8, -0.45], [0.9, 1.6, 0.9], (16, 0)),  # horn tip
        cube([-4.2, 31.5, -1.2], [1.4, 1.8, 1.4], (32, 0)),  # ear L
        cube([2.8, 31.5, -1.2], [1.4, 1.8, 1.4], (32, 0)),   # ear R
    ]
    write_json(os.path.join(RP, "models", "entity", sid + ".geo.json"),
               geo_json(sid, "head", [0, 24, 0], cubes))
    write_json(os.path.join(BP_ITEMS, sid + ".item.json"),
               item_json(sid, "유니콘 뿔 머리띠", "slot.armor.head"))
    write_json(os.path.join(RP, "attachables", sid + ".attachable.json"), attachable_json(sid))


def main():
    build_headband()


if __name__ == "__main__":
    main()
