"""Emit the Bedrock add-on wiring for the four kid-friendly unicorn furniture.

Per model: behavior entity, client entity, render controller, resources.json
(+ animation / animation_controller where the mechanic needs them).

Mechanics:
  unicorn_rocking_horse      minecraft:rideable (1 seat) + always-on "rock" loop animation
  unicorn_night_lamp         minecraft:variant on/off toggle -> animation controller shows/hides "glow"
  unicorn_ice_cream_machine  no behavior interaction; scripts/main.js gives a treat on interact
  unicorn_cloud_bunk_bed     minecraft:rideable (2 bunks)
"""
import json
import os

HERE = os.path.dirname(__file__)
ADDON = os.path.normpath(os.path.join(HERE, "..", "addon"))
BP = os.path.join(ADDON, "behavior_pack")
RP = os.path.join(ADDON, "resource_pack")
CONTENT = os.path.normpath(os.path.join(HERE, "..", "content", "furniture"))


def write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    print("wrote", path)


def base_components(width, height):
    return {
        "minecraft:type_family": {"family": ["mine_structure_furniture"]},
        "minecraft:collision_box": {"width": width, "height": height},
        "minecraft:health": {"value": 12, "max": 12},
        "minecraft:physics": {"has_gravity": False, "has_collision": True},
        "minecraft:pushable": {"is_pushable": False, "is_pushable_by_piston": False},
    }


def behavior_rideable(sid, width, height, seats):
    components = base_components(width, height)
    components["minecraft:type_family"]["family"].append(sid)
    components["minecraft:rideable"] = {
        "seat_count": len(seats),
        "family_types": ["player"],
        "interact_text": "action.interact.ride",
        "seats": seats,
    }
    return {
        "format_version": "1.20.0",
        "minecraft:entity": {
            "description": {
                "identifier": "mine_structure:" + sid,
                "is_spawnable": True, "is_summonable": True, "is_experimental": False,
            },
            "components": components,
        },
    }


def behavior_lamp(sid):
    interact = lambda text, ev: {
        "interactions": [{
            "interact_text": text, "swing": True, "play_sounds": "random.click",
            "on_interact": {"event": ev, "target": "self"},
        }]
    }
    return {
        "format_version": "1.20.0",
        "minecraft:entity": {
            "description": {
                "identifier": "mine_structure:" + sid,
                "is_spawnable": True, "is_summonable": True, "is_experimental": False,
            },
            "component_groups": {
                "mine_structure:light_off": {
                    "minecraft:variant": {"value": 0},
                    "minecraft:interact": interact("action.interact.light_on", "mine_structure:turn_light_on"),
                },
                "mine_structure:light_on": {
                    "minecraft:variant": {"value": 1},
                    "minecraft:interact": interact("action.interact.light_off", "mine_structure:turn_light_off"),
                },
            },
            "components": {
                **base_components(0.6, 1.3),
                "minecraft:type_family": {"family": ["mine_structure_furniture", sid]},
            },
            "events": {
                "minecraft:entity_spawned": {"add": {"component_groups": ["mine_structure:light_off"]}},
                "mine_structure:turn_light_on": {
                    "remove": {"component_groups": ["mine_structure:light_off"]},
                    "add": {"component_groups": ["mine_structure:light_on"]},
                },
                "mine_structure:turn_light_off": {
                    "remove": {"component_groups": ["mine_structure:light_on"]},
                    "add": {"component_groups": ["mine_structure:light_off"]},
                },
            },
        },
    }


def behavior_static(sid, width, height):
    components = base_components(width, height)
    components["minecraft:type_family"]["family"].append(sid)
    return {
        "format_version": "1.20.0",
        "minecraft:entity": {
            "description": {
                "identifier": "mine_structure:" + sid,
                "is_spawnable": True, "is_summonable": True, "is_experimental": False,
            },
            "components": components,
        },
    }


