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

function getStoredItems(storageEntity) {
  const raw = storageEntity.getDynamicProperty(STORAGE_PROPERTY);
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

function setStoredItems(storageEntity, items) {
  storageEntity.setDynamicProperty(STORAGE_PROPERTY, JSON.stringify(items));
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

function storeOrRetrieveItem(player, storageEntity) {
  const held = getMainhand(player);
  const items = getStoredItems(storageEntity);

  if (held) {
    if (items.length >= STORAGE_MAX_SLOTS) {
      return;
    }

    const split = takeOne(held);
    items.push({
      typeId: split.placed.typeId,
      amount: split.placed.amount,
    });
    setStoredItems(storageEntity, items);
    setMainhand(player, split.remaining);
    return;
  }

  const item = items.pop();
  if (!item) {
    return;
  }

  setStoredItems(storageEntity, items);
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
  }
}, 3);

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

world.afterEvents.playerInteractWithEntity.subscribe((event) => {
  const target = event.target;
  if (!target) {
    return;
  }

  if (SINK_IDS.includes(target.typeId)) {
    system.run(() => {
      if (!placeOnSinkCounter(event.player, target)) {
        toggleSinkWater(target);
      }
    });
  }

  if (target.typeId === ICE_CREAM_ID) {
    system.run(() => {
      dispenseTreat(event.player, target);
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
      storeOrRetrieveItem(event.player, target);
    });
  }
});
