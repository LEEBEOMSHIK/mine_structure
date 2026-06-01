# Weapon Content

## 등록 상태

| ID | Type | Status | Docs |
|----|------|--------|------|
| `mine_structure:unicorn_horn_blade` | weapon item (sword) | 2D icon + 3D attachable ready, in-hand pose needs in-game tuning | `unicorn_horn_blade.md` |

## Planned Structure

각 무기는 아래 정보를 가진 별도 문서로 등록한다.

- Bedrock identifier
- Weapon type
- Visual/model source
- Behavior pack item file
- Resource pack texture/model file
- Damage, durability, cooldown, special effect

## Naming

- Bedrock identifier: `mine_structure:<weapon_id>`
- File stem: `<weapon_id>`
- Behavior item file: `addon/behavior_pack/items/<weapon_id>.item.json`
- Texture path: `addon/resource_pack/textures/items/<weapon_id>.png`
