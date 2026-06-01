# unicorn_barrel_cabinet

## Registry

- Bedrock identifier: `mine_structure:unicorn_barrel_cabinet`
- Content type: furniture entity
- Category: fantasy storage furniture
- Status: model/texture/add-on files generated, Script API simple storage added

## Source Documents

- Progress summary: `../../README.md`
- Common Blockbench/MCP rules: `../../../../docs/agent-guides/blockbench-mcp-rules.md`
- Resource map: `unicorn_barrel_cabinet.resources.json`

## Add-on Files

Behavior pack:

- `../../addon/behavior_pack/entities/unicorn_barrel_cabinet.entity.json`
- `../../addon/behavior_pack/scripts/main.js`

Resource pack:

- `../../addon/resource_pack/entity/unicorn_barrel_cabinet.entity.json`
- `../../addon/resource_pack/models/entity/unicorn_barrel_cabinet.geo.json`
- `../../addon/resource_pack/textures/entity/unicorn_barrel_cabinet/unicorn_barrel_cabinet_atlas.png`
- `../../addon/resource_pack/render_controllers/unicorn_barrel_cabinet.render_controllers.json`
- `unicorn_barrel_cabinet.resources.json`

## First Version Goal

Unicorn-themed barrel cabinet with a pastel wooden barrel body, small front door, rainbow bands, and horn/ear accents.

## Behavior

Storage uses `../../addon/behavior_pack/scripts/main.js`.

1. Interacting while holding an item stores one item in the barrel.
2. Interacting with an empty hand retrieves the most recently stored item.
3. Storage is a simple Script API list stored on the entity dynamic property `barrel_storage_items`.
4. The first pass stores item type and amount only; it does not preserve custom item data or open a UI.
