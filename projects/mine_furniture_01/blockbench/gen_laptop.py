"""Unicorn laptop (mine_structure:unicorn_laptop).

A detailed open/close laptop: keyboard deck with individually modelled keys + a
trackpad, and a hinged screen lid. Right-click TOGGLES the lid open/closed
(minecraft:variant + animation controller rotating the "lid" bone). Pastel
unicorn palette, no horn (kept tasteful), with a cute-face screen + heart accent.

Geometry/atlas/bbmodel reuse gen_kids_furniture helpers; wiring is a variant toggle.
"""
import json
import os

from gen_kids_furniture import Builder, assemble, make_atlas

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
BP = os.path.join(BASE, "addon", "behavior_pack")
RP = os.path.join(BASE, "addon", "resource_pack")
CONTENT = os.path.normpath(os.path.join(BASE, "content", "furniture"))
SID = "unicorn_laptop"
# lid is modelled in the OPEN (upright) pose so the screen face reads upright;
# closing rotates it DOWN onto the keyboard.
LID_CLOSE_ANGLE = -100


def write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    print("wrote", path)


def build_model():
    specs = [
        ("shell", (216, 200, 240), "solid"),    # pastel lavender chassis
        ("keys", (238, 230, 248), "solid"),      # light keycaps
        ("pad", (202, 196, 226), "solid"),       # trackpad
        ("bezel", (96, 90, 130), "solid"),       # screen frame (soft, not black)
        ("screen", (190, 226, 250), "face"),     # cute-face display
        ("accent", (244, 182, 214), "solid"),    # pastel pink accent (no horn)
    ]
    atlas_rel, src, cm = make_atlas(SID, specs, 6402)
    b = Builder(cm)

    # --- base (static): deck + trackpad + hinge + keyboard grid ---
    b.add("base", "deck", [-7, 0, -6], [14, 1.5, 11], "shell")
    b.add("base", "front_lip", [-7, 1.5, -6], [14, 0.5, 1], "shell")
    b.add("base", "trackpad", [-2.6, 1.55, -5], [5.2, 0.3, 3.4], "pad")
    b.add("base", "hinge", [-7, 1.4, 4.5], [14, 1.1, 1], "accent")
    # individually modelled keycaps (4 rows x 8 cols)
    x0, dx, kw = -6.0, 1.5, 1.15
    z0, dz, kd = -0.6, 1.15, 0.9
    for r in range(4):
        for c in range(8):
            b.add("base", "key_%d_%d" % (r, c),
                  [x0 + c * dx, 1.5, z0 + r * dz], [kw, 0.45, kd], "keys")
    b.add("base", "spacebar", [-3, 1.5, 3.6], [6, 0.45, 0.8], "keys")

    # --- lid (hinged at the back; rotates open/closed) ---
    # modelled UPRIGHT (open): a vertical panel at the back; the screen sits on its
    # front (north, -Z) face so the cute face reads upright. Closing rotates it down.
    b.add("lid", "lid_panel", [-7, 2, 4.2], [14, 10, 0.8], "shell")
    b.add("lid", "bezel", [-6, 2.6, 3.78], [12, 9, 0.42], "bezel")
    b.add("lid", "screen", [-5, 3.1, 3.55], [10, 7, 0.3], "screen", face_cells={"north": "screen"})
    b.add("lid", "accent_heart", [-1.2, 10.6, 3.7], [2.4, 1.0, 0.3], "accent")

    bone_defs = [
        {"name": SID, "parent": None, "pivot": [0, 0, 0]},
        {"name": "base", "parent": SID, "pivot": [0, 0, 0]},
        {"name": "lid", "parent": SID, "pivot": [0, 1.9, 5.0]},
    ]
    assemble(SID, b, bone_defs, atlas_rel, src)


def interact(text, ev):
    return {"interactions": [{
        "interact_text": text, "swing": True, "play_sounds": "random.click",
        "on_interact": {"event": ev, "target": "self"},
    }]}


