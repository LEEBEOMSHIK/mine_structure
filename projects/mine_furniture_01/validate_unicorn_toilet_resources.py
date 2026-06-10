import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
RESOURCE_PACK = PROJECT_ROOT / "addon" / "resource_pack"
BEHAVIOR_PACK = PROJECT_ROOT / "addon" / "behavior_pack"
FURNITURE_ROOT = PROJECT_ROOT / "content" / "furniture"
WEAPONS_ROOT = PROJECT_ROOT / "content" / "weapons"
BLOCKBENCH_FURNITURE_MODEL = PROJECT_ROOT / "blockbench" / "furniture.bbmodel"
BLOCKBENCH_WEAPON_MODEL = PROJECT_ROOT / "blockbench" / "unicorn_horn_blade.bbmodel"

WEAPONS = {
    "unicorn_horn_blade": {
        "identifier": "mine_structure:unicorn_horn_blade",
        "icon_shortname": "unicorn_horn_blade",
    },
}

SINKS = {
    "unicorn_sink_l": {"identifier": "mine_structure:unicorn_sink_l"},
    "unicorn_sink_island": {"identifier": "mine_structure:unicorn_sink_island"},
    "unicorn_sink_u": {"identifier": "mine_structure:unicorn_sink_u"},
}

KIDS = {
    "unicorn_rocking_horse": {"mechanic": "rideable"},
    "unicorn_night_lamp": {"mechanic": "variant_light"},
    "unicorn_ice_cream_machine": {"mechanic": "script_give"},
    "unicorn_cloud_bunk_bed": {"mechanic": "rideable_bunk"},
    "unicorn_baby_pet": {"mechanic": "pet"},
    "unicorn_gacha_machine": {"mechanic": "script_give"},
    "unicorn_trampoline": {"mechanic": "script_bounce"},
    "unicorn_gift_box": {"mechanic": "interact_give"},
    "unicorn_car": {"mechanic": "drive"},
    "unicorn_baby_dragon": {"mechanic": "pet"},
    "unicorn_aquarium": {"mechanic": "variant_light"},
    "unicorn_pegasus": {"mechanic": "fly"},
    "unicorn_fridge": {"mechanic": "fridge"},
    "unicorn_laptop": {"mechanic": "variant_lid"},
    "unicorn_phone": {"mechanic": "variant_light"},
    "unicorn_tv": {"mechanic": "variant_light"},
    "unicorn_arcade": {"mechanic": "variant_light"},
    "unicorn_vanity": {"mechanic": "variant_light"},
    "unicorn_king_bed": {"mechanic": "rideable_simple"},
    "unicorn_bathtub": {"mechanic": "variant_fill"},
    "unicorn_oven": {"mechanic": "variant_light"},
    "unicorn_microwave": {"mechanic": "variant_light"},
    "unicorn_toaster": {"mechanic": "script_give"},
    "unicorn_robot_vacuum": {"mechanic": "wander"},
    "unicorn_swing": {"mechanic": "rideable"},
    "unicorn_slide": {"mechanic": "rideable_simple"},
    "unicorn_seesaw": {"mechanic": "rideable_simple"},
    "unicorn_sofa": {"mechanic": "rideable_simple"},
    "unicorn_fireplace": {"mechanic": "variant_light"},
    "unicorn_fan": {"mechanic": "variant_spin"},
    "unicorn_bookshelf": {"mechanic": "script_store"},
    "unicorn_wardrobe": {"mechanic": "script_store"},
    "unicorn_piano": {"mechanic": "script_play"},
    "unicorn_cruise": {"mechanic": "boat"},
    "unicorn_carousel": {"mechanic": "rideable_simple"},
    "unicorn_ferris_wheel": {"mechanic": "variant_spin"},
    "unicorn_balloon": {"mechanic": "rideable_simple"},
    "unicorn_castle_tent": {"mechanic": "rideable_simple"},
    "unicorn_dollhouse": {"mechanic": "variant_light"},
    "unicorn_toy_box": {"mechanic": "script_store"},
    "unicorn_easel": {"mechanic": "variant_light"},
    "unicorn_coffee_table": {"mechanic": "static"},
    "unicorn_rug": {"mechanic": "static"},
    "unicorn_wall_clock": {"mechanic": "static"},
    "unicorn_picture_frame": {"mechanic": "static"},
    "unicorn_potted_plant": {"mechanic": "static"},
    "unicorn_floor_lamp": {"mechanic": "variant_light"},
    "unicorn_dresser": {"mechanic": "script_store"},
    "unicorn_nightstand": {"mechanic": "static"},
    "unicorn_fountain": {"mechanic": "variant_light"},
    "unicorn_mailbox": {"mechanic": "static"},
    "unicorn_birdcage": {"mechanic": "static"},
    "unicorn_bench": {"mechanic": "rideable_simple"},
    "unicorn_parasol_table": {"mechanic": "static"},
    "unicorn_campfire": {"mechanic": "variant_light"},
    "unicorn_tent": {"mechanic": "rideable_simple"},
    "unicorn_garden_arch": {"mechanic": "static"},
    "unicorn_coffee_machine": {"mechanic": "script_give"},
    "unicorn_blender": {"mechanic": "variant_light"},
    "unicorn_cake_stand": {"mechanic": "static"},
    "unicorn_cupcake_tower": {"mechanic": "static"},
    "unicorn_water_dispenser": {"mechanic": "variant_light"},
    "unicorn_dish_rack": {"mechanic": "static"},
    "unicorn_bakery_oven": {"mechanic": "script_give"},
    "unicorn_cafe_bar": {"mechanic": "static"},
    "unicorn_birthday_cake": {"mechanic": "variant_light"},
    "unicorn_balloon_bunch": {"mechanic": "static"},
    "unicorn_garland": {"mechanic": "static"},
    "unicorn_chandelier": {"mechanic": "variant_light"},
    "unicorn_wall_sconce": {"mechanic": "variant_light"},
    "unicorn_standing_lantern": {"mechanic": "variant_light"},
    "unicorn_pool": {"mechanic": "variant_fill"},
    "unicorn_sandbox": {"mechanic": "static"},
    "unicorn_teacup": {"mechanic": "variant_spin"},
    "unicorn_ballpit": {"mechanic": "static"},
    "unicorn_junglegym": {"mechanic": "static"},
    "unicorn_clock_tower": {"mechanic": "variant_spin"},
    "unicorn_drums": {"mechanic": "static"},
    "unicorn_guitar": {"mechanic": "static"},
    "unicorn_jukebox": {"mechanic": "script_play"},
    "unicorn_mic_stage": {"mechanic": "variant_light"},
}

FOODS = {
    "unicorn_cookie": {"identifier": "mine_structure:unicorn_cookie", "icon_shortname": "unicorn_cookie"},
    "unicorn_cupcake": {"identifier": "mine_structure:unicorn_cupcake", "icon_shortname": "unicorn_cupcake"},
    "unicorn_lollipop": {"identifier": "mine_structure:unicorn_lollipop", "icon_shortname": "unicorn_lollipop"},
    "unicorn_rainbow_drink": {"identifier": "mine_structure:unicorn_rainbow_drink", "icon_shortname": "unicorn_rainbow_drink"},
    "unicorn_star_candy": {"identifier": "mine_structure:unicorn_star_candy", "icon_shortname": "unicorn_star_candy"},
}

TOOLS = {
    "unicorn_wand": {"identifier": "mine_structure:unicorn_wand", "icon_shortname": "unicorn_wand",
                     "script_marker": "itemUse", "attachable": True},
    "unicorn_transform_wand": {"identifier": "mine_structure:unicorn_transform_wand",
                               "icon_shortname": "unicorn_transform_wand", "script_marker": "transformAnimal",
                               "attachable": True},
}

