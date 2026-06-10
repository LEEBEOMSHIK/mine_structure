"""Kitchen / cafe batch 3: coffee machine, blender, cake stand, cupcake tower,
water dispenser, dish rack, bakery oven, cafe bar. Pastel unicorn theme.

  coffee_machine / bakery_oven   script_give (hand out a drink / cookie)
  blender / water_dispenser      variant_light (running / water glow on-off)
  cake_stand / cupcake_tower / dish_rack / cafe_bar   static decor

Reuses gen_kids_furniture (Builder/make_atlas/assemble), gen_room_furniture
(variant_light_wiring/write), gen_living_furniture (script_entity).
"""
from gen_kids_furniture import Builder, assemble, make_atlas
from gen_room_furniture import variant_light_wiring
from gen_living_furniture import script_entity


def finish(sid, b, bones, rel, src, mechanic, w, h):
    assemble(sid, b, bones, rel, src)
    script_entity(sid, mechanic, w, h)


# ---------------------------------------------------------------- coffee machine
def build_coffee_machine():
    sid = "unicorn_coffee_machine"
    specs = [("body", (244, 200, 230), "solid"), ("panel", (60, 56, 92), "face"),
             ("cup", (255, 250, 255), "solid"), ("button", (150, 210, 245), "solid"),
             ("coffee", (150, 100, 70), "solid"), ("trim", (245, 210, 120), "solid")]
    rel, src, cm = make_atlas(sid, specs, 7201)
    b = Builder(cm)
    b.add("body", "body", [-5, 0, -4], [10, 11, 8], "body")
    b.add("body", "head", [-5, 9, -5], [10, 3, 3.5], "body")
    b.add("body", "panel", [-4, 4, -4.2], [8, 5, 0.4], "panel", face_cells={"north": "panel"})
    b.add("body", "btn1", [-3.5, 9.5, -5.3], [1.2, 1.2, 0.4], "button")
    b.add("body", "btn2", [-1.6, 9.5, -5.3], [1.2, 1.2, 0.4], "button")
    b.add("body", "nozzle", [-1, 7.5, -5], [2, 1.5, 1], "trim")
    b.add("body", "tray", [-3, 1, -5.5], [6, 0.5, 2], "trim")
    b.add("body", "cup", [-1.6, 1.5, -5], [3.2, 2.5, 2.5], "cup")
    b.add("body", "coffee", [-1.3, 3.6, -4.7], [2.6, 0.3, 2], "coffee")
    b.add("body", "top_trim", [-5, 11.8, -5], [10, 0.6, 8], "trim")
    finish(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                    {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src, "script_give", 0.7, 0.9)


# ---------------------------------------------------------------- blender
def build_blender():
    sid = "unicorn_blender"
    specs = [("base", (204, 190, 234), "solid"), ("jar", (200, 235, 250), "solid"),
             ("juice", (255, 180, 210), "glow"), ("lid", (244, 170, 210), "solid"),
             ("button", (245, 210, 120), "solid")]
    rel, src, cm = make_atlas(sid, specs, 7202)
    b = Builder(cm)
    b.add("body", "base", [-3.5, 0, -3.5], [7, 5, 7], "base")
    b.add("body", "btn", [-1, 2, -3.7], [2, 1, 0.4], "button")
    b.add("body", "jar", [-3, 5, -3], [6, 8, 6], "jar")
    b.add("body", "lid", [-3.2, 13, -3.2], [6.4, 1.2, 6.4], "lid")
    b.add("body", "handle", [3, 6, -0.8], [1.2, 5, 1.6], "lid")
    b.add("glow", "juice", [-2.4, 5.5, -2.4], [4.8, 5, 4.8], "juice")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "glow", "parent": sid, "pivot": [0, 8, 0]}], rel, src)
    variant_light_wiring(sid, "action.interact.blend_on", "action.interact.blend_off", 0.6, 1.0)


