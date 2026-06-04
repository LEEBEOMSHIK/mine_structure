"""Build editable Blockbench .bbmodel sources for the costume pieces so they can
be opened/edited in Blockbench (the geo.json + atlas already exist from
gen_costume.py). Reuses gen_kids_furniture's Builder/assemble.

The geometry root bone is the player bone the attachable binds to (head / body),
so opened alone in Blockbench the horn/wings float where they'd sit on the player.
"""
import base64
import os

from gen_kids_furniture import Builder, assemble, RP

HERE = os.path.dirname(__file__)


def atlas_b64(sid):
    rel = os.path.join("textures", "entity", sid, sid + ".png")
    with open(os.path.join(RP, rel), "rb") as fh:
        return rel, "data:image/png;base64," + base64.b64encode(fh.read()).decode("ascii")


def build_headband():
    sid = "unicorn_horn_headband"
    rel, src = atlas_b64(sid)
    cm = {"band": (0, 0), "horn": (16, 0), "ear": (32, 0)}
    b = Builder(cm)
    b.add("head", "band", [-4.5, 25.5, -4.5], [9, 2, 9], "band")
    b.add("head", "horn1", [-1, 32, -1], [2, 2.4, 2], "horn")
    b.add("head", "horn2", [-0.7, 34.2, -0.7], [1.4, 2, 1.4], "horn")
    b.add("head", "horn_tip", [-0.45, 35.8, -0.45], [0.9, 1.6, 0.9], "horn")
    b.add("head", "ear_l", [-4.2, 31.5, -1.2], [1.4, 1.8, 1.4], "ear")
    b.add("head", "ear_r", [2.8, 31.5, -1.2], [1.4, 1.8, 1.4], "ear")
    assemble(sid, b, [{"name": "head", "parent": None, "pivot": [0, 24, 0]}], rel, src)


def main():
    # the elytra .bbmodel is written by gen_custom_elytra.py (flat textured wings)
    build_headband()


if __name__ == "__main__":
    main()
