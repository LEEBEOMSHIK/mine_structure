"""Living-room furniture: sofa, fireplace, fan, bookshelf, wardrobe, piano.

  unicorn_sofa       rideable, 3 seats
  unicorn_fireplace  variant toggle: flames (glow bone) on/off
  unicorn_fan        variant toggle: blades spin on/off (new "variant_spin")
  unicorn_bookshelf  Script storage (store/retrieve)
  unicorn_wardrobe   Script storage (store/retrieve)
  unicorn_piano      Script: plays a random note on interact

Reuses gen_kids_furniture (Builder/make_atlas/assemble), gen_room_furniture
(variant_light_wiring/rideable_wiring/render_controller/resources/common_components/write),
and gen_bath_kitchen (static_client).
"""
import os

from gen_kids_furniture import Builder, assemble, make_atlas
from gen_room_furniture import (BP, RP, common_components, render_controller,
                                resources, rideable_wiring, variant_light_wiring, write)
from gen_bath_kitchen import static_client


def interact(text, ev):
    return {"interactions": [{"interact_text": text, "swing": True, "play_sounds": "random.click",
                              "on_interact": {"event": ev, "target": "self"}}]}


def variant_spin_wiring(sid, on_text, off_text, width, height):
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
            "animation." + sid + ".off": {"loop": "hold_on_last_frame", "animation_length": 0.1,
                                          "bones": {"blades": {"rotation": [0, 0, 0]}}},
            "animation." + sid + ".on": {"loop": True, "animation_length": 0.7,
                                         "bones": {"blades": {"rotation": {"0.0": [0, 0, 0], "0.7": [0, 0, 360]}}}},
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
          resources(sid, "variant_spin", True))


def script_entity(sid, mechanic, width, height):
    write(os.path.join(BP, "entities", sid + ".entity.json"), {
        "format_version": "1.20.0",
        "minecraft:entity": {
            "description": {"identifier": "mine_structure:" + sid, "is_spawnable": True,
                            "is_summonable": True, "is_experimental": False},
            "components": common_components(sid, width, height),
        },
    })
    static_client(sid)
    write(os.path.join(RP, "render_controllers", sid + ".render_controllers.json"), render_controller(sid))
    write(os.path.normpath(os.path.join(BP, "..", "..", "content", "furniture", sid + ".resources.json")),
          resources(sid, mechanic, False))


# ---------------------------------------------------------------- models
def build_sofa():
    sid = "unicorn_sofa"
    specs = [("shell", (220, 196, 236), "solid"), ("pillow", (248, 196, 224), "solid"),
             ("leg", (245, 210, 120), "solid"), ("accent", (244, 160, 200), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6801)
    b = Builder(cm)
    b.add("body", "seat", [-9, 2, -5], [18, 3, 9], "shell")
    b.add("body", "back", [-9, 5, 3], [18, 7, 2], "shell")
    b.add("body", "arm_l", [-9, 3, -5], [2, 5, 9], "shell")
    b.add("body", "arm_r", [7, 3, -5], [2, 5, 9], "shell")
    for i, cx in enumerate((-8, -2.5, 3)):
        b.add("body", "cushion%d" % i, [cx, 5, -4], [5.5, 1.6, 7], "pillow")
        b.add("body", "backc%d" % i, [cx, 5.5, 1.2], [5.5, 5.5, 1.6], "pillow")
    for i, (lx, lz) in enumerate([(-8, -4.5), (6, -4.5), (-8, 3.5), (6, 3.5)]):
        b.add("body", "leg%d" % i, [lx, 0, lz], [1.5, 2, 1.5], "leg")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src)
    rideable_wiring(sid, [{"position": [-0.65, 0.4, -0.1], "lock_rider_rotation": 0},
                          {"position": [0, 0.4, -0.1], "lock_rider_rotation": 0},
                          {"position": [0.65, 0.4, -0.1], "lock_rider_rotation": 0}], 1.7, 0.8)


