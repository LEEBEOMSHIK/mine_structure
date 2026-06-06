# unicorn_wand

유니콘 마법 지팡이. 우클릭하면 파티클 + 점프/스피드 부스트가 발동하는 놀이용 도구 아이템.

## Registry

- Identifier: `mine_structure:unicorn_wand`
- Content type: tool item / 2D 아이콘 + 손에 드는 3D 모델(attachable)
- Menu category: equipment
- Status: add-on 파일 생성 완료, 인게임 테스트 대기.

## 동작

- 아이템 컴포넌트: `minecraft:display_name`, `minecraft:icon`, `max_stack_size 1`, `minecraft:hand_equipped`, `minecraft:cooldown`(category `unicorn_wand`, 2초).
- 사용: `scripts/main.js`의 `world.afterEvents.itemUse`가 지팡이 우클릭 시 플레이어에게 Jump Boost II + Speed I(6초)를 부여하고 토템 파티클 + `random.orb` 소리를 낸다.
- 3D 모델: 손에 들면 attachable로 입체 막대 지팡이가 보인다. 슬림한 라벤더 손잡이 + 그립 밴드 2개 + 별 헤드(정사각 큐브 2개를 45도로 겹쳐 별 실루엣) + 가운데 발광 코어. 인벤토리 아이콘(2D)과 우클릭 동작은 그대로다. 손 포즈는 인게임 튜닝 대기.

## Add-on Files

- `../../addon/behavior_pack/items/unicorn_wand.item.json`
- `../../addon/resource_pack/textures/items/unicorn_wand.png` (16×16 아이콘: 무지개 별 + 손잡이)
- `../../addon/resource_pack/textures/item_texture.json` (shortname `unicorn_wand`)
- `../../addon/resource_pack/attachables/unicorn_wand.attachable.json` (손에 든 3D 모델)
- `../../addon/resource_pack/models/entity/unicorn_wand.geo.json` + `.../textures/entity/unicorn_wand/unicorn_wand_atlas.png`
- `../../addon/resource_pack/animations/unicorn_wand.animation.json` (1·3인칭 손 포즈)
- 사용 로직: `../../addon/behavior_pack/scripts/main.js` (`itemUse` 핸들러)
- 생성: `../../blockbench/gen_item_icons.py`(아이콘), `../../blockbench/gen_wand_items.py`(3D 모델/attachable)
- Blockbench 소스: `../../blockbench/unicorn_wand.bbmodel`

## 테스트

```
/give @s mine_structure:unicorn_wand
```
우클릭 시 파티클 + 점프/스피드 부스트 + 쿨다운 확인(스크립트 효과 → behavior pack + Beta API 실험 옵션 필요).

## Pending

- 인게임 검증(README NEXT 16번). 부스트 세기/지속·쿨다운 조정 가능.
- 손에 든 3D 지팡이 모델 포즈는 인게임에서 보고 `gen_wand_items.py`의 `pose(...)` 값으로 보정.
