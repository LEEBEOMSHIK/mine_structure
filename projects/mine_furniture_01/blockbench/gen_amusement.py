"""Amusement-park rides: carousel, ferris wheel, hot-air balloon.

  unicorn_carousel      rideable (4 seats on horses) + always-on y-spin ("spin" bone)
  unicorn_ferris_wheel  variant toggle: wheel spins on/off ("blades" bone, z-axis)
  unicorn_balloon       rideable (1, in the basket) + gentle bob ("bob" bone)

Reuses gen_kids_furniture (Builder/make_atlas/assemble) and gen_room_furniture
(common_components/render_controller/resources/write); ferris wheel reuses
gen_living_furniture.variant_spin_wiring (the "blades" spin-toggle).
"""
import os

from gen_kids_furniture import Builder, assemble, make_atlas
from gen_room_furniture import (BP, RP, common_components, render_controller,
                                resources, write)
from gen_living_furniture import variant_spin_wiring


def rideable_animated_wiring(sid, seats, width, height, anim_name, anim_def,
                             mechanic="rideable_simple"):
    """rideable furniture that also plays one always-on animation (seesaw style)."""
    components = common_components(sid, width, height)
    components["minecraft:rideable"] = {
        "seat_count": len(seats), "family_types": ["player"],
        "interact_text": "action.interact.ride", "seats": seats,
    }
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
            "animations": {anim_name: "animation." + sid + "." + anim_name},
            "scripts": {"animate": [anim_name]},
            "render_controllers": ["controller.render." + sid],
        }},
    })
    write(os.path.join(RP, "render_controllers", sid + ".render_controllers.json"), render_controller(sid))
    write(os.path.join(RP, "animations", sid + ".animation.json"), {
        "format_version": "1.8.0",
        "animations": {"animation." + sid + "." + anim_name: anim_def},
    })
    write(os.path.normpath(os.path.join(BP, "..", "..", "content", "furniture", sid + ".resources.json")),
          resources(sid, mechanic, True))


# ---------------------------------------------------------------- carousel
def build_carousel():
    sid = "unicorn_carousel"
    specs = [("pole", (245, 210, 120), "solid"), ("base", (204, 190, 234), "solid"),
             ("roof", (244, 150, 190), "cone"), ("horse", (255, 250, 252), "solid"),
             ("saddle", (150, 210, 238), "solid"), ("rainbow", None, "horn"),
             ("trim", (150, 230, 200), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6801)
    b = Builder(cm)
    # static base: round-ish platform + centre column
    b.add("base", "platform", [-9, 0, -9], [18, 1.5, 18], "base")
    b.add("base", "platform_top", [-7.5, 1.5, -7.5], [15, 0.7, 15], "trim")
    b.add("base", "column", [-1.5, 1.5, -1.5], [3, 22, 3], "pole")
    # spinning part: striped roof (stacked shrinking boxes) + arms + horses
    b.add("spin", "roof1", [-10, 22, -10], [20, 2, 20], "roof")
    b.add("spin", "roof2", [-8, 24, -8], [16, 2, 16], "roof")
    b.add("spin", "roof3", [-5.5, 26, -5.5], [11, 2.5, 11], "roof")
    b.add("spin", "roof4", [-3, 28.5, -3], [6, 2.5, 6], "roof")
    b.add("spin", "finial", [-1, 31, -1], [2, 2.2, 2], "rainbow")
    positions = [(7, 0), (-7, 0), (0, 7), (0, -7)]
    for i, (hx, hz) in enumerate(positions):
        # support pole from the roof down to the horse
        b.add("spin", "hpole%d" % i, [hx - 0.4, 6, hz - 0.4], [0.8, 17, 0.8], "pole")
        # horse: body + neck + head + horn + 4 legs + saddle (faces +x in local space)
        b.add("spin", "hbody%d" % i, [hx - 3, 5.5, hz - 1.5], [6, 3.5, 3], "horse")
        b.add("spin", "hneck%d" % i, [hx + 1.6, 7.5, hz - 1.2], [2.4, 3.4, 2.4], "horse")
        b.add("spin", "hhead%d" % i, [hx + 3.2, 10, hz - 1.2], [3, 2.4, 2.4], "horse")
        b.add("spin", "hhorn%d" % i, [hx + 4.8, 12, hz - 0.45], [0.9, 2, 0.9], "rainbow")
        for j, (lx, lz) in enumerate(((-2.5, -1.3), (1.8, -1.3), (-2.5, 1.0), (1.8, 1.0))):
            b.add("spin", "hleg%d_%d" % (i, j), [hx + lx, 1.5, hz + lz], [1, 4.2, 1], "horse")
        b.add("spin", "hsaddle%d" % i, [hx - 1.6, 9.0, hz - 1.6], [3, 1, 3.2], "saddle")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "base", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "spin", "parent": sid, "pivot": [0, 0, 0]}], rel, src)
    seats = [{"position": [hx / 16, 0.62, hz / 16], "lock_rider_rotation": 0} for hx, hz in positions]
    spin = {"loop": True, "animation_length": 6.0,
            "bones": {"spin": {"rotation": {"0.0": [0, 0, 0], "6.0": [0, 360, 0]}}}}
    rideable_animated_wiring(sid, seats, 1.4, 2.2, "spin", spin)


