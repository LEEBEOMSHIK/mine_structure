"""Bathroom + kitchen + robot vacuum (detailed).

  unicorn_bathtub        toggle: water FILLS up (glow bone scales from the floor) + bubbles
  unicorn_oven           toggle: inner light; control panel with dials/buttons
  unicorn_microwave      toggle: window light; door + panel with display/buttons/dial
  unicorn_toaster        Script gives toast; popped toast slices + dial + lever + face
  unicorn_robot_vacuum   auto-wandering robot; brush, sensors, antenna, buttons, face
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


def interact(text, ev):
    return {"interactions": [{"interact_text": text, "swing": True, "play_sounds": "random.splash",
                              "on_interact": {"event": ev, "target": "self"}}]}


def variant_fill_wiring(sid, on_text, off_text, width, height):
    """Like variant_light, but ON animates the glow bone filling up (y 0->1 from the
    floor pivot) instead of just appearing; OFF leaves it empty (y 0)."""
    write(os.path.join(BP, "entities", sid + ".entity.json"), {
        "format_version": "1.20.0",
        "minecraft:entity": {
            "description": {"identifier": "mine_structure:" + sid, "is_spawnable": True,
                            "is_summonable": True, "is_experimental": False},
            "component_groups": {
                "mine_structure:light_off": {"minecraft:variant": {"value": 0},
                                             "minecraft:interact": interact(on_text, "mine_structure:turn_light_on")},
                "mine_structure:light_on": {"minecraft:variant": {"value": 1},
                                            "minecraft:interact": interact(off_text, "mine_structure:turn_light_off")},
            },
            "components": common_components(sid, width, height),
            "events": {
                "minecraft:entity_spawned": {"add": {"component_groups": ["mine_structure:light_off"]}},
                "mine_structure:turn_light_on": {"remove": {"component_groups": ["mine_structure:light_off"]},
                                                 "add": {"component_groups": ["mine_structure:light_on"]}},
                "mine_structure:turn_light_off": {"remove": {"component_groups": ["mine_structure:light_on"]},
                                                  "add": {"component_groups": ["mine_structure:light_off"]}},
            },
        },
    })
    write(os.path.join(RP, "entity", sid + ".entity.json"), {
        "format_version": "1.10.0",
        "minecraft:client_entity": {"description": {
            "identifier": "mine_structure:" + sid,
            "materials": {"default": "entity_alphatest"},
            "textures": {"default": "textures/entity/" + sid + "/" + sid + "_atlas"},
            "geometry": {"default": "geometry." + sid},
            "animations": {"on": "animation." + sid + ".on", "off": "animation." + sid + ".off",
                           "light_ctrl": "controller.animation." + sid + ".light"},
            "scripts": {"animate": ["light_ctrl"]},
            "render_controllers": ["controller.render." + sid],
        }},
    })
    write(os.path.join(RP, "render_controllers", sid + ".render_controllers.json"), render_controller(sid))
    write(os.path.join(RP, "animations", sid + ".animation.json"), {
        "format_version": "1.8.0",
        "animations": {
            "animation." + sid + ".off": {"loop": "hold_on_last_frame", "animation_length": 0.05,
                                          "bones": {"glow": {"scale": [1, 0, 1]}}},
            "animation." + sid + ".on": {"loop": "hold_on_last_frame", "animation_length": 1.6,
                                         "bones": {"glow": {"scale": {"0.0": [1, 0, 1], "1.6": [1, 1, 1]}}}},
        },
    })
    write(os.path.join(RP, "animation_controllers", sid + ".animation_controllers.json"), {
        "format_version": "1.10.0",
        "animation_controllers": {"controller.animation." + sid + ".light": {
            "initial_state": "off",
            "states": {"off": {"animations": ["off"], "transitions": [{"on": "q.variant == 1"}]},
                       "on": {"animations": ["on"], "transitions": [{"off": "q.variant == 0"}]}}}},
    })
    write(os.path.normpath(os.path.join(BP, "..", "..", "content", "furniture", sid + ".resources.json")),
          resources(sid, "variant_fill", True))


def build_bathtub():
    sid = "unicorn_bathtub"
    specs = [("shell", (246, 202, 230), "solid"), ("water", (150, 212, 238), "water"),
             ("bubble", (250, 250, 255), "solid"), ("faucet", (206, 204, 226), "solid"),
             ("gold", (245, 210, 120), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6601)
    b = Builder(cm)
    # clawfoot tub lifted on 4 gold feet
    for i, (fx, fz) in enumerate([(-6, -4), (4.4, -4), (-6, 4), (4.4, 4)]):
        b.add("body", "foot%d" % i, [fx, 0, fz], [1.6, 2.2, 1.6], "gold")
    b.add("body", "lower", [-7, 2, -5], [14, 5, 10], "shell")
    b.add("body", "rim_back", [-7, 7, 3], [14, 2, 2], "shell")
    b.add("body", "rim_front", [-7, 7, -5], [14, 2, 2], "shell")
    b.add("body", "rim_left", [-7, 7, -3], [2, 2, 6], "shell")
    b.add("body", "rim_right", [5, 7, -3], [2, 2, 6], "shell")
    b.add("body", "trim", [-7, 8.6, -5], [14, 0.5, 10], "gold")
    b.add("body", "faucet", [-1, 9, 3.4], [2, 3, 1.6], "faucet")
    b.add("body", "spout", [-1, 11, 0.5], [1.6, 1.2, 3], "faucet")
    b.add("body", "tap_l", [-2.6, 9, 3.4], [1, 1.4, 1], "gold")
    b.add("body", "tap_r", [1.6, 9, 3.4], [1, 1.4, 1], "gold")
    # water + bubbles (glow bone; fills up from the tub floor at y=3)
    b.add("glow", "water", [-5, 3, -3], [10, 4, 6], "water")
    for i, (bx, bz) in enumerate([(-3.5, -1.5), (-0.5, 1), (2.5, -1), (1, -2)]):
        b.add("glow", "bubble%d" % i, [bx, 6.4, bz], [1.2, 1, 1.2], "bubble")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "glow", "parent": sid, "pivot": [0, 3, 0]}], rel, src)
    variant_fill_wiring(sid, "action.interact.fill_water", "action.interact.drain_water", 1.1, 0.95)


def build_oven():
    sid = "unicorn_oven"
    specs = [("shell", (216, 200, 240), "solid"), ("bezel", (66, 62, 96), "solid"),
             ("glow", (255, 196, 120), "glow"), ("knob", (245, 210, 120), "solid"),
             ("panel", (150, 140, 184), "solid"), ("button", (140, 200, 245), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6602)
    b = Builder(cm)
    b.add("body", "body", [-5, 0, -5], [10, 11.5, 9], "shell")
    b.add("body", "panel", [-5, 11.5, -5.2], [10, 2.4, 0.5], "panel")
    for i in range(4):
        b.add("body", "dial%d" % i, [-4 + i * 2.3, 12.2, -5.5], [1, 1, 0.4], "knob")
    b.add("body", "lightbtn", [3.6, 12.2, -5.5], [0.8, 1, 0.4], "button")
    b.add("body", "window", [-4.3, 2, -5.4], [8.6, 7, 0.5], "bezel")
    b.add("body", "win_trim", [-4.6, 1.7, -5.5], [9.2, 0.4, 0.4], "knob")
    b.add("body", "handle", [-4.5, 8.6, -5.7], [9, 0.7, 0.7], "knob")
    b.add("body", "toekick", [-4, 0, -5.2], [8, 1, 0.4], "bezel")
    b.add("glow", "inner", [-3.9, 2.3, -5.6], [7.8, 5, 0.3], "glow")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "glow", "parent": sid, "pivot": [0, 5, -5]}], rel, src)
    variant_light_wiring(sid, "action.interact.oven_on", "action.interact.oven_off", 0.9, 1.2)


def build_microwave():
    sid = "unicorn_microwave"
    specs = [("shell", (244, 200, 230), "solid"), ("bezel", (66, 62, 96), "solid"),
             ("glow", (255, 236, 160), "glow"), ("knob", (245, 210, 120), "solid"),
             ("button", (140, 200, 245), "solid"), ("display", (120, 235, 150), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6603)
    b = Builder(cm)
    b.add("body", "body", [-5, 0, -4], [10, 6.5, 8], "shell")
    b.add("body", "door", [-4.9, 0.6, -4.4], [6.4, 5.2, 0.3], "knob")
    b.add("body", "window", [-4.6, 1, -4.55], [5.4, 4.2, 0.3], "bezel")
    b.add("body", "handle", [1.0, 1, -4.7], [0.5, 4.2, 0.5], "knob")
    b.add("body", "panel", [1.8, 0.6, -4.4], [3.2, 5.2, 0.3], "shell")
    b.add("body", "display", [2.0, 4, -4.6], [2.8, 0.8, 0.2], "display")
    for r in range(3):
        for c in range(2):
            b.add("body", "mbtn%d%d" % (r, c), [2.1 + c * 1.4, 1.2 + r * 0.9, -4.6], [0.8, 0.6, 0.2], "button")
    b.add("body", "mdial", [4.0, 1.4, -4.6], [0.8, 0.8, 0.3], "knob")
    b.add("glow", "win_glow", [-4.3, 1.3, -4.7], [4.8, 3.6, 0.3], "glow")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "glow", "parent": sid, "pivot": [0, 3, -4]}], rel, src)
    variant_light_wiring(sid, "action.interact.start", "action.interact.stop", 0.8, 0.6)


def build_toaster():
    sid = "unicorn_toaster"
    specs = [("shell", (248, 178, 214), "solid"), ("slot", (58, 54, 88), "solid"),
             ("lever", (245, 210, 120), "solid"), ("toast", (214, 162, 96), "solid"),
             ("eye", (60, 56, 80), "solid"), ("accent", (244, 140, 180), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6604)
    b = Builder(cm)
    b.add("body", "body", [-3.5, 1, -3], [7, 4, 6], "shell")
    b.add("body", "foot_l", [-3, 0, -2.5], [1.5, 1, 5], "accent")
    b.add("body", "foot_r", [1.5, 0, -2.5], [1.5, 1, 5], "accent")
    b.add("body", "slot1", [-2.4, 5, -1.6], [1.8, 0.5, 3.2], "slot")
    b.add("body", "slot2", [0.6, 5, -1.6], [1.8, 0.5, 3.2], "slot")
    b.add("body", "toast1", [-2.1, 5.4, -1], [1.4, 2.2, 2], "toast")
    b.add("body", "toast2", [0.7, 5.4, -1], [1.4, 2.2, 2], "toast")
    b.add("body", "lever", [3.5, 2, -0.5], [0.6, 2.2, 1], "lever")
    b.add("body", "lever_knob", [3.4, 3.8, -0.7], [1, 0.7, 1.4], "lever")
    b.add("body", "dial", [3.5, 1.3, 1.6], [0.4, 1.1, 1.1], "lever")
    b.add("body", "crumbtray", [-3.5, 1, -3.2], [7, 0.6, 0.3], "accent")
    b.add("body", "eye_l", [-1.8, 3, -3.05], [0.8, 0.8, 0.25], "eye")
    b.add("body", "eye_r", [1.0, 3, -3.05], [0.8, 0.8, 0.25], "eye")
    b.add("body", "blush_l", [-2.4, 2.2, -3.05], [0.7, 0.5, 0.2], "accent")
    b.add("body", "blush_r", [1.7, 2.2, -3.05], [0.7, 0.5, 0.2], "accent")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src)
    write(os.path.join(BP, "entities", sid + ".entity.json"), {
        "format_version": "1.20.0",
        "minecraft:entity": {
            "description": {"identifier": "mine_structure:" + sid, "is_spawnable": True,
                            "is_summonable": True, "is_experimental": False},
            "components": common_components(sid, 0.6, 0.5),
        },
    })
    static_client(sid)
    write(os.path.join(RP, "render_controllers", sid + ".render_controllers.json"), render_controller(sid))
    write(os.path.normpath(os.path.join(BP, "..", "..", "content", "furniture", sid + ".resources.json")),
          resources(sid, "script_give", False))


def build_robot():
    sid = "unicorn_robot_vacuum"
    specs = [("shell", (220, 210, 240), "solid"), ("face", (224, 236, 250), "face"),
             ("accent", (244, 160, 200), "solid"), ("sensor", (140, 200, 245), "solid"),
             ("dark", (70, 66, 96), "solid"), ("button", (245, 210, 120), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6605)
    b = Builder(cm)
    b.add("body", "disc", [-3, 0.6, -3], [6, 1.8, 6], "shell")
    b.add("body", "bumper", [-3.2, 0.6, -3.2], [6.4, 1, 6.4], "accent")
    b.add("body", "brush", [-2, 0, -3], [4, 0.6, 1], "dark")
    b.add("body", "wheel_l", [-3.1, 0.2, -0.8], [0.4, 0.8, 1.6], "dark")
    b.add("body", "wheel_r", [2.7, 0.2, -0.8], [0.4, 0.8, 1.6], "dark")
    b.add("body", "dome", [-2.2, 2.4, -2.2], [4.4, 1.2, 4.4], "shell")
    b.add("body", "sensor", [-0.7, 3.6, -0.7], [1.4, 0.9, 1.4], "sensor")
    b.add("body", "antenna", [-0.2, 4.5, -0.2], [0.4, 1.4, 0.4], "dark")
    b.add("body", "antenna_tip", [-0.4, 5.7, -0.4], [0.8, 0.8, 0.8], "accent")
    b.add("body", "btn1", [1, 2.5, 1.2], [0.8, 0.4, 0.8], "button")
    b.add("body", "btn2", [-1.8, 2.5, 1.2], [0.8, 0.4, 0.8], "sensor")
    b.add("body", "facepanel", [-1.7, 1.1, -3.25], [3.4, 1.3, 0.25], "face", face_cells={"north": "face"})
    write(os.path.join(BP, "entities", sid + ".entity.json"), {
        "format_version": "1.20.0",
        "minecraft:entity": {
            "description": {"identifier": "mine_structure:" + sid, "is_spawnable": True,
                            "is_summonable": True, "is_experimental": False},
            "components": {
                "minecraft:type_family": {"family": ["mine_structure_pet", sid]},
                "minecraft:collision_box": {"width": 0.55, "height": 0.4},
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
