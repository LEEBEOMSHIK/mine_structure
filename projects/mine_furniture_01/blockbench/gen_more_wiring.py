"""Emit Bedrock add-on wiring for the four new kid-friendly entities.

  unicorn_baby_pet      tameable walking mob; tamed -> follows owner + rideable
  unicorn_gacha_machine static; scripts/main.js gives a random reward on interact
  unicorn_trampoline    static (stand on top); scripts/main.js bounces players up
  unicorn_gift_box      minecraft:interact opens the lid (animation) + Script gift
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
            "json_links_ready": True, "geometry_exported": True,
            "texture_exported": True, "in_game_tested": False,
        },
    }


TAME_ITEMS = ["minecraft:sugar", "minecraft:apple", "minecraft:cookie"]


def pet_entity(sid):
    behavior = {
        "format_version": "1.20.0",
        "minecraft:entity": {
            "description": {
                "identifier": "mine_structure:" + sid,
                "is_spawnable": True, "is_summonable": True, "is_experimental": False,
            },
            "component_groups": {
                "mine_structure:tamed": {
                    "minecraft:is_tamed": {},
                    "minecraft:behavior.follow_owner": {
                        "priority": 4, "speed_multiplier": 1.2,
                        "start_distance": 4, "stop_distance": 2,
                    },
                    "minecraft:rideable": {
                        "seat_count": 1, "family_types": ["player"],
                        "interact_text": "action.interact.ride",
                        "seats": [{"position": [0, 0.6, 0]}],
                    },
                },
            },
            "components": {
                "minecraft:type_family": {"family": ["mine_structure_pet", sid]},
                "minecraft:collision_box": {"width": 0.7, "height": 0.9},
                "minecraft:health": {"value": 14, "max": 14},
                "minecraft:physics": {},
                "minecraft:movement": {"value": 0.25},
                "minecraft:navigation.walk": {"can_path_over_water": True, "avoid_water": True},
                "minecraft:movement.basic": {},
                "minecraft:jump.static": {},
                "minecraft:behavior.float": {"priority": 0},
                "minecraft:behavior.tempt": {
                    "priority": 4, "speed_multiplier": 1.2, "items": TAME_ITEMS,
                },
                "minecraft:behavior.follow_parent": {"priority": 5, "speed_multiplier": 1.1},
                "minecraft:behavior.random_stroll": {"priority": 6, "speed_multiplier": 1.0},
                "minecraft:behavior.look_at_player": {"priority": 7, "look_distance": 6.0},
                "minecraft:behavior.random_look_around": {"priority": 8},
                "minecraft:tameable": {
                    "probability": 1.0, "tame_items": TAME_ITEMS,
                    "tame_event": {"event": "minecraft:on_tame", "target": "self"},
                },
            },
            "events": {
                "minecraft:on_tame": {"add": {"component_groups": ["mine_structure:tamed"]}},
            },
        },
    }
    write(os.path.join(BP, "entities", sid + ".entity.json"), behavior)
    write(os.path.join(RP, "entity", sid + ".entity.json"),
          client_entity(sid,
                        animations={"idle": "animation." + sid + ".idle",
                                    "walk": "animation." + sid + ".walk",
                                    "move": "controller.animation." + sid + ".move"},
                        animate=["move"]))
    write(os.path.join(RP, "render_controllers", sid + ".render_controllers.json"), render_controller(sid))
    write(os.path.join(RP, "animations", sid + ".animation.json"), {
        "format_version": "1.8.0",
        "animations": {
            "animation." + sid + ".idle": {
                "loop": True, "animation_length": 3.0,
                "bones": {"head": {"rotation": {"0.0": [0, 0, 0], "1.5": [4, 0, 0], "3.0": [0, 0, 0]}}},
            },
            "animation." + sid + ".walk": {
                "loop": True, "animation_length": 1.0,
                "bones": {
                    "leg_fl": {"rotation": {"0.0": [25, 0, 0], "0.5": [-25, 0, 0], "1.0": [25, 0, 0]}},
                    "leg_br": {"rotation": {"0.0": [25, 0, 0], "0.5": [-25, 0, 0], "1.0": [25, 0, 0]}},
                    "leg_fr": {"rotation": {"0.0": [-25, 0, 0], "0.5": [25, 0, 0], "1.0": [-25, 0, 0]}},
                    "leg_bl": {"rotation": {"0.0": [-25, 0, 0], "0.5": [25, 0, 0], "1.0": [-25, 0, 0]}},
                    "head": {"rotation": {"0.0": [0, 0, 0], "0.5": [6, 0, 0], "1.0": [0, 0, 0]}},
                },
            },
        },
    })
    write(os.path.join(RP, "animation_controllers", sid + ".animation_controllers.json"), {
        "format_version": "1.10.0",
        "animation_controllers": {
            "controller.animation." + sid + ".move": {
                "initial_state": "default",
                "states": {
                    "default": {"animations": ["idle"], "transitions": [{"move": "q.modified_move_speed > 0.1"}]},
                    "move": {"animations": ["walk"], "transitions": [{"default": "q.modified_move_speed <= 0.1"}]},
                },
            }
        },
    })
    write(os.path.join(CONTENT, sid + ".resources.json"), resources(sid, "pet"))


def static_entity(sid, width, height, mechanic, interact=None, events=None, animations=None):
    components = {
        "minecraft:type_family": {"family": ["mine_structure_furniture", sid]},
        "minecraft:collision_box": {"width": width, "height": height},
        "minecraft:health": {"value": 12, "max": 12},
        "minecraft:physics": {"has_gravity": False, "has_collision": True},
        "minecraft:pushable": {"is_pushable": False, "is_pushable_by_piston": False},
    }
    if interact:
        components["minecraft:interact"] = interact
    entity = {
        "format_version": "1.20.0",
        "minecraft:entity": {
            "description": {
                "identifier": "mine_structure:" + sid,
                "is_spawnable": True, "is_summonable": True, "is_experimental": False,
            },
            "components": components,
        },
    }
    if events:
        entity["minecraft:entity"]["events"] = events
    write(os.path.join(BP, "entities", sid + ".entity.json"), entity)
    write(os.path.join(RP, "entity", sid + ".entity.json"), client_entity(sid, animations=animations))
    write(os.path.join(RP, "render_controllers", sid + ".render_controllers.json"), render_controller(sid))
    write(os.path.join(CONTENT, sid + ".resources.json"), resources(sid, mechanic))


def car():
    sid = "unicorn_car"
    behavior = {
        "format_version": "1.20.0",
        "minecraft:entity": {
            "description": {
                "identifier": "mine_structure:" + sid,
                "is_spawnable": True, "is_summonable": True, "is_experimental": False,
            },
            "components": {
                "minecraft:type_family": {"family": ["mine_structure_vehicle", sid]},
                "minecraft:collision_box": {"width": 1.2, "height": 0.8},
                "minecraft:health": {"value": 20, "max": 20},
                "minecraft:physics": {},
                "minecraft:movement": {"value": 0.3},
                "minecraft:navigation.walk": {"can_path_over_water": False, "avoid_water": True},
                "minecraft:movement.basic": {},
                "minecraft:jump.static": {},
                "minecraft:behavior.controlled_by_player": {"priority": 0},
                "minecraft:rideable": {
                    "seat_count": 1, "family_types": ["player"], "controlling_seat": 0,
                    "pull_in_entities": False, "interact_text": "action.interact.ride",
                    "seats": [{"position": [0, 0.55, 0], "lock_rider_rotation": 0}],
                },
            },
        },
    }
    write(os.path.join(BP, "entities", sid + ".entity.json"), behavior)
    write(os.path.join(RP, "entity", sid + ".entity.json"),
          client_entity(sid,
                        animations={"roll": "animation." + sid + ".roll",
                                    "wheels": "controller.animation." + sid + ".wheels"},
                        animate=["wheels"]))
    write(os.path.join(RP, "render_controllers", sid + ".render_controllers.json"), render_controller(sid))
    spin = {"rotation": {"0.0": [0, 0, 0], "1.0": [360, 0, 0]}}
    write(os.path.join(RP, "animations", sid + ".animation.json"), {
        "format_version": "1.8.0",
        "animations": {
            "animation." + sid + ".roll": {
                "loop": True, "animation_length": 1.0,
                "bones": {"wheel_fl": spin, "wheel_fr": spin, "wheel_bl": spin, "wheel_br": spin},
            }
        },
    })
    write(os.path.join(RP, "animation_controllers", sid + ".animation_controllers.json"), {
        "format_version": "1.10.0",
        "animation_controllers": {
            "controller.animation." + sid + ".wheels": {
                "initial_state": "default",
                "states": {
                    "default": {"transitions": [{"move": "q.modified_move_speed > 0.05"}]},
                    "move": {"animations": ["roll"], "transitions": [{"default": "q.modified_move_speed <= 0.05"}]},
                },
            }
        },
    })
    write(os.path.join(CONTENT, sid + ".resources.json"), resources(sid, "drive"))


def aquarium():
    sid = "unicorn_aquarium"
    interact = lambda text, ev: {
        "interactions": [{
            "interact_text": text, "swing": True, "play_sounds": "random.click",
            "on_interact": {"event": ev, "target": "self"},
        }]
    }
    behavior = {
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
                "minecraft:type_family": {"family": ["mine_structure_furniture", sid]},
                "minecraft:collision_box": {"width": 1.0, "height": 0.9},
                "minecraft:health": {"value": 12, "max": 12},
                "minecraft:physics": {"has_gravity": False, "has_collision": True},
                "minecraft:pushable": {"is_pushable": False, "is_pushable_by_piston": False},
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
    write(os.path.join(BP, "entities", sid + ".entity.json"), behavior)
    write(os.path.join(RP, "entity", sid + ".entity.json"),
          client_entity(sid,
                        animations={"fish": "animation." + sid + ".fish",
                                    "on": "animation." + sid + ".on",
                                    "off": "animation." + sid + ".off",
                                    "light_ctrl": "controller.animation." + sid + ".light"},
                        animate=["fish", "light_ctrl"]))
    write(os.path.join(RP, "render_controllers", sid + ".render_controllers.json"), render_controller(sid))
    write(os.path.join(RP, "animations", sid + ".animation.json"), {
        "format_version": "1.8.0",
        "animations": {
            "animation." + sid + ".fish": {
                "loop": True, "animation_length": 3.2,
                "bones": {
                    "fish1": {
                        "position": {"0.0": [0, 0, 0], "0.8": [3, 0.4, 0], "1.6": [0, 0, 0],
                                     "2.4": [-3, -0.4, 0], "3.2": [0, 0, 0]},
                        "rotation": {"0.0": [0, 0, 0], "0.8": [0, 14, 0], "1.6": [0, 0, 0],
                                     "2.4": [0, -14, 0], "3.2": [0, 0, 0]},
                    },
                    "fish2": {
                        "position": {"0.0": [0, 0, 0], "0.8": [-2.6, -0.3, 0], "1.6": [0, 0, 0],
                                     "2.4": [2.6, 0.3, 0], "3.2": [0, 0, 0]},
                        "rotation": {"0.0": [0, 0, 0], "0.8": [0, -14, 0], "1.6": [0, 0, 0],
                                     "2.4": [0, 14, 0], "3.2": [0, 0, 0]},
                    },
                },
            },
            "animation." + sid + ".off": {
                "loop": "hold_on_last_frame", "animation_length": 0.05,
                "bones": {"glow": {"scale": [0, 0, 0]}},
            },
            "animation." + sid + ".on": {
                "loop": True, "animation_length": 2.0,
                "bones": {"glow": {"scale": {"0.0": [1, 1, 1], "1.0": [1.05, 1, 1.05], "2.0": [1, 1, 1]}}},
            },
        },
    })
    write(os.path.join(RP, "animation_controllers", sid + ".animation_controllers.json"), {
        "format_version": "1.10.0",
        "animation_controllers": {
            "controller.animation." + sid + ".light": {
                "initial_state": "off",
                "states": {
                    "off": {"animations": ["off"], "transitions": [{"on": "q.variant == 1"}]},
                    "on": {"animations": ["on"], "transitions": [{"off": "q.variant == 0"}]},
                },
            }
        },
    })
    write(os.path.join(CONTENT, sid + ".resources.json"), resources(sid, "variant_light"))


def pegasus():
    sid = "unicorn_pegasus"
    behavior = {
        "format_version": "1.20.0",
        "minecraft:entity": {
            "description": {
                "identifier": "mine_structure:" + sid,
                "is_spawnable": True, "is_summonable": True, "is_experimental": False,
            },
            "components": {
                "minecraft:type_family": {"family": ["mine_structure_pet", sid]},
                "minecraft:collision_box": {"width": 1.0, "height": 1.4},
                "minecraft:health": {"value": 30, "max": 30},
                "minecraft:physics": {"has_gravity": False, "has_collision": True},
                "minecraft:movement": {"value": 0.4},
                "minecraft:movement.fly": {},
                "minecraft:navigation.fly": {"can_path_over_water": True},
                "minecraft:flying_speed": {"value": 0.6},
                "minecraft:jump.static": {},
                "minecraft:behavior.float": {"priority": 1},
                "minecraft:behavior.controlled_by_player": {"priority": 0},
                "minecraft:rideable": {
                    "seat_count": 1, "family_types": ["player"], "controlling_seat": 0,
                    "pull_in_entities": False, "interact_text": "action.interact.ride",
                    "seats": [{"position": [0, 1.0, 0], "lock_rider_rotation": 0}],
                },
            },
        },
    }
    write(os.path.join(BP, "entities", sid + ".entity.json"), behavior)
    write(os.path.join(RP, "entity", sid + ".entity.json"),
          client_entity(sid, animations={"flap": "animation." + sid + ".flap"}, animate=["flap"]))
    write(os.path.join(RP, "render_controllers", sid + ".render_controllers.json"), render_controller(sid))
    write(os.path.join(RP, "animations", sid + ".animation.json"), {
        "format_version": "1.8.0",
        "animations": {
            "animation." + sid + ".flap": {
                "loop": True, "animation_length": 0.8,
                "bones": {
                    "wing_l": {"rotation": {"0.0": [0, 0, 20], "0.4": [0, 0, -15], "0.8": [0, 0, 20]}},
                    "wing_r": {"rotation": {"0.0": [0, 0, -20], "0.4": [0, 0, 15], "0.8": [0, 0, -20]}},
                },
            }
        },
    })
    write(os.path.join(CONTENT, sid + ".resources.json"), resources(sid, "fly"))


def fridge():
    sid = "unicorn_fridge"
    behavior = {
        "format_version": "1.20.0",
        "minecraft:entity": {
            "description": {
                "identifier": "mine_structure:" + sid,
                "is_spawnable": True, "is_summonable": True, "is_experimental": False,
            },
            "components": {
                "minecraft:type_family": {"family": ["mine_structure_furniture", sid]},
                "minecraft:collision_box": {"width": 0.7, "height": 2.0},
                "minecraft:health": {"value": 12, "max": 12},
                "minecraft:physics": {"has_gravity": False, "has_collision": True},
                "minecraft:pushable": {"is_pushable": False, "is_pushable_by_piston": False},
                "minecraft:interact": {"interactions": [{
                    "interact_text": "action.interact.open", "swing": True,
                    "play_sounds": "random.door_open",
                    "on_interact": {"event": "mine_structure:open_fridge", "target": "self"},
                }]},
            },
            "events": {
                "mine_structure:open_fridge": {
                    "queue_command": {"target": "self", "command": "playanimation @s animation." + sid + ".door_open"}
                }
            },
        },
    }
    write(os.path.join(BP, "entities", sid + ".entity.json"), behavior)
    write(os.path.join(RP, "entity", sid + ".entity.json"),
          client_entity(sid, animations={"door_open": "animation." + sid + ".door_open"}))
    write(os.path.join(RP, "render_controllers", sid + ".render_controllers.json"), render_controller(sid))
    write(os.path.join(RP, "animations", sid + ".animation.json"), {
        "format_version": "1.8.0",
        "animations": {
            "animation." + sid + ".door_open": {
                "loop": False, "animation_length": 2.6,
                "bones": {"door": {"rotation": {
                    "0.0": [0, 0, 0], "0.4": [0, -115, 0], "2.0": [0, -115, 0], "2.6": [0, 0, 0],
                }}},
            }
        },
    })
    write(os.path.join(CONTENT, sid + ".resources.json"), resources(sid, "fridge"))


def main():
    pet_entity("unicorn_baby_pet")
    pet_entity("unicorn_baby_dragon")
    car()
    aquarium()
    pegasus()
    fridge()

    static_entity("unicorn_gacha_machine", 0.7, 1.3, "script_give")

    static_entity("unicorn_trampoline", 1.3, 0.45, "script_bounce")

    gift = "unicorn_gift_box"
    static_entity(
        gift, 0.8, 0.9, "interact_give",
        interact={"interactions": [{
            "interact_text": "action.interact.open", "swing": True, "play_sounds": "random.orb",
            "on_interact": {"event": "mine_structure:open_gift", "target": "self"},
        }]},
        events={"mine_structure:open_gift": {
            "queue_command": {"target": "self", "command": "playanimation @s animation." + gift + ".lid_open"}
        }},
        animations={"lid_open": "animation." + gift + ".lid_open"},
    )
    write(os.path.join(RP, "animations", gift + ".animation.json"), {
        "format_version": "1.8.0",
        "animations": {
            "animation." + gift + ".lid_open": {
                "loop": False, "animation_length": 1.6,
                "bones": {"lid": {"rotation": {
                    "0.0": [0, 0, 0], "0.3": [-100, 0, 0], "1.1": [-100, 0, 0], "1.6": [0, 0, 0],
                }}},
            }
        },
    })


if __name__ == "__main__":
    main()