HELD_ITEMS = {
    "unicorn_phone_item": {"identifier": "mine_structure:unicorn_phone_item", "scripted": True},
}

BLOCKS = {
    "unicorn_cloud_block": {"identifier": "mine_structure:unicorn_cloud_block", "texture": "unicorn_cloud"},
    "unicorn_candy_block": {"identifier": "mine_structure:unicorn_candy_block", "texture": "unicorn_candy"},
    "unicorn_star_block": {"identifier": "mine_structure:unicorn_star_block", "texture": "unicorn_star"},
}

WEARABLES = {
    "unicorn_horn_headband": {"identifier": "mine_structure:unicorn_horn_headband", "slot": "slot.armor.head", "bone": "head"},
    "unicorn_rainbow_skirt": {"identifier": "mine_structure:unicorn_rainbow_skirt", "slot": "slot.armor.legs", "bone": "body"},
}

FURNITURE_BBMODEL_TEXTURE_BY_ROOT = {
    "unicorn_toilet": "unicorn_toilet_atlas.png",
    "unicorn_dining_table": "unicorn_dining_table_atlas.png",
    "unicorn_chair": "unicorn_chair_atlas.png",
    "unicorn_barrel_cabinet": "unicorn_barrel_cabinet_atlas.png",
    "decorative_unicorn_doll": "decorative_unicorn_doll_atlas.png",
}
WEAPON_BBMODEL_TEXTURE_BY_ROOT = {"unicorn_horn_blade": "unicorn_horn_blade.png"}

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


def validate_png(path, failures, expected_size=(64, 64)):
    if not path.is_file():
        failures.append(f"missing texture: {path.relative_to(PROJECT_ROOT)}")
        return

    with path.open("rb") as file:
        if file.read(8) != b"\x89PNG\r\n\x1a\n":
            failures.append(f"{path.name} does not start with a PNG header")

    try:
        from PIL import Image

        with Image.open(path) as image:
            if expected_size is not None and image.size != expected_size:
                failures.append(f"{path.name} size is {image.size}, expected {expected_size}")
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
    if not BLOCKBENCH_FURNITURE_MODEL.is_file():
        failures.append(f"missing Blockbench source: {BLOCKBENCH_FURNITURE_MODEL.relative_to(PROJECT_ROOT)}")
        return

    source = load_json(BLOCKBENCH_FURNITURE_MODEL)
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

    for weapon_id in WEAPONS:
        if weapon_id in root_names:
            failures.append(f"furniture blockbench source still contains weapon root group {weapon_id}")

    if "horn_centerpiece" in json.dumps(source):
        failures.append("blockbench source still contains horn_centerpiece")

    validate_blockbench_face_textures(
        source,
        groups_by_uuid,
        FURNITURE_BBMODEL_TEXTURE_BY_ROOT,
        failures,
    )
    validate_weapon_blockbench_source(failures)


def validate_weapon_blockbench_source(failures):
    if not BLOCKBENCH_WEAPON_MODEL.is_file():
        failures.append(f"missing Blockbench weapon source: {BLOCKBENCH_WEAPON_MODEL.relative_to(PROJECT_ROOT)}")
        return

    source = load_json(BLOCKBENCH_WEAPON_MODEL)
    groups_by_uuid = {
        item.get("uuid"): item.get("name")
        for item in source.get("groups", [])
        if isinstance(item, dict)
    }
    root_names = {
        groups_by_uuid.get(item.get("uuid"))
        for item in source.get("outliner", [])
        if isinstance(item, dict)
    }
    if root_names != {"unicorn_horn_blade"}:
        failures.append(f"weapon blockbench source root groups are {sorted(root_names)}")

    validate_weapon_blockbench_bounds(source, failures)
    validate_blockbench_face_textures(
        source,
        groups_by_uuid,
        WEAPON_BBMODEL_TEXTURE_BY_ROOT,
        failures,
    )
    validate_blockbench_horn_blade_embedded_texture(source, failures)


def validate_weapon_blockbench_bounds(source, failures):
    elements = source.get("elements", [])
    if not elements:
        failures.append("weapon blockbench source has no elements")
        return

    mins = [999, 999, 999]
    maxs = [-999, -999, -999]
    for element in elements:
        for index, value in enumerate(element.get("from", [0, 0, 0])):
            mins[index] = min(mins[index], value)
        for index, value in enumerate(element.get("to", [0, 0, 0])):
            maxs[index] = max(maxs[index], value)

    if mins[0] < -8 or maxs[0] > 8:
        failures.append(f"weapon blockbench source x bounds are {mins[0]}..{maxs[0]}, expected near origin")


def validate_blockbench_face_textures(source, groups_by_uuid, expected_textures, failures):
    textures = source.get("textures", [])
    texture_names = [item.get("name") for item in textures if isinstance(item, dict)]
    missing = [
        texture_name
        for texture_name in expected_textures.values()
        if texture_name not in texture_names
    ]
    if missing:
        failures.append(f"blockbench source is missing textures: {missing}")
        return

    expected_indices = {
        root_name: texture_names.index(texture_name)
        for root_name, texture_name in expected_textures.items()
    }
    root_by_uuid = {}

    def walk(node, root_name):
        if isinstance(node, str):
            root_by_uuid[node] = root_name
            return
        if not isinstance(node, dict):
            return

        current_root = root_name or groups_by_uuid.get(node.get("uuid"))
        for child in node.get("children", []):
            walk(child, current_root)

    for top in source.get("outliner", []):
        walk(top, groups_by_uuid.get(top.get("uuid")) if isinstance(top, dict) else None)

    for element in source.get("elements", []):
        root_name = root_by_uuid.get(element.get("uuid"))
        if root_name not in expected_indices:
            continue

        expected_index = expected_indices[root_name]
        expected_texture = expected_textures[root_name]
        for face_name, face in element.get("faces", {}).items():
            if face.get("texture") != expected_index:
                actual = face.get("texture")
                failures.append(
                    f"blockbench {root_name}/{element.get('name')}/{face_name} "
                    f"uses texture {actual}, expected {expected_texture}"
                )
                return

def validate_blockbench_horn_blade_embedded_texture(source, failures):
    texture = next(
        (
            item
            for item in source.get("textures", [])
            if isinstance(item, dict) and item.get("name") == "unicorn_horn_blade.png"
        ),
        None,
    )
    if not texture:
        failures.append("blockbench source is missing embedded unicorn_horn_blade.png texture")
        return

    source_data = texture.get("source", "")
    prefix = "data:image/png;base64,"
    if not source_data.startswith(prefix):
        failures.append("blockbench unicorn_horn_blade.png texture is not embedded")
        return

    try:
        import base64
        from io import BytesIO
        from PIL import Image
    except ImportError:
        return

    raw = base64.b64decode(source_data[len(prefix):])
    with Image.open(BytesIO(raw)) as image:
        pixels = [
            image.getpixel((x, y))[:3]
            for y in range(16)
            for x in range(16)
        ]

    non_white = [pixel for pixel in pixels if pixel != (255, 255, 255)]
    if len(set(non_white)) < 4:
        failures.append("blockbench embedded unicorn_horn_blade horn swatch is not colorful enough")

    if len(non_white) != len(pixels):
        failures.append("blockbench embedded unicorn_horn_blade horn swatch contains white pixels")


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