def client_entity(sid, animations=None, animate=None):
    desc = {
        "identifier": "mine_structure:" + sid,
        "materials": {"default": "entity_alphatest"},
        "textures": {"default": "textures/entity/" + sid + "/" + sid + "_atlas"},
        "geometry": {"default": "geometry." + sid},
        "render_controllers": ["controller.render." + sid],
    }
    if animations:
        desc["animations"] = animations
    if animate:
        desc["scripts"] = {"animate": animate}
    return {"format_version": "1.10.0", "minecraft:client_entity": {"description": desc}}


def render_controller(sid):
    return {
        "format_version": "1.8.0",
        "render_controllers": {
            "controller.render." + sid: {
                "geometry": "Geometry.default",
                "materials": [{"*": "Material.default"}],
                "textures": ["Texture.default"],
            }
        },
    }


def resources(sid, mechanic):
    return {
        "identifier": "mine_structure:" + sid,
        "content_type": "furniture_entity",
        "mechanic": mechanic,
        "behavior_pack": {"entity": "../../addon/behavior_pack/entities/" + sid + ".entity.json"},
        "resource_pack": {
            "client_entity": "../../addon/resource_pack/entity/" + sid + ".entity.json",
            "geometry": "../../addon/resource_pack/models/entity/" + sid + ".geo.json",
            "texture": "../../addon/resource_pack/textures/entity/" + sid + "/" + sid + "_atlas.png",
            "render_controller": "../../addon/resource_pack/render_controllers/" + sid + ".render_controllers.json",
        },
        "blockbench_source": "../../blockbench/" + sid + ".bbmodel",
        "status": {
            "json_links_ready": True,
            "geometry_exported": True,
            "texture_exported": True,
            "in_game_tested": False,
        },
    }