def build_fireplace():
    sid = "unicorn_fireplace"
    specs = [("shell", (224, 206, 236), "solid"), ("bezel", (60, 54, 70), "solid"),
             ("log", (158, 110, 70), "solid"), ("flame", (255, 170, 90), "glow"),
             ("accent", (244, 160, 200), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6802)
    b = Builder(cm)
    # surround (with brick courses via accent stripes) + recessed firebox
    b.add("body", "body", [-7, 0, -3], [14, 12, 6], "shell")
    b.add("body", "brick1", [-7, 3.4, -3.05], [14, 0.4, 0.1], "accent")
    b.add("body", "brick2", [-7, 7.4, -3.05], [14, 0.4, 0.1], "accent")
    b.add("body", "opening", [-4.5, 1, -3.2], [9, 8, 0.5], "bezel")
    b.add("body", "firebox", [-4.5, 1, -3.0], [9, 8, 2.6], "bezel")
    b.add("body", "hearth", [-5.5, 0, -3.4], [11, 1, 3.4], "bezel")
    # andirons + logs (stacked)
    b.add("body", "andiron_l", [-3.8, 1, -2], [0.6, 2, 2.4], "log")
    b.add("body", "andiron_r", [3.2, 1, -2], [0.6, 2, 2.4], "log")
    b.add("body", "log1", [-3.5, 1.2, -2], [3, 1.4, 2.4], "log")
    b.add("body", "log2", [0.5, 1.2, -2], [3, 1.4, 2.4], "log")
    b.add("body", "log3", [-1.6, 2.4, -1.8], [3.2, 1.4, 2], "log")
    # mantel + decor
    b.add("body", "mantel", [-7.5, 11.8, -3.6], [15, 1.5, 7], "shell")
    b.add("body", "mantel_trim", [-7.5, 11.4, -3.6], [15, 0.5, 0.5], "accent")
    b.add("body", "vase_l", [-6, 13.3, -2.5], [1.4, 2, 1.4], "accent")
    b.add("body", "vase_r", [4.6, 13.3, -2.5], [1.2, 1.6, 1.2], "log")
    # flames (glow bone): layered flames + embers
    b.add("glow", "ember", [-4, 1.1, -2], [8, 0.8, 2.2], "flame")
    b.add("glow", "flame1", [-3.5, 1.5, -2.1], [7, 4.5, 1.4], "flame")
    b.add("glow", "flame2", [-2.2, 4.5, -2.1], [4.4, 3, 1.2], "flame")
    b.add("glow", "flame3", [-1, 6.8, -2.1], [2, 2, 1], "flame")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "glow", "parent": sid, "pivot": [0, 2, -2]}], rel, src)
    variant_light_wiring(sid, "action.interact.light_fire", "action.interact.put_out", 1.1, 1.1)


def build_fan():
    sid = "unicorn_fan"
    specs = [("shell", (216, 200, 240), "solid"), ("accent", (245, 210, 120), "solid"),
             ("blade", (190, 226, 250), "solid"), ("hub", (244, 160, 200), "solid"),
             ("cage", (228, 224, 240), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6803)
    b = Builder(cm)
    cx, cy, cz = 0.0, 11.0, -2.3  # fan-head centre (front = -Z)
    # stand: weighted base + pole + motor housing
    b.add("body", "base", [-3, 0, -3], [6, 1, 6], "shell")
    b.add("body", "base_top", [-2, 1, -2], [4, 0.8, 4], "accent")
    b.add("body", "pole", [-0.7, 1.8, -0.7], [1.4, 7.5, 1.4], "shell")
    b.add("body", "motor", [-1.8, 9.3, 0], [3.6, 3.2, 2.2], "shell")
    b.add("body", "motor_cap", [-1.4, 9.7, 2.1], [2.8, 2.4, 0.6], "accent")
    # round safety cage: a dense ring (segments touch) + cross bars (spokes)
    import math
    for i in range(20):
        a = math.radians(i * 18)
        bx = cx - 0.55 + 3.5 * math.cos(a)
        by = cy - 0.55 + 3.5 * math.sin(a)
        b.add("body", "cage%d" % i, [bx, by, cz - 0.35], [1.1, 1.1, 0.35], "cage")
    b.add("body", "cage_barh", [cx - 3.8, cy - 0.35, cz - 0.3], [7.6, 0.7, 0.3], "cage")
    b.add("body", "cage_barv", [cx - 0.35, cy - 3.8, cz - 0.3], [0.7, 7.6, 0.3], "cage")
    b.add("body", "cage_hub", [cx - 0.8, cy - 0.8, cz - 0.45], [1.6, 1.6, 0.3], "cage")
    # blades (their own bone; spins around z). 4 pitched blades at 0/90/180/270.
    for i, ang in enumerate((0, 90, 180, 270)):
        b.add("blades", "blade%d" % i, [cx - 0.6, cy + 0.3, cz - 0.1], [1.2, 3.2, 0.3],
              "blade", rotation=[18, 0, ang], pivot=[cx, cy, cz])
    b.add("blades", "hub", [cx - 0.9, cy - 0.9, cz - 0.2], [1.8, 1.8, 0.6], "hub")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "blades", "parent": sid, "pivot": [cx, cy, cz]}], rel, src)
    variant_spin_wiring(sid, "action.interact.fan_on", "action.interact.fan_off", 0.6, 1.4)


