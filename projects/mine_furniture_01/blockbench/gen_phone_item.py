"""Held unicorn phone item (mine_structure:unicorn_phone_item).

A 3D in-hand phone (attachable, like the sword) so it can be carried around. The
placed furniture phone (mine_structure:unicorn_phone) is unchanged. Screen shows a
cute face (always on while held). Hold poses need in-game tuning.

geo/atlas/bbmodel reuse gen_kids_furniture helpers; attachable mirrors the blade.
"""
import json
import os

from PIL import Image

from gen_kids_furniture import Builder, assemble, make_atlas

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
BP_ITEMS = os.path.join(BASE, "addon", "behavior_pack", "items")
RP = os.path.join(BASE, "addon", "resource_pack")
CONTENT_ITEMS = os.path.join(BASE, "content", "items")
SID = "unicorn_phone_item"


def write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    print("wrote", path)


def build_model():
    specs = [
        ("case", (244, 184, 216), "solid"),
        ("bezel", (70, 66, 104), "solid"),
        ("screen", (190, 226, 250), "face"),
        ("button", (245, 210, 120), "solid"),
    ]
    atlas_rel, src, cm = make_atlas(SID, specs, 6404)
    b = Builder(cm)
    # flat phone centred on the origin (hand poses position/scale it)
    b.add(SID, "case", [-2, -4, -0.4], [4, 8, 0.8], "case")
    b.add(SID, "bezel", [-1.7, -3.4, -0.5], [3.4, 6.9, 0.2], "bezel")
    b.add(SID, "screen", [-1.5, -3.2, -0.62], [3.0, 6.5, 0.25], "screen", face_cells={"north": "screen"})
    b.add(SID, "camera", [-0.3, 3.0, -0.5], [0.6, 0.6, 0.2], "button")
    b.add(SID, "home", [-0.5, -3.6, -0.5], [1.0, 0.4, 0.2], "button")
    assemble(SID, b, [{"name": SID, "parent": None, "pivot": [0, 0, 0]}], atlas_rel, src)


def build_icon():
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    case = (244, 184, 216, 255)
    bezel = (70, 66, 104, 255)
    for y in range(2, 15):
        for x in range(5, 11):
            img.putpixel((x, y), case)
    for y in range(4, 12):
        for x in range(6, 10):
            img.putpixel((x, y), bezel)
    # cute face dots on screen
    img.putpixel((7, 6), (255, 255, 255, 255))
    img.putpixel((9, 6), (255, 255, 255, 255))
    img.putpixel((8, 9), (255, 170, 200, 255))
    img.putpixel((7, 13), (245, 210, 120, 255))  # home button
    out = os.path.join(RP, "textures", "items", SID + ".png")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    img.save(out)
    print("wrote", out)


def wiring():
    write(os.path.join(BP_ITEMS, SID + ".item.json"), {
        "format_version": "1.20.10",
        "minecraft:item": {
            "description": {"identifier": "mine_structure:" + SID, "menu_category": {"category": "equipment"}},
            "components": {
                "minecraft:display_name": {"value": "유니콘 핸드폰"},
                "minecraft:icon": {"texture": SID},
                "minecraft:max_stack_size": 1,
                "minecraft:hand_equipped": True,
                "minecraft:cooldown": {"category": "unicorn_phone", "duration": 0.6},
            },
        },
    })
    write(os.path.join(RP, "attachables", SID + ".attachable.json"), {
        "format_version": "1.10.0",
        "minecraft:attachable": {
            "description": {
                "identifier": "mine_structure:" + SID,
                "materials": {"default": "entity_alphatest"},
                "textures": {"default": "textures/entity/" + SID + "/" + SID + "_atlas"},
                "geometry": {"default": "geometry." + SID},
                "scripts": {
                    "pre_animation": [
                        "v.main_hand = c.item_slot == 'main_hand';",
                        "v.off_hand = c.item_slot == 'off_hand';",
                    ],
                    "animate": [
                        {"first_person_main_hand": "v.main_hand && c.is_first_person"},
                        {"third_person_main_hand": "v.main_hand && !c.is_first_person"},
                        {"first_person_off_hand": "v.off_hand && c.is_first_person"},
                        {"third_person_off_hand": "v.off_hand && !c.is_first_person"},
                    ],
                },
                "animations": {
                    "first_person_main_hand": "animation." + SID + ".first_person_main_hand",
                    "third_person_main_hand": "animation." + SID + ".third_person_main_hand",
                    "first_person_off_hand": "animation." + SID + ".first_person_off_hand",
                    "third_person_off_hand": "animation." + SID + ".third_person_off_hand",
                },
                "render_controllers": ["controller.render.item_default"],
            }
        },
    })

    def pose(rot, pos, scale):
        return {"loop": True, "bones": {SID: {"rotation": rot, "position": pos, "scale": scale}}}

    write(os.path.join(RP, "animations", SID + ".animation.json"), {
        "format_version": "1.8.0",
        "animations": {
            "animation." + SID + ".third_person_main_hand": pose([0, 0, 0], [0, 3, 1], 0.6),
            "animation." + SID + ".third_person_off_hand": pose([0, 0, 0], [0, 3, 1], 0.6),
            "animation." + SID + ".first_person_main_hand": pose([10, -18, 0], [4, 4, 2], 0.75),
            "animation." + SID + ".first_person_off_hand": pose([10, 18, 0], [-4, 4, 2], 0.75),
        },
    })

    write(os.path.join(CONTENT_ITEMS, SID + ".resources.json"), {
        "identifier": "mine_structure:" + SID, "content_type": "held_item",
        "behavior_pack": {"item": "../../addon/behavior_pack/items/" + SID + ".item.json"},
        "resource_pack": {
            "attachable": "../../addon/resource_pack/attachables/" + SID + ".attachable.json",
            "geometry": "../../addon/resource_pack/models/entity/" + SID + ".geo.json",
            "animation": "../../addon/resource_pack/animations/" + SID + ".animation.json",
            "icon": "../../addon/resource_pack/textures/items/" + SID + ".png",
            "texture": "../../addon/resource_pack/textures/entity/" + SID + "/" + SID + "_atlas.png",
        },
        "blockbench_source": "../../blockbench/" + SID + ".bbmodel",
        "status": {"json_links_ready": True, "geometry_exported": True, "texture_exported": True,
                   "in_hand_pose_tuned": False, "in_game_tested": False},
    })


def main():
    build_model()
    build_icon()
    wiring()


if __name__ == "__main__":
    main()
