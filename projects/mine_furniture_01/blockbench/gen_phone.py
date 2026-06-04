"""Unicorn phone (mine_structure:unicorn_phone).

A small smartphone standing on a little dock. Right-click toggles the SCREEN
on/off (minecraft:variant + animation controller): on shows a bright cute-face
display ("glow" bone) over the dark bezel; off hides it. Pastel, no horn.

geo/atlas/bbmodel reuse gen_kids_furniture helpers; wiring = variant_light pattern.
"""
import json
import os

from gen_kids_furniture import Builder, assemble, make_atlas

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
BP = os.path.join(BASE, "addon", "behavior_pack")
RP = os.path.join(BASE, "addon", "resource_pack")
CONTENT = os.path.normpath(os.path.join(BASE, "content", "furniture"))
SID = "unicorn_phone"


def write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    print("wrote", path)


def build_model():
    specs = [
        ("case", (244, 184, 216), "solid"),    # pastel pink case
        ("base", (210, 200, 234), "solid"),     # lavender dock
        ("bezel", (70, 66, 104), "solid"),      # dark screen frame
        ("screen", (190, 226, 250), "face"),    # cute-face display
        ("button", (245, 210, 120), "solid"),   # gold home button / camera ring
    ]
    atlas_rel, src, cm = make_atlas(SID, specs, 6403)
    b = Builder(cm)
    # dock + slight kickstand behind the phone (front = -Z)
    b.add("body", "dock", [-2.5, 0, -1.5], [5, 1, 3], "base")
    b.add("body", "kickstand", [-1, 0.6, 0.9], [2, 4.5, 0.8], "base")
    # phone body (upright slab) + dark bezel + camera + home button
    b.add("body", "case", [-3, 1, 0], [6, 11, 1], "case")
    b.add("body", "bezel", [-2.6, 1.8, -0.2], [5.2, 8.8, 0.3], "bezel")
    b.add("body", "camera", [-0.4, 10.6, -0.25], [0.8, 0.8, 0.25], "button")
    b.add("body", "home", [-0.7, 1.35, -0.25], [1.4, 0.5, 0.25], "button")
    # lit display panel in front of the bezel (toggled; cute face)
    b.add("glow", "screen", [-2.3, 2.2, -0.4], [4.6, 8, 0.2], "screen", face_cells={"north": "screen"})

    bone_defs = [
        {"name": SID, "parent": None, "pivot": [0, 0, 0]},
        {"name": "body", "parent": SID, "pivot": [0, 0, 0]},
        {"name": "glow", "parent": SID, "pivot": [0, 6.2, -0.3]},
    ]
    assemble(SID, b, bone_defs, atlas_rel, src)


def interact(text, ev):
    return {"interactions": [{
        "interact_text": text, "swing": True, "play_sounds": "random.click",
        "on_interact": {"event": ev, "target": "self"},
    }]}


def wiring():
    write(os.path.join(BP, "entities", SID + ".entity.json"), {
        "format_version": "1.20.0",
        "minecraft:entity": {
            "description": {"identifier": "mine_structure:" + SID,
                            "is_spawnable": True, "is_summonable": True, "is_experimental": False},
            "component_groups": {
                "mine_structure:light_off": {"minecraft:variant": {"value": 0},
                                             "minecraft:interact": interact("action.interact.screen_on", "mine_structure:turn_light_on")},
                "mine_structure:light_on": {"minecraft:variant": {"value": 1},
                                            "minecraft:interact": interact("action.interact.screen_off", "mine_structure:turn_light_off")},
            },
            "components": {
                "minecraft:type_family": {"family": ["mine_structure_furniture", SID]},
                "minecraft:collision_box": {"width": 0.45, "height": 0.85},
                "minecraft:health": {"value": 12, "max": 12},
                "minecraft:physics": {"has_gravity": False, "has_collision": True},
                "minecraft:pushable": {"is_pushable": False, "is_pushable_by_piston": False},
            },
            "events": {
                "minecraft:entity_spawned": {"add": {"component_groups": ["mine_structure:light_off"]}},
                "mine_structure:turn_light_on": {"remove": {"component_groups": ["mine_structure:light_off"]},
                                                 "add": {"component_groups": ["mine_structure:light_on"]}},
                "mine_structure:turn_light_off": {"remove": {"component_groups": ["mine_structure:light_on"]},
                                                  "add": {"component_groups": ["mine_structure:light_off"]}},
            },
        },
    })
    write(os.path.join(RP, "entity", SID + ".entity.json"), {
        "format_version": "1.10.0",
        "minecraft:client_entity": {"description": {
            "identifier": "mine_structure:" + SID,
            "materials": {"default": "entity_alphatest"},
            "textures": {"default": "textures/entity/" + SID + "/" + SID + "_atlas"},
            "geometry": {"default": "geometry." + SID},
            "animations": {"on": "animation." + SID + ".on", "off": "animation." + SID + ".off",
                           "light_ctrl": "controller.animation." + SID + ".light"},
            "scripts": {"animate": ["light_ctrl"]},
            "render_controllers": ["controller.render." + SID],
        }},
    })
    write(os.path.join(RP, "render_controllers", SID + ".render_controllers.json"), {
        "format_version": "1.8.0",
        "render_controllers": {"controller.render." + SID: {
            "geometry": "Geometry.default", "materials": [{"*": "Material.default"}], "textures": ["Texture.default"]}},
    })
    write(os.path.join(RP, "animations", SID + ".animation.json"), {
        "format_version": "1.8.0",
        "animations": {
            "animation." + SID + ".off": {"loop": "hold_on_last_frame", "animation_length": 0.05,
                                          "bones": {"glow": {"scale": [0, 0, 0]}}},
            "animation." + SID + ".on": {"loop": True, "animation_length": 2.0,
                                         "bones": {"glow": {"scale": {"0.0": [1, 1, 1], "1.0": [1.03, 1.03, 1], "2.0": [1, 1, 1]}}}},
        },
    })
    write(os.path.join(RP, "animation_controllers", SID + ".animation_controllers.json"), {
        "format_version": "1.10.0",
        "animation_controllers": {"controller.animation." + SID + ".light": {
            "initial_state": "off",
            "states": {"off": {"animations": ["off"], "transitions": [{"on": "q.variant == 1"}]},
                       "on": {"animations": ["on"], "transitions": [{"off": "q.variant == 0"}]}}}},
    })
    write(os.path.join(CONTENT, SID + ".resources.json"), {
        "identifier": "mine_structure:" + SID, "content_type": "furniture_entity", "mechanic": "variant_light",
        "behavior_pack": {"entity": "../../addon/behavior_pack/entities/" + SID + ".entity.json"},
        "resource_pack": {
            "client_entity": "../../addon/resource_pack/entity/" + SID + ".entity.json",
            "geometry": "../../addon/resource_pack/models/entity/" + SID + ".geo.json",
            "texture": "../../addon/resource_pack/textures/entity/" + SID + "/" + SID + "_atlas.png",
            "render_controller": "../../addon/resource_pack/render_controllers/" + SID + ".render_controllers.json",
            "animation": "../../addon/resource_pack/animations/" + SID + ".animation.json",
            "animation_controller": "../../addon/resource_pack/animation_controllers/" + SID + ".animation_controllers.json",
        },
        "blockbench_source": "../../blockbench/" + SID + ".bbmodel",
        "status": {"json_links_ready": True, "geometry_exported": True, "texture_exported": True, "in_game_tested": False},
    })


def main():
    build_model()
    wiring()


if __name__ == "__main__":
    main()