def validate_weapon(weapon_id, config, failures):
    expected_identifier = config["identifier"]
    expected_geometry = f"geometry.{weapon_id}"
    icon_shortname = config["icon_shortname"]

    resource_map_path = WEAPONS_ROOT / f"{weapon_id}.resources.json"
    item_path = BEHAVIOR_PACK / "items" / f"{weapon_id}.item.json"
    attachable_path = RESOURCE_PACK / "attachables" / f"{weapon_id}.attachable.json"
    geometry_path = RESOURCE_PACK / "models" / "entity" / f"{weapon_id}.geo.json"
    animation_path = RESOURCE_PACK / "animations" / f"{weapon_id}.animation.json"
    item_texture_path = RESOURCE_PACK / "textures" / "item_texture.json"
    icon_path = RESOURCE_PACK / "textures" / "items" / f"{weapon_id}.png"
    model_texture_path = RESOURCE_PACK / "textures" / "entity" / weapon_id / f"{weapon_id}.png"

    for path in [
        resource_map_path,
        item_path,
        attachable_path,
        geometry_path,
        animation_path,
        item_texture_path,
    ]:
        if not path.is_file():
            failures.append(f"missing file for {weapon_id}: {path.relative_to(PROJECT_ROOT)}")

    validate_png(icon_path, failures, expected_size=(16, 16))
    validate_png(model_texture_path, failures, expected_size=(64, 64))
    if weapon_id == "unicorn_horn_blade":
        validate_horn_blade_texture(model_texture_path, failures)

    if not item_path.is_file() or not attachable_path.is_file() or not item_texture_path.is_file():
        return

    item = load_json(item_path)
    item_identifier = item.get("minecraft:item", {}).get("description", {}).get("identifier")
    if item_identifier != expected_identifier:
        failures.append(f"{weapon_id} item identifier is {item_identifier}, expected {expected_identifier}")

    components = item.get("minecraft:item", {}).get("components", {})
    if "minecraft:damage" not in components:
        failures.append(f"{weapon_id} item is missing minecraft:damage (sword behavior)")
    if components.get("minecraft:enchantable", {}).get("slot") != "sword":
        failures.append(f"{weapon_id} item enchantable slot is not 'sword'")
    if components.get("minecraft:icon", {}).get("texture") != icon_shortname:
        failures.append(f"{weapon_id} item icon does not reference {icon_shortname}")

    attachable = load_json(attachable_path)
    attach_desc = attachable.get("minecraft:attachable", {}).get("description", {})
    if attach_desc.get("identifier") != expected_identifier:
        failures.append(f"{weapon_id} attachable identifier mismatch")
    if attach_desc.get("geometry", {}).get("default") != expected_geometry:
        failures.append(f"{weapon_id} attachable geometry does not reference {expected_geometry}")
    if attach_desc.get("textures", {}).get("default") != f"textures/entity/{weapon_id}/{weapon_id}":
        failures.append(f"{weapon_id} attachable default texture path mismatch")

    item_texture = load_json(item_texture_path)
    texture_data = item_texture.get("texture_data", {})
    if icon_shortname not in texture_data:
        failures.append(f"item_texture.json is missing texture_data.{icon_shortname}")
    elif texture_data[icon_shortname].get("textures") != f"textures/items/{weapon_id}":
        failures.append(f"item_texture.json {icon_shortname} does not point to textures/items/{weapon_id}")

    if geometry_path.is_file():
        geometry = load_json(geometry_path)
        geometry_identifier = geometry.get("minecraft:geometry", [{}])[0].get("description", {}).get("identifier")
        if geometry_identifier != expected_geometry:
            failures.append(f"{weapon_id} geometry identifier is {geometry_identifier}, expected {expected_geometry}")

    resource_map = load_json(resource_map_path) if resource_map_path.is_file() else {}
    if resource_map.get("identifier") != expected_identifier:
        failures.append(f"{weapon_id} resource map identifier mismatch")


def validate_horn_blade_texture(path, failures):
    if not path.is_file():
        return

    try:
        from PIL import Image
    except ImportError:
        return

    with Image.open(path) as image:
        pixels = [
            image.getpixel((x, y))[:3]
            for y in range(16)
            for x in range(16)
        ]

    non_white = [pixel for pixel in pixels if pixel != (255, 255, 255)]
    if len(set(non_white)) < 4:
        failures.append("unicorn_horn_blade horn swatch is not colorful enough")

    if len(non_white) != len(pixels):
        failures.append("unicorn_horn_blade horn swatch contains white pixels")


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


def validate_sink(sid, config, failures):
    expected_identifier = config["identifier"]
    expected_geometry = f"geometry.{sid}"

    resource_map_path = FURNITURE_ROOT / f"{sid}.resources.json"
    behavior_path = BEHAVIOR_PACK / "entities" / f"{sid}.entity.json"
    client_path = RESOURCE_PACK / "entity" / f"{sid}.entity.json"
    geometry_path = RESOURCE_PACK / "models" / "entity" / f"{sid}.geo.json"
    render_path = RESOURCE_PACK / "render_controllers" / f"{sid}.render_controllers.json"
    animation_path = RESOURCE_PACK / "animations" / f"{sid}.animation.json"
    controller_path = RESOURCE_PACK / "animation_controllers" / f"{sid}.animation_controllers.json"
    texture_path = RESOURCE_PACK / "textures" / "entity" / "unicorn_sink" / f"{sid}_atlas.png"
    expected_texture = f"textures/entity/unicorn_sink/{sid}_atlas"
    expected_bbmodel_texture = f"{sid}_atlas.png"

    required = [
        resource_map_path, behavior_path, client_path, geometry_path,
        render_path, animation_path, controller_path,
    ]
    for path in required:
        if not path.is_file():
            failures.append(f"missing file for {sid}: {path.relative_to(PROJECT_ROOT)}")
    validate_png(texture_path, failures)

    if not (behavior_path.is_file() and client_path.is_file()
            and animation_path.is_file() and controller_path.is_file()):
        return

    # behavior: variant water toggle
    behavior = load_json(behavior_path)
    entity = behavior.get("minecraft:entity", {})
    if entity.get("description", {}).get("identifier") != expected_identifier:
        failures.append(f"{sid} behavior identifier mismatch")
    groups = entity.get("component_groups", {})
    for state, value in (("mine_structure:water_off", 0), ("mine_structure:water_on", 1)):
        group = groups.get(state, {})
        if group.get("minecraft:variant", {}).get("value") != value:
            failures.append(f"{sid} {state} does not set minecraft:variant value {value}")
    events = entity.get("events", {})
    for ev in ("mine_structure:turn_water_on", "mine_structure:turn_water_off",
               "minecraft:entity_spawned"):
        if ev not in events:
            failures.append(f"{sid} behavior is missing event {ev}")

    # interaction (water toggle + counter item placement) is handled in main.js
    script = (BEHAVIOR_PACK / "scripts" / "main.js").read_text(encoding="utf-8")
    for snippet in (expected_identifier, "triggerEvent", "placeOnSinkCounter", "toggleSinkWater"):
        if snippet not in script:
            failures.append(f"scripts/main.js is missing {snippet} for {sid}")

    # client entity: shared atlas + animate controller
    client = load_json(client_path)
    desc = client.get("minecraft:client_entity", {}).get("description", {})
    if desc.get("identifier") != expected_identifier:
        failures.append(f"{sid} client identifier mismatch")
    if desc.get("geometry", {}).get("default") != expected_geometry:
        failures.append(f"{sid} client geometry does not reference {expected_geometry}")
    if desc.get("textures", {}).get("default") != expected_texture:
        failures.append(f"{sid} client texture does not reference {expected_texture}")
    if "water_ctrl" not in desc.get("scripts", {}).get("animate", []):
        failures.append(f"{sid} client scripts.animate is missing water_ctrl")
    anims = desc.get("animations", {})
    for key in ("water_on", "water_off", "water_ctrl"):
        if key not in anims:
            failures.append(f"{sid} client animations is missing {key}")

    # geometry: water bones present
    if geometry_path.is_file():
        geometry = load_json(geometry_path)
        geo0 = geometry.get("minecraft:geometry", [{}])[0]
        if geo0.get("description", {}).get("identifier") != expected_geometry:
            failures.append(f"{sid} geometry identifier mismatch")
        bone_names = {b.get("name") for b in geo0.get("bones", [])}
        for bone in ("water_stream", "basin_pool", "faucet", "cabinet"):
            if bone not in bone_names:
                failures.append(f"{sid} geometry is missing bone {bone}")

    # animations: water bones scaled
    animation = load_json(animation_path)
    anim_defs = animation.get("animations", {})
    off = anim_defs.get(f"animation.{sid}.water_off", {})
    if off.get("bones", {}).get("water_stream", {}).get("scale") != [0, 0, 0]:
        failures.append(f"{sid} water_off does not scale water_stream to zero")
    if f"animation.{sid}.water_on" not in anim_defs:
        failures.append(f"{sid} is missing water_on animation")

    # animation controller: off<->flowing on q.variant
    controller = load_json(controller_path)
    ctrl = controller.get("animation_controllers", {}).get(f"controller.animation.{sid}.water", {})
    states = ctrl.get("states", {})
    if "off" not in states or "flowing" not in states:
        failures.append(f"{sid} animation controller is missing off/flowing states")
    else:
        if ctrl.get("initial_state") != "off":
            failures.append(f"{sid} animation controller initial_state is not off")
        if not any("q.variant" in str(t) for t in states["off"].get("transitions", [])):
            failures.append(f"{sid} off state does not transition on q.variant")

    # resource map
    resource_map = load_json(resource_map_path) if resource_map_path.is_file() else {}
    if resource_map.get("identifier") != expected_identifier:
        failures.append(f"{sid} resource map identifier mismatch")
    status = resource_map.get("status", {})
    for key in ("json_links_ready", "geometry_exported", "texture_exported", "water_toggle_ready"):
        if not status.get(key):
            failures.append(f"{sid} resource map status.{key} is not true")

    validate_sink_blockbench_source(sid, failures)


