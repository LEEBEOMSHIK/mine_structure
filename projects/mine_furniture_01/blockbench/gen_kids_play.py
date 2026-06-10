"""Play batch 5: pool, sandbox, teacup ride, ball pit, jungle gym, clock tower.
Pastel unicorn theme. (Distinct from gen_playground.py = swing/slide/seesaw.)

  unicorn_pool          variant_fill  (water fills the glow bone)
  unicorn_teacup        variant_spin  (cups spin around Y on the blades bone)
  unicorn_clock_tower   variant_spin  (hands sweep around Z on the blades bone)
  unicorn_sandbox       static
  unicorn_ballpit       static
  unicorn_junglegym     static

Reuses gen_kids_furniture (Builder/make_atlas/assemble), gen_room_furniture
(common_components/resources/render_controller/write/interact),
gen_bath_kitchen (variant_fill_wiring), gen_living_furniture
(script_entity, variant_spin_wiring).
"""
import os

from gen_kids_furniture import Builder, assemble, make_atlas
from gen_room_furniture import (BP, RP, common_components, interact,
                                render_controller, resources, write)
from gen_bath_kitchen import variant_fill_wiring
from gen_living_furniture import script_entity, variant_spin_wiring

RAINBOW = [(255, 150, 170), (255, 190, 140), (255, 232, 150), (170, 222, 170),
           (150, 200, 245), (200, 165, 240)]


def static_decor(sid, b, bones, rel, src, w, h):
    assemble(sid, b, bones, rel, src)
    script_entity(sid, "static", w, h)


def fill_decor(sid, b, bones, rel, src, w, h):
    assemble(sid, b, bones, rel, src)
    variant_fill_wiring(sid, "action.interact.light_on", "action.interact.light_off", w, h)


def spin_y_wiring(sid, on_text, off_text, width, height):
    """Like variant_spin_wiring but rotates the blades bone around Y (flat spin,
    for ride platforms) instead of Z. Registered as the 'variant_spin' mechanic."""
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
            "animation." + sid + ".on": {"loop": True, "animation_length": 2.5,
                                         "bones": {"blades": {"rotation": {"0.0": [0, 0, 0], "2.5": [0, 360, 0]}}}},
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


# ------------------------------------------------------------------------ pool
def build_pool():
    sid = "unicorn_pool"
    specs = [("rim", (204, 190, 234), "solid"), ("wall", (235, 232, 248), "solid"),
             ("floor", (255, 250, 255), "solid"), ("water", (74, 165, 226), "water"),
             ("ladder", (245, 210, 120), "solid"), ("ring", (247, 167, 200), "solid")]
    rel, src, cm = make_atlas(sid, specs, 7401)
    b = Builder(cm)
    b.add("body", "floor", [-9, 0, -9], [18, 1, 18], "floor")
    for (x, z, w, d) in ((-9, -9, 18, 1.2), (-9, 7.8, 18, 1.2), (-9, -9, 1.2, 18), (7.8, -9, 1.2, 18)):
        b.add("body", "wall_%d_%d" % (x, z), [x, 1, z], [w, 5, d], "wall")
    # coping = a frame around the rim (open middle so the water surface shows)
    for (x, z, w, d) in ((-9.6, -9.6, 19.2, 1.8), (-9.6, 7.8, 19.2, 1.8),
                         (-9.6, -7.8, 1.8, 15.6), (7.8, -7.8, 1.8, 15.6)):
        b.add("body", "rim_%d_%d" % (int(x), int(z)), [x, 5.6, z], [w, 1, d], "rim")
    # ladder on +x side
    b.add("body", "ladder_l", [8.4, 1, -2], [0.6, 7, 0.6], "ladder")
    b.add("body", "ladder_r", [8.4, 1, 1.4], [0.6, 7, 0.6], "ladder")
    for ry in (2.5, 4.5):
        b.add("body", "rung%d" % int(ry), [8.4, ry, -2], [0.6, 0.6, 3.4], "ladder")
    # water (recessed below the coping) + a float ring on the glow bone so they rise as it fills
    b.add("glow", "water", [-7.8, 1, -7.8], [15.6, 3.8, 15.6], "water")
    b.add("glow", "ring1", [-6, 4.2, -2], [4, 0.8, 4], "ring")
    b.add("glow", "ring_hole", [-5, 4.25, -1], [2, 0.8, 2], "water")
    fill_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                        {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                        {"name": "glow", "parent": sid, "pivot": [0, 1, 0]}], rel, src, 1.6, 0.7)


