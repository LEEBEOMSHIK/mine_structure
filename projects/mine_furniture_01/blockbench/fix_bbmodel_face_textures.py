"""Repair per-face texture bindings in blockbench/furniture.bbmodel.

Why this exists:
  The Blockbench (MCP) project-codec in this environment flattens every cube
  face's texture binding to the *currently selected* texture on save. So after
  any save, the file ends up with every model wearing one texture, which makes
  the editor preview look wrong when the file is re-opened (e.g. the dining
  table wearing the toilet atlas).

  The in-game resources are NOT affected by this (each entity ships its own
  atlas and its own hand-authored .geo.json); this only restores the .bbmodel
  preview bindings so the source-of-truth file opens looking correct, with each
  model showing its own atlas.

Run this after every Blockbench save of furniture.bbmodel:
  python blockbench/fix_bbmodel_face_textures.py

It is idempotent (safe to run repeatedly).
"""
import json
import os

HERE = os.path.dirname(__file__)
MODEL = os.path.join(HERE, "furniture.bbmodel")

# Root outliner group name -> the texture (by name) that group's cubes should use.
GROUP_TEXTURE = {
    "unicorn_toilet": "unicorn_toilet_atlas.png",
    "unicorn_dining_table": "unicorn_dining_table_atlas.png",
    "unicorn_chair": "unicorn_chair_atlas.png",
    "unicorn_barrel_cabinet": "unicorn_barrel_cabinet_atlas.png",
    "decorative_unicorn_doll": "decorative_unicorn_doll_atlas.png",
    "unicorn_horn_blade": "unicorn_horn_blade.png",
}
FALLBACK_TEXTURE = "unicorn_toilet_atlas.png"

# Some doll cubes (e.g. the forelock) sit loose at the outliner root with no
# parent group, so they can't be mapped by root group. Map them by name.
NAME_TEXTURE = {
    "forelock": "decorative_unicorn_doll_atlas.png",
}


def build_root_map(data):
    """element uuid -> root group name, from the outliner tree."""
    groups = {g["uuid"]: g.get("name") for g in data.get("groups", []) if isinstance(g, dict)}
    root_of = {}

    def walk(node, root_name):
        if isinstance(node, str):
            root_of[node] = root_name
        elif isinstance(node, dict):
            name = root_name or groups.get(node.get("uuid"))
            for child in node.get("children", []):
                walk(child, name)

    for top in data.get("outliner", []):
        top_name = groups.get(top.get("uuid")) if isinstance(top, dict) else None
        walk(top, top_name)
    return root_of


def main():
    with open(MODEL, encoding="utf-8") as file:
        data = json.load(file)

    textures = data.get("textures", [])
    name_to_index = {t.get("name"): i for i, t in enumerate(textures)}

    missing = [tex for tex in set(GROUP_TEXTURE.values()) | {FALLBACK_TEXTURE}
               if tex not in name_to_index]
    if missing:
        raise SystemExit(f"textures not loaded in {MODEL}: {missing}")

    root_of = build_root_map(data)
    fallback_idx = name_to_index[FALLBACK_TEXTURE]

    fixed = 0
    for element in data.get("elements", []):
        root = root_of.get(element.get("uuid"))
        tex_name = GROUP_TEXTURE.get(root)
        if tex_name is None:
            element_name = (element.get("name") or "").lower()
            for needle, name in NAME_TEXTURE.items():
                if needle in element_name:
                    tex_name = name
                    break
        if tex_name is None:
            tex_name = FALLBACK_TEXTURE
        target = name_to_index.get(tex_name, fallback_idx)
        for face in element.get("faces", {}).values():
            if face.get("texture") != target:
                face["texture"] = target
                fixed += 1

    with open(MODEL, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, separators=(",", ":"))

    print(f"fixed {fixed} face texture bindings across "
          f"{len(GROUP_TEXTURE)} models")


if __name__ == "__main__":
    main()
