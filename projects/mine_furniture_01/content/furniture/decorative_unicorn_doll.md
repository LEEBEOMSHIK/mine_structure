# decorative_unicorn_doll

## Registry

- Bedrock identifier: `mine_structure:decorative_unicorn_doll`
- Content type: furniture entity
- Category: fantasy decoration
- Status: static model/add-on files generated (texture is placeholder)

## Source Documents

- Progress summary: `../../README.md`
- Common Blockbench/MCP rules: `../../../../docs/agent-guides/blockbench-mcp-rules.md`
- Resource map: `decorative_unicorn_doll.resources.json`

## Add-on Files

Behavior pack:

- `../../addon/behavior_pack/entities/decorative_unicorn_doll.entity.json`

Resource pack:

- `../../addon/resource_pack/entity/decorative_unicorn_doll.entity.json`
- `../../addon/resource_pack/models/entity/decorative_unicorn_doll.geo.json`
- `../../addon/resource_pack/textures/entity/decorative_unicorn_doll/decorative_unicorn_doll_atlas.png`
- `../../addon/resource_pack/render_controllers/decorative_unicorn_doll.render_controllers.json`
- `decorative_unicorn_doll.resources.json`

## First Version Goal

Small static decorative unicorn doll shaped as a chibi pony so it clearly reads as a horse, not an upright plush.

## Model Notes (2026-06-01)

- Rebuilt from an upright box-body plush into a **four-legged pony silhouette**: horizontal barrel body, raised forward-leaning neck, head with a forward muzzle (+ nostrils/mouth).
- Unicorn features: tapered 3-segment pointed horn (forward tilt), small upright ears, forelock over the brow, rainbow mane crest down the neck, and a 2-segment tail at the rear.
- Geometry: `geometry.decorative_unicorn_doll`, 6 bones / 27 cubes. Source of truth is `blockbench/furniture.bbmodel` (doll lives at world offset, exported to centered coords by subtracting `[72, 0, 7]`).
- Texture `decorative_unicorn_doll_atlas.png` was re-skinned (2026-06-01) by `blockbench/gen_cute_furniture_atlases.py` to add toilet-style sparkle/droplet detail on top of each cell's base colour, so the pony shows cute varied texture in both editor and in-game. Each model now binds to its own atlas in the editor (no longer borrows the toilet atlas).

## Behavior

This is pure decoration. It intentionally has no `minecraft:interact`, no Script API handler, and no rideable behavior.
