"""Music / performance batch 6: drum kit, guitar on stand, jukebox, mic stage.
Pastel unicorn theme. Pairs with the existing unicorn_piano for a band corner.

  unicorn_jukebox    script_play   (plays a short melody + note particles on interact)
  unicorn_mic_stage  variant_light (stage spotlights toggle on/off, glow bone)
  unicorn_drums      static
  unicorn_guitar     static

Reuses gen_kids_furniture (Builder/make_atlas/assemble), gen_room_furniture
(variant_light_wiring), gen_living_furniture (script_entity).
"""
from gen_kids_furniture import Builder, assemble, make_atlas
from gen_room_furniture import variant_light_wiring
from gen_living_furniture import script_entity


def static_decor(sid, b, bones, rel, src, w, h):
    assemble(sid, b, bones, rel, src)
    script_entity(sid, "static", w, h)


def play_decor(sid, b, bones, rel, src, w, h):
    assemble(sid, b, bones, rel, src)
    script_entity(sid, "script_play", w, h)


def light_decor(sid, b, bones, rel, src, w, h):
    assemble(sid, b, bones, rel, src)
    variant_light_wiring(sid, "action.interact.light_on", "action.interact.light_off", w, h)


# ------------------------------------------------------------------------ drums
def build_drums():
    sid = "unicorn_drums"
    specs = [("shell", (255, 250, 255), "solid"), ("rim", (247, 167, 200), "solid"),
             ("tom1", (185, 242, 208), "solid"), ("tom2", (169, 216, 255), "solid"),
             ("metal", (245, 210, 120), "solid"), ("stick", (235, 215, 180), "solid"),
             ("head", (244, 238, 250), "solid")]
    rel, src, cm = make_atlas(sid, specs, 7501)
    b = Builder(cm)
    # bass drum (big, lying so the head faces -z) + rim ring + feet
    b.add("body", "bass", [-6, 1.5, -3], [12, 11, 8], "shell")
    b.add("body", "bass_rim", [-6.4, 1.1, -3.4], [12.8, 11.8, 0.6], "rim")
    b.add("body", "bass_head", [-5.4, 2.1, -3.6], [10.8, 9.8, 0.4], "head")
    b.add("body", "foot_l", [-6.5, 0, -1], [1, 1.5, 5], "metal")
    b.add("body", "foot_r", [5.5, 0, -1], [1, 1.5, 5], "metal")
    b.add("body", "pedal", [-1.5, 0, -6], [3, 0.8, 3], "metal")
    # two toms tilted on top of the bass
    b.add("body", "tom1", [-5, 12, -2], [5, 4, 5], "tom1", rotation=[-18, 0, 0], pivot=[-2.5, 12, 0])
    b.add("body", "tom1_rim", [-5.2, 11.8, -2.2], [5.4, 0.5, 5.4], "metal", rotation=[-18, 0, 0], pivot=[-2.5, 12, 0])
    b.add("body", "tom2", [0.5, 12, -2], [5, 4, 5], "tom2", rotation=[-18, 0, 0], pivot=[3, 12, 0])
    b.add("body", "tom2_rim", [0.3, 11.8, -2.2], [5.4, 0.5, 5.4], "metal", rotation=[-18, 0, 0], pivot=[3, 12, 0])
    # snare drum on a 3-leg stand (front-left, raised so it reads)
    b.add("body", "snare", [-11, 7, -6], [5, 3.5, 5], "shell")
    b.add("body", "snare_rim", [-11.2, 10.2, -6.2], [5.4, 0.5, 5.4], "metal")
    for (lx, lz) in ((-10.5, -5.5), (-7, -5.5), (-8.8, -2)):
        b.add("body", "sleg_%d_%d" % (int(lx * 10), int(lz * 10)), [lx, 0, lz], [0.7, 7, 0.7], "metal")
    # crash cymbal on a tall pole (right) + smaller hi-hat (left)
    b.add("body", "cym_pole", [10, 0, 0], [0.8, 15, 0.8], "metal")
    b.add("body", "cymbal", [7, 15, -2], [6, 0.4, 6], "metal", rotation=[16, 0, 0], pivot=[10.4, 15.2, 0.8])
    b.add("body", "hat_pole", [-13, 0, -5], [0.8, 11, 0.8], "metal")
    b.add("body", "hihat", [-15, 11, -7], [5, 0.4, 5], "metal", rotation=[10, 0, 0], pivot=[-12.6, 11.2, -2.6])
    # drumsticks resting on the snare
    b.add("body", "stick1", [-10, 10.6, -7], [0.5, 0.5, 7], "stick", rotation=[8, 16, 0], pivot=[-10, 10.6, -4])
    b.add("body", "stick2", [-8.2, 10.6, -7], [0.5, 0.5, 7], "stick", rotation=[8, -8, 0], pivot=[-8.2, 10.6, -4])
    static_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                          {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src, 1.8, 0.9)


