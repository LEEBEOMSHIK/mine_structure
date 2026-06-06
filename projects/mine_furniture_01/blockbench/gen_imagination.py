"""Imagination / pretend-play set: castle tent, dollhouse, toy box, easel.

  unicorn_castle_tent  rideable (1, sit inside) — pointed castle play-tent
  unicorn_dollhouse    variant_light: window lights on/off ("glow" bone)
  unicorn_toy_box      Script storage (store/retrieve toys); lid ajar + peeking toy
  unicorn_easel        variant_light: painting appears/clears on the canvas ("glow")

Reuses gen_kids_furniture (Builder/make_atlas/assemble), gen_room_furniture
(variant_light_wiring/rideable_wiring/write), gen_living_furniture (script_entity).
"""
import os

from gen_kids_furniture import Builder, assemble, make_atlas
from gen_room_furniture import rideable_wiring, variant_light_wiring, write  # noqa: F401
from gen_living_furniture import script_entity


# ---------------------------------------------------------------- castle tent
def build_castle_tent():
    sid = "unicorn_castle_tent"
    specs = [("tent", (244, 170, 210), "solid"), ("roof", (150, 200, 240), "cone"),
             ("trim", (245, 210, 120), "solid"), ("flag", None, "horn"),
             ("door", (120, 90, 140), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6901)
    b = Builder(cm)
    # square walls with a front doorway
    b.add("body", "wall_back", [-8, 0, 6.5], [16, 13, 1.5], "tent")
    b.add("body", "wall_l", [-8, 0, -8], [1.5, 13, 16], "tent")
    b.add("body", "wall_r", [6.5, 0, -8], [1.5, 13, 16], "tent")
    b.add("body", "wall_fl", [-8, 0, -8], [5, 13, 1.5], "tent")
    b.add("body", "wall_fr", [3, 0, -8], [5, 13, 1.5], "tent")
    b.add("body", "lintel", [-8, 10, -8], [16, 3, 1.5], "tent")
    b.add("body", "door_l", [-3.2, 0, -8.1], [0.6, 10, 0.6], "door")
    b.add("body", "door_r", [2.6, 0, -8.1], [0.6, 10, 0.6], "door")
    # conical roof (stacked shrinking boxes) + spire + flag
    b.add("body", "trim", [-8.5, 12.5, -8.5], [17, 1, 17], "trim")
    b.add("body", "roof1", [-9.5, 13, -9.5], [19, 2.5, 19], "roof")
    b.add("body", "roof2", [-7, 15.5, -7], [14, 3, 14], "roof")
    b.add("body", "roof3", [-4, 18.5, -4], [8, 4, 8], "roof")
    b.add("body", "spire", [-1.5, 22.5, -1.5], [3, 4, 3], "roof")
    b.add("body", "pole", [-0.4, 26, -0.4], [0.8, 4.5, 0.8], "trim")
    b.add("body", "flag", [0.4, 26.3, -0.3], [4, 2.6, 0.4], "flag")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src)
    rideable_wiring(sid, [{"position": [0, 0.3, 0.1], "lock_rider_rotation": 0}], 1.2, 2.0)


# ---------------------------------------------------------------- dollhouse
def build_dollhouse():
    sid = "unicorn_dollhouse"
    specs = [("wall", (248, 222, 200), "solid"), ("roof", (244, 150, 190), "cone"),
             ("window", (185, 235, 255), "glow"), ("door", (196, 150, 110), "solid"),
             ("trim", (150, 230, 200), "solid"), ("chimney", (220, 180, 170), "solid"),
             ("heart", None, "horn")]
    rel, src, cm = make_atlas(sid, specs, 6902)
    b = Builder(cm)
    b.add("body", "house", [-7, 0, -5], [14, 14, 10], "wall")
    b.add("body", "floortrim", [-7.1, 7, -5.1], [14.2, 0.8, 10.2], "trim")
    # gable roof (stacked shrinking) + ridge heart
    b.add("body", "roof1", [-8, 14, -6], [16, 2, 12], "roof")
    b.add("body", "roof2", [-6, 16, -4.5], [12, 2, 9], "roof")
    b.add("body", "roof3", [-3.5, 18, -3], [7, 2, 6], "roof")
    b.add("body", "heart", [-1, 20, -2.5], [2, 2.2, 1], "heart")
    b.add("body", "door", [-2, 0, -5.25], [4, 7, 0.4], "door")
    b.add("body", "knob", [0.9, 3.3, -5.5], [0.5, 0.5, 0.4], "trim")
    b.add("body", "chimney", [3.5, 17, 0], [2.5, 5, 2.5], "chimney")
    # window panes glow when the lights are on
    for i, (wx, wy) in enumerate(((-5.5, 2.5), (2.5, 2.5), (-5.5, 9), (2.5, 9))):
        b.add("glow", "win%d" % i, [wx, wy, -5.3], [3, 3, 0.3], "window",
              face_cells={"north": "window"})
        b.add("body", "winframe%d" % i, [wx - 0.4, wy - 0.4, -5.2], [3.8, 3.8, 0.3], "trim")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "glow", "parent": sid, "pivot": [0, 5, -5]}], rel, src)
    variant_light_wiring(sid, "action.interact.lights_on", "action.interact.lights_off", 1.0, 1.4)