# --------------------------------------------------------------------- sandbox
def build_sandbox():
    sid = "unicorn_sandbox"
    specs = [("post", (247, 167, 200), "solid"), ("rail", (204, 190, 234), "solid"),
             ("sand", (245, 224, 170), "solid"), ("bucket", (169, 216, 255), "solid"),
             ("scoop", (185, 242, 208), "solid"), ("handle", (245, 210, 120), "solid")]
    rel, src, cm = make_atlas(sid, specs, 7402)
    b = Builder(cm)
    for (cx, cz) in ((-7, -7), (5, -7), (-7, 5), (5, 5)):
        b.add("body", "post_%d_%d" % (cx, cz), [cx, 0, cz], [2, 4, 2], "post")
    for (x, z, w, d) in ((-7, -7, 14, 1.2), (-7, 5.8, 14, 1.2), (-7, -7, 1.2, 14), (5.8, -7, 1.2, 14)):
        b.add("body", "rail_%d_%d" % (x, z), [x, 2.4, z], [w, 1.2, d], "rail")
    # sand fill + a stepped sandcastle
    b.add("body", "sand", [-6, 0, -6], [12, 2.6, 12], "sand")
    b.add("body", "castle1", [-3, 2.6, -3], [6, 2, 6], "sand")
    b.add("body", "castle2", [-2, 4.6, -2], [4, 1.6, 4], "sand")
    for (cx, cz) in ((-3, -3), (1.5, -3), (-3, 1.5), (1.5, 1.5)):
        b.add("body", "turret_%d_%d" % (int(cx), int(cz)), [cx, 4.6, cz], [1.5, 2.4, 1.5], "sand")
    # bucket + shovel resting on the rail
    b.add("body", "bucket", [3.5, 3.6, -5], [3, 3, 3], "bucket")
    b.add("body", "shovel_h", [-6, 3.6, 4], [0.6, 6, 0.6], "handle", rotation=[20, 0, 0], pivot=[-5.7, 3.6, 4.3])
    b.add("body", "shovel_s", [-6.6, 3.4, 6], [1.8, 0.6, 2.4], "scoop", rotation=[20, 0, 0], pivot=[-5.7, 3.6, 4.3])
    static_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                          {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src, 1.4, 0.6)


# ---------------------------------------------------------------------- teacup
def build_teacup():
    sid = "unicorn_teacup"
    specs = [("base", (204, 190, 234), "solid"), ("hub", (245, 210, 120), "solid"),
             ("cup1", (247, 167, 200), "solid"), ("cup2", (185, 242, 208), "solid"),
             ("cup3", (169, 216, 255), "solid"), ("saucer", (255, 250, 255), "solid")]
    rel, src, cm = make_atlas(sid, specs, 7403)
    b = Builder(cm)
    # static base platform
    b.add("body", "base", [-8, 0, -8], [16, 1.5, 16], "base")
    b.add("body", "skirt", [-7, -0.5, -7], [14, 0.6, 14], "saucer")
    # spinning deck + 3 teacups around the centre (blades bone)
    b.add("blades", "deck", [-7, 1.5, -7], [14, 0.8, 14], "base")
    b.add("blades", "hub", [-1.5, 2.3, -1.5], [3, 3, 3], "hub")
    cups = [(0, -5, "cup1"), (4.3, 2.5, "cup2"), (-4.3, 2.5, "cup3")]
    for i, (cx, cz, col) in enumerate(cups):
        b.add("blades", "saucer%d" % i, [cx - 2.5, 2.3, cz - 2.5], [5, 0.6, 5], "saucer")
        b.add("blades", "cup%d" % i, [cx - 2, 2.9, cz - 2], [4, 3, 4], col)
        b.add("blades", "lip%d" % i, [cx - 2.2, 5.6, cz - 2.2], [4.4, 0.6, 4.4], "saucer")
        hx = cx + (2 if cx >= 0 else -2.6)
        b.add("blades", "handle%d" % i, [hx, 3.4, cz - 0.4], [0.6, 2, 0.8], col)
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "blades", "parent": sid, "pivot": [0, 1.5, 0]}], rel, src)
    spin_y_wiring(sid, "action.interact.light_on", "action.interact.light_off", 1.4, 0.9)


