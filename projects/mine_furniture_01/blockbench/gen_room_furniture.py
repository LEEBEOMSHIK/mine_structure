"""More unicorn room furniture: TV, arcade machine, vanity (mirror w/ bulbs), and a
single-level king-size bed.

  unicorn_tv      variant_light screen on/off (cute-face display)
  unicorn_arcade  variant_light screen on/off (arcade cabinet)
  unicorn_vanity  variant_light mirror bulbs on/off (+ static mirror/drawers)
  unicorn_king_bed  minecraft:rideable, 2 seats (lie/sit), single level

geo/atlas/bbmodel reuse gen_kids_furniture helpers. Pastel palette, no horn.
"""
import json
import os

from gen_kids_furniture import Builder, assemble, make_atlas

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
BP = os.path.join(BASE, "addon", "behavior_pack")
RP = os.path.join(BASE, "addon", "resource_pack")
CONTENT = os.path.normpath(os.path.join(BASE, "content", "furniture"))


def write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    print("wrote", path)


def interact(text, ev):
    return {"interactions": [{
        "interact_text": text, "swing": True, "play_sounds": "random.click",
        "on_interact": {"event": ev, "target": "self"},
    }]}


def render_controller(sid):
    return {"format_version": "1.8.0", "render_controllers": {
        "controller.render." + sid: {"geometry": "Geometry.default",
                                     "materials": [{"*": "Material.default"}], "textures": ["Texture.default"]}}}


def resources(sid, mechanic, animated):
    rp = {
        "client_entity": "../../addon/resource_pack/entity/" + sid + ".entity.json",
        "geometry": "../../addon/resource_pack/models/entity/" + sid + ".geo.json",
        "texture": "../../addon/resource_pack/textures/entity/" + sid + "/" + sid + "_atlas.png",
        "render_controller": "../../addon/resource_pack/render_controllers/" + sid + ".render_controllers.json",
    }
    if animated:
        rp["animation"] = "../../addon/resource_pack/animations/" + sid + ".animation.json"
        rp["animation_controller"] = "../../addon/resource_pack/animation_controllers/" + sid + ".animation_controllers.json"
    return {
        "identifier": "mine_structure:" + sid, "content_type": "furniture_entity", "mechanic": mechanic,
        "behavior_pack": {"entity": "../../addon/behavior_pack/entities/" + sid + ".entity.json"},
        "resource_pack": rp, "blockbench_source": "../../blockbench/" + sid + ".bbmodel",
        "status": {"json_links_ready": True, "geometry_exported": True, "texture_exported": True, "in_game_tested": False},
    }


def common_components(sid, width, height):
    return {
        "minecraft:type_family": {"family": ["mine_structure_furniture", sid]},
        "minecraft:collision_box": {"width": width, "height": height},
        "minecraft:health": {"value": 12, "max": 12},
        "minecraft:physics": {"has_gravity": False, "has_collision": True},
        "minecraft:pushable": {"is_pushable": False, "is_pushable_by_piston": False},
    }


def variant_light_wiring(sid, on_text, off_text, width, height):
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
                                          "bones": {"glow": {"scale": [0, 0, 0]}}},
            "animation." + sid + ".on": {"loop": True, "animation_length": 2.0,
                                         "bones": {"glow": {"scale": {"0.0": [1, 1, 1], "1.0": [1.03, 1.03, 1], "2.0": [1, 1, 1]}}}},
        },
    })
    write(os.path.join(RP, "animation_controllers", sid + ".animation_controllers.json"), {
        "format_version": "1.10.0",
        "animation_controllers": {"controller.animation." + sid + ".light": {
            "initial_state": "off",
            "states": {"off": {"animations": ["off"], "transitions": [{"on": "q.variant == 1"}]},
                       "on": {"animations": ["on"], "transitions": [{"off": "q.variant == 0"}]}}}},
    })
    write(os.path.join(CONTENT, sid + ".resources.json"), resources(sid, "variant_light", True))