# ---------------------------------------------------------------- toy box
def build_toy_box():
    sid = "unicorn_toy_box"
    specs = [("box", (244, 184, 130), "solid"), ("lid", (244, 150, 190), "solid"),
             ("trim", (150, 230, 200), "solid"), ("star", None, "horn"),
             ("ball", (150, 200, 245), "solid"), ("block", (245, 210, 120), "solid")]
    rel, src, cm = make_atlas(sid, specs, 6903)
    b = Builder(cm)
    b.add("body", "box", [-7, 0, -5], [14, 9, 10], "box")
    b.add("body", "trim_top", [-7.2, 8.4, -5.2], [14.4, 0.8, 10.4], "trim")
    b.add("body", "trim_bot", [-7.2, 0, -5.2], [14.4, 0.8, 10.4], "trim")
    # lid ajar (hinged at the back, tilted open)
    b.add("body", "lid", [-7.2, 9.2, -5.2], [14.4, 2, 10.4], "lid", rotation=[-58, 0, 0], pivot=[0, 9.2, 5.2])
    b.add("body", "star", [-1.4, 3.5, -5.4], [2.8, 2.8, 0.6], "star")
    # toys peeking out of the open box
    b.add("body", "ball", [-3.5, 8, -2], [3.2, 3.2, 3.2], "ball")
    b.add("body", "block", [1, 8.5, 0.5], [2.6, 2.6, 2.6], "block")
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src)
    script_entity(sid, "script_store", 1.0, 0.8)


# ---------------------------------------------------------------- easel
def build_easel():
    sid = "unicorn_easel"
    specs = [("wood", (200, 150, 110), "solid"), ("canvas", (252, 248, 240), "solid"),
             ("paint", (244, 150, 190), "glow"), ("trim", (150, 230, 200), "solid"),
             ("star", None, "horn")]
    rel, src, cm = make_atlas(sid, specs, 6904)
    b = Builder(cm)
    # tripod: two front legs splayed out + one back leg
    b.add("body", "leg_l", [-6, 0, -2], [1.4, 20, 1.4], "wood", rotation=[0, 0, 12], pivot=[-6, 0, 0])
    b.add("body", "leg_r", [4.6, 0, -2], [1.4, 20, 1.4], "wood", rotation=[0, 0, -12], pivot=[6, 0, 0])
    b.add("body", "leg_back", [-0.7, 0, 3], [1.4, 19, 1.4], "wood", rotation=[14, 0, 0], pivot=[0, 0, 3])
    b.add("body", "tray", [-7, 9, -2.6], [14, 1, 1.8], "wood")
    b.add("body", "frame", [-6.5, 9.6, -2.2], [13, 12, 0.9], "trim")
    b.add("body", "canvas", [-5.5, 10.4, -2.4], [11, 10.4, 0.4], "canvas")
    b.add("body", "star", [-1, 20.8, -2], [2, 2, 0.6], "star")
    # painting appears on the canvas when "on"
    b.add("glow", "paint", [-5, 10.9, -2.55], [10, 9.4, 0.3], "paint",
          face_cells={"north": "paint"})
    assemble(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                      {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                      {"name": "glow", "parent": sid, "pivot": [0, 15, -2.4]}], rel, src)
    variant_light_wiring(sid, "action.interact.paint", "action.interact.clear", 1.0, 1.4)


def main():
    build_castle_tent()
    build_dollhouse()
    build_toy_box()
    build_easel()


if __name__ == "__main__":
    main()
