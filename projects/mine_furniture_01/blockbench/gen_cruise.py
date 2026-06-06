"""Driveable unicorn cruise boat (mine_structure:unicorn_cruise).

Like the car, but on water: minecraft:buoyant floats it, behavior.controlled_by_player
+ movement let the driver steer it across water (amphibious so it also moves on land).
minecraft:rideable with 4 seats (controlling_seat 0 = driver + 3 passengers). A small
rainbow flag waves (scripts.animate). Bow = -Z.

NOTE: player-driven water vehicles are version-sensitive; verify in-game (steering,
buoyancy, seat positions).
"""
import json
import os

from gen_kids_furniture import Builder, assemble, make_atlas
from gen_room_furniture import RP, BP, render_controller, resources, write

SID = "unicorn_cruise"


def build_model():
    specs = [("hull", (248, 244, 250), "solid"), ("deck", (224, 206, 236), "solid"),
             ("accent", (244, 150, 196), "solid"), ("window", (70, 92, 130), "solid"),
             ("gold", (245, 210, 120), "solid"), ("rainbow", None, "horn")]
    rel, src, cm = make_atlas(SID, specs, 6901)
    b = Builder(cm)
    # hull (tapered bow toward -Z)
    b.add("ship", "hull", [-8, 0, -15], [16, 5, 30], "hull")
    b.add("ship", "bow1", [-6, 0, -18], [12, 5, 3], "hull")
    b.add("ship", "bow2", [-4, 0, -21], [8, 5, 3], "hull")
    b.add("ship", "bowtip", [-2, 0, -23], [4, 5, 2], "hull")
    b.add("ship", "stripe", [-8.2, 2, -18], [16.4, 1, 33], "accent")
    # deck + low rails
    b.add("ship", "deck", [-7, 5, -16], [14, 1, 33], "deck")
    b.add("ship", "rail_l", [-7.2, 6, -16], [0.6, 1, 33], "gold")
    b.add("ship", "rail_r", [6.6, 6, -16], [0.6, 1, 33], "gold")
    b.add("ship", "rail_b", [-7, 6, 16.4], [14, 1, 0.6], "gold")
    # superstructure / cabins
    b.add("ship", "cabin", [-5, 6, -4], [10, 6, 14], "hull")
    b.add("ship", "cabin_win", [-5.2, 8, -4.1], [10.4, 2, 0.2], "window")
    b.add("ship", "bridge", [-4, 12, 0], [8, 4, 9], "hull")
    b.add("ship", "bridge_win", [-4.2, 13, -0.1], [8.4, 2, 0.2], "window")
    # funnels
    b.add("ship", "stack1", [-2.5, 16, 2], [2.6, 5, 2.6], "accent")
    b.add("ship", "stack1_top", [-2.6, 20.5, 1.9], [2.8, 0.8, 2.8], "gold")
    b.add("ship", "stack2", [-2.5, 16, 6], [2.6, 5, 2.6], "accent")
    b.add("ship", "stack2_top", [-2.6, 20.5, 5.9], [2.8, 0.8, 2.8], "gold")
    # portholes (cute accents on the hull)
    for i, pz in enumerate((-10, -4, 2, 8)):
        b.add("ship", "port_l%d" % i, [-8.1, 2.5, pz], [0.2, 1.2, 1.2], "window")
        b.add("ship", "port_r%d" % i, [7.9, 2.5, pz], [0.2, 1.2, 1.2], "window")
    # passenger cushions on the open rear deck
    for i, (cx, cz) in enumerate([(-3, 11), (3, 11), (0, 13.5)]):
        b.add("ship", "seat%d" % i, [cx - 1.5, 6, cz - 1.5], [3, 1, 3], "accent")
    # flag pole at the bow + waving rainbow flag (bone "flag")
    b.add("ship", "flagpole", [-0.4, 5, -22], [0.8, 9, 0.8], "gold")
    b.add("flag", "flag", [0.4, 11, -22], [0.3, 2.6, 4.5], "rainbow")

    bone_defs = [
        {"name": SID, "parent": None, "pivot": [0, 0, 0]},
        {"name": "ship", "parent": SID, "pivot": [0, 0, 0]},
        {"name": "flag", "parent": "ship", "pivot": [0.5, 13.6, -22]},
    ]
    assemble(SID, b, bone_defs, rel, src)


def wiring():
    write(os.path.join(BP, "entities", SID + ".entity.json"), {
        "format_version": "1.20.0",
        "minecraft:entity": {
            "description": {"identifier": "mine_structure:" + SID, "is_spawnable": True,
                            "is_summonable": True, "is_experimental": False},
            "components": {
                "minecraft:type_family": {"family": ["mine_structure_vehicle", SID]},
                "minecraft:collision_box": {"width": 1.8, "height": 1.4},
                "minecraft:health": {"value": 50, "max": 50},
                "minecraft:physics": {"has_gravity": True, "has_collision": True},
                "minecraft:buoyant": {
                    "base_buoyancy": 1.0, "big_wave_probability": 0.0,
                    "drag_down_on_buoyancy_removed": 0.0, "simulate_waves": True,
                    "liquid_blocks": ["minecraft:water", "minecraft:flowing_water"],
                },
                "minecraft:movement": {"value": 0.3},
                "minecraft:navigation.generic": {"is_amphibious": True, "can_path_over_water": True,
                                                 "can_swim": True, "can_walk": True, "avoid_water": False},
                "minecraft:movement.amphibious": {},
                "minecraft:jump.static": {},
                "minecraft:behavior.controlled_by_player": {"priority": 0},
                "minecraft:rideable": {
                    "seat_count": 4, "family_types": ["player"], "controlling_seat": 0,
                    "pull_in_entities": False, "interact_text": "action.interact.ride",
                    "seats": [
                        {"position": [0, 1.4, -0.3], "lock_rider_rotation": 0},
                        {"position": [-0.5, 0.7, 0.6], "lock_rider_rotation": 0},
                        {"position": [0.5, 0.7, 0.6], "lock_rider_rotation": 0},
                        {"position": [0, 0.7, 0.9], "lock_rider_rotation": 0},
                    ],
                },
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
            "animations": {"wave": "animation." + SID + ".wave"},
            "scripts": {"animate": ["wave"]},
            "render_controllers": ["controller.render." + SID],
        }},
    })
    write(os.path.join(RP, "render_controllers", SID + ".render_controllers.json"), render_controller(SID))
    write(os.path.join(RP, "animations", SID + ".animation.json"), {
        "format_version": "1.8.0",
        "animations": {"animation." + SID + ".wave": {
            "loop": True, "animation_length": 1.6,
            "bones": {"flag": {"rotation": {"0.0": [0, 0, 0], "0.4": [0, 10, 0], "0.8": [0, 0, 0],
                                            "1.2": [0, -10, 0], "1.6": [0, 0, 0]}}}}},
    })
    write(os.path.normpath(os.path.join(BP, "..", "..", "content", "furniture", SID + ".resources.json")),
          resources(SID, "boat", False))


def main():
    build_model()
    wiring()


if __name__ == "__main__":
    main()
