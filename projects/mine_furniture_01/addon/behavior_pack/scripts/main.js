import { EntityComponentTypes, EquipmentSlot, system, world } from "@minecraft/server";

const TABLE_ID = "mine_structure:unicorn_dining_table";

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

world.afterEvents.playerInteractWithEntity.subscribe((event) => {
  const target = event.target;
  if (!target || target.typeId !== TABLE_ID) {
    return;
  }

  system.run(() => {
    placeItemOnTable(event.player, target);
  });
});