# ----------------------------------------------------------------------- guitar
def build_guitar():
    sid = "unicorn_guitar"
    specs = [("stand", (245, 210, 120), "solid"), ("bodyc", (247, 167, 200), "solid"),
             ("neck", (204, 190, 234), "solid"), ("hole", (90, 78, 120), "solid"),
             ("string", (245, 225, 160), "solid"), ("peg", (255, 250, 255), "solid")]
    rel, src, cm = make_atlas(sid, specs, 7502)
    b = Builder(cm)
    # A-frame stand: two splayed legs + cross brace + bottom cradle
    b.add("body", "leg_l", [-3.5, 0, -1.5], [0.9, 14, 0.9], "stand", rotation=[0, 0, 12], pivot=[0, 0, 0])
    b.add("body", "leg_r", [2.6, 0, -1.5], [0.9, 14, 0.9], "stand", rotation=[0, 0, -12], pivot=[0, 0, 0])
    b.add("body", "leg_b", [-0.45, 0, 2.5], [0.9, 13, 0.9], "stand", rotation=[14, 0, 0], pivot=[0, 0, 2.9])
    b.add("body", "brace", [-3, 4.5, -1.5], [6, 0.8, 0.8], "stand")
    b.add("body", "cradle_l", [-2.6, 1.5, -1.8], [1, 2, 1], "stand")
    b.add("body", "cradle_r", [1.6, 1.5, -1.8], [1, 2, 1], "stand")
    # guitar leaning back on the stand (rotate the whole instrument slightly)
    rot, piv = [10, 0, 0], [0, 2, -1]
    b.add("body", "gbody", [-3.5, 1.5, -2.2], [7, 8, 1.6], "bodyc", rotation=rot, pivot=piv)
    b.add("body", "gbody_low", [-2.8, 0.2, -2.1], [5.6, 2.4, 1.5], "bodyc", rotation=rot, pivot=piv)
    b.add("body", "hole", [-1.4, 4, -2.4], [2.8, 2.8, 0.4], "hole", rotation=rot, pivot=piv)
    b.add("body", "neck", [-1, 9, -2], [2, 11, 1.2], "neck", rotation=rot, pivot=piv)
    b.add("body", "head", [-1.3, 19.5, -2], [2.6, 3, 1.2], "neck", rotation=rot, pivot=piv)
    for i in range(3):
        b.add("body", "peg_l%d" % i, [-2.2, 20 - i * 0.9, -2], [0.9, 0.5, 0.6], "peg", rotation=rot, pivot=piv)
        b.add("body", "peg_r%d" % i, [1.3, 20 - i * 0.9, -2], [0.9, 0.5, 0.6], "peg", rotation=rot, pivot=piv)
    # strings running down the neck + over the body
    for i in range(3):
        b.add("body", "string%d" % i, [-0.7 + i * 0.6, 4.5, -2.5], [0.18, 15, 0.18], "string",
              rotation=rot, pivot=piv)
    static_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                          {"name": "body", "parent": sid, "pivot": [0, 0, 0]}], rel, src, 0.8, 1.5)


# ---------------------------------------------------------------------- jukebox
def build_jukebox():
    sid = "unicorn_jukebox"
    specs = [("body", (204, 190, 234), "solid"), ("trim", (247, 167, 200), "solid"),
             ("panel", (170, 220, 250), "glow"), ("grille", (110, 96, 140), "solid"),
             ("btn", (255, 233, 154), "solid"), ("note", (245, 210, 120), "solid"),
             ("arch", (247, 167, 200), "glow")]
    rel, src, cm = make_atlas(sid, specs, 7503)
    b = Builder(cm)
    b.add("body", "base", [-6, 0, -4], [12, 2, 8], "trim")
    b.add("body", "cab", [-5.5, 2, -3.5], [11, 14, 7], "body")
    # rounded top (stepped) + a glowing arch
    b.add("body", "top1", [-5.5, 16, -3.5], [11, 2, 7], "trim")
    b.add("body", "top2", [-4, 18, -3.5], [8, 2, 7], "trim")
    b.add("glow", "arch", [-3.5, 16.5, -3.7], [7, 3, 0.4], "arch")
    # glowing front display + speaker grilles + buttons + a note
    b.add("glow", "panel", [-4.2, 9.5, -3.9], [8.4, 5.5, 0.4], "panel")
    b.add("body", "grille_l", [-4.5, 3, -3.9], [3.6, 5, 0.4], "grille")
    b.add("body", "grille_r", [0.9, 3, -3.9], [3.6, 5, 0.4], "grille")
    for i, col in enumerate(("btn", "btn", "btn")):
        b.add("body", "btn%d" % i, [-3.5 + i * 2.4, 2.6, -3.9], [1.4, 0.8, 0.4], "btn")
    b.add("body", "note", [-0.9, 10.6, -4.1], [1, 3, 0.3], "note")
    b.add("body", "note_head", [-1.7, 10.4, -4.1], [1.6, 1.2, 0.3], "note")
    play_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                        {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                        {"name": "glow", "parent": sid, "pivot": [0, 10, 0]}], rel, src, 1.0, 1.4)


