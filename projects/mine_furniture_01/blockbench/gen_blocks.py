"""Emit the unicorn building block definitions + terrain_texture mapping.

Modern data-driven blocks: the block's minecraft:material_instances points at a
terrain_texture.json shortname, so no legacy blocks.json is needed.
"""
import json
import os

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
BP_BLOCKS = os.path.join(BASE, "addon", "behavior_pack", "blocks")
RP = os.path.join(BASE, "addon", "resource_pack")

# id -> (display name, texture shortname, map color)
BLOCKS = {
    "unicorn_cloud_block": ("구름 블록", "unicorn_cloud", "#EAF2FF"),
    "unicorn_candy_block": ("사탕 블록", "unicorn_candy", "#F69AC4"),
    "unicorn_star_block": ("별 블록", "unicorn_star", "#4E4480"),
}


def write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    print("wrote", path)


def block_json(sid, name, texture, map_color):
    return {
        "format_version": "1.20.10",
        "minecraft:block": {
            "description": {
                "identifier": "mine_structure:" + sid,
                "menu_category": {"category": "construction"},
            },
            "components": {
                "minecraft:display_name": name,
                "minecraft:destructible_by_mining": {"seconds_to_destroy": 0.5},
                "minecraft:destructible_by_explosion": {"explosion_resistance": 1.0},
                "minecraft:material_instances": {
                    "*": {"texture": texture, "render_method": "opaque"}
                },
                "minecraft:map_color": map_color,
                "minecraft:friction": 0.6,
            },
        },
    }


def main():
    for sid, (name, texture, color) in BLOCKS.items():
        write(os.path.join(BP_BLOCKS, sid + ".block.json"), block_json(sid, name, texture, color))

    write(os.path.join(RP, "textures", "terrain_texture.json"), {
        "resource_pack_name": "mine_structure",
        "texture_name": "atlas.terrain",
        "padding": 8,
        "num_mip_levels": 4,
        "texture_data": {
            texture: {"textures": "textures/blocks/" + texture}
            for (_n, texture, _c) in BLOCKS.values()
        },
    })


if __name__ == "__main__":
    main()
