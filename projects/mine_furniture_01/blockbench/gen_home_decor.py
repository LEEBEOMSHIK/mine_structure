"""Home decor batch 1: coffee table, rug, wall clock, picture frame, potted plant,
floor lamp, dresser, nightstand. Pastel unicorn theme.

  static decor      coffee_table / rug / wall_clock / picture_frame / potted_plant / nightstand
  floor_lamp        variant_light (glow shade on/off)
  dresser           Script storage (store/retrieve)

Reuses gen_kids_furniture (Builder/make_atlas/assemble), gen_room_furniture
(variant_light_wiring/write), gen_living_furniture (script_entity).
"""
from gen_kids_furniture import Builder, assemble, make_atlas
from gen_room_furniture import variant_light_wiring
from gen_living_furniture import script_entity


def static_decor(sid, b, bones, rel, src, w, h):
    assemble(sid, b, bones, rel, src)
    script_entity(sid, "static", w, h)


# ---------------------------------------------------------------- coffee table
def build_coffee_table():
    sid = "unicorn_coffee_table"
    specs = [("top", (244, 200, 230), "solid"), ("leg", (245, 210, 120), "solid"),
             ("shelf", (204, 190, 234), "solid"), ("heart", None, "horn")]
    rel, src, cm = make_atlas(sid, specs, 7001)
    b = Builder(cm)
    b.add("body", "top", [-7, 6, -4], [14, 1.5, 8], "top")
    for i, (lx, lz) in enumerate(((-6.5, -3.5), (5, -3.5), (-6.5, 2.5), (5, 2.5))):
        b.add("body", "leg%d" % i, [lx, 0, lz], [1.5, 6, 1.5], "leg")
    b.add("body", "shelf", [-6, 2.5, -3.5], [12, 0.8, 7], "shelf")
    b.add("body", "heart", [-1, 7.5, -0.4], [2, 2, 0.6], "heart")
    static_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                          {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src, 1.0, 0.6)


# ---------------------------------------------------------------- rug
def build_rug():
    sid = "unicorn_rug"
    specs = [("rug", (248, 196, 224), "solid"), ("ring", (180, 220, 250), "solid"),
             ("core", (255, 235, 180), "solid"), ("star", None, "horn")]
    rel, src, cm = make_atlas(sid, specs, 7002)
    b = Builder(cm)
    b.add("body", "rug", [-8, 0, -6], [16, 0.4, 12], "rug")
    b.add("body", "ring", [-5, 0.4, -4], [10, 0.2, 8], "ring")
    b.add("body", "core", [-3, 0.5, -2.5], [6, 0.2, 5], "core")
    b.add("body", "star", [-1, 0.6, -1], [2, 0.2, 2], "star")
    static_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                          {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src, 1.4, 0.2)


# ---------------------------------------------------------------- wall clock
def build_wall_clock():
    sid = "unicorn_wall_clock"
    specs = [("frame", (204, 190, 234), "solid"), ("face", (255, 250, 255), "face"),
             ("hand", (90, 78, 120), "solid"), ("dot", (245, 210, 120), "solid")]
    rel, src, cm = make_atlas(sid, specs, 7003)
    b = Builder(cm)
    b.add("body", "frame", [-5, 2, 0.4], [10, 10, 1], "frame")
    b.add("body", "face", [-4, 3, 0.1], [8, 8, 0.4], "face", face_cells={"north": "face"})
    b.add("body", "hand_h", [-0.4, 7, -0.1], [0.8, 3, 0.3], "hand")
    b.add("body", "hand_m", [-0.4, 7, -0.1], [0.8, 4.2, 0.3], "hand", rotation=[0, 0, 70], pivot=[0, 7, 0])
    b.add("body", "dot_t", [-0.5, 10.6, 0], [1, 1, 0.3], "dot")
    b.add("body", "dot_b", [-0.5, 3.4, 0], [1, 1, 0.3], "dot")
    b.add("body", "dot_l", [-4.4, 6.5, 0], [1, 1, 0.3], "dot")
    b.add("body", "dot_r", [3.4, 6.5, 0], [1, 1, 0.3], "dot")
    static_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                          {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src, 0.7, 1.0)


# ---------------------------------------------------------------- picture frame
def build_picture_frame():
    sid = "unicorn_picture_frame"
    specs = [("frame", (245, 210, 120), "solid"), ("mat", (255, 250, 255), "solid"),
             ("pic", (188, 226, 250), "face"), ("rainbow", None, "horn")]
    rel, src, cm = make_atlas(sid, specs, 7004)
    b = Builder(cm)
    b.add("body", "frame", [-5, 1, 0.4], [10, 8, 1], "frame")
    b.add("body", "mat", [-4.2, 1.8, 0.1], [8.4, 6.4, 0.4], "mat")
    b.add("body", "pic", [-3.5, 2.4, -0.05], [7, 5.2, 0.4], "pic", face_cells={"north": "pic"})
    static_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                          {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src, 0.7, 0.8)


