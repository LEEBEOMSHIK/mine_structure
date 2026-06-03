"""Generate four more kid-friendly unicorn entities (geo + atlas + bbmodel).

Reuses the helpers in gen_kids_furniture so the first batch's .bbmodel files are
not re-touched (importing does not run that module's main()).

  unicorn_baby_pet      tameable mob: separate leg/head bones for walk + idle anim
  unicorn_gacha_machine capsule (gachapon) globe, Script gives a random reward
  unicorn_trampoline    flat mat to stand on; Script bounces players up
  unicorn_gift_box      hinged "lid" bone for an open animation + Script gift

Front = -Z (north face), 16 units = 1 block, feet at y=0, no rotated cubes.
"""
from gen_kids_furniture import Builder, make_atlas, assemble


def build_baby_pet():
    sid = "unicorn_baby_pet"
    specs = [
        ("body", (250, 246, 240), "solid"),
        ("hoof", (204, 190, 234), "solid"),
        ("eye", (74, 60, 96), "solid"),
        ("blush", (255, 170, 202), "solid"),
        ("rainbow", None, "horn"),
    ]
    atlas_rel, src, cm = make_atlas(sid, specs, 6101)
    b = Builder(cm)
    # body + chest (small, chubby baby proportions). Front (muzzle) at +Z.
    b.add("body", "barrel", [-3.5, 5, -5], [7, 5, 10], "body")
    b.add("body", "rump", [-3, 5.2, -6], [6, 4.6, 1.5], "body")
    # rainbow mane crest + tail
    b.add("body", "mane1", [-1, 10, 3.5], [2, 1.6, 1.6], "rainbow")
    b.add("body", "mane2", [-1, 9.6, 2], [2, 1.6, 1.6], "rainbow")
    b.add("body", "tail1", [-1, 5.5, -6.5], [2, 4.5, 1.5], "rainbow")
    # head (own bone for idle bob); front = +Z
    b.add("head", "head", [-2.5, 9, 4.5], [5, 5, 4], "body")
    b.add("head", "muzzle", [-2, 9.4, 8.5], [4, 3, 2], "body")
    b.add("head", "ear_l", [-2.2, 13.4, 5], [1.2, 1.6, 1.2], "body")
    b.add("head", "ear_r", [1, 13.4, 5], [1.2, 1.6, 1.2], "body")
    # face built from small cubes so nothing hides it: eyes + blush above the
    # muzzle, nostrils + mouth on the muzzle front.
    b.add("head", "eye_l", [-1.9, 12.6, 8.4], [0.9, 0.9, 0.35], "eye")
    b.add("head", "eye_r", [1.0, 12.6, 8.4], [0.9, 0.9, 0.35], "eye")
    b.add("head", "blush_l", [-2.3, 11.3, 8.4], [0.9, 0.6, 0.25], "blush")
    b.add("head", "blush_r", [1.4, 11.3, 8.4], [0.9, 0.6, 0.25], "blush")
    b.add("head", "nostril_l", [-1.2, 10.3, 10.4], [0.5, 0.5, 0.25], "eye")
    b.add("head", "nostril_r", [0.7, 10.3, 10.4], [0.5, 0.5, 0.25], "eye")
    b.add("head", "mouth", [-0.6, 9.5, 10.4], [1.2, 0.4, 0.25], "eye")
    b.add("head", "horn1", [-0.8, 13.4, 6], [1.6, 2, 1.6], "rainbow")
    b.add("head", "horn2", [-0.5, 15.2, 6.2], [1, 1.6, 1], "rainbow")
    b.add("head", "forelock", [-1.4, 12.8, 7.6], [2.8, 1.5, 1], "rainbow")
    # four legs (each its own bone, pivot at the hip)
    b.add("leg_fl", "leg_fl", [-3, 0, 3], [2, 5, 2], "hoof")
    b.add("leg_fr", "leg_fr", [1, 0, 3], [2, 5, 2], "hoof")
    b.add("leg_bl", "leg_bl", [-3, 0, -4], [2, 5, 2], "hoof")
    b.add("leg_br", "leg_br", [1, 0, -4], [2, 5, 2], "hoof")

    bone_defs = [
        {"name": sid, "parent": None, "pivot": [0, 0, 0]},
        {"name": "body", "parent": sid, "pivot": [0, 7, 0]},
        {"name": "head", "parent": "body", "pivot": [0, 9.5, 6]},
        {"name": "leg_fl", "parent": "body", "pivot": [-2, 5, 4]},
        {"name": "leg_fr", "parent": "body", "pivot": [2, 5, 4]},
        {"name": "leg_bl", "parent": "body", "pivot": [-2, 5, -3]},
        {"name": "leg_br", "parent": "body", "pivot": [2, 5, -3]},
    ]
    assemble(sid, b, bone_defs, atlas_rel, src)