# ---------------------------------------------------------------- cake stand
def build_cake_stand():
    sid = "unicorn_cake_stand"
    specs = [("plate", (255, 250, 255), "solid"), ("stem", (245, 210, 120), "solid"),
             ("cake", (248, 220, 200), "solid"), ("cream", (255, 235, 245), "solid"),
             ("berry", (240, 120, 150), "solid"), ("mint", (182, 232, 212), "solid")]
    rel, src, cm = make_atlas(sid, specs, 7203)
    b = Builder(cm)
    b.add("body", "foot", [-4, 0, -4], [8, 0.8, 8], "plate")
    b.add("body", "stem", [-1, 0.8, -1], [2, 3, 2], "stem")
    b.add("body", "plate", [-6, 3.8, -6], [12, 0.8, 12], "plate")
    b.add("body", "plate_rim", [-6, 3.8, -6], [12, 0.4, 12], "mint")
    b.add("body", "cake", [-4.5, 4.6, -4.5], [9, 4, 9], "cake")
    b.add("body", "cream", [-4.7, 8.4, -4.7], [9.4, 1, 9.4], "cream")
    for i, (cx, cz) in enumerate(((-3, -3), (1.5, -3), (-3, 1.5), (1.5, 1.5), (-0.75, -0.75))):
        b.add("body", "berry%d" % i, [cx, 9.2, cz], [1.5, 1.5, 1.5], "berry")
    finish(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                    {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src, "static", 0.9, 0.7)


# ---------------------------------------------------------------- cupcake tower
def build_cupcake_tower():
    sid = "unicorn_cupcake_tower"
    specs = [("plate", (255, 250, 255), "solid"), ("pole", (245, 210, 120), "solid"),
             ("cup", (244, 170, 130), "solid"), ("cream", (255, 200, 225), "solid"),
             ("cream2", (190, 235, 250), "solid"), ("cherry", (240, 120, 150), "solid")]
    rel, src, cm = make_atlas(sid, specs, 7204)
    b = Builder(cm)
    b.add("body", "pole", [-0.6, 0, -0.6], [1.2, 22, 1.2], "pole")
    tiers = [(0.5, 7), (8, 5.5), (15, 4)]
    for ti, (y, r) in enumerate(tiers):
        b.add("body", "plate%d" % ti, [-r, y, -r], [r * 2, 0.7, r * 2], "plate")
        # cupcakes around each tier
        n = 4 if ti < 2 else 3
        import math
        for k in range(n):
            a = 2 * math.pi * k / n
            cx = round((r - 1.6) * math.cos(a), 1)
            cz = round((r - 1.6) * math.sin(a), 1)
            b.add("body", "cup%d_%d" % (ti, k), [cx - 1, y + 0.7, cz - 1], [2, 2, 2], "cup")
            cream = "cream" if (ti + k) % 2 == 0 else "cream2"
            b.add("body", "cr%d_%d" % (ti, k), [cx - 1, y + 2.7, cz - 1], [2, 1.4, 2], cream)
            b.add("body", "ch%d_%d" % (ti, k), [cx - 0.4, y + 4, cz - 0.4], [0.8, 0.8, 0.8], "cherry")
    finish(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                    {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src, "static", 1.0, 2.2)


# ---------------------------------------------------------------- water dispenser
def build_water_dispenser():
    sid = "unicorn_water_dispenser"
    specs = [("body", (230, 224, 240), "solid"), ("tank", (200, 235, 250), "solid"),
             ("water", (150, 212, 246), "glow"), ("tap", (245, 210, 120), "solid"),
             ("trim", (182, 232, 212), "solid")]
    rel, src, cm = make_atlas(sid, specs, 7205)
    b = Builder(cm)
    b.add("body", "body", [-4, 0, -4], [8, 12, 8], "body")
    b.add("body", "top", [-4.3, 12, -4.3], [8.6, 1, 8.6], "trim")
    b.add("body", "tank", [-3, 13, -3], [6, 6, 6], "tank")
    b.add("body", "tap", [-1, 5, -4.6], [2, 1.5, 1], "tap")
    b.add("body", "tray", [-2.5, 3.5, -4.8], [5, 0.5, 1.5], "trim")
    b.add("glow", "water", [-2.6, 13.3, -2.6], [5.2, 5.2, 5.2], "water")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "glow", "parent": sid, "pivot": [0, 16, 0]}], rel, src)
    variant_light_wiring(sid, "action.interact.water_on", "action.interact.water_off", 0.6, 1.3)


