"""Garden / outdoor batch 2: fountain, mailbox, birdcage, bench, parasol table,
campfire, camping tent, garden arch. Pastel unicorn theme.

  fountain / campfire   variant_light (water / flames glow on-off)
  bench / tent          rideable (sit / sit inside)
  mailbox / birdcage / parasol_table / garden_arch   static decor

Reuses gen_kids_furniture (Builder/make_atlas/assemble), gen_room_furniture
(variant_light_wiring/rideable_wiring/write), gen_living_furniture (script_entity).
"""
from gen_kids_furniture import Builder, assemble, make_atlas
from gen_room_furniture import variant_light_wiring, rideable_wiring
from gen_living_furniture import script_entity


def static_decor(sid, b, bones, rel, src, w, h):
    assemble(sid, b, bones, rel, src)
    script_entity(sid, "static", w, h)


# ---------------------------------------------------------------- fountain
def build_fountain():
    sid = "unicorn_fountain"
    specs = [("stone", (210, 198, 238), "solid"), ("water", (150, 212, 246), "glow"),
             ("rim", (182, 232, 212), "solid"), ("top", (244, 200, 230), "solid"),
             ("star", None, "horn")]
    rel, src, cm = make_atlas(sid, specs, 7101)
    b = Builder(cm)
    b.add("body", "pool", [-8, 0, -8], [16, 2.5, 16], "stone")
    b.add("body", "pool_rim", [-8, 2.5, -8], [16, 0.8, 16], "rim")
    b.add("body", "tier2", [-5, 3, -5], [10, 2, 10], "stone")
    b.add("body", "tier2_rim", [-5, 5, -5], [10, 0.6, 10], "rim")
    b.add("body", "pole", [-1.5, 5, -1.5], [3, 5, 3], "stone")
    b.add("body", "topbowl", [-3, 10, -3], [6, 1.5, 6], "top")
    b.add("body", "star", [-1, 14, -1], [2, 2, 0.6], "star")
    b.add("glow", "water_low", [-7, 2.6, -7], [14, 0.6, 14], "water")
    b.add("glow", "water_mid", [-4, 5.1, -4], [8, 0.5, 8], "water")
    b.add("glow", "spout", [-1, 11.5, -1], [2, 2.5, 2], "water")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "glow", "parent": sid, "pivot": [0, 6, 0]}], rel, src)
    variant_light_wiring(sid, "action.interact.water_on", "action.interact.water_off", 1.2, 1.0)


# ---------------------------------------------------------------- mailbox
def build_mailbox():
    sid = "unicorn_mailbox"
    specs = [("post", (200, 150, 110), "solid"), ("box", (248, 196, 224), "solid"),
             ("flag", (240, 120, 150), "solid"), ("trim", (182, 232, 212), "solid"),
             ("heart", None, "horn")]
    rel, src, cm = make_atlas(sid, specs, 7102)
    b = Builder(cm)
    b.add("body", "post", [-1, 0, -1], [2, 9, 2], "post")
    b.add("body", "box", [-3, 9, -3], [6, 5, 7], "box")
    b.add("body", "roof", [-3.4, 13.5, -3.4], [6.8, 1, 7.8], "trim")
    b.add("body", "door", [-2.4, 9.6, -3.4], [4.8, 3.8, 0.4], "trim")
    b.add("body", "heart", [-1, 10.5, -3.6], [2, 1.8, 0.5], "heart")
    b.add("body", "flagpole", [3, 10, -1], [0.6, 3, 0.6], "flag")
    b.add("body", "flag", [3.4, 11.5, -1], [1.5, 1.5, 0.4], "flag")
    static_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                          {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src, 0.6, 1.4)


# ---------------------------------------------------------------- birdcage
def build_birdcage():
    sid = "unicorn_birdcage"
    specs = [("bar", (245, 210, 120), "solid"), ("base", (210, 198, 238), "solid"),
             ("bird", (255, 200, 215), "solid"), ("wing", (180, 220, 250), "solid"),
             ("star", None, "horn")]
    rel, src, cm = make_atlas(sid, specs, 7103)
    b = Builder(cm)
    b.add("body", "base", [-4, 0, -4], [8, 1.5, 8], "base")
    b.add("body", "floor", [-3.5, 1.5, -3.5], [7, 0.6, 7], "bar")
    for i, (cx, cz) in enumerate(((-3.4, -3.4), (2.8, -3.4), (-3.4, 2.8), (2.8, 2.8))):
        b.add("body", "bar%d" % i, [cx, 2, cz], [0.6, 12, 0.6], "bar")
    b.add("body", "ring_top", [-3.5, 14, -3.5], [7, 0.8, 7], "bar")
    b.add("body", "dome", [-2.5, 14.5, -2.5], [5, 2, 5], "bar")
    b.add("body", "hook", [-0.4, 16.5, -0.4], [0.8, 2, 0.8], "bar")
    # little bird on a perch
    b.add("body", "perch", [-3, 6, -0.3], [6, 0.6, 0.6], "bar")
    b.add("body", "bird", [-1.2, 6.6, -1], [2.4, 2.4, 2], "bird")
    b.add("body", "wing", [-1.6, 7, -0.6], [0.6, 1.4, 1.6], "wing")
    static_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                          {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src, 0.7, 1.8)


