# unicorn_dining_table

## Registry

- Bedrock identifier: `mine_structure:unicorn_dining_table`
- Content type: furniture entity
- Category: fantasy dining furniture
- Status: static model/texture/add-on files generated

## Source Documents

- Progress summary: `../../README.md`
- Common Blockbench/MCP rules: `../../../../docs/agent-guides/blockbench-mcp-rules.md`
- Resource map: `unicorn_dining_table.resources.json`

## Add-on Files

Behavior pack:

- `../../addon/behavior_pack/entities/unicorn_dining_table.entity.json`

Resource pack:

- `../../addon/resource_pack/entity/unicorn_dining_table.entity.json`
- `../../addon/resource_pack/models/entity/unicorn_dining_table.geo.json`
- `../../addon/resource_pack/textures/entity/unicorn_dining_table/unicorn_dining_table_atlas.png`
- `../../addon/resource_pack/render_controllers/unicorn_dining_table.render_controllers.json`
- `unicorn_dining_table.resources.json`

## First Version Goal

Static unicorn-themed dining table:

1. Pastel ceramic table top.
2. Lavender legs and trim.
3. Rainbow runner across the table.
4. Small unicorn horn centerpiece.

## Behavior

Player interaction is handled by `../../addon/behavior_pack/scripts/main.js`.

1. If the player interacts while holding an item, one item is spawned at the table top position.
2. The player's main hand stack is reduced by one.
3. If the player interacts with an empty hand, nothing changes.

This first behavior pass uses a normal dropped item entity on top of the table. It does not yet lock the item in place or prevent pickup.