def build_bookshelf():
    sid = "unicorn_bookshelf"
    specs = [("shell", (210, 190, 230), "solid"), ("plank", (236, 210, 180), "solid"),
             ("book_a", (244, 140, 170), "solid"), ("book_b", (150, 210, 240), "solid"),
             ("book_c", (160, 224, 170), "solid"), ("book_d", (245, 210, 120), "solid"),
             ("plant", (120, 200, 150), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6804)
    b = Builder(cm)
    # carcass: sides + top crown + base + back panel
    b.add("body", "side_l", [-6, 0, -3], [1, 17, 6], "shell")
    b.add("body", "side_r", [5, 0, -3], [1, 17, 6], "shell")
    b.add("body", "bottom", [-5, 0, -3], [10, 1.2, 6], "shell")
    b.add("body", "crown", [-6.5, 17, -3.3], [13, 1.2, 6.6], "shell")
    b.add("body", "crown_trim", [-6.5, 16.6, -3.3], [13, 0.4, 0.4], "book_d")
    b.add("body", "back", [-5, 1, 2.4], [10, 16, 0.3], "plank")
    books = ["book_a", "book_b", "book_c", "book_d"]
    heights = [3.6, 4.2, 3.0, 3.8, 4.0, 3.2, 4.2, 3.4, 3.9]
    for s, shelf_y in enumerate((1.2, 5.2, 9.2, 13.2)):
        b.add("body", "shelf%d" % s, [-5, shelf_y - 0.5, -3], [10, 0.6, 5.5], "plank")
        for i in range(9):
            h = heights[(s * 2 + i) % len(heights)]
            b.add("body", "book_%d_%d" % (s, i), [-4.8 + i * 1.05, shelf_y, -2], [0.95, h, 2.6],
                  books[(s + i) % 4])
    # top decoration: a little potted plant + a clock
    b.add("body", "pot", [-4.5, 17.2, -0.5], [2, 1.4, 2], "book_d")
    b.add("body", "plant", [-4.2, 18.6, -0.2], [1.4, 2, 1.4], "plant")
    b.add("body", "clock", [2.5, 17.2, -0.5], [2, 2, 0.6], "book_b")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src)
    script_entity(sid, "script_store", 0.9, 1.2)


def build_wardrobe():
    sid = "unicorn_wardrobe"
    specs = [("shell", (220, 200, 238), "solid"), ("door", (236, 214, 244), "solid"),
             ("knob", (245, 210, 120), "solid"), ("accent", (244, 160, 200), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6805)
    b = Builder(cm)
    b.add("body", "body", [-5, 0, -4], [10, 18, 8], "shell")
    b.add("body", "door_l", [-4.7, 1, -4.4], [4.6, 16, 0.6], "door")
    b.add("body", "door_r", [0.1, 1, -4.4], [4.6, 16, 0.6], "door")
    b.add("body", "knob_l", [-0.6, 8.5, -4.7], [0.7, 0.7, 0.4], "knob")
    b.add("body", "knob_r", [0.0, 8.5, -4.7], [0.7, 0.7, 0.4], "knob")
    b.add("body", "top", [-5.5, 18, -4.5], [11, 1.5, 9], "shell")
    b.add("body", "trim", [-5, 17.4, -4.4], [10, 0.6, 0.5], "accent")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src)
    script_entity(sid, "script_store", 0.8, 1.6)


def build_piano():
    sid = "unicorn_piano"
    specs = [("shell", (212, 192, 232), "solid"), ("white", (248, 246, 250), "solid"),
             ("black", (52, 48, 70), "solid"), ("accent", (244, 160, 200), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6806)
    b = Builder(cm)
    b.add("body", "body", [-7, 0, -3], [14, 14, 6], "shell")
    b.add("body", "music_stand", [-5.5, 9, -3.4], [11, 4, 0.5], "accent")
    b.add("body", "keybed", [-6.5, 6.5, -5], [13, 1.5, 2], "shell")
    b.add("body", "keys", [-6, 7, -5.2], [12, 0.8, 1.6], "white")
    for i in range(7):
        b.add("body", "bkey%d" % i, [-5.2 + i * 1.6, 7.6, -5.0], [0.7, 0.5, 1], "black")
    b.add("body", "lid", [-7, 14, -3], [14, 0.6, 6], "shell")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src)
    script_entity(sid, "script_play", 1.0, 1.0)


def main():
    build_sofa()
    build_fireplace()
    build_fan()
    build_bookshelf()
    build_wardrobe()
    build_piano()


if __name__ == "__main__":
    main()
