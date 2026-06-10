import { EntityComponentTypes, EquipmentSlot, ItemStack, system, world } from "@minecraft/server";

const TABLE_ID = "mine_structure:unicorn_dining_table";
const STORAGE_ID = "mine_structure:unicorn_barrel_cabinet";
const STORAGE_PROPERTY = "barrel_storage_items";
const STORAGE_MAX_SLOTS = 9;
const ICE_CREAM_ID = "mine_structure:unicorn_ice_cream_machine";
const ICE_CREAM_TREATS = [
  "minecraft:cookie",
  "minecraft:sweet_berries",
  "minecraft:glow_berries",
  "minecraft:pumpkin_pie",
  "minecraft:honey_bottle",
];
const TOASTER_ID = "mine_structure:unicorn_toaster";
const BOOKSHELF_ID = "mine_structure:unicorn_bookshelf";
const BOOKSHELF_PROPERTY = "bookshelf_items";
const WARDROBE_ID = "mine_structure:unicorn_wardrobe";
const WARDROBE_PROPERTY = "wardrobe_items";
const TOY_BOX_ID = "mine_structure:unicorn_toy_box";
const TOY_BOX_PROPERTY = "toy_box_items";
const DRESSER_ID = "mine_structure:unicorn_dresser";
const DRESSER_PROPERTY = "dresser_items";
const PIANO_ID = "mine_structure:unicorn_piano";
const PIANO_PITCHES = [0.6, 0.7, 0.8, 0.95, 1.1, 1.25, 1.5, 1.8];
const TRANSFORM_WAND_ID = "mine_structure:unicorn_transform_wand";
const TRANSFORM_ANIMALS = [
  "minecraft:pig", "minecraft:cow", "minecraft:sheep", "minecraft:chicken",
  "minecraft:rabbit", "minecraft:cat", "minecraft:wolf", "minecraft:fox",
  "minecraft:horse", "minecraft:llama", "minecraft:goat", "minecraft:mooshroom",
  "minecraft:ocelot", "minecraft:panda", "minecraft:turtle", "minecraft:parrot",
];
const GACHA_ID = "mine_structure:unicorn_gacha_machine";
const GACHA_REWARDS = [
  "minecraft:cake",
  "minecraft:cookie",
  "minecraft:emerald",
  "minecraft:slime_ball",
  "minecraft:name_tag",
  "minecraft:music_disc_cat",
  "minecraft:golden_apple",
  "minecraft:diamond",
  "minecraft:firework_rocket",
  "minecraft:painting",
];
const GIFT_ID = "mine_structure:unicorn_gift_box";
const GIFT_REWARDS = [
  "minecraft:cookie",
  "minecraft:cake",
  "minecraft:pumpkin_pie",
  "minecraft:emerald",
  "minecraft:slime_ball",
  "minecraft:firework_rocket",
  "minecraft:golden_carrot",
  "minecraft:music_disc_pigstep",
];
const TRAMPOLINE_ID = "mine_structure:unicorn_trampoline";
const TRAMPOLINE_DIMENSIONS = ["minecraft:overworld", "minecraft:nether", "minecraft:the_end"];
const SINK_IDS = [
  "mine_structure:unicorn_sink_l",
  "mine_structure:unicorn_sink_island",
  "mine_structure:unicorn_sink_u",
];
// local counter offset (blocks) of a non-basin cell to display placed items on
const SINK_COUNTER_OFFSET = {
  "mine_structure:unicorn_sink_l": { x: -1.0, z: 0.5 },
  "mine_structure:unicorn_sink_island": { x: -1.0, z: 1.0 },
  "mine_structure:unicorn_sink_u": { x: -1.0, z: 1.0 },
};
const SINK_WATER_PROPERTY = "sink_water_on";
const BUNK_ID = "mine_structure:unicorn_cloud_bunk_bed";
const BUNK_SEATLOCK_PROPERTY = "bunk_seatlock";
const FRIDGE_ID = "mine_structure:unicorn_fridge";
const FRIDGE_PROPERTY = "fridge_items";
const FRIDGE_MAX_SLOTS = 18;
const PEGASUS_ID = "mine_structure:unicorn_pegasus";
const WAND_ID = "mine_structure:unicorn_wand";
// sparkle particle emitted from the gem while a wand is held in the main hand
const WAND_SPARKLE = {
  [WAND_ID]: "mine_structure:wand_sparkle_cyan",
  [TRANSFORM_WAND_ID]: "mine_structure:wand_sparkle_amethyst",
};
const PHONE_ITEM_ID = "mine_structure:unicorn_phone_item";
const PHONE_FLASHLIGHT_PROPERTY = "phone_flashlight";
const PHONE_RINGTONE = [1.0, 1.18, 1.33, 1.0];
// edible items -> [effectName, durationTicks, amplifier] applied when finished eating
const FOOD_EFFECTS = {
  "mine_structure:unicorn_cookie": [["regeneration", 100, 1], ["saturation", 1, 19]],
  "mine_structure:unicorn_cupcake": [["regeneration", 140, 1], ["saturation", 1, 19]],
  "mine_structure:unicorn_lollipop": [["speed", 600, 0]],
  "mine_structure:unicorn_rainbow_drink": [["speed", 600, 0], ["jump_boost", 600, 0]],
  "mine_structure:unicorn_star_candy": [["night_vision", 1200, 0], ["saturation", 1, 4]],
};