# ---------------------------------------------------------------- bench
def build_bench():
    sid = "unicorn_bench"
    specs = [("seat", (248, 196, 224), "solid"), ("frame", (245, 210, 120), "solid"),
             ("back", (204, 190, 234), "solid"), ("heart", None, "horn")]
    rel, src, cm = make_atlas(sid, specs, 7104)
    b = Builder(cm)
    b.add("body", "seat", [-9, 5, -3], [18, 1.5, 6], "seat")
    b.add("body", "back", [-9, 6.5, 2.5], [18, 6, 1], "back")
    for i in range(5):
        b.add("body", "slat%d" % i, [-8 + i * 3.6, 7, 2.4], [1.2, 5, 0.4], "frame")
    b.add("body", "arm_l", [-9.5, 5, -3], [1, 5, 6], "frame")
    b.add("body", "arm_r", [8.5, 5, -3], [1, 5, 6], "frame")
    for i, lx in enumerate((-8.5, 7)):
        b.add("body", "leg%d_f" % i, [lx, 0, -2.5], [1.5, 5, 1.5], "frame")
        b.add("body", "leg%d_b" % i, [lx, 0, 1.5], [1.5, 5, 1.5], "frame")
    b.add("body", "heart", [-1, 9, 3], [2, 1.8, 0.5], "heart")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src)
    rideable_wiring(sid, [{"position": [-0.5, 0.45, -0.05], "lock_rider_rotation": 0},
                          {"position": [0.5, 0.45, -0.05], "lock_rider_rotation": 0}], 1.5, 0.9)


# ---------------------------------------------------------------- parasol table
def build_parasol_table():
    sid = "unicorn_parasol_table"
    specs = [("top", (255, 250, 255), "solid"), ("pole", (245, 210, 120), "solid"),
             ("canopy", (244, 170, 210), "cone"), ("canopy2", (180, 220, 250), "cone"),
             ("trim", (182, 232, 212), "solid")]
    rel, src, cm = make_atlas(sid, specs, 7105)
    b = Builder(cm)
    b.add("body", "top", [-6, 6, -6], [12, 1, 12], "top")
    b.add("body", "top_trim", [-6, 6, -6], [12, 0.4, 12], "trim")
    b.add("body", "pole", [-0.6, 0, -0.6], [1.2, 22, 1.2], "pole")
    b.add("body", "foot", [-2, 0, -2], [4, 1, 4], "trim")
    b.add("body", "canopy1", [-10, 16, -10], [20, 2, 20], "canopy")
    b.add("body", "canopy2", [-7, 18, -7], [14, 2, 14], "canopy2")
    b.add("body", "canopy3", [-4, 20, -4], [8, 2, 8], "canopy")
    b.add("body", "finial", [-1, 22, -1], [2, 1.5, 2], "trim")
    static_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                          {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src, 1.4, 2.2)


# ---------------------------------------------------------------- campfire
def build_campfire():
    sid = "unicorn_campfire"
    specs = [("stone", (200, 192, 210), "solid"), ("log", (196, 150, 110), "solid"),
             ("flame", (255, 180, 150), "glow"), ("flame2", (255, 232, 150), "glow")]
    rel, src, cm = make_atlas(sid, specs, 7106)
    b = Builder(cm)
    # ring of stones
    for i, (cx, cz) in enumerate(((-5, -2), (3, -2), (-5, 2), (3, 2), (-1, -5), (-1, 3))):
        b.add("body", "stone%d" % i, [cx, 0, cz], [2, 1.5, 2], "stone")
    b.add("body", "log1", [-4, 0.5, -1], [8, 1.2, 1.2], "log", rotation=[0, 20, 0], pivot=[0, 0, 0])
    b.add("body", "log2", [-4, 0.5, -1], [8, 1.2, 1.2], "log", rotation=[0, -20, 0], pivot=[0, 0, 0])
    b.add("glow", "flame_b", [-2.5, 1.5, -2.5], [5, 3, 5], "flame")
    b.add("glow", "flame_t", [-1.5, 4, -1.5], [3, 2.5, 3], "flame2")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "glow", "parent": sid, "pivot": [0, 1.5, 0]}], rel, src)
    variant_light_wiring(sid, "action.interact.light_fire", "action.interact.put_out", 0.9, 0.5)