# --------------------------------------------------------------------- ballpit
def build_ballpit():
    sid = "unicorn_ballpit"
    specs = [("pad", (247, 167, 200), "solid"), ("wall", (185, 242, 208), "solid"),
             ("floor", (255, 250, 255), "solid"), ("r0", RAINBOW[0], "solid"),
             ("r1", RAINBOW[2], "solid"), ("r2", RAINBOW[4], "solid"), ("r3", RAINBOW[5], "solid")]
    rel, src, cm = make_atlas(sid, specs, 7404)
    b = Builder(cm)
    b.add("body", "floor", [-9, 0, -9], [18, 1, 18], "floor")
    for (x, z, w, d) in ((-9, -9, 18, 1.4), (-9, 7.6, 18, 1.4), (-9, -9, 1.4, 18), (7.6, -9, 1.4, 18)):
        b.add("body", "wall_%d_%d" % (x, z), [x, 1, z], [w, 5, d], "wall")
    # padded rim = a frame around the edge (open middle so the balls show)
    for (x, z, w, d) in ((-9.6, -9.6, 19.2, 1.8), (-9.6, 7.8, 19.2, 1.8),
                         (-9.6, -7.8, 1.8, 15.6), (7.8, -7.8, 1.8, 15.6)):
        b.add("body", "pad_%d_%d" % (int(x), int(z)), [x, 5.5, z], [w, 1.4, d], "pad")
    # rainbow ball pile mounding up above the rim (staggered heights)
    cols = ["r0", "r1", "r2", "r3"]
    balls = [(-6, 1, -6), (-2, 1, -5), (2, 1, -6), (5, 1, -3), (-6, 1, 0), (-1, 1, 1),
             (4, 1, 2), (-4, 1, 4), (1, 1, 5), (5, 1, 5), (-3, 4, -2), (2, 4, -1),
             (-1, 4, 3), (3.5, 4, 3), (-4, 5.5, -4), (3, 5.5, 4), (-1, 7.5, 0)]
    for i, (bx, by, bz) in enumerate(balls):
        b.add("body", "ball%d" % i, [bx, by, bz], [3, 3, 3], cols[i % 4])
    static_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                          {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src, 1.6, 0.7)


# -------------------------------------------------------------------- junglegym
def build_junglegym():
    sid = "unicorn_junglegym"
    specs = [("bar", (245, 210, 120), "solid"), ("post", (204, 190, 234), "solid"),
             ("rung", (185, 242, 208), "solid"), ("slide", (247, 167, 200), "solid"),
             ("deck", (255, 233, 154), "solid"), ("flag", (169, 216, 255), "solid")]
    rel, src, cm = make_atlas(sid, specs, 7405)
    b = Builder(cm)
    # 4 corner posts of a climbing cube
    corners = [(-8, -5), (5, -5), (-8, 6), (5, 6)]
    for (cx, cz) in corners:
        b.add("body", "post_%d_%d" % (cx, cz), [cx, 0, cz], [1.4, 16, 1.4], "post")
    # top frame rails
    for (x, z, w, d) in ((-8, -5, 14.4, 1.2), (-8, 6, 14.4, 1.2), (-8, -5, 1.2, 12.4), (5, -5, 1.2, 12.4)):
        b.add("body", "toprail_%d_%d" % (x, z), [x, 15, z], [w, 1.2, d], "bar")
    # climbing rungs on the -x face
    for ry in (3, 6, 9, 12):
        b.add("body", "rung%d" % ry, [-8, ry, -5], [1.2, 0.8, 12.4], "rung")
    # platform deck halfway up
    b.add("body", "deck", [-8, 8, -5], [8, 1, 12.4], "deck")
    # slide attached to the deck's +x edge, sloping down to the ground (rotate about
    # the deck-edge pivot so the far +x end drops toward the floor)
    rot, piv = [0, 0, -38], [0, 8.5, 0]
    b.add("body", "slide", [0, 7.7, -3], [13, 0.8, 6], "slide", rotation=rot, pivot=piv)
    b.add("body", "slide_l", [0, 8.5, -3.3], [13, 1.6, 0.4], "slide", rotation=rot, pivot=piv)
    b.add("body", "slide_r", [0, 8.5, 2.9], [13, 1.6, 0.4], "slide", rotation=rot, pivot=piv)
    # flag on top
    b.add("body", "flagpole", [-1.6, 16, 0], [0.6, 4, 0.6], "post")
    b.add("body", "flag", [-1, 17.5, 0.1], [3, 2, 0.3], "flag")
    static_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                          {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src, 1.6, 1.6)