def wiring():
    write(os.path.join(BP, "entities", SID + ".entity.json"), {
        "format_version": "1.20.0",
        "minecraft:entity": {
            "description": {"identifier": "mine_structure:" + SID,
                            "is_spawnable": True, "is_summonable": True, "is_experimental": False},
            "component_groups": {
                "mine_structure:lid_open": {"minecraft:variant": {"value": 0},
                                            "minecraft:interact": interact("action.interact.close", "mine_structure:close_lid")},
                "mine_structure:lid_closed": {"minecraft:variant": {"value": 1},
                                              "minecraft:interact": interact("action.interact.open", "mine_structure:open_lid")},
            },
            "components": {
                "minecraft:type_family": {"family": ["mine_structure_furniture", SID]},
                "minecraft:collision_box": {"width": 0.95, "height": 0.6},
                "minecraft:health": {"value": 12, "max": 12},
                "minecraft:physics": {"has_gravity": False, "has_collision": True},
                "minecraft:pushable": {"is_pushable": False, "is_pushable_by_piston": False},
            },
            "events": {
                "minecraft:entity_spawned": {"add": {"component_groups": ["mine_structure:lid_open"]}},
                "mine_structure:close_lid": {"remove": {"component_groups": ["mine_structure:lid_open"]},
                                             "add": {"component_groups": ["mine_structure:lid_closed"]}},
                "mine_structure:open_lid": {"remove": {"component_groups": ["mine_structure:lid_closed"]},
                                            "add": {"component_groups": ["mine_structure:lid_open"]}},
            },
        },
    })
    write(os.path.join(RP, "entity", SID + ".entity.json"), {
        "format_version": "1.10.0",
        "minecraft:client_entity": {"description": {
            "identifier": "mine_structure:" + SID,
            "materials": {"default": "entity_alphatest"},
            "textures": {"default": "textures/entity/" + SID + "/" + SID + "_atlas"},
            "geometry": {"default": "geometry." + SID},
            "animations": {"open": "animation." + SID + ".open", "closed": "animation." + SID + ".closed",
                           "lid_ctrl": "controller.animation." + SID + ".lid"},
            "scripts": {"animate": ["lid_ctrl"]},
            "render_controllers": ["controller.render." + SID],
        }},
    })
    write(os.path.join(RP, "render_controllers", SID + ".render_controllers.json"), {
        "format_version": "1.8.0",
        "render_controllers": {"controller.render." + SID: {
            "geometry": "Geometry.default", "materials": [{"*": "Material.default"}], "textures": ["Texture.default"]}},
    })
    write(os.path.join(RP, "animations", SID + ".animation.json"), {
        "format_version": "1.8.0",
        "animations": {
            "animation." + SID + ".open": {"loop": "hold_on_last_frame", "animation_length": 0.45,
                                           "bones": {"lid": {"rotation": {"0.0": [0, 0, 0], "0.45": [0, 0, 0]}}}},
            "animation." + SID + ".closed": {"loop": "hold_on_last_frame", "animation_length": 0.45,
                                             "bones": {"lid": {"rotation": {"0.0": [0, 0, 0], "0.45": [LID_CLOSE_ANGLE, 0, 0]}}}},
        },
    })
    write(os.path.join(RP, "animation_controllers", SID + ".animation_controllers.json"), {
        "format_version": "1.10.0",
        "animation_controllers": {"controller.animation." + SID + ".lid": {
            "initial_state": "open",
            "states": {"open": {"animations": ["open"], "transitions": [{"closed": "q.variant == 1"}]},
                       "closed": {"animations": ["closed"], "transitions": [{"open": "q.variant == 0"}]}}}},
    })
    write(os.path.join(CONTENT, SID + ".resources.json"), {
        "identifier": "mine_structure:" + SID, "content_type": "furniture_entity", "mechanic": "variant_lid",
        "behavior_pack": {"entity": "../../addon/behavior_pack/entities/" + SID + ".entity.json"},
        "resource_pack": {
            "client_entity": "../../addon/resource_pack/entity/" + SID + ".entity.json",
            "geometry": "../../addon/resource_pack/models/entity/" + SID + ".geo.json",
            "texture": "../../addon/resource_pack/textures/entity/" + SID + "/" + SID + "_atlas.png",
            "render_controller": "../../addon/resource_pack/render_controllers/" + SID + ".render_controllers.json",
            "animation": "../../addon/resource_pack/animations/" + SID + ".animation.json",
            "animation_controller": "../../addon/resource_pack/animation_controllers/" + SID + ".animation_controllers.json",
        },
        "blockbench_source": "../../blockbench/" + SID + ".bbmodel",
        "status": {"json_links_ready": True, "geometry_exported": True, "texture_exported": True, "in_game_tested": False},
    })


def main():
    build_model()
    wiring()


if __name__ == "__main__":
    main()