# ---------------------------------------------------------------- potted plant
def build_potted_plant():
    sid = "unicorn_potted_plant"
    specs = [("pot", (244, 170, 140), "solid"), ("rim", (255, 200, 175), "solid"),
             ("soil", (120, 90, 72), "solid"), ("leaf", (150, 220, 160), "solid"),
             ("flower", (255, 180, 210), "solid")]
    rel, src, cm = make_atlas(sid, specs, 7005)
    b = Builder(cm)
    b.add("body", "pot", [-3, 0, -3], [6, 5, 6], "pot")
    b.add("body", "rim", [-3.4, 5, -3.4], [6.8, 1, 6.8], "rim")
    b.add("body", "soil", [-2.6, 5.6, -2.6], [5.2, 0.5, 5.2], "soil")
    b.add("body", "stem", [-0.5, 6, -0.5], [1, 4, 1], "leaf")
    for i, (lx, ly, lz) in enumerate(((-3, 7, -0.5), (2, 8, -0.5), (-0.5, 9.5, -3), (-0.5, 8.5, 2))):
        b.add("body", "leaf%d" % i, [lx, ly, lz], [2.5, 2, 2.5], "leaf")
    b.add("body", "flower", [-1, 11, -1], [2, 2, 2], "flower")
    static_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                          {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src, 0.7, 0.9)


# ---------------------------------------------------------------- floor lamp
def build_floor_lamp():
    sid = "unicorn_floor_lamp"
    specs = [("base", (204, 190, 234), "solid"), ("pole", (245, 210, 120), "solid"),
             ("shade", (248, 196, 224), "solid"), ("glow", (255, 246, 200), "glow"),
             ("trim", (150, 230, 200), "solid")]
    rel, src, cm = make_atlas(sid, specs, 7006)
    b = Builder(cm)
    b.add("body", "base", [-3, 0, -3], [6, 1, 6], "base")
    b.add("body", "pole", [-0.5, 1, -0.5], [1, 16, 1], "pole")
    b.add("body", "shade", [-4, 16.5, -4], [8, 5, 8], "shade")
    b.add("body", "shade_trim", [-4, 16.5, -4], [8, 0.8, 8], "trim")
    b.add("glow", "bulb", [-3, 17, -3], [6, 4, 6], "glow")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "glow", "parent": sid, "pivot": [0, 19, 0]}], rel, src)
    variant_light_wiring(sid, "action.interact.lights_on", "action.interact.lights_off", 0.7, 1.4)


# ---------------------------------------------------------------- dresser
def build_dresser():
    sid = "unicorn_dresser"
    specs = [("body", (244, 200, 230), "solid"), ("drawer", (255, 238, 248), "solid"),
             ("knob", (245, 210, 120), "solid"), ("top", (204, 190, 234), "solid"),
             ("heart", None, "horn")]
    rel, src, cm = make_atlas(sid, specs, 7007)
    b = Builder(cm)
    b.add("body", "box", [-7, 0, -5], [14, 14, 10], "body")
    b.add("body", "top", [-7.5, 14, -5.5], [15, 1, 11], "top")
    for i, y in enumerate((1, 5.5, 10)):
        b.add("body", "drawer%d" % i, [-6, y, -5.3], [12, 3.5, 0.5], "drawer")
        b.add("body", "knob%d" % i, [-0.6, y + 1.4, -5.7], [1.2, 0.8, 0.5], "knob")
    b.add("body", "heart", [-1, 15, -0.4], [2, 1.8, 0.6], "heart")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src)
    script_entity(sid, "script_store", 1.0, 1.0)


# ---------------------------------------------------------------- nightstand
def build_nightstand():
    sid = "unicorn_nightstand"
    specs = [("body", (204, 190, 234), "solid"), ("drawer", (255, 238, 248), "solid"),
             ("knob", (245, 210, 120), "solid"), ("leg", (245, 210, 120), "solid")]
    rel, src, cm = make_atlas(sid, specs, 7008)
    b = Builder(cm)
    b.add("body", "box", [-4, 4, -4], [8, 7, 8], "body")
    b.add("body", "top", [-4.5, 11, -4.5], [9, 1, 9], "body")
    b.add("body", "drawer", [-3.4, 5, -4.3], [6.8, 4, 0.5], "drawer")
    b.add("body", "knob", [-0.6, 6.6, -4.7], [1.2, 0.8, 0.5], "knob")
    for i, (lx, lz) in enumerate(((-3.5, -3.5), (2.5, -3.5), (-3.5, 2.5), (2.5, 2.5))):
        b.add("body", "leg%d" % i, [lx, 0, lz], [1, 4, 1], "leg")
    static_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                          {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src, 0.6, 0.8)


def main():
    build_coffee_table()
    build_rug()
    build_wall_clock()
    build_picture_frame()
    build_potted_plant()
    build_floor_lamp()
    build_dresser()
    build_nightstand()


if __name__ == "__main__":
    main()