# ---------------------------------------------------------------- ferris wheel
def build_ferris():
    sid = "unicorn_ferris_wheel"
    specs = [("frame", (204, 190, 234), "solid"), ("spoke", (245, 210, 120), "solid"),
             ("cabin_a", (244, 150, 190), "solid"), ("cabin_b", (150, 210, 238), "solid"),
             ("cabin_c", (255, 235, 150), "solid"), ("rainbow", None, "horn"),
             ("hub", (150, 230, 200), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6802)
    b = Builder(cm)
    HUB_Y, R = 16.0, 12.0
    # static A-frame legs + base + axle
    b.add("base", "foot", [-11, 0, -2.5], [22, 1.5, 5], "frame")
    b.add("base", "leg_l", [-9, 0, -0.75], [1.6, 17.5, 1.6], "frame", rotation=[0, 0, 20], pivot=[-9, 0, 0])
    b.add("base", "leg_r", [7.4, 0, -0.75], [1.6, 17.5, 1.6], "frame", rotation=[0, 0, -20], pivot=[9, 0, 0])
    b.add("base", "axle", [-3, HUB_Y - 0.9, -1.0], [6, 1.8, 2], "hub")
    # spinning wheel ("blades" bone, z-axis), pivot at the hub
    b.add("blades", "hub", [-2, HUB_Y - 2, -1.5], [4, 4, 3], "hub")
    cabins = ["cabin_a", "cabin_b", "cabin_c"]
    for i in range(8):
        ang = -i * 45
        b.add("blades", "spoke%d" % i, [-0.4, HUB_Y, -0.4], [0.8, R, 0.8], "spoke",
              rotation=[0, 0, ang], pivot=[0, HUB_Y, 0])
        b.add("blades", "cabin%d" % i, [-2, HUB_Y + R - 1.0, -1.6], [4, 3, 3.2], cabins[i % 3],
              rotation=[0, 0, ang], pivot=[0, HUB_Y, 0])
        b.add("blades", "rim%d" % i, [-1.2, HUB_Y + R - 0.6, -0.6], [2.4, 1, 1.2], "frame",
              rotation=[0, 0, ang - 22.5], pivot=[0, HUB_Y, 0])
    b.add("blades", "star", [-1, HUB_Y - 1, 1.5], [2, 2, 0.8], "rainbow")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "base", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "blades", "parent": sid, "pivot": [0, HUB_Y, 0]}], rel, src)
    variant_spin_wiring(sid, "action.interact.spin_on", "action.interact.spin_off", 1.6, 2.0)


# ---------------------------------------------------------------- hot-air balloon
def build_balloon():
    sid = "unicorn_balloon"
    specs = [("balloon_a", (244, 150, 190), "solid"), ("balloon_b", (150, 210, 238), "solid"),
             ("balloon_c", (255, 235, 150), "solid"), ("basket", (196, 150, 100), "solid"),
             ("rope", (245, 210, 120), "solid"), ("rainbow", None, "horn")]
    rel, src, cm = make_atlas(sid, specs, 6803)
    b = Builder(cm)
    # everything floats together on the "bob" bone
    # balloon envelope: stacked boxes forming a rounded teardrop, striped colours
    layers = [
        (-7, 14, 14, "balloon_a"), (-8, 17, 16, "balloon_b"), (-8, 21, 16, "balloon_c"),
        (-7, 25, 14, "balloon_a"), (-5.5, 28, 11, "balloon_b"), (-3.5, 30.5, 7, "balloon_c"),
    ]
    for i, (x0, y0, w, color) in enumerate(layers):
        b.add("bob", "env%d" % i, [x0, y0, x0], [w, (layers[i + 1][1] - y0) if i + 1 < len(layers) else 2.5, w], color)
    b.add("bob", "neck", [-2, 11.5, -2], [4, 3, 4], "balloon_a")
    b.add("bob", "finial", [-1, 32.5, -1], [2, 2, 2], "rainbow")
    # ropes from the envelope neck down to the basket
    for rx, rz in ((-3.2, -3.2), (2.4, -3.2), (-3.2, 2.4), (2.4, 2.4)):
        b.add("bob", "rope_%d_%d" % (int(rx), int(rz)), [rx, 5, rz], [0.6, 7, 0.6], "rope")
    # basket
    b.add("bob", "basket", [-4, 0, -4], [8, 5, 8], "basket")
    b.add("bob", "basket_rim", [-4.3, 4.6, -4.3], [8.6, 0.8, 8.6], "rope")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "bob", "parent": sid, "pivot": [0, 0, 0]}], rel, src)
    seats = [{"position": [0, 0.35, 0], "lock_rider_rotation": 0}]
    bob = {"loop": True, "animation_length": 4.0,
           "bones": {"bob": {"position": {"0.0": [0, 0, 0], "2.0": [0, 1.2, 0], "4.0": [0, 0, 0]}}}}
    rideable_animated_wiring(sid, seats, 1.0, 2.2, "bob", bob)


def main():
    build_carousel()
    build_ferris()
    build_balloon()


if __name__ == "__main__":
    main()