function getMainhand(player) {
  const equippable = player.getComponent(EntityComponentTypes.Equippable);
  if (!equippable) {
    return undefined;
  }
  return equippable.getEquipment(EquipmentSlot.Mainhand);
}

function setMainhand(player, itemStack) {
  const equippable = player.getComponent(EntityComponentTypes.Equippable);
  if (!equippable) {
    return false;
  }
  return equippable.setEquipment(EquipmentSlot.Mainhand, itemStack);
}

function takeOne(itemStack) {
  const placed = itemStack.clone();
  placed.amount = 1;

  const remaining = itemStack.clone();
  remaining.amount -= 1;

  return {
    placed,
    remaining: remaining.amount > 0 ? remaining : undefined,
  };
}

function placeItemOnTable(player, table) {
  const held = getMainhand(player);
  if (!held) {
    return;
  }

  const split = takeOne(held);
  const location = table.location;
  const displayLocation = {
    x: location.x,
    y: location.y + 0.95,
    z: location.z,
  };

  table.dimension.spawnItem(split.placed, displayLocation);
  setMainhand(player, split.remaining);
}

function getStoredItems(storageEntity, property) {
  const raw = storageEntity.getDynamicProperty(property);
  if (typeof raw !== "string" || raw.length === 0) {
    return [];
  }

  try {
    const parsed = JSON.parse(raw);
    if (!Array.isArray(parsed)) {
      return [];
    }
    return parsed.filter((item) => {
      return (
        item &&
        typeof item.typeId === "string" &&
        Number.isInteger(item.amount) &&
        item.amount > 0
      );
    });
  } catch {
    return [];
  }
}

function setStoredItems(storageEntity, property, items) {
  storageEntity.setDynamicProperty(property, JSON.stringify(items));
}

function spawnStoredItem(storageEntity, item) {
  const location = storageEntity.location;
  const amount = Math.max(1, Math.min(64, item.amount));
  const itemStack = new ItemStack(item.typeId, amount);
  storageEntity.dimension.spawnItem(itemStack, {
    x: location.x,
    y: location.y + 1.05,
    z: location.z,
  });
}

function storeOrRetrieveItem(player, storageEntity, property, maxSlots) {
  const held = getMainhand(player);
  const items = getStoredItems(storageEntity, property);

  if (held) {
    if (items.length >= maxSlots) {
      return;
    }

    const split = takeOne(held);
    items.push({
      typeId: split.placed.typeId,
      amount: split.placed.amount,
    });
    setStoredItems(storageEntity, property, items);
    setMainhand(player, split.remaining);
    return;
  }

  const item = items.pop();
  if (!item) {
    return;
  }

  setStoredItems(storageEntity, property, items);
  spawnStoredItem(storageEntity, item);
}

function giveItem(player, sourceEntity, itemStack, soundId) {
  const inventory = player.getComponent(EntityComponentTypes.Inventory);
  const container = inventory ? inventory.container : undefined;
  const leftover = container ? container.addItem(itemStack) : itemStack;

  if (leftover) {
    const location = sourceEntity.location;
    sourceEntity.dimension.spawnItem(leftover, {
      x: location.x,
      y: location.y + 1.0,
      z: location.z,
    });
  }

  if (soundId) {
    sourceEntity.dimension.playSound(soundId, sourceEntity.location);
  }
}

