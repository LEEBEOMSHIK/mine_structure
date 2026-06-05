"""Bathroom + kitchen + robot vacuum.

  unicorn_bathtub        variant toggle: water + bubbles show/hide (glow bone)
  unicorn_oven           variant toggle: inner light glow
  unicorn_microwave      variant toggle: window glow
  unicorn_toaster        Script: gives toast (bread) on interact
  unicorn_robot_vacuum   auto-wandering little robot (new "wander" mechanic)

Reuses gen_kids_furniture (Builder/make_atlas/assemble) and gen_room_furniture
(variant_light_wiring/render_controller/resources/common_components/write).
"""
import os

from gen_kids_furniture import Builder, assemble, make_atlas
from gen_room_furniture import (BP, RP, common_components, render_controller,
                                resources, variant_light_wiring, write)


def static_client(sid):
    write(os.path.join(RP, "entity", sid + ".entity.json"), {
        "format_version": "1.10.0",
        "minecraft:client_entity": {"description": {
            "identifier": "mine_structure:" + sid,
            "materials": {"default": "entity_alphatest"},
            "textures": {"default": "textures/entity/" + sid + "/" + sid + "_atlas"},
            "geometry": {"default": "geometry." + sid},
            "render_controllers": ["controller.render." + sid],
        }},
    })


def build_bathtub():
    sid = "unicorn_bathtub"
    specs = [("shell", (246, 202, 230), "solid"), ("water", (150, 212, 238), "water"),
             ("bubble", (250, 250, 255), "solid"), ("faucet", (206, 204, 226), "solid"),
             ("gold", (245, 210, 120), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6601)
    b = Builder(cm)
    b.add("body", "lower", [-7, 0, -5], [14, 5, 10], "shell")
    b.add("body", "rim_back", [-7, 5, 3], [14, 2, 2], "shell")
    b.add("body", "rim_front", [-7, 5, -5], [14, 2, 2], "shell")
    b.add("body", "rim_left", [-7, 5, -3], [2, 2, 6], "shell")
    b.add("body", "rim_right", [5, 5, -3], [2, 2, 6], "shell")
    b.add("body", "trim", [-7, 6.6, -5], [14, 0.5, 10], "gold")
    b.add("body", "faucet", [-1, 7, 3.4], [2, 3.5, 1.6], "faucet")
    b.add("body", "spout", [-1, 9.5, 0.5], [1.6, 1.2, 3], "faucet")
    # water + bubbles (toggled)
    b.add("glow", "water", [-5, 4.5, -3], [10, 1.4, 6], "water")
    for i, (bx, bz) in enumerate([(-3.5, -1.5), (-0.5, 1), (2.5, -1), (1, -2)]):
        b.add("glow", "bubble%d" % i, [bx, 5.6, bz], [1.2, 1, 1.2], "bubble")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "glow", "parent": sid, "pivot": [0, 5, 0]}], rel, src)
    variant_light_wiring(sid, "action.interact.fill_water", "action.interact.drain_water", 1.1, 0.7)


def build_oven():
    sid = "unicorn_oven"
    specs = [("shell", (216, 200, 240), "solid"), ("bezel", (66, 62, 96), "solid"),
             ("glow", (255, 196, 120), "glow"), ("knob", (245, 210, 120), "solid"),
             ("accent", (244, 160, 200), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6602)
    b = Builder(cm)
    b.add("body", "body", [-5, 0, -5], [10, 12, 9], "shell")
    b.add("body", "window", [-4.5, 2, -5.3], [9, 7, 0.5], "bezel")
    b.add("body", "handle", [-4.5, 9.4, -5.6], [9, 0.6, 0.5], "knob")
    b.add("body", "knob1", [-3, 11.6, -5.3], [1, 0.8, 0.4], "knob")
    b.add("body", "knob2", [2, 11.6, -5.3], [1, 0.8, 0.4], "knob")
    b.add("glow", "inner", [-4, 2.4, -5.5], [8, 6, 0.3], "glow")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "glow", "parent": sid, "pivot": [0, 5, -5]}], rel, src)
    variant_light_wiring(sid, "action.interact.oven_on", "action.interact.oven_off", 0.9, 1.0)


