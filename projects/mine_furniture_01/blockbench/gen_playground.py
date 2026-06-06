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
    b.add("body", "topbar", [-8, 15.3, -3], [16, 1.5, 6], "frame")  # spans both leg rows
    b.add("body", "star", [-1, 16.8, -1], [2, 2, 0.8], "rainbow")
    # swinging part (bone "rock"): ropes + seat, pivots at the top bar
    b.add("rock", "rope_l", [-3, 4, -0.4], [0.6, 11.5, 0.6], "rope")
    b.add("rock", "rope_r", [2.4, 4, -0.4], [0.6, 11.5, 0.6], "rope")
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
    # back tower: posts + platform + rails + ladder
    b.add("frame", "post_l", [-5, 0, 3], [1.5, 11, 1.5], "frame")
    b.add("frame", "post_r", [3.5, 0, 3], [1.5, 11, 1.5], "frame")
    b.add("frame", "platform", [-5, 10.3, 1], [10, 1.5, 5], "frame")
    b.add("frame", "prail_l", [-5, 11.8, 1], [1, 3, 5], "frame")
    b.add("frame", "prail_r", [4, 11.8, 1], [1, 3, 5], "frame")
    b.add("frame", "back", [-5, 11.8, 5.4], [10, 4, 0.8], "frame")
    b.add("frame", "ladder_rail_l", [-4.2, 1.5, 5.5], [0.7, 9.5, 0.9], "frame")
    b.add("frame", "ladder_rail_r", [3.5, 1.5, 5.5], [0.7, 9.5, 0.9], "frame")
    for i, y in enumerate((2, 4.5, 7, 9.5)):
        b.add("frame", "step%d" % i, [-4, y, 5.6], [8, 0.8, 1], "step")
    # a real SLANTED slide chute (one tilted board) + side walls, sloping to -Z
    rot, piv = [-40, 0, 0], [0, 11, 1.5]
    b.add("frame", "chute", [-4, 10.2, -14], [8, 1, 16], "slide", rotation=rot, pivot=piv)
    b.add("frame", "side_l", [-4.7, 10.2, -14], [0.7, 2.4, 16], "frame", rotation=rot, pivot=piv)
    b.add("frame", "side_r", [4, 10.2, -14], [0.7, 2.4, 16], "frame", rotation=rot, pivot=piv)
    b.add("frame", "star", [-1, 12.5, 4.6], [2, 2, 0.7], "rainbow")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "frame", "parent": sid, "pivot": [0, 0, 0]}], rel, src)
    rideable_wiring(sid, [{"position": [0, 0.85, 0.3], "lock_rider_rotation": 0}], 1.4, 1.6)


def build_seesaw():
    sid = "unicorn_seesaw"
    specs = [("plank", (244, 170, 210), "solid"), ("base", (204, 190, 234), "solid"),
             ("handle", (245, 210, 120), "solid"), ("rainbow", None, "horn")]
    rel, src, cm = make_atlas(sid, specs, 6703)
    b = Builder(cm)
    # static fulcrum
    b.add("base", "fulcrum", [-1.5, 0, -1.5], [3, 4, 3], "base")
    b.add("base", "cap", [-2, 4, -2], [4, 1, 4], "base")
    # the balanced plank (its own bone, gently tilts); symmetric about x=0
    b.add("plank", "plank", [-13, 4.8, -1.5], [26, 1.2, 3], "plank")
    b.add("plank", "seat_l", [-12.5, 6, -1.6], [4, 0.8, 3.2], "plank")
    b.add("plank", "seat_r", [8.5, 6, -1.6], [4, 0.8, 3.2], "plank")
    b.add("plank", "handle_l", [-10.3, 6, 0], [0.8, 3, 0.8], "handle")
    b.add("plank", "handle_r", [9.5, 6, 0], [0.8, 3, 0.8], "handle")
    b.add("plank", "ball_l", [-10.5, 8.6, -0.3], [1.2, 1.2, 1.2], "rainbow")
    b.add("plank", "ball_r", [9.3, 8.6, -0.3], [1.2, 1.2, 1.2], "rainbow")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "base", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "plank", "parent": sid, "pivot": [0, 5.4, 0]}], rel, src)
    # rideable 2 + gentle seesaw tilt animation
    components = common_components(sid, 1.8, 0.7)
    components["minecraft:rideable"] = {"seat_count": 2, "family_types": ["player"],
                                        "interact_text": "action.interact.ride",
                                        "seats": [{"position": [-0.65, 0.45, 0], "lock_rider_rotation": 0},
                                                  {"position": [0.65, 0.45, 0], "lock_rider_rotation": 0}]}
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
            "animations": {"tilt": "animation." + sid + ".tilt"},
            "scripts": {"animate": ["tilt"]},
            "render_controllers": ["controller.render." + sid],
        }},
    })
    write(os.path.join(RP, "render_controllers", sid + ".render_controllers.json"), render_controller(sid))
    write(os.path.join(RP, "animations", sid + ".animation.json"), {
        "format_version": "1.8.0",
        "animations": {"animation." + sid + ".tilt": {
            "loop": True, "animation_length": 4.0,
            "bones": {"plank": {"rotation": {"0.0": [0, 0, 0], "1.0": [7, 0, 0], "2.0": [0, 0, 0],
                                             "3.0": [-7, 0, 0], "4.0": [0, 0, 0]}}}}},
    })
    write(os.path.normpath(os.path.join(BP, "..", "..", "content", "furniture", sid + ".resources.json")),
          resources(sid, "rideable_simple", True))


def main():
    build_swing()
    build_slide()
    build_seesaw()


if __name__ == "__main__":
    main()
