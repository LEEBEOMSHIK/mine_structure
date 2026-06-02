"""Split unicorn_horn_blade into its own Blockbench project.

The shared furniture.bbmodel is useful for placing related furniture together,
but weapon texture editing should be isolated. This script moves the
unicorn_horn_blade root group, its cubes, and its texture into
unicorn_horn_blade.bbmodel, then removes that root from furniture.bbmodel.
"""
import json
import os
import copy


HERE = os.path.dirname(__file__)
FURNITURE_MODEL = os.path.join(HERE, "furniture.bbmodel")
WEAPON_MODEL = os.path.join(HERE, "unicorn_horn_blade.bbmodel")
WEAPON_ROOT = "unicorn_horn_blade"
WEAPON_TEXTURE = "unicorn_horn_blade.png"
WEAPON_SOURCE_OFFSET = [120, 0, 0]


def collect_tree(node, group_ids, element_ids):
    if isinstance(node, str):
        element_ids.add(node)
        return
    if isinstance(node, dict):
        uuid = node.get("uuid")
        if uuid:
            group_ids.add(uuid)
        for child in node.get("children", []):
            collect_tree(child, group_ids, element_ids)


def remap_face_textures(elements, old_texture_index, new_texture_index):
    for element in elements:
        for face in element.get("faces", {}).values():
            if face.get("texture") == old_texture_index:
                face["texture"] = new_texture_index


def shift_xyz(value, offset):
    if not isinstance(value, list) or len(value) < 3:
        return
    for index, delta in enumerate(offset):
        if isinstance(value[index], (int, float)):
            value[index] -= delta


def recenter_weapon_source(elements, groups, root_node):
    for element in elements:
        for key in ("from", "to", "origin", "pivot"):
            shift_xyz(element.get(key), WEAPON_SOURCE_OFFSET)
    for group in groups:
        for key in ("origin", "pivot"):
            shift_xyz(group.get(key), WEAPON_SOURCE_OFFSET)
    if isinstance(root_node, dict):
        for key in ("origin", "pivot"):
            shift_xyz(root_node.get(key), WEAPON_SOURCE_OFFSET)


def remove_root_project_content(data, root_node, group_ids, element_ids, texture_index):
    data["outliner"] = [
        item for item in data.get("outliner", [])
        if not (isinstance(item, dict) and item.get("uuid") == root_node.get("uuid"))
    ]
    data["groups"] = [
        group for group in data.get("groups", [])
        if not (isinstance(group, dict) and group.get("uuid") in group_ids)
    ]
    data["elements"] = [
        element for element in data.get("elements", [])
        if not (isinstance(element, dict) and element.get("uuid") in element_ids)
    ]
    data["textures"] = [
        texture for index, texture in enumerate(data.get("textures", []))
        if index != texture_index
    ]


def main():
    with open(FURNITURE_MODEL, encoding="utf-8") as file:
        furniture = json.load(file)

    groups_by_uuid = {
        group.get("uuid"): group
        for group in furniture.get("groups", [])
        if isinstance(group, dict)
    }

    weapon_root_node = None
    for item in furniture.get("outliner", []):
        if not isinstance(item, dict):
            continue
        group = groups_by_uuid.get(item.get("uuid"))
        if group and group.get("name") == WEAPON_ROOT:
            weapon_root_node = item
            break
    if weapon_root_node is None:
        raise SystemExit(f"{WEAPON_ROOT} root group not found in {FURNITURE_MODEL}")

    group_ids = set()
    element_ids = set()
    collect_tree(weapon_root_node, group_ids, element_ids)

    weapon_elements = copy.deepcopy([
        element for element in furniture.get("elements", [])
        if isinstance(element, dict) and element.get("uuid") in element_ids
    ])
    weapon_groups = copy.deepcopy([
        group for group in furniture.get("groups", [])
        if isinstance(group, dict) and group.get("uuid") in group_ids
    ])

    textures = furniture.get("textures", [])
    texture_index = next(
        (index for index, texture in enumerate(textures) if texture.get("name") == WEAPON_TEXTURE),
        None,
    )
    if texture_index is None:
        raise SystemExit(f"{WEAPON_TEXTURE} texture not found in {FURNITURE_MODEL}")
    weapon_texture = copy.deepcopy(textures[texture_index])
    weapon_root_node = copy.deepcopy(weapon_root_node)

    remap_face_textures(weapon_elements, texture_index, 0)
    recenter_weapon_source(weapon_elements, weapon_groups, weapon_root_node)

    weapon_project = {
        "meta": furniture.get("meta", {}),
        "name": WEAPON_ROOT,
        "model_identifier": "",
        "visible_box": [2.5, 11, 1.5],
        "variable_placeholders": "",
        "multi_file_ruleset": "",
        "variable_placeholder_buttons": [],
        "bedrock_animation_mode": "entity",
        "timeline_setups": [],
        "unhandled_root_fields": {},
        "resolution": {"width": 64, "height": 64},
        "elements": weapon_elements,
        "groups": weapon_groups,
        "outliner": [weapon_root_node],
        "textures": [weapon_texture],
        "animations": [],
    }

    remove_root_project_content(furniture, weapon_root_node, group_ids, element_ids, texture_index)
    furniture["name"] = "furniture"

    with open(FURNITURE_MODEL, "w", encoding="utf-8") as file:
        json.dump(furniture, file, ensure_ascii=False, separators=(",", ":"))
    with open(WEAPON_MODEL, "w", encoding="utf-8") as file:
        json.dump(weapon_project, file, ensure_ascii=False, separators=(",", ":"))

    print(f"wrote {WEAPON_MODEL}")
    print(f"removed {WEAPON_ROOT} from {FURNITURE_MODEL}")


if __name__ == "__main__":
    main()