def validate_sink_blockbench_source(sid, failures):
    model_path = PROJECT_ROOT / "blockbench" / f"{sid}.bbmodel"
    if not model_path.is_file():
        failures.append(f"missing Blockbench sink source: {model_path.relative_to(PROJECT_ROOT)}")
        return

    source = load_json(model_path)
    groups_by_uuid = {
        item.get("uuid"): item.get("name")
        for item in source.get("groups", [])
        if isinstance(item, dict)
    }
    root_names = {
        groups_by_uuid.get(item.get("uuid"))
        for item in source.get("outliner", [])
        if isinstance(item, dict)
    }
    if root_names != {sid}:
        failures.append(f"{sid} blockbench source root groups are {sorted(root_names)}")

    texture_names = [t.get("name") for t in source.get("textures", []) if isinstance(t, dict)]
    if texture_names != [f"{sid}_atlas.png"]:
        failures.append(f"{sid} blockbench source textures are {texture_names}, expected [{sid}_atlas.png]")

    for element in source.get("elements", []):
        for face_name, face in element.get("faces", {}).items():
            if face.get("texture") not in (0, None):
                failures.append(
                    f"{sid} blockbench {element.get('name')}/{face_name} uses texture "
                    f"{face.get('texture')}, expected the single embedded atlas"
                )
                return


def validate_single_texture_bbmodel(sid, failures):
    model_path = PROJECT_ROOT / "blockbench" / f"{sid}.bbmodel"
    if not model_path.is_file():
        failures.append(f"missing Blockbench source: {model_path.relative_to(PROJECT_ROOT)}")
        return
    source = load_json(model_path)
    groups_by_uuid = {
        item.get("uuid"): item.get("name")
        for item in source.get("groups", [])
        if isinstance(item, dict)
    }
    root_names = {
        groups_by_uuid.get(item.get("uuid"))
        for item in source.get("outliner", [])
        if isinstance(item, dict)
    }
    if root_names != {sid}:
        failures.append(f"{sid} blockbench source root groups are {sorted(root_names)}")
    texture_names = [t.get("name") for t in source.get("textures", []) if isinstance(t, dict)]
    if texture_names != [f"{sid}_atlas.png"]:
        failures.append(f"{sid} blockbench source textures are {texture_names}, expected [{sid}_atlas.png]")
    for element in source.get("elements", []):
        for face_name, face in element.get("faces", {}).items():
            if face.get("texture") not in (0, None):
                failures.append(
                    f"{sid} blockbench {element.get('name')}/{face_name} uses texture "
                    f"{face.get('texture')}, expected the single embedded atlas"
                )
                return


