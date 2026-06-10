"""Party / decoration batch 4: birthday cake, balloon bunch, garland, chandelier,
wall sconce, standing lantern. Pastel unicorn theme.

  birthday_cake / chandelier / wall_sconce / standing_lantern   variant_light (flame/light glow)
  balloon_bunch / garland                                       static decor

Reuses gen_kids_furniture (Builder/make_atlas/assemble), gen_room_furniture
(variant_light_wiring/write), gen_living_furniture (script_entity).
"""
import math

from gen_kids_furniture import Builder, assemble, make_atlas
from gen_room_furniture import variant_light_wiring
from gen_living_furniture import script_entity

RAINBOW = [(255, 160, 178), (255, 200, 150), (255, 240, 158), (168, 226, 168), (150, 202, 246), (202, 166, 240)]


def static_decor(sid, b, bones, rel, src, w, h):
    assemble(sid, b, bones, rel, src)
    script_entity(sid, "static", w, h)


def light_decor(sid, b, bones, rel, src, w, h):
    assemble(sid, b, bones, rel, src)
    variant_light_wiring(sid, "action.interact.light_on", "action.interact.light_off", w, h)


# ---------------------------------------------------------------- birthday cake
def build_birthday_cake():
    sid = "unicorn_birthday_cake"
    specs = [("sponge", (248, 220, 200), "solid"), ("cream", (255, 236, 246), "solid"),
             ("cream2", (190, 235, 250), "solid"), ("candle", (255, 200, 150), "solid"),
             ("flame", (255, 232, 150), "glow"), ("berry", (240, 120, 150), "solid"),
             ("plate", (255, 250, 255), "solid")]
    rel, src, cm = make_atlas(sid, specs, 7301)
    b = Builder(cm)
    b.add("body", "plate", [-8, 0, -8], [16, 0.8, 16], "plate")
    b.add("body", "tier1", [-7, 0.8, -7], [14, 5, 14], "sponge")
    b.add("body", "drip1", [-7.2, 5, -7.2], [14.4, 1.2, 14.4], "cream")
    b.add("body", "tier2", [-4.5, 6, -4.5], [9, 4, 9], "sponge")
    b.add("body", "drip2", [-4.7, 9.2, -4.7], [9.4, 1.2, 9.4], "cream2")
    for i, (cx, cz) in enumerate(((-5.5, -5.5), (3.5, -5.5), (-5.5, 3.5), (3.5, 3.5))):
        b.add("body", "berry%d" % i, [cx, 5.2, cz], [1.6, 1.6, 1.6], "berry")
    for i, (cx, cz) in enumerate(((-3, -3), (1.5, -3), (-3, 1.5), (1.5, 1.5), (-0.75, -0.75))):
        b.add("body", "candle%d" % i, [cx, 10.4, cz], [0.8, 3, 0.8], "candle")
        b.add("glow", "flame%d" % i, [cx - 0.1, 13.4, cz - 0.1], [1, 1.6, 1], "flame")
    light_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                         {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                         {"name": "glow", "parent": sid, "pivot": [0, 11, 0]}], rel, src, 1.0, 1.0)


# ---------------------------------------------------------------- balloon bunch
def build_balloon_bunch():
    sid = "unicorn_balloon_bunch"
    specs = [("b1", (255, 158, 188), "solid"), ("b2", (170, 215, 250), "solid"),
             ("b3", (255, 236, 150), "solid"), ("b4", (200, 170, 240), "solid"),
             ("string", (245, 210, 120), "solid"), ("weight", (204, 190, 234), "solid")]
    rel, src, cm = make_atlas(sid, specs, 7302)
    b = Builder(cm)
    b.add("body", "weight", [-2, 0, -2], [4, 3, 4], "weight")
    b.add("body", "bow", [-1.2, 3, -1.2], [2.4, 1.5, 2.4], "b1")
    balloons = [(-4, 13, -2, "b1"), (1.5, 15, -1, "b2"), (-2, 17, 1.5, "b3"), (3, 12, 1, "b4")]
    for i, (bx, by, bz, col) in enumerate(balloons):
        b.add("body", "bln%d" % i, [bx, by, bz], [5, 6, 5], col)
        b.add("body", "knot%d" % i, [bx + 1.8, by - 1, bz + 1.8], [1, 1, 1], col)
        # string from the weight up to the balloon (thin pole)
        b.add("body", "str%d" % i, [bx + 2, 3.5, bz + 2], [0.4, by - 3, 0.4], "string")
    static_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                          {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src, 0.9, 2.2)


# ---------------------------------------------------------------- garland
def build_garland():
    sid = "unicorn_garland"
    specs = [("rope", (200, 150, 110), "solid"), ("f0", RAINBOW[0], "solid"),
             ("f1", RAINBOW[1], "solid"), ("f2", RAINBOW[2], "solid"),
             ("f3", RAINBOW[3], "solid"), ("f4", RAINBOW[4], "solid"), ("f5", RAINBOW[5], "solid")]
    rel, src, cm = make_atlas(sid, specs, 7303)
    b = Builder(cm)
    b.add("body", "rope", [-11, 14, -0.3], [22, 0.6, 0.6], "rope")
    # triangular pennants hanging from the rope (pointed down via rotated thin cubes)
    cols = ["f0", "f1", "f2", "f3", "f4", "f5", "f0", "f1"]
    for i, c in enumerate(cols):
        x = -10 + i * 2.6
        b.add("body", "flag%d" % i, [x, 9.5, -0.35], [2.2, 4.5, 0.3], c)
        b.add("body", "tip%d" % i, [x + 0.6, 8, -0.35], [1, 1.5, 0.3], c, rotation=[0, 0, 45], pivot=[x + 1.1, 9.5, 0])
    static_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                          {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src, 1.6, 0.4)