def build_gacha_machine():
    sid = "unicorn_gacha_machine"
    specs = [
        ("body", (248, 178, 214), "solid"),
        ("globe", (236, 246, 252), "capsule"),
        ("knob", (247, 212, 120), "solid"),
        ("tray", (200, 186, 232), "solid"),
        ("rainbow", None, "horn"),
    ]
    atlas_rel, src, cm = make_atlas(sid, specs, 6102)
    b = Builder(cm)
    M = "machine"
    b.add(M, "base", [-5, 0, -5], [10, 4, 10], "body")
    b.add(M, "globe", [-4.5, 4, -4.5], [9, 8, 9], "globe")
    b.add(M, "globe_cap", [-3, 12, -3], [6, 2, 6], "body")
    # coin knob + dispense tray on the front (-Z)
    b.add(M, "knob", [-1, 1.5, -6], [2, 2, 1], "knob")
    b.add(M, "tray", [-3, 0.5, -6], [6, 1.5, 1.2], "tray")
    b.add(M, "coin_slot", [1.4, 2.2, -5.6], [1.4, 0.8, 0.6], "knob")
    # unicorn topper
    b.add(M, "ear_l", [-3.4, 14, -0.5], [1.4, 2, 1.4], "body")
    b.add(M, "ear_r", [2, 14, -0.5], [1.4, 2, 1.4], "body")
    b.add(M, "horn1", [-0.8, 14, -0.3], [1.6, 2.2, 1.6], "rainbow")
    b.add(M, "horn2", [-0.5, 16.2, -0.1], [1, 1.6, 1], "rainbow")

    bone_defs = [
        {"name": sid, "parent": None, "pivot": [0, 0, 0]},
        {"name": M, "parent": sid, "pivot": [0, 0, 0]},
    ]
    assemble(sid, b, bone_defs, atlas_rel, src)


def build_trampoline():
    sid = "unicorn_trampoline"
    specs = [
        ("frame", (204, 190, 234), "solid"),
        ("pad", (248, 168, 206), "solid"),
        ("mat", (132, 206, 234), "solid"),
        ("spring", (247, 212, 120), "solid"),
        ("rainbow", None, "horn"),
    ]
    atlas_rel, src, cm = make_atlas(sid, specs, 6103)
    b = Builder(cm)
    T = "frame"
    # legs
    for lx, lz, nm in [(-9, -9, "leg_a"), (7, -9, "leg_b"), (-9, 7, "leg_c"), (7, 7, "leg_d")]:
        b.add(T, nm, [lx, 0, lz], [2, 4, 2], "frame")
    # padded ring
    b.add(T, "pad_front", [-10, 4, -10], [20, 2, 2], "pad")
    b.add(T, "pad_back", [-10, 4, 8], [20, 2, 2], "pad")
    b.add(T, "pad_left", [-10, 4, -8], [2, 2, 16], "pad")
    b.add(T, "pad_right", [8, 4, -8], [2, 2, 16], "pad")
    # springs (decorative)
    for sx in (-6, -2, 2, 6):
        b.add(T, "spring_f%d" % sx, [sx, 4.2, -8.4], [1.5, 1.2, 1], "spring")
        b.add(T, "spring_b%d" % sx, [sx, 4.2, 7.4], [1.5, 1.2, 1], "spring")
    # the bouncy mat (stand on top, y top = 5.5)
    b.add(T, "mat", [-8, 4.5, -8], [16, 1, 16], "mat")
    # unicorn corner topper
    b.add(T, "horn1", [8.2, 6, 8.2], [1.6, 2.2, 1.6], "rainbow")
    b.add(T, "horn2", [8.5, 8.2, 8.5], [1, 1.6, 1], "rainbow")

    bone_defs = [
        {"name": sid, "parent": None, "pivot": [0, 0, 0]},
        {"name": T, "parent": sid, "pivot": [0, 0, 0]},
    ]
    assemble(sid, b, bone_defs, atlas_rel, src)


def build_gift_box():
    sid = "unicorn_gift_box"
    specs = [
        ("box", (170, 210, 245), "solid"),
        ("ribbon", (248, 150, 196), "solid"),
        ("tag", (252, 250, 246), "solid"),
        ("rainbow", None, "horn"),
    ]
    atlas_rel, src, cm = make_atlas(sid, specs, 6104)
    b = Builder(cm)
    # base box + cross ribbon
    b.add("box", "base", [-5, 0, -5], [10, 8, 10], "box")
    b.add("box", "band_x", [-5.1, 0, -1.5], [10.2, 8.05, 3], "ribbon")
    b.add("box", "band_z", [-1.5, 0, -5.1], [3, 8.05, 10.2], "ribbon")
    b.add("box", "tag", [3, 4, -5.6], [2, 1.5, 0.6], "tag")
    # lid (hinged at back-top), opens via animation
    b.add("lid", "lid", [-5.5, 8, -5.5], [11, 2, 11], "box")
    b.add("lid", "lid_band_x", [-5.6, 8, -1.5], [11.2, 2.1, 3], "ribbon")
    b.add("lid", "lid_band_z", [-1.5, 8, -5.6], [3, 2.1, 11.2], "ribbon")
    # bow on the lid (lifts with the lid)
    b.add("lid", "bow_c", [-1.5, 10, -1.5], [3, 2, 3], "ribbon")
    b.add("lid", "bow_l", [-3.6, 10.3, -1], [2.2, 1.6, 2], "ribbon")
    b.add("lid", "bow_r", [1.4, 10.3, -1], [2.2, 1.6, 2], "ribbon")
    b.add("lid", "bow_knot", [-0.8, 10.6, -0.8], [1.6, 1.6, 1.6], "rainbow")

    bone_defs = [
        {"name": sid, "parent": None, "pivot": [0, 0, 0]},
        {"name": "box", "parent": sid, "pivot": [0, 0, 0]},
        {"name": "lid", "parent": sid, "pivot": [0, 8, 5]},
    ]
    assemble(sid, b, bone_defs, atlas_rel, src)


def main():
    build_baby_pet()
    build_gacha_machine()
    build_trampoline()
    build_gift_box()


if __name__ == "__main__":
    main()