def build_microwave():
    sid = "unicorn_microwave"
    specs = [("shell", (244, 200, 230), "solid"), ("bezel", (66, 62, 96), "solid"),
             ("glow", (255, 236, 160), "glow"), ("button", (140, 200, 245), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6603)
    b = Builder(cm)
    b.add("body", "body", [-5, 0, -4], [10, 6, 8], "shell")
    b.add("body", "window", [-4.5, 1, -4.3], [5.5, 4, 0.4], "bezel")
    for i in range(3):
        b.add("body", "btn%d" % i, [3.4, 1.4 + i * 1.3, -4.3], [1, 0.8, 0.3], "button")
    b.add("glow", "win_glow", [-4.2, 1.3, -4.5], [5.1, 3.4, 0.3], "glow")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "glow", "parent": sid, "pivot": [0, 3, -4]}], rel, src)
    variant_light_wiring(sid, "action.interact.start", "action.interact.stop", 0.8, 0.6)


def build_toaster():
    sid = "unicorn_toaster"
    specs = [("shell", (248, 178, 214), "solid"), ("slot", (58, 54, 88), "solid"),
             ("lever", (245, 210, 120), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6604)
    b = Builder(cm)
    b.add("body", "body", [-3, 0, -3], [6, 4, 6], "shell")
    b.add("body", "slot", [-2, 4, -1.5], [4, 0.6, 3], "slot")
    b.add("body", "lever", [3, 1.5, -0.5], [0.8, 2, 1], "lever")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src)
    # static behavior; scripts/main.js gives toast on interact
    write(os.path.join(BP, "entities", sid + ".entity.json"), {
        "format_version": "1.20.0",
        "minecraft:entity": {
            "description": {"identifier": "mine_structure:" + sid, "is_spawnable": True,
                            "is_summonable": True, "is_experimental": False},
            "components": common_components(sid, 0.5, 0.4),
        },
    })
    static_client(sid)
    write(os.path.join(RP, "render_controllers", sid + ".render_controllers.json"), render_controller(sid))
    write(os.path.normpath(os.path.join(BP, "..", "..", "content", "furniture", sid + ".resources.json")),
          resources(sid, "script_give", False))


def build_robot():
    sid = "unicorn_robot_vacuum"
    specs = [("shell", (220, 210, 240), "solid"), ("face", (224, 236, 250), "face"),
             ("accent", (244, 160, 200), "solid"), ("sensor", (140, 200, 245), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6605)
    b = Builder(cm)
    b.add("body", "disc", [-3, 0, -3], [6, 1.8, 6], "shell")
    b.add("body", "dome", [-2, 1.8, -2], [4, 1, 4], "shell")
    b.add("body", "sensor", [-0.6, 2.8, -1.4], [1.2, 0.8, 1.2], "sensor")
    b.add("body", "bumper", [-3, 0, -3.2], [6, 1, 0.3], "accent")
    b.add("body", "facepanel", [-1.6, 0.5, -3.25], [3.2, 1.1, 0.25], "face", face_cells={"north": "face"})
    write(os.path.join(BP, "entities", sid + ".entity.json"), {
        "format_version": "1.20.0",
        "minecraft:entity": {
            "description": {"identifier": "mine_structure:" + sid, "is_spawnable": True,
                            "is_summonable": True, "is_experimental": False},
            "components": {
                "minecraft:type_family": {"family": ["mine_structure_pet", sid]},
                "minecraft:collision_box": {"width": 0.5, "height": 0.35},
                "minecraft:health": {"value": 10, "max": 10},
                "minecraft:physics": {},
                "minecraft:movement": {"value": 0.16},
                "minecraft:navigation.walk": {"can_path_over_water": False, "avoid_water": True},
                "minecraft:movement.basic": {},
                "minecraft:jump.static": {},
                "minecraft:behavior.float": {"priority": 0},
                "minecraft:behavior.random_stroll": {"priority": 1, "speed_multiplier": 1.0},
                "minecraft:behavior.random_look_around": {"priority": 2},
            },
        },
    })
    static_client(sid)
    write(os.path.join(RP, "render_controllers", sid + ".render_controllers.json"), render_controller(sid))
    write(os.path.normpath(os.path.join(BP, "..", "..", "content", "furniture", sid + ".resources.json")),
          resources(sid, "wander", False))
    # assemble geometry/bbmodel last (writes geo)
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src)


def main():
    build_bathtub()
    build_oven()
    build_microwave()
    build_toaster()
    build_robot()


if __name__ == "__main__":
    main()
