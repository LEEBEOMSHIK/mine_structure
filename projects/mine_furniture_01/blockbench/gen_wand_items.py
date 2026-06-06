"""3D held wand items (mine_structure:unicorn_wand, unicorn_transform_wand).

Turns the two flat-icon wands into 3D in-hand sticks (attachables, like the
phone item / sword): a slim pastel handle, a grip band, and a star head made of
two overlapped cubes (one rotated 45 deg) so it reads as a star from every side.

The inventory icon (2D png) and item.json/script behaviour are unchanged — this
only adds the attachable + geometry + animation + bbmodel + resources.json so the
item shows as a 3D wand while held. Hold poses need in-game tuning.
"""
import json
import os

from gen_kids_furniture import Builder, assemble, make_atlas

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
RP = os.path.join(BASE, "addon", "resource_pack")
CONTENT_ITEMS = os.path.join(BASE, "content", "items")

# sid -> (display_name, handle_rgb, grip_rgb, star_a_rgb, star_b_rgb, core_rgb, seed)
WANDS = {
    "unicorn_wand": {
        "handle": (200, 180, 235),
        "grip": (244, 184, 216),
        "star_a": (245, 210, 120),   # gold star
        "star_b": (252, 226, 160),   # lighter gold for the rotated layer
        "core": (120, 215, 230),     # cyan gem
        "seed": 7711,
    },
    "unicorn_transform_wand": {
        "handle": (150, 110, 200),   # purple handle (matches icon)
        "grip": (200, 160, 240),
        "star_a": (250, 150, 200),   # pink star
        "star_b": (150, 200, 245),   # sky-blue rotated layer -> rainbow feel
        "core": (200, 130, 240),     # amethyst gem
        "seed": 7722,
    },
}


def write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    print("wrote", path)


def build_model(sid, cfg):
    specs = [
        ("handle", cfg["handle"], "solid"),
        ("grip", cfg["grip"], "solid"),
        ("star_a", cfg["star_a"], "solid"),
        ("star_b", cfg["star_b"], "solid"),
        ("core", cfg["core"], "glow"),
    ]
    atlas_rel, src, cm = make_atlas(sid, specs, cfg["seed"])
    b = Builder(cm)
    # slim handle centred on the origin, running up the +y axis
    b.add(sid, "handle", [-0.6, -7.0, -0.6], [1.2, 11.0, 1.2], "handle")
    # two grip bands near the bottom where the hand wraps
    b.add(sid, "grip_a", [-0.75, -5.2, -0.75], [1.5, 1.0, 1.5], "grip")
    b.add(sid, "grip_b", [-0.75, -3.4, -0.75], [1.5, 1.0, 1.5], "grip")
    # star head at the top: two overlapped square cubes, one rotated 45 deg
    b.add(sid, "star_a", [-1.6, 4.0, -0.4], [3.2, 3.2, 0.8], "star_a",
          rotation=[0, 0, 0], pivot=[0, 5.6, 0])
    b.add(sid, "star_b", [-1.6, 4.0, -0.35], [3.2, 3.2, 0.7], "star_b",
          rotation=[0, 0, 45], pivot=[0, 5.6, 0])
    # small glowing gem set on the front of the star (45 deg -> diamond
    # silhouette, raised forward so it reads as a jewel rather than a flat patch)
    b.add(sid, "core", [-0.65, 4.95, -0.95], [1.3, 1.3, 1.0], "core",
          rotation=[0, 0, 45], pivot=[0, 5.6, -0.45])
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]}], atlas_rel, src)


def wiring(sid):
    write(os.path.join(RP, "attachables", sid + ".attachable.json"), {
        "format_version": "1.10.0",
        "minecraft:attachable": {
            "description": {
                "identifier": "mine_structure:" + sid,
                "materials": {"default": "entity_alphatest"},
                "textures": {"default": "textures/entity/" + sid + "/" + sid + "_atlas"},
                "geometry": {"default": "geometry." + sid},
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
                    "first_person_main_hand": "animation." + sid + ".first_person_main_hand",
                    "third_person_main_hand": "animation." + sid + ".third_person_main_hand",
                    "first_person_off_hand": "animation." + sid + ".first_person_off_hand",
                    "third_person_off_hand": "animation." + sid + ".first_person_off_hand",
                },
                "render_controllers": ["controller.render.item_default"],
            }
        },
    })

    def pose(rot, pos, scale):
        return {"loop": True, "bones": {sid: {"rotation": rot, "position": pos, "scale": scale}}}

    write(os.path.join(RP, "animations", sid + ".animation.json"), {
        "format_version": "1.8.0",
        "animations": {
            # held upright like a wand, head pointing up-forward
            "animation." + sid + ".third_person_main_hand": pose([-55, 0, 0], [0, 4.5, 1.5], 0.85),
            "animation." + sid + ".third_person_off_hand": pose([-55, 0, 0], [0, 4.5, 1.5], 0.85),
            "animation." + sid + ".first_person_main_hand": pose([-35, -10, 0], [3, 5, 3], 0.9),
            "animation." + sid + ".first_person_off_hand": pose([-35, 10, 0], [-3, 5, 3], 0.9),
        },
    })


def resources(sid, display):
    write(os.path.join(CONTENT_ITEMS, sid + ".resources.json"), {
        "identifier": "mine_structure:" + sid, "content_type": "held_item",
        "display_name": display,
        "behavior_pack": {"item": "../../addon/behavior_pack/items/" + sid + ".item.json"},
        "resource_pack": {
            "attachable": "../../addon/resource_pack/attachables/" + sid + ".attachable.json",
            "geometry": "../../addon/resource_pack/models/entity/" + sid + ".geo.json",
            "animation": "../../addon/resource_pack/animations/" + sid + ".animation.json",
            "icon": "../../addon/resource_pack/textures/items/" + sid + ".png",
            "texture": "../../addon/resource_pack/textures/entity/" + sid + "/" + sid + "_atlas.png",
        },
        "blockbench_source": "../../blockbench/" + sid + ".bbmodel",
        "status": {"json_links_ready": True, "geometry_exported": True, "texture_exported": True,
                   "in_hand_pose_tuned": False, "in_game_tested": False},
    })


DISPLAY = {"unicorn_wand": "유니콘 마법 지팡이", "unicorn_transform_wand": "변신 마법봉"}


def main():
    for sid, cfg in WANDS.items():
        build_model(sid, cfg)
        wiring(sid)
        resources(sid, DISPLAY[sid])


if __name__ == "__main__":
    main()