def validate_kids(sid, config, failures):
    expected_identifier = f"mine_structure:{sid}"
    expected_geometry = f"geometry.{sid}"
    expected_texture = f"textures/entity/{sid}/{sid}_atlas"

    resource_map_path = FURNITURE_ROOT / f"{sid}.resources.json"
    behavior_path = BEHAVIOR_PACK / "entities" / f"{sid}.entity.json"
    client_path = RESOURCE_PACK / "entity" / f"{sid}.entity.json"
    geometry_path = RESOURCE_PACK / "models" / "entity" / f"{sid}.geo.json"
    render_path = RESOURCE_PACK / "render_controllers" / f"{sid}.render_controllers.json"
    texture_path = RESOURCE_PACK / "textures" / "entity" / sid / f"{sid}_atlas.png"

    for path in [resource_map_path, behavior_path, client_path, geometry_path, render_path]:
        if not path.is_file():
            failures.append(f"missing file for {sid}: {path.relative_to(PROJECT_ROOT)}")
    validate_png(texture_path, failures)

    if not (behavior_path.is_file() and client_path.is_file()):
        return

    behavior = load_json(behavior_path)
    entity = behavior.get("minecraft:entity", {})
    if entity.get("description", {}).get("identifier") != expected_identifier:
        failures.append(f"{sid} behavior identifier mismatch")
    components = entity.get("components", {})

    client = load_json(client_path)
    desc = client.get("minecraft:client_entity", {}).get("description", {})
    if desc.get("identifier") != expected_identifier:
        failures.append(f"{sid} client identifier mismatch")
    if desc.get("geometry", {}).get("default") != expected_geometry:
        failures.append(f"{sid} client geometry does not reference {expected_geometry}")
    if desc.get("textures", {}).get("default") != expected_texture:
        failures.append(f"{sid} client texture does not reference {expected_texture}")

    if geometry_path.is_file():
        geometry = load_json(geometry_path)
        if geometry.get("minecraft:geometry", [{}])[0].get("description", {}).get("identifier") != expected_geometry:
            failures.append(f"{sid} geometry identifier mismatch")

    resource_map = load_json(resource_map_path) if resource_map_path.is_file() else {}
    if resource_map.get("identifier") != expected_identifier:
        failures.append(f"{sid} resource map identifier mismatch")
    status = resource_map.get("status", {})
    for key in ("json_links_ready", "geometry_exported", "texture_exported"):
        if not status.get(key):
            failures.append(f"{sid} resource map status.{key} is not true")

    mechanic = config["mechanic"]
    if mechanic == "rideable":
        rideable = components.get("minecraft:rideable")
        if not rideable:
            failures.append(f"{sid} is missing minecraft:rideable")
        else:
            if "player" not in rideable.get("family_types", []):
                failures.append(f"{sid} rideable family_types does not include player")
            if rideable.get("seat_count") != 1:
                failures.append(f"{sid} rideable seat_count is {rideable.get('seat_count')}, expected 1")
        anim_path = RESOURCE_PACK / "animations" / f"{sid}.animation.json"
        if "rock" not in desc.get("scripts", {}).get("animate", []):
            failures.append(f"{sid} client scripts.animate is missing rock")
        if not anim_path.is_file():
            failures.append(f"{sid} is missing rock animation file")
        elif f"animation.{sid}.rock" not in load_json(anim_path).get("animations", {}):
            failures.append(f"{sid} animation file is missing animation.{sid}.rock")

    elif mechanic == "drive":
        rideable = components.get("minecraft:rideable")
        if not rideable:
            failures.append(f"{sid} is missing minecraft:rideable")
        else:
            if rideable.get("controlling_seat") != 0:
                failures.append(f"{sid} rideable controlling_seat is not 0")
            if "player" not in rideable.get("family_types", []):
                failures.append(f"{sid} rideable family_types does not include player")
        if "minecraft:behavior.controlled_by_player" not in components:
            failures.append(f"{sid} is missing minecraft:behavior.controlled_by_player")
        if "minecraft:movement" not in components:
            failures.append(f"{sid} is missing minecraft:movement")
        if "wheels" not in desc.get("scripts", {}).get("animate", []):
            failures.append(f"{sid} client scripts.animate is missing wheels")

    elif mechanic == "fly":
        rideable = components.get("minecraft:rideable")
        if not rideable:
            failures.append(f"{sid} is missing minecraft:rideable")
        else:
            if rideable.get("controlling_seat") != 0:
                failures.append(f"{sid} rideable controlling_seat is not 0")
            if "player" not in rideable.get("family_types", []):
                failures.append(f"{sid} rideable family_types does not include player")
        for comp in ("minecraft:behavior.controlled_by_player", "minecraft:movement.fly",
                     "minecraft:navigation.fly"):
            if comp not in components:
                failures.append(f"{sid} is missing {comp}")
        if "flap" not in desc.get("scripts", {}).get("animate", []):
            failures.append(f"{sid} client scripts.animate is missing flap")
        script = (BEHAVIOR_PACK / "scripts" / "main.js").read_text(encoding="utf-8")
        for snippet in (expected_identifier, "isJumping", "applyImpulse"):
            if snippet not in script:
                failures.append(f"scripts/main.js is missing {snippet} for {sid}")

    elif mechanic == "fridge":
        interact = components.get("minecraft:interact")
        if not interact:
            failures.append(f"{sid} is missing minecraft:interact")
        else:
            has_open = any(
                isinstance(item, dict)
                and item.get("on_interact", {}).get("event") == "mine_structure:open_fridge"
                for item in interact.get("interactions", [])
            )
            if not has_open:
                failures.append(f"{sid} interact does not trigger mine_structure:open_fridge")
        if "mine_structure:open_fridge" not in entity.get("events", {}):
            failures.append(f"{sid} is missing mine_structure:open_fridge event")
        anim_path = RESOURCE_PACK / "animations" / f"{sid}.animation.json"
        if not anim_path.is_file() or f"animation.{sid}.door_open" not in load_json(anim_path).get("animations", {}):
            failures.append(f"{sid} is missing animation.{sid}.door_open")
        if f"animation.{sid}.door_open" not in desc.get("animations", {}).values():
            failures.append(f"{sid} client entity does not register door_open animation")
        script = (BEHAVIOR_PACK / "scripts" / "main.js").read_text(encoding="utf-8")
        for snippet in (expected_identifier, "storeOrRetrieveItem"):
            if snippet not in script:
                failures.append(f"scripts/main.js is missing {snippet} for {sid}")

    elif mechanic == "variant_fill":
        groups = entity.get("component_groups", {})
        for state, value in (("mine_structure:light_off", 0), ("mine_structure:light_on", 1)):
            if groups.get(state, {}).get("minecraft:variant", {}).get("value") != value:
                failures.append(f"{sid} {state} does not set variant {value}")
        if "light_ctrl" not in desc.get("scripts", {}).get("animate", []):
            failures.append(f"{sid} client scripts.animate is missing light_ctrl")
        anim_path = RESOURCE_PACK / "animations" / f"{sid}.animation.json"
        if anim_path.is_file():
            on = load_json(anim_path).get("animations", {}).get(f"animation.{sid}.on", {})
            if "glow" not in str(on.get("bones", {})):
                failures.append(f"{sid} on animation does not fill the glow bone")
        else:
            failures.append(f"{sid} is missing animation file")

    elif mechanic == "boat":
        rideable = components.get("minecraft:rideable")
        if not rideable:
            failures.append(f"{sid} is missing minecraft:rideable")
        else:
            if rideable.get("controlling_seat") != 0:
                failures.append(f"{sid} rideable controlling_seat is not 0")
            if "player" not in rideable.get("family_types", []):
                failures.append(f"{sid} rideable family_types does not include player")
        for comp in ("minecraft:behavior.controlled_by_player", "minecraft:movement", "minecraft:buoyant"):
            if comp not in components:
                failures.append(f"{sid} (boat) is missing {comp}")

    elif mechanic == "variant_spin":
        groups = entity.get("component_groups", {})
        for state, value in (("mine_structure:light_off", 0), ("mine_structure:light_on", 1)):
            if groups.get(state, {}).get("minecraft:variant", {}).get("value") != value:
                failures.append(f"{sid} {state} does not set variant {value}")
        if "light_ctrl" not in desc.get("scripts", {}).get("animate", []):
            failures.append(f"{sid} client scripts.animate is missing light_ctrl")
        anim_path = RESOURCE_PACK / "animations" / f"{sid}.animation.json"
        if anim_path.is_file():
            on = load_json(anim_path).get("animations", {}).get(f"animation.{sid}.on", {})
            if "blades" not in str(on.get("bones", {})):
                failures.append(f"{sid} on animation does not spin the blades bone")
        else:
            failures.append(f"{sid} is missing animation file")

    elif mechanic in ("script_store", "script_play"):
        script = (BEHAVIOR_PACK / "scripts" / "main.js").read_text(encoding="utf-8")
        marker = "storeOrRetrieveItem" if mechanic == "script_store" else "note.harp"
        for snippet in (expected_identifier, marker):
            if snippet not in script:
                failures.append(f"scripts/main.js is missing {snippet} for {sid}")

    elif mechanic == "wander":
        for comp in ("minecraft:movement", "minecraft:navigation.walk",
                     "minecraft:behavior.random_stroll"):
            if comp not in components:
                failures.append(f"{sid} (wander) is missing {comp}")

    elif mechanic == "static":
        pass  # decorative-only entity; file/identifier checks above are sufficient

    elif mechanic == "rideable_simple":
        rideable = components.get("minecraft:rideable")
        if not rideable:
            failures.append(f"{sid} is missing minecraft:rideable")
        elif "player" not in rideable.get("family_types", []):
            failures.append(f"{sid} rideable family_types does not include player")

    elif mechanic == "rideable_bunk":
        groups = entity.get("component_groups", {})
        for group_name in ("mine_structure:order_bottom", "mine_structure:order_top"):
            rideable = groups.get(group_name, {}).get("minecraft:rideable")
            if not rideable:
                failures.append(f"{sid} {group_name} is missing minecraft:rideable")
            elif rideable.get("seat_count") != 2:
                failures.append(f"{sid} {group_name} rideable seat_count is not 2")
        for ev in ("mine_structure:order_top", "mine_structure:order_bottom", "minecraft:entity_spawned"):
            if ev not in entity.get("events", {}):
                failures.append(f"{sid} behavior is missing event {ev}")
        script = (BEHAVIOR_PACK / "scripts" / "main.js").read_text(encoding="utf-8")
        for snippet in (expected_identifier, "rideBunkTop", "triggerEvent"):
            if snippet not in script:
                failures.append(f"scripts/main.js is missing {snippet} for {sid}")

    elif mechanic == "variant_lid":
        groups = entity.get("component_groups", {})
        for state, value in (("mine_structure:lid_open", 0), ("mine_structure:lid_closed", 1)):
            group = groups.get(state, {})
            if group.get("minecraft:variant", {}).get("value") != value:
                failures.append(f"{sid} {state} does not set variant {value}")
            if "minecraft:interact" not in group:
                failures.append(f"{sid} {state} is missing minecraft:interact")
        for ev in ("mine_structure:open_lid", "mine_structure:close_lid", "minecraft:entity_spawned"):
            if ev not in entity.get("events", {}):
                failures.append(f"{sid} behavior is missing event {ev}")
        if "lid_ctrl" not in desc.get("scripts", {}).get("animate", []):
            failures.append(f"{sid} client scripts.animate is missing lid_ctrl")
        controller_path = RESOURCE_PACK / "animation_controllers" / f"{sid}.animation_controllers.json"
        anim_path = RESOURCE_PACK / "animations" / f"{sid}.animation.json"
        if controller_path.is_file():
            ctrl = load_json(controller_path).get("animation_controllers", {}).get(f"controller.animation.{sid}.lid", {})
            if set(ctrl.get("states", {})) != {"open", "closed"}:
                failures.append(f"{sid} lid controller states are not open/closed")
        else:
            failures.append(f"{sid} is missing animation controller")
        if anim_path.is_file():
            anims = load_json(anim_path).get("animations", {})
            for key in (f"animation.{sid}.open", f"animation.{sid}.closed"):
                if key not in anims:
                    failures.append(f"{sid} animation file is missing {key}")
            if "lid" not in str(anims.get(f"animation.{sid}.open", {}).get("bones", {})):
                failures.append(f"{sid} open animation does not rotate the lid bone")
        else:
            failures.append(f"{sid} is missing animation file")
        if geometry_path.is_file():
            geo_bones = {b.get("name") for b in load_json(geometry_path).get("minecraft:geometry", [{}])[0].get("bones", [])}
            if "lid" not in geo_bones:
                failures.append(f"{sid} geometry is missing lid bone")

    elif mechanic == "variant_light":
        groups = entity.get("component_groups", {})
        for state, value in (("mine_structure:light_off", 0), ("mine_structure:light_on", 1)):
            group = groups.get(state, {})
            if group.get("minecraft:variant", {}).get("value") != value:
                failures.append(f"{sid} {state} does not set variant {value}")
            if "minecraft:interact" not in group:
                failures.append(f"{sid} {state} is missing minecraft:interact")
        for ev in ("mine_structure:turn_light_on", "mine_structure:turn_light_off", "minecraft:entity_spawned"):
            if ev not in entity.get("events", {}):
                failures.append(f"{sid} behavior is missing event {ev}")
        if "light_ctrl" not in desc.get("scripts", {}).get("animate", []):
            failures.append(f"{sid} client scripts.animate is missing light_ctrl")
        controller_path = RESOURCE_PACK / "animation_controllers" / f"{sid}.animation_controllers.json"
        anim_path = RESOURCE_PACK / "animations" / f"{sid}.animation.json"
        if not controller_path.is_file():
            failures.append(f"{sid} is missing animation controller")
        else:
            ctrl = load_json(controller_path).get("animation_controllers", {}).get(f"controller.animation.{sid}.light", {})
            if set(ctrl.get("states", {})) != {"off", "on"}:
                failures.append(f"{sid} light controller states are not off/on")
        if anim_path.is_file():
            off = load_json(anim_path).get("animations", {}).get(f"animation.{sid}.off", {})
            if off.get("bones", {}).get("glow", {}).get("scale") != [0, 0, 0]:
                failures.append(f"{sid} off animation does not hide glow")

    elif mechanic == "script_give":
        script = (BEHAVIOR_PACK / "scripts" / "main.js").read_text(encoding="utf-8")
        for snippet in (expected_identifier, "addItem"):
            if snippet not in script:
                failures.append(f"scripts/main.js is missing {snippet} for {sid}")

    elif mechanic == "pet":
        for comp in ("minecraft:tameable", "minecraft:navigation.walk",
                     "minecraft:movement", "minecraft:behavior.float"):
            if comp not in components:
                failures.append(f"{sid} pet is missing {comp}")
        tamed = entity.get("component_groups", {}).get("mine_structure:tamed", {})
        if "minecraft:rideable" not in tamed:
            failures.append(f"{sid} tamed group is missing minecraft:rideable")
        if "minecraft:behavior.follow_owner" not in tamed:
            failures.append(f"{sid} tamed group is missing minecraft:behavior.follow_owner")
        if "minecraft:on_tame" not in entity.get("events", {}):
            failures.append(f"{sid} is missing minecraft:on_tame event")
        if "move" not in desc.get("scripts", {}).get("animate", []):
            failures.append(f"{sid} client scripts.animate is missing move controller")
        anim_path = RESOURCE_PACK / "animations" / f"{sid}.animation.json"
        if anim_path.is_file():
            anims = load_json(anim_path).get("animations", {})
            for key in (f"animation.{sid}.idle", f"animation.{sid}.walk"):
                if key not in anims:
                    failures.append(f"{sid} animation file is missing {key}")
        else:
            failures.append(f"{sid} is missing animation file")
        controller_path = RESOURCE_PACK / "animation_controllers" / f"{sid}.animation_controllers.json"
        if controller_path.is_file():
            ctrl = load_json(controller_path).get("animation_controllers", {}).get(f"controller.animation.{sid}.move", {})
            if set(ctrl.get("states", {})) != {"default", "move"}:
                failures.append(f"{sid} move controller states are not default/move")
        else:
            failures.append(f"{sid} is missing animation controller")

    elif mechanic == "script_bounce":
        script = (BEHAVIOR_PACK / "scripts" / "main.js").read_text(encoding="utf-8")
        for snippet in (expected_identifier, "applyKnockback", "runInterval"):
            if snippet not in script:
                failures.append(f"scripts/main.js is missing {snippet} for {sid}")

    elif mechanic == "interact_give":
        interact = components.get("minecraft:interact")
        events = entity.get("events", {})
        if not interact:
            failures.append(f"{sid} is missing minecraft:interact")
        else:
            has_open = any(
                isinstance(item, dict)
                and item.get("on_interact", {}).get("event") == "mine_structure:open_gift"
                for item in interact.get("interactions", [])
            )
            if not has_open:
                failures.append(f"{sid} interact does not trigger mine_structure:open_gift")
        if "mine_structure:open_gift" not in events:
            failures.append(f"{sid} is missing mine_structure:open_gift event")
        anim_path = RESOURCE_PACK / "animations" / f"{sid}.animation.json"
        if not anim_path.is_file() or f"animation.{sid}.lid_open" not in load_json(anim_path).get("animations", {}):
            failures.append(f"{sid} is missing animation.{sid}.lid_open")
        if f"animation.{sid}.lid_open" not in desc.get("animations", {}).values():
            failures.append(f"{sid} client entity does not register lid_open animation")
        script = (BEHAVIOR_PACK / "scripts" / "main.js").read_text(encoding="utf-8")
        if expected_identifier not in script:
            failures.append(f"scripts/main.js is missing {expected_identifier} for {sid}")

    validate_single_texture_bbmodel(sid, failures)


