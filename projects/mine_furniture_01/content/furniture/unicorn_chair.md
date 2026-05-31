# unicorn_chair

## Registry

- Bedrock identifier: `mine_structure:unicorn_chair`
- Content type: furniture entity
- Category: fantasy dining furniture
- Status: static model/texture/add-on files generated

## Source Documents

- Progress summary: `../../README.md`
- Common Blockbench/MCP rules: `../../../../docs/agent-guides/blockbench-mcp-rules.md`
- Resource map: `unicorn_chair.resources.json`

## Add-on Files

Behavior pack:

- `../../addon/behavior_pack/entities/unicorn_chair.entity.json`

Resource pack:

- `../../addon/resource_pack/entity/unicorn_chair.entity.json`
- `../../addon/resource_pack/models/entity/unicorn_chair.geo.json`
- `../../addon/resource_pack/textures/entity/unicorn_chair/unicorn_chair_atlas.png`
- `../../addon/resource_pack/render_controllers/unicorn_chair.render_controllers.json`
- `unicorn_chair.resources.json`

## First Version Goal

Static unicorn-themed dining chair:

1. Pastel pink seat.
2. White backrest with unicorn ears and horn.
3. Rainbow mane strips on the back.
4. Lavender legs and trim.

## Behavior

The chair uses `minecraft:rideable` in `../../addon/behavior_pack/entities/unicorn_chair.entity.json`.

1. Players can interact with the chair to sit.
2. Seat count is 1.
3. Seat position is `[0, 0.55, 0]`.