def rideable_wiring(sid, seats, width, height):
    components = common_components(sid, width, height)
    components["minecraft:rideable"] = {"seat_count": len(seats), "family_types": ["player"],
                                        "interact_text": "action.interact.ride", "seats": seats}
    write(os.path.join(BP, "entities", sid + ".entity.json"), {
        "format_version": "1.20.0",
        "minecraft:entity": {
            "description": {"identifier": "mine_structure:" + sid, "is_spawnable": True,
                            "is_summonable": True, "is_experimental": False},
            "components": components,
        },
    })
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
    write(os.path.join(RP, "render_controllers", sid + ".render_controllers.json"), render_controller(sid))
    write(os.path.join(CONTENT, sid + ".resources.json"), resources(sid, "rideable_simple", False))


# ---------------------------------------------------------------- models
def build_tv():
    sid = "unicorn_tv"
    specs = [("frame", (216, 200, 240), "solid"), ("bezel", (60, 56, 92), "solid"),
             ("screen", (188, 230, 252), "face"), ("shell", (204, 190, 234), "solid"),
             ("accent", (244, 182, 214), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6501)
    b = Builder(cm)
    b.add("body", "stand", [-5, 0, -2], [10, 1.5, 5], "shell")
    b.add("body", "neck", [-1.5, 1.5, 1], [3, 1, 1.5], "frame")
    b.add("body", "tv", [-9, 2.5, 1], [18, 11, 1.5], "frame")
    b.add("body", "bezel", [-8.5, 3, 0.6], [17, 10, 0.4], "bezel")
    b.add("body", "trim", [-9, 13.6, 1], [18, 0.6, 1.5], "accent")
    b.add("glow", "screen", [-8, 3.4, 0.45], [16, 9, 0.3], "screen", face_cells={"north": "screen"})
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "glow", "parent": sid, "pivot": [0, 8, 0.6]}], rel, src)
    variant_light_wiring(sid, "action.interact.screen_on", "action.interact.screen_off", 1.6, 1.0)


def build_arcade():
    sid = "unicorn_arcade"
    specs = [("shell", (224, 168, 210), "solid"), ("bezel", (58, 54, 92), "solid"),
             ("screen", (188, 230, 252), "face"), ("accent", (245, 210, 120), "solid"),
             ("button", (140, 200, 245), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6502)
    b = Builder(cm)
    b.add("body", "foot", [-5.5, 0, -5.5], [11, 1, 10], "shell")
    b.add("body", "cabinet", [-5, 1, -5], [10, 21, 9], "shell")
    b.add("body", "bezel", [-4.5, 12, -5.4], [9, 7, 0.6], "bezel")
    b.add("body", "panel", [-4.5, 7.5, -7.4], [9, 1.3, 2.6], "bezel")
    b.add("body", "joystick", [-2.9, 8.5, -6.4], [0.8, 2, 0.8], "accent")
    b.add("body", "joy_ball", [-3.1, 10.3, -6.6], [1.2, 1.2, 1.2], "button")
    for i, bx in enumerate((0.4, 2.0, 3.6)):
        b.add("body", "btn%d" % i, [bx, 8.6, -6.6], [1, 0.6, 1], "button")
    b.add("body", "marquee", [-5, 19.5, -5.4], [10, 2.5, 0.6], "accent")
    b.add("glow", "screen", [-4, 12.4, -5.6], [8, 6, 0.3], "screen", face_cells={"north": "screen"})
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "glow", "parent": sid, "pivot": [0, 15, -5.5]}], rel, src)
    variant_light_wiring(sid, "action.interact.screen_on", "action.interact.screen_off", 0.8, 2.2)