function giveRandom(player, sourceEntity, rewards, soundId) {
  const id = rewards[Math.floor(Math.random() * rewards.length)];
  giveItem(player, sourceEntity, new ItemStack(id, 1), soundId);
}

function dispenseTreat(player, machine) {
  const treatId = ICE_CREAM_TREATS[Math.floor(Math.random() * ICE_CREAM_TREATS.length)];
  giveItem(player, machine, new ItemStack(treatId, 1), "random.pop");
}

system.runInterval(() => {
  for (const dimensionId of TRAMPOLINE_DIMENSIONS) {
    let dimension;
    try {
      dimension = world.getDimension(dimensionId);
    } catch {
      continue;
    }
    const pads = dimension.getEntities({ type: TRAMPOLINE_ID });
    for (const pad of pads) {
      const padLocation = pad.location;
      const players = dimension.getEntities({
        type: "minecraft:player",
        location: padLocation,
        maxDistance: 2,
      });
      for (const player of players) {
        const dy = player.location.y - padLocation.y;
        if (dy < 0.2 || dy > 1.1) {
          continue;
        }
        if (player.isSneaking) {
          continue;
        }
        if (player.getVelocity().y <= 0.08) {
          player.applyKnockback({ x: 0, z: 0 }, 0.9);
        }
      }
    }

    // flying unicorn: rider jumps to climb, sneaks to descend (horizontal is
    // handled by behavior.controlled_by_player; gravity is off so it hovers)
    const flyers = dimension.getEntities({ type: PEGASUS_ID });
    for (const flyer of flyers) {
      const flyerRideable = flyer.getComponent("minecraft:rideable");
      if (!flyerRideable) {
        continue;
      }
      const riders = flyerRideable.getRiders();
      if (riders.length === 0) {
        continue;
      }
      const rider = riders[0];
      if (!rider || rider.typeId !== "minecraft:player") {
        continue;
      }
      const vy = flyer.getVelocity().y;
      if (rider.isJumping && vy < 0.55) {
        flyer.applyImpulse({ x: 0, y: 0.16, z: 0 });
      } else if (rider.isSneaking && vy > -0.55) {
        flyer.applyImpulse({ x: 0, y: -0.16, z: 0 });
      }
    }

    // reset an empty bunk to "bottom first" so the next solo gets the bottom bunk
    const bunks = dimension.getEntities({ type: BUNK_ID });
    for (const bunk of bunks) {
      const rideable = bunk.getComponent("minecraft:rideable");
      if (!rideable || rideable.getRiders().length > 0) {
        continue;
      }
      const lock = bunk.getDynamicProperty(BUNK_SEATLOCK_PROPERTY);
      if (typeof lock === "number" && lock > system.currentTick) {
        continue;
      }
      bunk.triggerEvent("mine_structure:order_bottom");
    }
  }
}, 3);

// while a wand is held, the gem twinkles: spawn one tinted sparkle near the
// held wand head roughly every 0.6s (approximated from the player's view).
system.runInterval(() => {
  for (const player of world.getAllPlayers()) {
    const held = getMainhand(player);
    if (!held) {
      continue;
    }
    const particle = WAND_SPARKLE[held.typeId];
    if (!particle) {
      continue;
    }
    const head = player.getHeadLocation();
    const dir = player.getViewDirection();
    // right vector on the horizontal plane (view x world-up), to nudge toward the hand
    const rlen = Math.hypot(dir.z, dir.x) || 1;
    const loc = {
      x: head.x + dir.x * 0.5 + (-dir.z / rlen) * 0.3,
      y: head.y + dir.y * 0.5 + 0.15,
      z: head.z + dir.z * 0.5 + (dir.x / rlen) * 0.3,
    };
    try {
      player.dimension.spawnParticle(particle, loc);
    } catch {
      // player may be mid-teleport/unloaded chunk; skip this tick
    }
  }
}, 12);

