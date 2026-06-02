"""Emit the Bedrock add-on wiring for the three unicorn sinks.

Per sink it writes:
  behavior_pack/entities/<id>.entity.json          variant water on/off toggle
  resource_pack/entity/<id>.entity.json            client entity (shared atlas)
  resource_pack/render_controllers/<id>.render_controllers.json
  resource_pack/animations/<id>.animation.json     water_on / water_off (scale water bones)
  resource_pack/animation_controllers/<id>.animation_controllers.json  off<->flowing on q.variant

Water state is persistent: minecraft:variant (0 off / 1 on) drives the resource-side
animation controller, so it survives chunk reloads. The faucet uses vanilla water
sounds (bucket.fill_water / bucket.empty_water) so no custom audio asset is needed.
"""
import json
import os

HERE = os.path.dirname(__file__)
ADDON = os.path.normpath(os.path.join(HERE, "..", "addon"))
BP = os.path.join(ADDON, "behavior_pack")
RP = os.path.join(ADDON, "resource_pack")
CONTENT = os.path.normpath(os.path.join(HERE, "..", "content", "furniture"))

SINKS = ["unicorn_sink_l", "unicorn_sink_island", "unicorn_sink_u"]


def write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    print("wrote", path)


def behavior(sid):
    ident = "mine_structure:" + sid
    interact = lambda text, ev, snd: {
        "interactions": [{
            "interact_text": text,
            "swing": True,
            "play_sounds": snd,
            "on_interact": {"event": ev, "target": "self"},
        }]
    }
    return {
        "format_version": "1.20.0",
        "minecraft:entity": {
            "description": {
                "identifier": ident,
                "is_spawnable": True,
                "is_summonable": True,
                "is_experimental": False,
            },
            "component_groups": {
                "mine_structure:water_off": {
                    "minecraft:variant": {"value": 0},
                    "minecraft:interact": interact(
                        "action.interact.water_on",
                        "mine_structure:turn_water_on",
                        "bucket.fill_water",
                    ),
                },
                "mine_structure:water_on": {
                    "minecraft:variant": {"value": 1},
                    "minecraft:interact": interact(
                        "action.interact.water_off",
                        "mine_structure:turn_water_off",
                        "bucket.empty_water",
                    ),
                },
            },
            "components": {
                "minecraft:type_family": {"family": ["mine_structure_furniture", "unicorn_sink"]},
                "minecraft:collision_box": {"width": 3.0, "height": 1.0},
                "minecraft:health": {"value": 12, "max": 12},
                "minecraft:physics": {"has_gravity": False, "has_collision": True},
                "minecraft:pushable": {"is_pushable": False, "is_pushable_by_piston": False},
            },
            "events": {
                "minecraft:entity_spawned": {"add": {"component_groups": ["mine_structure:water_off"]}},
                "mine_structure:turn_water_on": {
                    "remove": {"component_groups": ["mine_structure:water_off"]},
                    "add": {"component_groups": ["mine_structure:water_on"]},
                },
                "mine_structure:turn_water_off": {
                    "remove": {"component_groups": ["mine_structure:water_on"]},
                    "add": {"component_groups": ["mine_structure:water_off"]},
                },
            },
        },
    }


def client_entity(sid):
    return {
        "format_version": "1.10.0",
        "minecraft:client_entity": {
            "description": {
                "identifier": "mine_structure:" + sid,
                "materials": {"default": "entity_alphatest"},
                "textures": {"default": "textures/entity/unicorn_sink/" + sid + "_atlas"},
                "geometry": {"default": "geometry." + sid},
                "animations": {
                    "water_on": "animation." + sid + ".water_on",
                    "water_off": "animation." + sid + ".water_off",
                    "water_ctrl": "controller.animation." + sid + ".water",
                },
                "scripts": {"animate": ["water_ctrl"]},
                "render_controllers": ["controller.render." + sid],
            }
        },
    }


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


def animations(sid):
    return {
        "format_version": "1.8.0",
        "animations": {
            "animation." + sid + ".water_off": {
                "loop": "hold_on_last_frame",
                "animation_length": 0.05,
                "bones": {
                    "water_stream": {"scale": [0, 0, 0]},
                    "basin_pool": {"scale": [0, 0, 0]},
                },
            },
            "animation." + sid + ".water_on": {
                "loop": True,
                "animation_length": 1.2,
                "bones": {
                    "water_stream": {
                        "scale": {"0.0": [1, 1, 1], "1.2": [1, 1, 1]},
                        "position": {
                            "0.0": [0, 0, 0],
                            "0.3": [0, -0.18, 0],
                            "0.6": [0, 0, 0],
                            "0.9": [0, -0.18, 0],
                            "1.2": [0, 0, 0],
                        },
                    },
                    "basin_pool": {
                        "scale": {"0.0": [1, 1, 1], "0.6": [1.05, 1, 1.05], "1.2": [1, 1, 1]},
                    },
                },
            },
        },
    }


def anim_controller(sid):
    return {
        "format_version": "1.10.0",
        "animation_controllers": {
            "controller.animation." + sid + ".water": {
                "initial_state": "off",
                "states": {
                    "off": {
                        "animations": ["water_off"],
                        "transitions": [{"flowing": "q.variant == 1"}],
                    },
                    "flowing": {
                        "animations": ["water_on"],
                        "transitions": [{"off": "q.variant == 0"}],
                    },
                },
            }
        },
    }


def resources(sid):
    return {
        "identifier": "mine_structure:" + sid,
        "content_type": "furniture_entity",
        "behavior_pack": {
            "entity": "../../addon/behavior_pack/entities/" + sid + ".entity.json",
        },
        "resource_pack": {
            "client_entity": "../../addon/resource_pack/entity/" + sid + ".entity.json",
            "geometry": "../../addon/resource_pack/models/entity/" + sid + ".geo.json",
            "texture": "../../addon/resource_pack/textures/entity/unicorn_sink/" + sid + "_atlas.png",
            "render_controller": "../../addon/resource_pack/render_controllers/" + sid + ".render_controllers.json",
            "animation": "../../addon/resource_pack/animations/" + sid + ".animation.json",
            "animation_controller": "../../addon/resource_pack/animation_controllers/" + sid + ".animation_controllers.json",
        },
        "blockbench_source": "../../blockbench/" + sid + ".bbmodel",
        "status": {
            "json_links_ready": True,
            "geometry_exported": True,
            "texture_exported": True,
            "water_toggle_ready": True,
            "in_game_tested": False,
        },
    }


def main():
    for sid in SINKS:
        write(os.path.join(CONTENT, sid + ".resources.json"), resources(sid))
        write(os.path.join(BP, "entities", sid + ".entity.json"), behavior(sid))
        write(os.path.join(RP, "entity", sid + ".entity.json"), client_entity(sid))
        write(os.path.join(RP, "render_controllers", sid + ".render_controllers.json"), render_controller(sid))
        write(os.path.join(RP, "animations", sid + ".animation.json"), animations(sid))
        write(os.path.join(RP, "animation_controllers", sid + ".animation_controllers.json"), anim_controller(sid))


if __name__ == "__main__":
    main()
