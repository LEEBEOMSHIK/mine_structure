"""Emit the unicorn food/treat item JSONs, the magic wand item, and refresh
item_texture.json with every custom item icon.
"""
import json
import os

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
BP_ITEMS = os.path.join(BASE, "addon", "behavior_pack", "items")
RP = os.path.join(BASE, "addon", "resource_pack")


def write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    print("wrote", path)


def food_item(sid, name, nutrition, saturation, use_anim, can_always_eat):
    return {
        "format_version": "1.20.10",
        "minecraft:item": {
            "description": {"identifier": "mine_structure:" + sid, "menu_category": {"category": "nature"}},
            "components": {
                "minecraft:display_name": {"value": name},
                "minecraft:icon": {"texture": sid},
                "minecraft:max_stack_size": 64,
                "minecraft:use_animation": use_anim,
                "minecraft:use_modifiers": {"use_duration": 1.6, "movement_modifier": 0.35},
                "minecraft:food": {
                    "nutrition": nutrition,
                    "saturation_modifier": saturation,
                    "can_always_eat": can_always_eat,
                },
            },
        },
    }


FOODS = [
    ("unicorn_cupcake", "유니콘 컵케이크", 5, "good", "eat", False),
    ("unicorn_lollipop", "유니콘 막대사탕", 3, "normal", "eat", True),
    ("unicorn_rainbow_drink", "무지개 음료", 3, "normal", "drink", True),
    ("unicorn_star_candy", "별사탕", 2, "low", "eat", True),
]

ICONS = ["unicorn_horn_blade", "unicorn_cookie", "unicorn_cupcake", "unicorn_lollipop",
         "unicorn_rainbow_drink", "unicorn_star_candy", "unicorn_wand",
         "unicorn_horn_headband", "unicorn_elytra", "unicorn_phone_item",
         "unicorn_transform_wand"]


def main():
    for sid, name, nutrition, sat, anim, always in FOODS:
        write(os.path.join(BP_ITEMS, sid + ".item.json"),
              food_item(sid, name, nutrition, sat, anim, always))

    # magic wand (not a food): right-click triggers a script effect, with a cooldown
    write(os.path.join(BP_ITEMS, "unicorn_wand.item.json"), {
        "format_version": "1.20.10",
        "minecraft:item": {
            "description": {"identifier": "mine_structure:unicorn_wand", "menu_category": {"category": "equipment"}},
            "components": {
                "minecraft:display_name": {"value": "유니콘 마법 지팡이"},
                "minecraft:icon": {"texture": "unicorn_wand"},
                "minecraft:max_stack_size": 1,
                "minecraft:hand_equipped": True,
                "minecraft:cooldown": {"category": "unicorn_wand", "duration": 2.0},
            },
        },
    })

    # transform wand (not a food): right-click an animal to morph it (scripts/main.js)
    write(os.path.join(BP_ITEMS, "unicorn_transform_wand.item.json"), {
        "format_version": "1.20.10",
        "minecraft:item": {
            "description": {"identifier": "mine_structure:unicorn_transform_wand", "menu_category": {"category": "equipment"}},
            "components": {
                "minecraft:display_name": {"value": "변신 마법봉"},
                "minecraft:icon": {"texture": "unicorn_transform_wand"},
                "minecraft:max_stack_size": 1,
                "minecraft:hand_equipped": True,
                "minecraft:cooldown": {"category": "unicorn_transform_wand", "duration": 1.0},
            },
        },
    })

    write(os.path.join(RP, "textures", "item_texture.json"), {
        "resource_pack_name": "mine_structure",
        "texture_name": "atlas.items",
        "texture_data": {sid: {"textures": "textures/items/" + sid} for sid in ICONS},
    })


if __name__ == "__main__":
    main()