def validate_food(food_id, config, failures):
    expected_identifier = config["identifier"]
    icon_shortname = config["icon_shortname"]

    item_path = BEHAVIOR_PACK / "items" / f"{food_id}.item.json"
    icon_path = RESOURCE_PACK / "textures" / "items" / f"{food_id}.png"
    item_texture_path = RESOURCE_PACK / "textures" / "item_texture.json"

    for path in [item_path, item_texture_path]:
        if not path.is_file():
            failures.append(f"missing file for {food_id}: {path.relative_to(PROJECT_ROOT)}")
    validate_png(icon_path, failures, expected_size=(16, 16))

    if not item_path.is_file() or not item_texture_path.is_file():
        return

    item = load_json(item_path)
    components = item.get("minecraft:item", {}).get("components", {})
    if item.get("minecraft:item", {}).get("description", {}).get("identifier") != expected_identifier:
        failures.append(f"{food_id} item identifier mismatch")
    if "minecraft:food" not in components:
        failures.append(f"{food_id} item is missing minecraft:food")
    if components.get("minecraft:icon", {}).get("texture") != icon_shortname:
        failures.append(f"{food_id} item icon does not reference {icon_shortname}")

    texture_data = load_json(item_texture_path).get("texture_data", {})
    if icon_shortname not in texture_data:
        failures.append(f"item_texture.json is missing texture_data.{icon_shortname}")

    script = (BEHAVIOR_PACK / "scripts" / "main.js").read_text(encoding="utf-8")
    for snippet in (expected_identifier, "addEffect"):
        if snippet not in script:
            failures.append(f"scripts/main.js is missing {snippet} for {food_id}")


