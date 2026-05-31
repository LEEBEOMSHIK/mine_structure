# unicorn_toilet

## Registry

- Bedrock identifier: `mine_structure:unicorn_toilet`
- Content type: furniture entity
- Category: fantasy bathroom furniture
- Status: model/texture/animation spec ready, add-on files scaffolded

## Source Documents

- Progress summary: `../../README.md`
- Detailed model spec: `../../unicorn_toilet_spec.md`
- Common Blockbench/MCP rules: `../../../../docs/agent-guides/blockbench-mcp-rules.md`
- Resource map: `unicorn_toilet.resources.json`

## Add-on Files

Behavior pack:

- `../../addon/behavior_pack/entities/unicorn_toilet.entity.json`

Resource pack:

- `../../addon/resource_pack/entity/unicorn_toilet.entity.json`
- `../../addon/resource_pack/models/entity/unicorn_toilet.geo.json`
- `../../addon/resource_pack/textures/entity/unicorn_toilet/unicorn_toilet_atlas.png`
- `../../addon/resource_pack/animations/unicorn_toilet.animation.json`
- `../../addon/resource_pack/render_controllers/unicorn_toilet.render_controllers.json`
- `../../addon/resource_pack/sounds/sound_definitions.json`
- `../../addon/resource_pack/sounds/flush.ogg`
- `unicorn_toilet.resources.json`

## Export Requirements

1. Export Bedrock geometry from Blockbench as `unicorn_toilet.geo.json`.
2. Save the 64x64 atlas as `unicorn_toilet_atlas.png`.
3. Export animations with names:
   - `animation.unicorn_toilet.lid_open`
   - `animation.unicorn_toilet.lid_close`
   - `animation.unicorn_toilet.flush`
4. Add `flush.ogg` and verify the animation sound keyframe resolves to `flush`.

Use `../../blockbench/export_unicorn_toilet_to_resource_pack.js` as the MCP export target reference.

## Interaction Goal

The target in-game behavior is:

1. Player interacts with the toilet.
2. Add-on triggers the `flush` animation.
3. Add-on plays the `flush` sound.
4. Optional later behavior: open/close lid interaction using `lid_open` and `lid_close`.