function rideBunkTop(player, bunk) {
  // the player has just auto-mounted the bottom seat; swap the seat order so the
  // top bunk becomes seat 0, then re-seat the player there.
  bunk.setDynamicProperty(BUNK_SEATLOCK_PROPERTY, system.currentTick + 20);
  bunk.triggerEvent("mine_structure:order_top");
  system.runTimeout(() => {
    const rideable = bunk.getComponent("minecraft:rideable");
    if (rideable) {
      rideable.addRider(player);
    }
  }, 2);
}

function placeOnSinkCounter(player, sink) {
  const held = getMainhand(player);
  if (!held) {
    return false;
  }

  const offset = SINK_COUNTER_OFFSET[sink.typeId] || { x: 0, z: 0 };
  const yaw = (sink.getRotation().y * Math.PI) / 180;
  const sin = Math.sin(yaw);
  const cos = Math.cos(yaw);
  const location = sink.location;

  const split = takeOne(held);
  sink.dimension.spawnItem(split.placed, {
    x: location.x + offset.x * cos - offset.z * sin,
    y: location.y + 0.95,
    z: location.z + offset.x * sin + offset.z * cos,
  });
  setMainhand(player, split.remaining);
  return true;
}

function toggleSinkWater(sink) {
  const next = sink.getDynamicProperty(SINK_WATER_PROPERTY) !== true;
  sink.setDynamicProperty(SINK_WATER_PROPERTY, next);
  sink.triggerEvent(next ? "mine_structure:turn_water_on" : "mine_structure:turn_water_off");
  sink.dimension.playSound(next ? "bucket.fill_water" : "bucket.empty_water", sink.location);
}

function transformAnimal(target) {
  const dimension = target.dimension;
  const location = target.location;
  let next = target.typeId;
  while (next === target.typeId) {
    next = TRANSFORM_ANIMALS[Math.floor(Math.random() * TRANSFORM_ANIMALS.length)];
  }
  try {
    dimension.spawnParticle("minecraft:totem_particle", { x: location.x, y: location.y + 0.8, z: location.z });
  } catch (error) { /* cosmetic */ }
  try {
    dimension.playSound("random.orb", location);
  } catch (error) { /* cosmetic */ }
  dimension.spawnEntity(next, location);
  target.remove();
}

world.afterEvents.playerInteractWithEntity.subscribe((event) => {
  const target = event.target;
  if (!target) {
    return;
  }

  // transform wand: zap an animal -> a random different animal
  if (event.itemStack && event.itemStack.typeId === TRANSFORM_WAND_ID) {
    if (TRANSFORM_ANIMALS.includes(target.typeId)) {
      system.run(() => {
        transformAnimal(target);
      });
    }
    return;
  }

  if (SINK_IDS.includes(target.typeId)) {
    system.run(() => {
      if (!placeOnSinkCounter(event.player, target)) {
        toggleSinkWater(target);
      }
    });
  }

  if (target.typeId === BUNK_ID && event.player.isSneaking) {
    system.run(() => {
      rideBunkTop(event.player, target);
    });
  }

  if (target.typeId === ICE_CREAM_ID) {
    system.run(() => {
      dispenseTreat(event.player, target);
    });
  }

  if (target.typeId === TOASTER_ID) {
    system.run(() => {
      giveItem(event.player, target, new ItemStack("minecraft:bread", 1), "random.pop");
    });
  }

  if (target.typeId === BOOKSHELF_ID) {
    system.run(() => {
      storeOrRetrieveItem(event.player, target, BOOKSHELF_PROPERTY, 12);
    });
  }

  if (target.typeId === WARDROBE_ID) {
    system.run(() => {
      storeOrRetrieveItem(event.player, target, WARDROBE_PROPERTY, 18);
    });
  }

  if (target.typeId === TOY_BOX_ID) {
    system.run(() => {
      storeOrRetrieveItem(event.player, target, TOY_BOX_PROPERTY, 12);
    });
  }

  if (target.typeId === DRESSER_ID) {
    system.run(() => {
      storeOrRetrieveItem(event.player, target, DRESSER_PROPERTY, 18);
    });
  }

  if (target.typeId === PIANO_ID) {
    system.run(() => {
      const pitch = PIANO_PITCHES[Math.floor(Math.random() * PIANO_PITCHES.length)];
      try {
        target.dimension.playSound("note.harp", target.location, { pitch });
      } catch (error) { /* cosmetic */ }
      try {
        const loc = target.location;
        target.dimension.spawnParticle("minecraft:note_particle", { x: loc.x, y: loc.y + 1.4, z: loc.z });
      } catch (error) { /* cosmetic */ }
    });
  }

  if (target.typeId === GACHA_ID) {
    system.run(() => {
      giveRandom(event.player, target, GACHA_REWARDS, "random.orb");
    });
  }

  if (target.typeId === GIFT_ID) {
    system.run(() => {
      giveRandom(event.player, target, GIFT_REWARDS, "random.orb");
    });
  }

  if (target.typeId === TABLE_ID) {
    system.run(() => {
      placeItemOnTable(event.player, target);
    });
  }

  if (target.typeId === STORAGE_ID) {
    system.run(() => {
      storeOrRetrieveItem(event.player, target, STORAGE_PROPERTY, STORAGE_MAX_SLOTS);
    });
  }

  if (target.typeId === FRIDGE_ID) {
    system.run(() => {
      storeOrRetrieveItem(event.player, target, FRIDGE_PROPERTY, FRIDGE_MAX_SLOTS);
    });
  }
});

