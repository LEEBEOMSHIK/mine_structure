import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
RESOURCE_PACK = PROJECT_ROOT / "addon" / "resource_pack"
BEHAVIOR_PACK = PROJECT_ROOT / "addon" / "behavior_pack"
FURNITURE_ROOT = PROJECT_ROOT / "content" / "furniture"
BLOCKBENCH_MODEL = PROJECT_ROOT / "blockbench" / "furniture.bbmodel"

FURNITURE = {
    "unicorn_toilet": {
        "identifier": "mine_structure:unicorn_toilet",
        "requires_flush": True,
    },
    "unicorn_dining_table": {
        "identifier": "mine_structure:unicorn_dining_table",
        "requires_flush": False,
        "requires_table_script": True,
    },
    "unicorn_chair": {
        "identifier": "mine_structure:unicorn_chair",
        "requires_flush": False,
        "requires_rideable": True,
    },
    "unicorn_barrel_cabinet": {
        "identifier": "mine_structure:unicorn_barrel_cabinet",
        "requires_flush": False,
        "requires_storage_script": True,
    },
    "decorative_unicorn_doll": {
        "identifier": "mine_structure:decorative_unicorn_doll",
        "requires_flush": False,
        "requires_static_decoration": True,
    },
}


def load_json(path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def validate_png(path, failures):
    if not path.is_file():
        failures.append(f"missing texture atlas: {path.relative_to(PROJECT_ROOT)}")
        return

    with path.open("rb") as file:
        if file.read(8) != b"\x89PNG\r\n\x1a\n":
            failures.append(f"{path.name} does not start with a PNG header")

    try:
        from PIL import Image

        with Image.open(path) as image:
            if image.size != (64, 64):
                failures.append(f"{path.name} size is {image.size}, expected (64, 64)")
    except ImportError:
        pass


def validate_common_furniture(content_id, config, failures):
    expected_identifier = config["identifier"]
    expected_geometry = f"geometry.{content_id}"
    expected_texture = f"textures/entity/{content_id}/{content_id}_atlas"

    resource_map_path = FURNITURE_ROOT / f"{content_id}.resources.json"
    behavior_entity_path = BEHAVIOR_PACK / "entities" / f"{content_id}.entity.json"
    client_entity_path = RESOURCE_PACK / "entity" / f"{content_id}.entity.json"
    geometry_path = RESOURCE_PACK / "models" / "entity" / f"{content_id}.geo.json"
    texture_path = RESOURCE_PACK / "textures" / "entity" / content_id / f"{content_id}_atlas.png"
    render_controller_path = RESOURCE_PACK / "render_controllers" / f"{content_id}.render_controllers.json"

    for path in [
        resource_map_path,
        behavior_entity_path,
        client_entity_path,
        geometry_path,
        render_controller_path,
    ]:
        if not path.is_file():
            failures.append(f"missing file for {content_id}: {path.relative_to(PROJECT_ROOT)}")

    validate_png(texture_path, failures)

    if not resource_map_path.is_file() or not behavior_entity_path.is_file() or not client_entity_path.is_file():
        return

    resource_map = load_json(resource_map_path)
    behavior_entity = load_json(behavior_entity_path)
    client_entity = load_json(client_entity_path)

    if resource_map.get("identifier") != expected_identifier:
        failures.append(f"{content_id} resource map identifier mismatch")

    behavior_identifier = behavior_entity.get("minecraft:entity", {}).get("description", {}).get("identifier")
    if behavior_identifier != expected_identifier:
        failures.append(f"{content_id} behavior identifier is {behavior_identifier}")

    client_description = client_entity.get("minecraft:client_entity", {}).get("description", {})
    if client_description.get("identifier") != expected_identifier:
        failures.append(f"{content_id} client identifier mismatch")

    if client_description.get("geometry", {}).get("default") != expected_geometry:
        failures.append(f"{content_id} client geometry does not reference {expected_geometry}")

    if client_description.get("textures", {}).get("default") != expected_texture:
        failures.append(f"{content_id} client texture does not reference {expected_texture}")

    if geometry_path.is_file():
        geometry = load_json(geometry_path)
        geometry_identifier = geometry.get("minecraft:geometry", [{}])[0].get("description", {}).get("identifier")
        if geometry_identifier != expected_geometry:
            failures.append(f"{content_id} geometry identifier is {geometry_identifier}, expected {expected_geometry}")

    status = resource_map.get("status", {})
    for key in ["json_links_ready", "geometry_exported", "texture_exported"]:
        if not status.get(key):
            failures.append(f"{content_id} resource map status.{key} is not true")

    if config["requires_flush"]:
        validate_flush_behavior(resource_map, behavior_entity, failures)

    if config.get("requires_rideable"):
        validate_chair_rideable(content_id, behavior_entity, failures)

    if config.get("requires_table_script"):
        validate_table_interaction(content_id, behavior_entity, failures)

    if config.get("requires_storage_script"):
        validate_storage_interaction(content_id, behavior_entity, failures)

    if config.get("requires_static_decoration"):
        validate_static_decoration(content_id, behavior_entity, failures)


def validate_blockbench_source(failures):
    if not BLOCKBENCH_MODEL.is_file():
        failures.append(f"missing Blockbench source: {BLOCKBENCH_MODEL.relative_to(PROJECT_ROOT)}")
        return

    source = load_json(BLOCKBENCH_MODEL)
    groups_by_uuid = {
        item.get("uuid"): item.get("name")
        for item in source.get("groups", [])
        if isinstance(item, dict)
    }
    roots = source.get("outliner", [])
    root_names = {
        groups_by_uuid.get(item.get("uuid"))
        for item in roots
        if isinstance(item, dict)
    }

    for content_id in FURNITURE:
        if content_id not in root_names:
            failures.append(f"blockbench source is missing root group {content_id}")

    if "horn_centerpiece" in json.dumps(source):
        failures.append("blockbench source still contains horn_centerpiece")


def validate_chair_rideable(content_id, behavior_entity, failures):
    components = behavior_entity.get("minecraft:entity", {}).get("components", {})
    rideable = components.get("minecraft:rideable")
    if not rideable:
        failures.append(f"{content_id} behavior entity is missing minecraft:rideable")
        return

    if rideable.get("seat_count") != 1:
        failures.append(f"{content_id} rideable seat_count is not 1")

    if "player" not in rideable.get("family_types", []):
        failures.append(f"{content_id} rideable family_types does not include player")

    seats = rideable.get("seats", {})
    position = seats.get("position") if isinstance(seats, dict) else None
    if position != [0, 0.55, 0]:
        failures.append(f"{content_id} rideable seat position is {position}, expected [0, 0.55, 0]")


def validate_table_interaction(content_id, behavior_entity, failures):
    components = behavior_entity.get("minecraft:entity", {}).get("components", {})
    interact = components.get("minecraft:interact")
    if not interact:
        failures.append(f"{content_id} behavior entity is missing minecraft:interact")
    else:
        interactions = interact.get("interactions", [])
        has_table_interaction = any(
            isinstance(item, dict)
            and item.get("on_interact", {}).get("event") == "mine_structure:table_interact"
            for item in interactions
        )
        if not has_table_interaction:
            failures.append(f"{content_id} interact does not trigger mine_structure:table_interact")

    manifest_path = BEHAVIOR_PACK / "manifest.json"
    script_path = BEHAVIOR_PACK / "scripts" / "main.js"
    manifest = load_json(manifest_path)
    modules = manifest.get("modules", [])
    dependencies = manifest.get("dependencies", [])
    has_script_module = any(
        module.get("type") == "script" and module.get("entry") == "scripts/main.js"
        for module in modules
        if isinstance(module, dict)
    )
    has_server_dependency = any(
        dependency.get("module_name") == "@minecraft/server"
        for dependency in dependencies
        if isinstance(dependency, dict)
    )
    if not has_script_module:
        failures.append("behavior manifest is missing scripts/main.js script module")
    if not has_server_dependency:
        failures.append("behavior manifest is missing @minecraft/server dependency")
    if not script_path.is_file():
        failures.append("behavior pack is missing scripts/main.js")
        return

    script = script_path.read_text(encoding="utf-8")
    required_snippets = [
        "world.afterEvents.playerInteractWithEntity.subscribe",
        "mine_structure:unicorn_dining_table",
        "spawnItem",
        "EquipmentSlot.Mainhand",
    ]
    for snippet in required_snippets:
        if snippet not in script:
            failures.append(f"scripts/main.js is missing {snippet}")


def validate_storage_interaction(content_id, behavior_entity, failures):
    components = behavior_entity.get("minecraft:entity", {}).get("components", {})
    interact = components.get("minecraft:interact")
    if not interact:
        failures.append(f"{content_id} behavior entity is missing minecraft:interact")
    else:
        interactions = interact.get("interactions", [])
        has_storage_interaction = any(
            isinstance(item, dict)
            and item.get("on_interact", {}).get("event") == "mine_structure:storage_interact"
            for item in interactions
        )
        if not has_storage_interaction:
            failures.append(f"{content_id} interact does not trigger mine_structure:storage_interact")

    script_path = BEHAVIOR_PACK / "scripts" / "main.js"
    if not script_path.is_file():
        failures.append("behavior pack is missing scripts/main.js")
        return

    script = script_path.read_text(encoding="utf-8")
    required_snippets = [
        "mine_structure:unicorn_barrel_cabinet",
        "barrel_storage_items",
        "getDynamicProperty",
        "setDynamicProperty",
        "ItemStack",
    ]
    for snippet in required_snippets:
        if snippet not in script:
            failures.append(f"scripts/main.js is missing {snippet}")


def validate_static_decoration(content_id, behavior_entity, failures):
    components = behavior_entity.get("minecraft:entity", {}).get("components", {})
    if "minecraft:interact" in components:
        failures.append(f"{content_id} should be static decoration without minecraft:interact")
    if "minecraft:rideable" in components:
        failures.append(f"{content_id} should be static decoration without minecraft:rideable")


def validate_flush_behavior(resource_map, behavior_entity, failures):
    sound_definitions_path = RESOURCE_PACK / "sounds" / "sound_definitions.json"
    sound_path = RESOURCE_PACK / "sounds" / "flush.ogg"

    if not sound_path.is_file():
        failures.append(f"missing sound file: {sound_path.relative_to(PROJECT_ROOT)}")
    elif sound_path.stat().st_size == 0:
        failures.append(f"empty sound file: {sound_path.relative_to(PROJECT_ROOT)}")
    else:
        with sound_path.open("rb") as file:
            if file.read(4) != b"OggS":
                failures.append("flush.ogg does not start with an OggS header")

    sound_definitions = load_json(sound_definitions_path)
    flush = sound_definitions.get("sound_definitions", {}).get("flush")
    if not flush:
        failures.append("sound_definitions.json is missing sound_definitions.flush")
    else:
        sounds = flush.get("sounds", [])
        names = [sound.get("name") for sound in sounds if isinstance(sound, dict)]
        if "sounds/flush" not in names:
            failures.append("sound_definitions.flush does not reference sounds/flush")

    mapped_sound = resource_map.get("resource_pack", {}).get("sound")
    if mapped_sound != "../../addon/resource_pack/sounds/flush.ogg":
        failures.append("unicorn_toilet resource map sound path does not point to flush.ogg")

    if not resource_map.get("status", {}).get("sound_added"):
        failures.append("unicorn_toilet resource map status.sound_added is not true")

    behavior_root = behavior_entity.get("minecraft:entity", {})
    interact = behavior_root.get("components", {}).get("minecraft:interact")
    if not interact:
        failures.append("unicorn_toilet behavior entity is missing minecraft:interact")
    else:
        interactions = interact.get("interactions", [])
        has_flush_interaction = any(
            isinstance(item, dict)
            and item.get("on_interact", {}).get("event") == "mine_structure:flush"
            and item.get("play_sounds") == "flush"
            for item in interactions
        )
        if not has_flush_interaction:
            failures.append("unicorn_toilet interact does not trigger mine_structure:flush with flush sound")

    flush_event = behavior_root.get("events", {}).get("mine_structure:play_flush", {})
    queued_command = flush_event.get("queue_command", {}).get("command")
    if queued_command != "playanimation @s animation.unicorn_toilet.flush":
        failures.append("mine_structure:play_flush does not queue the flush playanimation command")


def main():
    failures = []

    for content_id, config in FURNITURE.items():
        validate_common_furniture(content_id, config, failures)

    validate_blockbench_source(failures)

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        raise SystemExit(1)

    print("PASS: furniture resource links are valid")


if __name__ == "__main__":
    main()