def build_vanity():
    sid = "unicorn_vanity"
    specs = [("shell", (244, 200, 230), "solid"), ("frame", (216, 200, 240), "solid"),
             ("mirror", (200, 230, 248), "solid"), ("bulb", (255, 240, 180), "glow"),
             ("knob", (245, 210, 120), "solid"), ("accent", (244, 160, 200), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6503)
    b = Builder(cm)
    b.add("body", "dresser", [-6, 0, -3], [12, 6, 6], "shell")
    b.add("body", "drawer1", [-5.6, 1.2, -3.06], [11.2, 0.4, 0.1], "accent")
    b.add("body", "drawer2", [-5.6, 3.6, -3.06], [11.2, 0.4, 0.1], "accent")
    for i, kx in enumerate((-3.5, 3.0)):
        b.add("body", "knob_a%d" % i, [kx, 2.0, -3.2], [0.7, 0.7, 0.3], "knob")
        b.add("body", "knob_b%d" % i, [kx, 4.4, -3.2], [0.7, 0.7, 0.3], "knob")
    b.add("body", "mirror_frame", [-4, 6, 2], [8, 10, 0.8], "frame")
    b.add("body", "mirror_glass", [-3.4, 6.6, 1.55], [6.8, 8.8, 0.3], "mirror", face_cells={"north": "mirror"})
    b.add("body", "perfume1", [-5, 6, -1], [1, 1.6, 1], "accent")
    b.add("body", "perfume2", [4, 6, -0.6], [0.8, 1.3, 0.8], "knob")
    # mirror bulbs (toggled) around the frame
    bulbs = [(-4.4, 7), (-4.4, 11), (-4.4, 14.5), (3.5, 7), (3.5, 11), (3.5, 14.5),
             (-1.5, 15.6), (1.0, 15.6)]
    for i, (bx, by) in enumerate(bulbs):
        b.add("glow", "bulb%d" % i, [bx, by, 1.9], [0.9, 0.9, 0.5], "bulb")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "glow", "parent": sid, "pivot": [0, 11, 2]}], rel, src)
    variant_light_wiring(sid, "action.interact.lights_on", "action.interact.lights_off", 1.0, 1.2)


def build_king_bed():
    sid = "unicorn_king_bed"
    specs = [("shell", (204, 190, 234), "solid"), ("mattress", (190, 214, 245), "solid"),
             ("pillow", (248, 196, 224), "solid"), ("blanket", None, "horn"),
             ("accent", (245, 210, 120), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6504)
    b = Builder(cm)
    # king size: wide (x 24) AND long (z 26)
    b.add("frame", "base", [-12.5, 0, -13], [25, 3, 26], "shell")
    b.add("frame", "mattress", [-12, 3, -12.5], [24, 4, 25], "mattress")
    b.add("frame", "footboard", [-12.5, 3, -13], [25, 5, 1.4], "shell")
    b.add("frame", "headboard", [-12.5, 3, 11.6], [25, 11, 1.4], "shell")
    b.add("frame", "head_accent", [-12, 12, 11.7], [24, 1.5, 1.2], "accent")
    b.add("frame", "pillow_l", [-10.5, 7, 7], [9, 2.5, 5], "pillow")
    b.add("frame", "pillow_r", [1.5, 7, 7], [9, 2.5, 5], "pillow")
    b.add("frame", "blanket", [-12, 7, -12], [24, 1, 17], "blanket")
    b.add("frame", "star_l", [-11, 12.5, 11.8], [1.6, 1.6, 0.6], "accent")
    b.add("frame", "star_r", [9.4, 12.5, 11.8], [1.6, 1.6, 0.6], "accent")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "frame", "parent": sid, "pivot": [0, 0, 0]}], rel, src)
    rideable_wiring(sid, [{"position": [-0.5, 0.55, -0.2], "lock_rider_rotation": 0},
                          {"position": [0.5, 0.55, -0.2], "lock_rider_rotation": 0}], 1.8, 0.7)


def main():
    build_tv()
    build_arcade()
    build_vanity()
    build_king_bed()


if __name__ == "__main__":
    main()