def validate_tool(tool_id, config, failures):
    expected_identifier = config["identifier"]
    icon_shortname = config["icon_shortname"]
    item_path = BEHAVIOR_PACK / "items" / f"{tool_id}.item.json"
    icon_path = RESOURCE_PACK / "textures" / "items" / f"{tool_id}.png"
    item_texture_path = RESOURCE_PACK / "textures" / "item_texture.json"

    if not item_path.is_file():
        failures.append(f"missing item for {tool_id}: {item_path.relative_to(PROJECT_ROOT)}")
    validate_png(icon_path, failures, expected_size=(16, 16))

    if item_path.is_file():
        item = load_json(item_path)
        components = item.get("minecraft:item", {}).get("components", {})
        if item.get("minecraft:item", {}).get("description", {}).get("identifier") != expected_identifier:
            failures.append(f"{tool_id} item identifier mismatch")
        if components.get("minecraft:icon", {}).get("texture") != icon_shortname:
            failures.append(f"{tool_id} item icon does not reference {icon_shortname}")

    if item_texture_path.is_file():
        if icon_shortname not in load_json(item_texture_path).get("texture_data", {}):
            failures.append(f"item_texture.json is missing texture_data.{icon_shortname}")

    script = (BEHAVIOR_PACK / "scripts" / "main.js").read_text(encoding="utf-8")
    for snippet in (expected_identifier, config.get("script_marker", "itemUse")):
        if snippet not in script:
            failures.append(f"scripts/main.js is missing {snippet} for {tool_id}")

    # optional 3D in-hand model (attachable + geometry + atlas), like the held items
    if config.get("attachable"):
        expected_geometry = f"geometry.{tool_id}"
        attachable_path = RESOURCE_PACK / "attachables" / f"{tool_id}.attachable.json"
        geometry_path = RESOURCE_PACK / "models" / "entity" / f"{tool_id}.geo.json"
        atlas_path = RESOURCE_PACK / "textures" / "entity" / tool_id / f"{tool_id}_atlas.png"
        for path in (attachable_path, geometry_path):
            if not path.is_file():
                failures.append(f"missing file for {tool_id}: {path.relative_to(PROJECT_ROOT)}")
        validate_png(atlas_path, failures, expected_size=(64, 64))
        if item_path.is_file() and not load_json(item_path).get(
                "minecraft:item", {}).get("components", {}).get("minecraft:hand_equipped"):
            failures.append(f"{tool_id} item is missing minecraft:hand_equipped for the 3D model")
        if attachable_path.is_file():
            desc = load_json(attachable_path).get("minecraft:attachable", {}).get("description", {})
            if desc.get("identifier") != expected_identifier:
                failures.append(f"{tool_id} attachable identifier mismatch")
            if desc.get("geometry", {}).get("default") != expected_geometry:
                failures.append(f"{tool_id} attachable geometry mismatch")
        if geometry_path.is_file() and load_json(geometry_path).get(
                "minecraft:geometry", [{}])[0].get("description", {}).get("identifier") != expected_geometry:
            failures.append(f"{tool_id} geometry identifier mismatch")


def validate_elytra(failures):
    # custom glider item mine_structure:unicorn_elytra (vanilla elytra untouched)
    sid = "unicorn_elytra"
    ident = "mine_structure:unicorn_elytra"
    item_path = BEHAVIOR_PACK / "items" / f"{sid}.item.json"
    attachable_path = RESOURCE_PACK / "attachables" / f"{sid}.attachable.json"
    geometry_path = RESOURCE_PACK / "models" / "entity" / f"{sid}.geo.json"
    controller_path = RESOURCE_PACK / "animation_controllers" / f"{sid}.animation_controllers.json"
    animation_path = RESOURCE_PACK / "animations" / f"{sid}.animation.json"

    validate_png(RESOURCE_PACK / "textures" / "items" / f"{sid}.png", failures, expected_size=(16, 16))
    validate_png(RESOURCE_PACK / "textures" / "entity" / sid / f"{sid}.png", failures, expected_size=(128, 128))

    if item_path.is_file():
        components = load_json(item_path).get("minecraft:item", {}).get("components", {})
        if components.get("minecraft:wearable", {}).get("slot") != "slot.armor.chest":
            failures.append(f"{sid} wearable slot is not chest")
        if "minecraft:glider" not in components:
            failures.append(f"{sid} is missing minecraft:glider")
    else:
        failures.append(f"missing item {item_path.relative_to(PROJECT_ROOT)}")

    if attachable_path.is_file():
        desc = load_json(attachable_path).get("minecraft:attachable", {}).get("description", {})
        if desc.get("identifier") != ident:
            failures.append(f"{sid} attachable identifier mismatch")
        if desc.get("geometry", {}).get("default") != f"geometry.{sid}":
            failures.append(f"{sid} attachable geometry mismatch")
        if "glide" not in desc.get("scripts", {}).get("animate", []):
            failures.append(f"{sid} attachable scripts.animate is missing glide")
    else:
        failures.append(f"missing attachable {attachable_path.relative_to(PROJECT_ROOT)}")

    if geometry_path.is_file():
        geo = load_json(geometry_path).get("minecraft:geometry", [{}])[0]
        bone_names = {b.get("name") for b in geo.get("bones", [])}
        for bone in ("body", "left_wing", "right_wing"):
            if bone not in bone_names:
                failures.append(f"{sid} geometry is missing bone {bone}")
    else:
        failures.append(f"missing geometry {geometry_path.relative_to(PROJECT_ROOT)}")

    if animation_path.is_file():
        anims = load_json(animation_path).get("animations", {})
        for key in (f"animation.{sid}.folded", f"animation.{sid}.spread"):
            if key not in anims:
                failures.append(f"{sid} animation file is missing {key}")
    else:
        failures.append(f"missing animation {animation_path.relative_to(PROJECT_ROOT)}")

    if controller_path.is_file():
        ctrl = load_json(controller_path).get("animation_controllers", {}).get(f"controller.animation.{sid}.glide", {})
        states = ctrl.get("states", {})
        if set(states) != {"folded", "spread"}:
            failures.append(f"{sid} glide controller states are not folded/spread")
        elif not any("is_gliding" in str(t) for t in states.get("folded", {}).get("transitions", [])):
            failures.append(f"{sid} folded state does not transition on q.is_gliding")
    else:
        failures.append(f"missing animation controller {controller_path.relative_to(PROJECT_ROOT)}")

    item_texture_path = RESOURCE_PACK / "textures" / "item_texture.json"
    if item_texture_path.is_file() and sid not in load_json(item_texture_path).get("texture_data", {}):
        failures.append(f"item_texture.json is missing texture_data.{sid}")