function sparkle(entity, particle) {
  try {
    const location = entity.location;
    entity.dimension.spawnParticle(particle, {
      x: location.x,
      y: location.y + 1.6,
      z: location.z,
    });
  } catch (error) {
    // particles are cosmetic; ignore if they cannot spawn
  }
}

// Eating a unicorn treat tops up hunger and applies its effect(s).
world.afterEvents.itemCompleteUse.subscribe((event) => {
  const effects = event.itemStack ? FOOD_EFFECTS[event.itemStack.typeId] : undefined;
  const player = event.source;
  if (!effects || !player) {
    return;
  }
  for (const [name, duration, amplifier] of effects) {
    player.addEffect(name, duration, { amplifier, showParticles: true });
  }
  sparkle(player, "minecraft:heart_particle");
});

// The magic wand: right-click for a sparkle + a short jump/speed boost.
world.afterEvents.itemUse.subscribe((event) => {
  if (!event.itemStack || event.itemStack.typeId !== WAND_ID) {
    return;
  }
  const player = event.source;
  if (!player) {
    return;
  }
  player.addEffect("jump_boost", 120, { amplifier: 1, showParticles: true });
  player.addEffect("speed", 120, { amplifier: 0, showParticles: true });
  sparkle(player, "minecraft:totem_particle");
  try {
    player.dimension.playSound("random.orb", player.location);
  } catch (error) {
    // sound is cosmetic
  }
});

function phoneSelfie(player) {
  sparkle(player, "minecraft:heart_particle");
  try {
    const loc = player.location;
    player.dimension.spawnParticle("minecraft:villager_happy", { x: loc.x, y: loc.y + 1.8, z: loc.z });
  } catch (error) {
    // flash particle is cosmetic
  }
  try {
    player.dimension.playSound("random.orb", player.location);  // shutter "click"
  } catch (error) { /* cosmetic */ }
  // short cheerful ringtone melody
  PHONE_RINGTONE.forEach((pitch, i) => {
    system.runTimeout(() => {
      try {
        player.dimension.playSound("note.bell", player.location, { pitch });
      } catch (error) { /* cosmetic */ }
    }, i * 4);
  });
}

function phoneFlashlight(player) {
  const next = player.getDynamicProperty(PHONE_FLASHLIGHT_PROPERTY) !== true;
  player.setDynamicProperty(PHONE_FLASHLIGHT_PROPERTY, next);
  if (next) {
    player.addEffect("night_vision", 1000000, { amplifier: 0, showParticles: false });
  } else {
    try {
      player.removeEffect("night_vision");
    } catch (error) { /* may not be present */ }
  }
  try {
    player.dimension.playSound("random.click", player.location);
  } catch (error) { /* cosmetic */ }
}

// Held phone: right-click = selfie (flash + shutter + ringtone), sneak = flashlight.
world.afterEvents.itemUse.subscribe((event) => {
  if (!event.itemStack || event.itemStack.typeId !== PHONE_ITEM_ID) {
    return;
  }
  const player = event.source;
  if (!player) {
    return;
  }
  if (player.isSneaking) {
    phoneFlashlight(player);
  } else {
    phoneSelfie(player);
  }
});
