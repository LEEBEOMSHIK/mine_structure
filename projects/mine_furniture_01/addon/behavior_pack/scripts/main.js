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

function dispenseTreat(player, machine) {
  const treatId = ICE_CREAM_TREATS[Math.floor(Math.random() * ICE_CREAM_TREATS.length)];
  const treat = new ItemStack(treatId, 1);

  const inventory = player.getComponent(EntityComponentTypes.Inventory);
  const container = inventory ? inventory.container : undefined;
  const leftover = container ? container.addItem(treat) : treat;

  if (leftover) {
    const location = machine.location;
    machine.dimension.spawnItem(leftover, {
      x: location.x,
      y: location.y + 1.0,
      z: location.z,
    });
  }

  machine.dimension.playSound("random.pop", machine.location);
}

world.afterEvents.playerInteractWithEntity.subscribe((event) => {
  const target = event.target;
  if (!target) {
    return;
  }

  if (target.typeId === ICE_CREAM_ID) {
    system.run(() => {
      dispenseTreat(event.player, target);
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