# ---------------------------------------------------------------- dish rack
def build_dish_rack():
    sid = "unicorn_dish_rack"
    specs = [("rack", (245, 210, 120), "solid"), ("plate", (255, 250, 255), "solid"),
             ("plate2", (200, 235, 250), "solid"), ("cup", (244, 170, 210), "solid"),
             ("tray", (182, 232, 212), "solid")]
    rel, src, cm = make_atlas(sid, specs, 7206)
    b = Builder(cm)
    b.add("body", "tray", [-6, 0, -4], [12, 0.8, 8], "tray")
    for i in range(5):
        b.add("body", "wire%d" % i, [-5 + i * 2.4, 0.8, -3], [0.4, 5, 6], "rack")
    # plates standing in the slots
    for i, col in enumerate(("plate", "plate2", "plate", "plate2")):
        b.add("body", "plate%d" % i, [-4.2 + i * 2.4, 1, -2.5], [0.6, 4.5, 5], col)
    b.add("body", "cup", [4, 0.8, -1], [2.5, 2.5, 2.5], "cup")
    finish(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                    {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src, "static", 1.0, 0.6)


# ---------------------------------------------------------------- bakery oven
def build_bakery_oven():
    sid = "unicorn_bakery_oven"
    specs = [("body", (248, 220, 210), "solid"), ("door", (120, 90, 140), "solid"),
             ("window", (255, 230, 160), "face"), ("knob", (245, 210, 120), "solid"),
             ("trim", (244, 170, 210), "solid"), ("bread", (220, 160, 110), "solid")]
    rel, src, cm = make_atlas(sid, specs, 7207)
    b = Builder(cm)
    b.add("body", "body", [-6, 0, -5], [12, 13, 10], "body")
    b.add("body", "top", [-6.3, 13, -5.3], [12.6, 1, 10.6], "trim")
    b.add("body", "chimney", [3, 14, -1], [2.5, 3, 2.5], "trim")
    b.add("body", "door", [-4.5, 2, -5.3], [9, 7, 0.5], "door")
    b.add("body", "window", [-3.5, 3, -5.6], [7, 4.5, 0.4], "window", face_cells={"north": "window"})
    b.add("body", "handle", [-4.5, 5, -6], [9, 0.8, 0.6], "knob")
    for i, kx in enumerate((-4, -2)):
        b.add("body", "knob%d" % i, [kx, 10, -5.4], [1, 1, 0.5], "knob")
    b.add("body", "tray", [-3, 1.5, -5.5], [6, 0.4, 1], "trim")
    b.add("body", "bread", [-2, 1.9, -5.3], [4, 1.5, 1.5], "bread")
    finish(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                    {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src, "script_give", 1.0, 1.0)


# ---------------------------------------------------------------- cafe bar
def build_cafe_bar():
    sid = "unicorn_cafe_bar"
    specs = [("counter", (244, 200, 230), "solid"), ("top", (255, 250, 255), "solid"),
             ("panel", (204, 190, 234), "solid"), ("trim", (245, 210, 120), "solid"),
             ("jar", (200, 235, 250), "solid"), ("heart", None, "horn")]
    rel, src, cm = make_atlas(sid, specs, 7208)
    b = Builder(cm)
    b.add("body", "counter", [-10, 0, -3], [20, 9, 6], "counter")
    b.add("body", "top", [-10.5, 9, -4], [21, 1, 8], "top")
    b.add("body", "panel", [-10, 1, -3.3], [20, 7, 0.4], "panel")
    b.add("body", "trim", [-10, 8, -3.4], [20, 1, 0.5], "trim")
    b.add("body", "heart", [-1, 3.5, -3.5], [2, 1.8, 0.5], "heart")
    # a couple of jars / a sign on the counter top
    b.add("body", "jar1", [6, 10, -1], [2.5, 3, 2.5], "jar")
    b.add("body", "jar2", [-8, 10, -1], [2.5, 2.5, 2.5], "jar")
    b.add("body", "sign", [-2, 10, 0], [4, 3, 0.5], "trim")
    finish(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                    {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src, "static", 1.6, 0.9)


def main():
    build_coffee_machine()
    build_blender()
    build_cake_stand()
    build_cupcake_tower()
    build_water_dispenser()
    build_dish_rack()
    build_bakery_oven()
    build_cafe_bar()


if __name__ == "__main__":
    main()