def validate_wearable(sid, config, failures):
    expected_identifier = config["identifier"]
    expected_geometry = f"geometry.{sid}"
    item_path = BEHAVIOR_PACK / "items" / f"{sid}.item.json"
    attachable_path = RESOURCE_PACK / "attachables" / f"{sid}.attachable.json"
    geometry_path = RESOURCE_PACK / "models" / "entity" / f"{sid}.geo.json"
    icon_path = RESOURCE_PACK / "textures" / "items" / f"{sid}.png"
    atlas_path = RESOURCE_PACK / "textures" / "entity" / sid / f"{sid}.png"
    item_texture_path = RESOURCE_PACK / "textures" / "item_texture.json"

    for path in [item_path, attachable_path, geometry_path]:
        if not path.is_file():
            failures.append(f"missing file for {sid}: {path.relative_to(PROJECT_ROOT)}")
    validate_png(icon_path, failures, expected_size=(16, 16))
    validate_png(atlas_path, failures, expected_size=(64, 64))

    if item_path.is_file():
        item = load_json(item_path)
        components = item.get("minecraft:item", {}).get("components", {})
        if item.get("minecraft:item", {}).get("description", {}).get("identifier") != expected_identifier:
            failures.append(f"{sid} item identifier mismatch")
        if components.get("minecraft:wearable", {}).get("slot") != config["slot"]:
            failures.append(f"{sid} wearable slot is not {config['slot']}")

    if attachable_path.is_file():
        desc = load_json(attachable_path).get("minecraft:attachable", {}).get("description", {})
        if desc.get("identifier") != expected_identifier:
            failures.append(f"{sid} attachable identifier mismatch")
        if desc.get("geometry", {}).get("default") != expected_geometry:
            failures.append(f"{sid} attachable geometry does not reference {expected_geometry}")

    if geometry_path.is_file():
        geo = load_json(geometry_path).get("minecraft:geometry", [{}])[0]
        if geo.get("description", {}).get("identifier") != expected_geometry:
            failures.append(f"{sid} geometry identifier mismatch")
        bone_names = {b.get("name") for b in geo.get("bones", [])}
        if config["bone"] not in bone_names:
            failures.append(f"{sid} geometry is missing player bone '{config['bone']}'")

    if item_texture_path.is_file():
        if sid not in load_json(item_texture_path).get("texture_data", {}):
            failures.append(f"item_texture.json is missing texture_data.{sid}")


def validate_held(sid, config, failures):
    expected_identifier = config["identifier"]
    expected_geometry = f"geometry.{sid}"
    item_path = BEHAVIOR_PACK / "items" / f"{sid}.item.json"
    attachable_path = RESOURCE_PACK / "attachables" / f"{sid}.attachable.json"
    geometry_path = RESOURCE_PACK / "models" / "entity" / f"{sid}.geo.json"
    icon_path = RESOURCE_PACK / "textures" / "items" / f"{sid}.png"
    atlas_path = RESOURCE_PACK / "textures" / "entity" / sid / f"{sid}_atlas.png"
    item_texture_path = RESOURCE_PACK / "textures" / "item_texture.json"

    for path in [item_path, attachable_path, geometry_path]:
        if not path.is_file():
            failures.append(f"missing file for {sid}: {path.relative_to(PROJECT_ROOT)}")
    validate_png(icon_path, failures, expected_size=(16, 16))
    validate_png(atlas_path, failures, expected_size=(64, 64))

    if item_path.is_file():
        item = load_json(item_path)
        components = item.get("minecraft:item", {}).get("components", {})
        if item.get("minecraft:item", {}).get("description", {}).get("identifier") != expected_identifier:
            failures.append(f"{sid} item identifier mismatch")
        if not components.get("minecraft:hand_equipped"):
            failures.append(f"{sid} item is missing minecraft:hand_equipped")
        if components.get("minecraft:icon", {}).get("texture") != sid:
            failures.append(f"{sid} item icon does not reference {sid}")

    if attachable_path.is_file():
        desc = load_json(attachable_path).get("minecraft:attachable", {}).get("description", {})
        if desc.get("identifier") != expected_identifier:
            failures.append(f"{sid} attachable identifier mismatch")
        if desc.get("geometry", {}).get("default") != expected_geometry:
            failures.append(f"{sid} attachable geometry mismatch")

    if geometry_path.is_file():
        if load_json(geometry_path).get("minecraft:geometry", [{}])[0].get("description", {}).get("identifier") != expected_geometry:
            failures.append(f"{sid} geometry identifier mismatch")

    if item_texture_path.is_file() and sid not in load_json(item_texture_path).get("texture_data", {}):
        failures.append(f"item_texture.json is missing texture_data.{sid}")

    if config.get("scripted"):
        script = (BEHAVIOR_PACK / "scripts" / "main.js").read_text(encoding="utf-8")
        if expected_identifier not in script:
            failures.append(f"scripts/main.js is missing {expected_identifier} for {sid}")


def validate_block(block_id, config, failures):
    expected_identifier = config["identifier"]
    texture = config["texture"]
    block_path = BEHAVIOR_PACK / "blocks" / f"{block_id}.block.json"
    terrain_path = RESOURCE_PACK / "textures" / "terrain_texture.json"
    texture_path = RESOURCE_PACK / "textures" / "blocks" / f"{texture}.png"

    if not block_path.is_file():
        failures.append(f"missing block for {block_id}: {block_path.relative_to(PROJECT_ROOT)}")
    validate_png(texture_path, failures, expected_size=(16, 16))

    if block_path.is_file():
        block = load_json(block_path)
        desc = block.get("minecraft:block", {}).get("description", {})
        if desc.get("identifier") != expected_identifier:
            failures.append(f"{block_id} block identifier mismatch")
        instances = block.get("minecraft:block", {}).get("components", {}).get("minecraft:material_instances", {})
        if instances.get("*", {}).get("texture") != texture:
            failures.append(f"{block_id} material_instances texture is not {texture}")

    if terrain_path.is_file():
        terrain = load_json(terrain_path).get("texture_data", {})
        if texture not in terrain:
            failures.append(f"terrain_texture.json is missing texture_data.{texture}")
        elif terrain[texture].get("textures") != f"textures/blocks/{texture}":
            failures.append(f"terrain_texture.json {texture} path mismatch")
    else:
        failures.append("missing terrain_texture.json")


def main():
    failures = []

    for content_id, config in FURNITURE.items():
        validate_common_furniture(content_id, config, failures)

    for weapon_id, config in WEAPONS.items():
        validate_weapon(weapon_id, config, failures)

    for food_id, config in FOODS.items():
        validate_food(food_id, config, failures)

    for tool_id, config in TOOLS.items():
        validate_tool(tool_id, config, failures)

    for held_id, config in HELD_ITEMS.items():
        validate_held(held_id, config, failures)

    for block_id, config in BLOCKS.items():
        validate_block(block_id, config, failures)

    for wearable_id, config in WEARABLES.items():
        validate_wearable(wearable_id, config, failures)

    validate_elytra(failures)

    for sink_id, config in SINKS.items():
        validate_sink(sink_id, config, failures)

    for kid_id, config in KIDS.items():
        validate_kids(kid_id, config, failures)

    validate_blockbench_source(failures)

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        raise SystemExit(1)

    print("PASS: furniture resource links are valid")


if __name__ == "__main__":
    main()