# ------------------------------------------------------------------- clocktower
def build_clock_tower():
    sid = "unicorn_clock_tower"
    specs = [("body", (204, 190, 234), "solid"), ("trim", (247, 167, 200), "solid"),
             ("roof", (247, 167, 200), "cone"), ("face", (255, 250, 255), "solid"),
             ("hand", (245, 210, 120), "solid"), ("star", None, "horn")]
    rel, src, cm = make_atlas(sid, specs, 7406)
    b = Builder(cm)
    FACE_Y, FACE_Z = 19, -4.4  # face front protrudes from the shaft front (z=-4)
    b.add("body", "base", [-5, 0, -5], [10, 2, 10], "trim")
    b.add("body", "shaft", [-4, 2, -4], [8, 22, 8], "body")
    b.add("body", "belt", [-4.4, 11, -4.4], [8.8, 1.2, 8.8], "trim")
    b.add("body", "head", [-4.6, 24, -4.6], [9.2, 1.2, 9.2], "trim")
    # pointed (stepped) pyramid roof + finial
    b.add("body", "roof1", [-5, 25, -5], [10, 2, 10], "roof")
    b.add("body", "roof2", [-3.5, 27, -3.5], [7, 2, 7], "roof")
    b.add("body", "roof3", [-2, 29, -2], [4, 2, 4], "roof")
    b.add("body", "star", [-1.2, 31, -1.2], [2.4, 2.4, 2.4], "star")
    # clock face on the -z front: pink rim frames a white dial that sits proud of it
    b.add("body", "facerim", [-4.6, FACE_Y - 4.6, FACE_Z], [9.2, 9.2, 0.4], "trim")
    b.add("body", "face", [-4.2, FACE_Y - 4.2, FACE_Z - 0.4], [8.4, 8.4, 0.6], "face")
    for (mx, my) in ((-0.4, 3.2), (-0.4, -3.9), (3.2, -0.4), (-3.9, -0.4)):
        b.add("body", "mark_%d_%d" % (int(mx * 10), int(my * 10)), [mx, FACE_Y + my, FACE_Z - 0.7],
              [0.8, 0.8, 0.4], "hand")
    # rotating hands (blades bone, spin around Z on the face plane)
    b.add("blades", "hand_h", [-0.4, FACE_Y, FACE_Z - 0.9], [0.8, 3, 0.5], "hand")
    b.add("blades", "hand_m", [-0.3, FACE_Y, FACE_Z - 1.0], [0.6, 4, 0.5], "hand")
    b.add("blades", "pin", [-0.6, FACE_Y - 0.6, FACE_Z - 1.1], [1.2, 1.2, 0.5], "trim")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "blades", "parent": sid, "pivot": [0, FACE_Y, FACE_Z]}], rel, src)
    variant_spin_wiring(sid, "action.interact.light_on", "action.interact.light_off", 0.9, 2.0)


def main():
    build_pool()
    build_sandbox()
    build_teacup()
    build_ballpit()
    build_junglegym()
    build_clock_tower()


if __name__ == "__main__":
    main()