# -------------------------------------------------------------------- mic stage
def build_mic_stage():
    sid = "unicorn_mic_stage"
    specs = [("stage", (204, 190, 234), "solid"), ("trim", (247, 167, 200), "solid"),
             ("pole", (245, 210, 120), "solid"), ("mic", (90, 78, 120), "solid"),
             ("speaker", (110, 96, 140), "solid"), ("beam", (255, 244, 190), "glow"),
             ("star", None, "horn")]
    rel, src, cm = make_atlas(sid, specs, 7504)
    b = Builder(cm)
    # low stage platform + skirt trim
    b.add("body", "stage", [-9, 1, -7], [18, 1.5, 14], "stage")
    b.add("body", "skirt", [-9.2, 0, -7.2], [18.4, 1, 14.4], "trim")
    # backdrop panel with stars
    b.add("body", "backdrop", [-9, 2.5, 6], [18, 14, 0.8], "trim")
    for (sx, sy) in ((-6, 12), (-2, 14), (3, 11), (6, 13), (0, 9)):
        b.add("body", "star_%d_%d" % (sx, sy), [sx, sy, 5.5], [1.6, 1.6, 0.6], "star")
    # mic stand (centre, front): base + pole + mic head at chest height so it reads
    b.add("body", "mic_base", [-2, 2.5, -4], [4, 0.8, 4], "pole")
    b.add("body", "mic_pole", [-0.5, 3.3, -2.5], [1, 8, 1], "pole")
    b.add("body", "mic_head", [-1.3, 11, -2.8], [2.6, 3, 2.6], "mic")
    b.add("body", "mic_grille", [-1.5, 11.3, -3.1], [3, 2.2, 0.5], "speaker")
    # side speakers
    b.add("body", "spk_l", [-8, 2.5, -5], [4, 7, 4], "speaker")
    b.add("body", "spk_r", [4, 2.5, -5], [4, 7, 4], "speaker")
    for (cx, cz) in ((-7, -5.1), (5, -5.1)):
        b.add("body", "spk_cone_%d" % cx, [cx, 5, cz], [2, 2, 0.4], "pole")
    # lighting truss across the top + 3 spotlights; the glowing lenses live on the
    # glow bone so variant_light toggles the stage lights on/off
    b.add("body", "truss", [-8, 15.5, 3.5], [16, 1, 1], "speaker")
    b.add("body", "truss_l", [-8, 14, 3.7], [1, 1.6, 0.6], "speaker")
    b.add("body", "truss_r", [7, 14, 3.7], [1, 1.6, 0.6], "speaker")
    for lx in (-6, 0, 6):
        b.add("body", "can%d" % lx, [lx - 1.2, 13.6, 2.6], [2.4, 1.9, 2.4], "speaker",
              rotation=[28, 0, 0], pivot=[lx, 15.5, 3.5])
        b.add("glow", "lens%d" % lx, [lx - 1, 12.9, 1.6], [2, 1.2, 1.6], "beam",
              rotation=[28, 0, 0], pivot=[lx, 15.5, 3.5])
    light_decor(sid, b, [{"name": sid, "parent": None, "pivot": [0, 0, 0]},
                         {"name": "body", "parent": sid, "pivot": [0, 0, 0]},
                         {"name": "glow", "parent": sid, "pivot": [0, 12, 2]}], rel, src, 1.8, 1.5)


def main():
    build_drums()
    build_guitar()
    build_jukebox()
    build_mic_stage()


if __name__ == "__main__":
    main()