# ---------------------------------------------------------------- camping tent
def build_tent():
    sid = "unicorn_tent"
    specs = [("tent", (180, 220, 250), "solid"), ("tent2", (244, 170, 210), "solid"),
             ("pole", (245, 210, 120), "solid"), ("door", (120, 90, 140), "solid"),
             ("flag", None, "horn")]
    rel, src, cm = make_atlas(sid, specs, 7107)
    b = Builder(cm)
    # A-frame (∧) built as stepped panels (no rotation): two sloped sides that
    # narrow toward the ridge, a stepped triangular back wall, an open front.
    steps = [(0.0, 7.0), (2.6, 5.2), (5.2, 3.4), (7.8, 1.6)]
    for i, (y, xo) in enumerate(steps):
        b.add("body", "roof_l%d" % i, [-xo - 2, y, -8], [2, 2.7, 16], "tent")
        b.add("body", "roof_r%d" % i, [xo, y, -8], [2, 2.7, 16], "tent2")
        b.add("body", "back%d" % i, [-xo - 2, y, 7], [(xo + 2) * 2, 2.7, 1], "tent")
    b.add("body", "ridge", [-1, 10.4, -8], [2, 1.6, 16], "pole")
    b.add("body", "back_top", [-1, 10.4, 7], [2, 1.6, 1], "tent")
    # front doorway posts + flag at the ridge
    b.add("body", "door_l", [-3, 0, -8.3], [0.9, 8, 0.9], "door")
    b.add("body", "door_r", [2.1, 0, -8.3], [0.9, 8, 0.9], "door")
    b.add("body", "pole", [-0.4, 11, -8.2], [0.8, 4, 0.8], "pole")
    b.add("body", "flag", [0.4, 12, -8.2], [3, 2, 0.4], "flag")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src)
    rideable_wiring(sid, [{"position": [0, 0.2, 0.5], "lock_rider_rotation": 0}], 1.6, 1.6)


# ---------------------------------------------------------------- garden arch
def build_garden_arch():
    sid = "unicorn_garden_arch"
    specs = [("frame", (255, 250, 255), "solid"), ("vine", (150, 220, 160), "solid"),
             ("flower", (255, 180, 210), "solid"), ("flower2", (255, 232, 150), "solid"),
             ("trim", (182, 232, 212), "solid")]
    rel, src, cm = make_atlas(sid, specs, 7108)
    b = Builder(cm)
    b.add("body", "post_l", [-8, 0, -1], [1.5, 18, 1.5], "frame")
    b.add("body", "post_r", [6.5, 0, -1], [1.5, 18, 1.5], "frame")
    b.add("body", "top", [-8, 18, -1], [16, 1.5, 1.5], "frame")
    # arch curve (two angled segments)
    b.add("body", "arch_l", [-8, 16.5, -1], [4, 1.5, 1.5], "frame", rotation=[0, 0, 28], pivot=[-6.5, 18, 0])
    b.add("body", "arch_r", [4, 16.5, -1], [4, 1.5, 1.5], "frame", rotation=[0, 0, -28], pivot=[5.5, 18, 0])
    # vines + flowers climbing the posts and top
    for i, y in enumerate((2, 6, 10, 14)):
        b.add("body", "vine_l%d" % i, [-8.3, y, -1.2], [2, 2, 2], "vine")
        b.add("body", "vine_r%d" % i, [6.3, y, -1.2], [2, 2, 2], "vine")
    for i, x in enumerate((-6, -2, 2, 5)):
        b.add("body", "ftop%d" % i, [x, 18.5, -1.2], [2, 2, 2], "vine")
    b.add("body", "fl1", [-8.4, 8, -1.4], [1.4, 1.4, 1.4], "flower")
    b.add("body", "fl2", [6.6, 12, -1.4], [1.4, 1.4, 1.4], "flower2")
    b.add("body", "fl3", [-2, 19, -1.4], [1.4, 1.4, 1.4], "flower")
    static_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                          {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src, 1.4, 2.2)


def main():
    build_fountain()
    build_mailbox()
    build_birdcage()
    build_bench()
    build_parasol_table()
    build_campfire()
    build_tent()
    build_garden_arch()


if __name__ == "__main__":
    main()