def main():
    # --- rocking horse: rideable + always-on rock loop ---
    horse = "unicorn_rocking_horse"
    write(os.path.join(BP, "entities", horse + ".entity.json"),
          behavior_rideable(horse, 1.2, 1.4, [{"position": [0, 0.9, 0], "lock_rider_rotation": 0}]))
    write(os.path.join(RP, "entity", horse + ".entity.json"),
          client_entity(horse, animations={"rock": "animation." + horse + ".rock"}, animate=["rock"]))
    write(os.path.join(RP, "render_controllers", horse + ".render_controllers.json"), render_controller(horse))
    write(os.path.join(RP, "animations", horse + ".animation.json"), {
        "format_version": "1.8.0",
        "animations": {
            "animation." + horse + ".rock": {
                "loop": True, "animation_length": 2.4,
                "bones": {
                    "rock": {
                        "rotation": {
                            "0.0": [0, 0, 0], "0.6": [7, 0, 0], "1.2": [0, 0, 0],
                            "1.8": [-7, 0, 0], "2.4": [0, 0, 0],
                        }
                    }
                },
            }
        },
    })
    write(os.path.join(CONTENT, horse + ".resources.json"), resources(horse, "rideable"))

    # --- night lamp: variant on/off toggle ---
    lamp = "unicorn_night_lamp"
    write(os.path.join(BP, "entities", lamp + ".entity.json"), behavior_lamp(lamp))
    write(os.path.join(RP, "entity", lamp + ".entity.json"),
          client_entity(lamp,
                        animations={"on": "animation." + lamp + ".on",
                                    "off": "animation." + lamp + ".off",
                                    "light_ctrl": "controller.animation." + lamp + ".light"},
                        animate=["light_ctrl"]))
    write(os.path.join(RP, "render_controllers", lamp + ".render_controllers.json"), render_controller(lamp))
    write(os.path.join(RP, "animations", lamp + ".animation.json"), {
        "format_version": "1.8.0",
        "animations": {
            "animation." + lamp + ".off": {
                "loop": "hold_on_last_frame", "animation_length": 0.05,
                "bones": {"glow": {"scale": [0, 0, 0]}},
            },
            "animation." + lamp + ".on": {
                "loop": True, "animation_length": 2.0,
                "bones": {"glow": {"scale": {"0.0": [1, 1, 1], "1.0": [1.06, 1.06, 1.06], "2.0": [1, 1, 1]}}},
            },
        },
    })
    write(os.path.join(RP, "animation_controllers", lamp + ".animation_controllers.json"), {
        "format_version": "1.10.0",
        "animation_controllers": {
            "controller.animation." + lamp + ".light": {
                "initial_state": "off",
                "states": {
                    "off": {"animations": ["off"], "transitions": [{"on": "q.variant == 1"}]},
                    "on": {"animations": ["on"], "transitions": [{"off": "q.variant == 0"}]},
                },
            }
        },
    })
    write(os.path.join(CONTENT, lamp + ".resources.json"), resources(lamp, "variant_light"))

    # --- ice cream machine: Script API give (no behavior interaction) ---
    machine = "unicorn_ice_cream_machine"
    write(os.path.join(BP, "entities", machine + ".entity.json"), behavior_static(machine, 0.8, 1.6))
    write(os.path.join(RP, "entity", machine + ".entity.json"), client_entity(machine))
    write(os.path.join(RP, "render_controllers", machine + ".render_controllers.json"), render_controller(machine))
    write(os.path.join(CONTENT, machine + ".resources.json"), resources(machine, "script_give"))

    # --- cloud bunk bed: rideable, two bunks, solo can pick top via sneak ---
    # Two component groups carry the same 2 seats in a different ORDER. Bedrock
    # fills the lowest free seat, so the first-listed seat is what a solo player
    # gets. main.js swaps to "order_top" (top listed first) when the player
    # sneak-interacts, then re-seats them; an idle bunk is reset to order_bottom.
    bunk = "unicorn_cloud_bunk_bed"
    bottom_seat = {"position": [0, 0.5, 0], "lock_rider_rotation": 0}
    top_seat = {"position": [0, 1.3, 0], "lock_rider_rotation": 0}

    def rideable_group(first, second):
        return {"minecraft:rideable": {
            "seat_count": 2, "family_types": ["player"],
            "interact_text": "action.interact.ride", "seats": [first, second],
        }}

    write(os.path.join(BP, "entities", bunk + ".entity.json"), {
        "format_version": "1.20.0",
        "minecraft:entity": {
            "description": {
                "identifier": "mine_structure:" + bunk,
                "is_spawnable": True, "is_summonable": True, "is_experimental": False,
            },
            "component_groups": {
                "mine_structure:order_bottom": rideable_group(bottom_seat, top_seat),
                "mine_structure:order_top": rideable_group(top_seat, bottom_seat),
            },
            "components": {
                "minecraft:type_family": {"family": ["mine_structure_furniture", bunk]},
                "minecraft:collision_box": {"width": 1.6, "height": 1.9},
                "minecraft:health": {"value": 12, "max": 12},
                "minecraft:physics": {"has_gravity": False, "has_collision": True},
                "minecraft:pushable": {"is_pushable": False, "is_pushable_by_piston": False},
            },
            "events": {
                "minecraft:entity_spawned": {"add": {"component_groups": ["mine_structure:order_bottom"]}},
                "mine_structure:order_bottom": {
                    "add": {"component_groups": ["mine_structure:order_bottom"]},
                    "remove": {"component_groups": ["mine_structure:order_top"]},
                },
                "mine_structure:order_top": {
                    "add": {"component_groups": ["mine_structure:order_top"]},
                    "remove": {"component_groups": ["mine_structure:order_bottom"]},
                },
            },
        },
    })
    write(os.path.join(RP, "entity", bunk + ".entity.json"), client_entity(bunk))
    write(os.path.join(RP, "render_controllers", bunk + ".render_controllers.json"), render_controller(bunk))
    write(os.path.join(CONTENT, bunk + ".resources.json"), resources(bunk, "rideable_bunk"))


if __name__ == "__main__":
    main()
