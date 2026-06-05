"""Playground: swing, slide, seesaw.

  unicorn_swing   rideable (1) + always-on swing animation (bone "rock")
  unicorn_slide   rideable (1, sit at the top)
  unicorn_seesaw  rideable (2, one each end)

Reuses gen_kids_furniture (Builder/make_atlas/assemble) and gen_room_furniture
(rideable_wiring/render_controller/resources/common_components/write).
"""
import os

from gen_kids_furniture import Builder, assemble, make_atlas
from gen_room_furniture import (BP, RP, common_components, render_controller,
                                resources, rideable_wiring, write)


def build_swing():
    sid = "unicorn_swing"
    specs = [("frame", (204, 190, 234), "solid"), ("rope", (245, 210, 120), "solid"),
             ("seat", (244, 170, 210), "solid"), ("rainbow", None, "horn")]
    rel, src, cm = make_atlas(sid, specs, 6701)
    b = Builder(cm)
    # A-frame (static): legs + top bar
    b.add("body", "leg_lf", [-8, 0, -3], [1.5, 16, 1.5], "frame")
    b.add("body", "leg_lb", [-8, 0, 1.5], [1.5, 16, 1.5], "frame")
    b.add("body", "leg_rf", [6.5, 0, -3], [1.5, 16, 1.5], "frame")
    b.add("body", "leg_rb", [6.5, 0, 1.5], [1.5, 16, 1.5], "frame")
    b.add("body", "topbar", [-8, 15.5, -1], [16, 1.5, 1.5], "frame")
    b.add("body", "star", [-1, 17, -0.7], [2, 2, 0.8], "rainbow")
    # swinging part (bone "rock"): ropes + seat, pivots at the top bar
    b.add("rock", "rope_l", [-3, 4, -0.4], [0.6, 11, 0.6], "rope")
    b.add("rock", "rope_r", [2.4, 4, -0.4], [0.6, 11, 0.6], "rope")
    b.add("rock", "seat", [-3.5, 3, -1.5], [7, 0.8, 3], "seat")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "rock", "parent": sid, "pivot": [0, 16, -0.2]}], rel, src)
    # rideable + always-on swing (reuses the "rideable" validator: bone+anim "rock")
    components = common_components(sid, 1.2, 1.2)
    components["minecraft:rideable"] = {"seat_count": 1, "family_types": ["player"],
                                        "interact_text": "action.interact.ride",
                                        "seats": [{"position": [0, 0.35, 0], "lock_rider_rotation": 0}]}
    write(os.path.join(BP, "entities", sid + ".entity.json"), {
        "format_version": "1.20.0",
        "minecraft:entity": {"description": {"identifier": "mine_structure:" + sid, "is_spawnable": True,
                                             "is_summonable": True, "is_experimental": False},
                             "components": components},
    })
    write(os.path.join(RP, "entity", sid + ".entity.json"), {
        "format_version": "1.10.0",
        "minecraft:client_entity": {"description": {
            "identifier": "mine_structure:" + sid,
            "materials": {"default": "entity_alphatest"},
            "textures": {"default": "textures/entity/" + sid + "/" + sid + "_atlas"},
            "geometry": {"default": "geometry." + sid},
            "animations": {"rock": "animation." + sid + ".rock"},
            "scripts": {"animate": ["rock"]},
            "render_controllers": ["controller.render." + sid],
        }},
    })
    write(os.path.join(RP, "render_controllers", sid + ".render_controllers.json"), render_controller(sid))
    write(os.path.join(RP, "animations", sid + ".animation.json"), {
        "format_version": "1.8.0",
        "animations": {"animation." + sid + ".rock": {
            "loop": True, "animation_length": 2.6,
            "bones": {"rock": {"rotation": {"0.0": [0, 0, 0], "0.65": [22, 0, 0], "1.3": [0, 0, 0],
                                            "1.95": [-22, 0, 0], "2.6": [0, 0, 0]}}}}},
    })
    write(os.path.normpath(os.path.join(BP, "..", "..", "content", "furniture", sid + ".resources.json")),
          resources(sid, "rideable", True))


def build_slide():
    sid = "unicorn_slide"
    specs = [("frame", (204, 190, 234), "solid"), ("slide", (150, 210, 238), "solid"),
             ("step", (244, 170, 210), "solid"), ("rainbow", None, "horn")]
    rel, src, cm = make_atlas(sid, specs, 6702)
    b = Builder(cm)
    # platform at the back (top), ladder, slide ramp to the front (-Z)
    b.add("frame", "post_l", [-5, 0, 4], [1.5, 12, 1.5], "frame")
    b.add("frame", "post_r", [3.5, 0, 4], [1.5, 12, 1.5], "frame")
    b.add("frame", "platform", [-5, 11, 2], [10, 1.5, 4], "frame")
    b.add("frame", "rail_l", [-5, 12.5, 2], [1, 3, 4], "frame")
    b.add("frame", "rail_r", [4, 12.5, 2], [1, 3, 4], "frame")
    # ladder steps (back)
    for i, y in enumerate((2.5, 5, 7.5, 10)):
        b.add("frame", "step%d" % i, [-4, y, 5.4], [8, 0.8, 1], "step")
    # slide ramp (stepped down toward the front)
    for i in range(5):
        b.add("frame", "ramp%d" % i, [-4, 10 - i * 2.0, 1 - i * 2.2], [8, 1, 3], "slide")
    b.add("frame", "star", [-1, 14.5, 2], [2, 2, 0.8], "rainbow")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "frame", "parent": sid, "pivot": [0, 0, 0]}], rel, src)
    rideable_wiring(sid, [{"position": [0, 0.9, 0.3], "lock_rider_rotation": 0}], 1.2, 1.6)


def build_seesaw():
    sid = "unicorn_seesaw"
    specs = [("plank", (244, 170, 210), "solid"), ("base", (204, 190, 234), "solid"),
             ("handle", (245, 210, 120), "solid"), ("rainbow", None, "horn")]
    rel, src, cm = make_atlas(sid, specs, 6703)
    b = Builder(cm)
    b.add("body", "fulcrum", [-1.5, 0, -1.5], [3, 4, 3], "base")
    b.add("body", "pivot_cap", [-2, 4, -2], [4, 1, 4], "base")
    b.add("body", "plank", [-13, 4.8, -1.5], [26, 1.2, 3], "plank")
    b.add("body", "seat_l", [-12.5, 6, -1.6], [4, 0.8, 3.2], "plank")
    b.add("body", "seat_r", [8.5, 6, -1.6], [4, 0.8, 3.2], "plank")
    b.add("body", "handle_l", [-10.5, 6, 0], [0.8, 3, 0.8], "handle")
    b.add("body", "handle_r", [9.7, 6, 0], [0.8, 3, 0.8], "handle")
    b.add("body", "ball_l", [-11.4, 8.6, -0.3], [1.2, 1.2, 1.2], "rainbow")
    b.add("body", "ball_r", [9.2, 8.6, -0.3], [1.2, 1.2, 1.2], "rainbow")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src)
    rideable_wiring(sid, [{"position": [-0.7, 0.45, 0], "lock_rider_rotation": 0},
                          {"position": [0.7, 0.45, 0], "lock_rider_rotation": 0}], 1.8, 0.7)


def main():
    build_swing()
    build_slide()
    build_seesaw()


if __name__ == "__main__":
    main()