# ---------------------------------------------------------------- chandelier
def build_chandelier():
    sid = "unicorn_chandelier"
    specs = [("metal", (245, 210, 120), "solid"), ("crystal", (200, 235, 250), "solid"),
             ("candle", (255, 236, 246), "solid"), ("flame", (255, 232, 150), "glow"),
             ("gem", (244, 170, 210), "solid")]
    rel, src, cm = make_atlas(sid, specs, 7304)
    b = Builder(cm)
    b.add("body", "chain", [-0.4, 18, -0.4], [0.8, 6, 0.8], "metal")
    b.add("body", "hub", [-2, 15, -2], [4, 3, 4], "metal")
    b.add("body", "gem", [-1, 13.5, -1], [2, 2, 2], "gem")
    # 4 arms with candles + crystals
    for i in range(4):
        ang = i * 90
        b.add("body", "arm%d" % i, [-0.6, 15.5, -0.6], [7, 0.8, 1.2], "metal",
              rotation=[0, ang, 0], pivot=[0, 16, 0])
        b.add("body", "cup%d" % i, [4.5, 15.5, -0.8], [1.6, 1, 1.6], "metal",
              rotation=[0, ang, 0], pivot=[0, 16, 0])
        b.add("body", "candle%d" % i, [4.8, 16.5, -0.5], [1, 2, 1], "candle",
              rotation=[0, ang, 0], pivot=[0, 16, 0])
        b.add("glow", "flame%d" % i, [4.8, 18.5, -0.5], [1, 1.5, 1], "flame",
              rotation=[0, ang, 0], pivot=[0, 16, 0])
        b.add("body", "crystal%d" % i, [4.6, 13.5, -0.6], [1.2, 2, 1.2], "crystal",
              rotation=[0, ang, 0], pivot=[0, 16, 0])
    light_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                         {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                         {"name": "glow", "parent": sid, "pivot": [0, 16, 0]}], rel, src, 1.4, 1.5)


# ---------------------------------------------------------------- wall sconce
def build_wall_sconce():
    sid = "unicorn_wall_sconce"
    specs = [("plate", (204, 190, 234), "solid"), ("arm", (245, 210, 120), "solid"),
             ("candle", (255, 236, 246), "solid"), ("flame", (255, 232, 150), "glow"),
             ("heart", None, "horn")]
    rel, src, cm = make_atlas(sid, specs, 7305)
    b = Builder(cm)
    b.add("body", "plate", [-2.5, 0, 6.5], [5, 9, 1], "plate")
    b.add("body", "heart", [-1, 7, 6], [2, 1.8, 0.6], "heart")
    b.add("body", "arm", [-0.6, 2, 1], [1.2, 1.2, 6], "arm")
    b.add("body", "cup", [-1.5, 3, -0.5], [3, 1, 3], "arm")
    b.add("body", "candle", [-1, 4, 0], [2, 3, 2], "candle")
    b.add("glow", "flame", [-1, 7, 0], [2, 2, 2], "flame")
    light_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                         {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                         {"name": "glow", "parent": sid, "pivot": [0, 7, 0]}], rel, src, 0.7, 1.0)


# ---------------------------------------------------------------- standing lantern
def build_standing_lantern():
    sid = "unicorn_standing_lantern"
    specs = [("pole", (245, 210, 120), "solid"), ("base", (204, 190, 234), "solid"),
             ("cage", (230, 224, 240), "solid"), ("glass", (255, 244, 200), "glow"),
             ("cap", (244, 170, 210), "cone"), ("star", None, "horn")]
    rel, src, cm = make_atlas(sid, specs, 7306)
    b = Builder(cm)
    b.add("body", "base", [-3, 0, -3], [6, 1.5, 6], "base")
    b.add("body", "pole", [-0.6, 1.5, -0.6], [1.2, 16, 1.2], "pole")
    b.add("body", "hook", [-0.6, 17.5, -0.6], [1.2, 1, 4], "pole")
    b.add("body", "lantern_top", [-2.5, 13, -2.5], [5, 1, 5], "cap")
    for i, (cx, cz) in enumerate(((-2.4, -2.4), (1.4, -2.4), (-2.4, 1.4), (1.4, 1.4))):
        b.add("body", "post%d" % i, [cx, 8, cz], [1, 5, 1], "cage")
    b.add("body", "lantern_bot", [-2.5, 7.5, -2.5], [5, 1, 5], "cage")
    b.add("body", "roof", [-3, 14, -3], [6, 2, 6], "cap")
    b.add("body", "star", [-1, 16, -1], [2, 2, 2], "star")
    b.add("glow", "glass", [-2, 8.5, -2], [4, 4.5, 4], "glass")
    light_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                         {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                         {"name": "glow", "parent": sid, "pivot": [0, 10, 0]}], rel, src, 0.7, 1.8)


def main():
    build_birthday_cake()
    build_balloon_bunch()
    build_garland()
    build_chandelier()
    build_wall_sconce()
    build_standing_lantern()


if __name__ == "__main__":
    main()
