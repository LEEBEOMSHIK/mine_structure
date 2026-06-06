# unicorn_transform_wand

동물 변신 마법봉. 들고 동물을 우클릭하면 그 동물이 랜덤으로 다른 동물로 바뀐다.

## Registry

- Identifier: `mine_structure:unicorn_transform_wand`
- Content type: tool item (2D 아이콘)
- Menu category: equipment
- Status: add-on 파일 생성 완료, 인게임 테스트 대기.

## 동작

- 아이템: `minecraft:hand_equipped` + `minecraft:icon` + `minecraft:display_name` + `minecraft:cooldown`(1초).
- 변신: Bedrock은 엔티티 타입을 직접 바꿀 수 없으므로 "제거 + 재소환" 방식. `scripts/main.js`의 `world.afterEvents.playerInteractWithEntity`가 들고 있는 아이템이 이 마법봉이고 대상이 동물이면 `transformAnimal(target)`을 호출:
  1. 대상 위치에 `TRANSFORM_ANIMALS`(돼지/소/양/닭/토끼/고양이/늑대/여우/말/라마/염소/무시룸/오실롯/판다/거북/앵무 16종) 중 **현재와 다른** 랜덤 동물을 `spawnEntity`
  2. 기존 동물을 `remove`
  3. totem 파티클 + `random.orb` 소리로 변신 연출
- **대상 제한**: `TRANSFORM_ANIMALS`에 포함된 **바닐라 동물만** 변신한다(플레이어·몬스터·우리 가구/탈것/펫 엔티티는 영향 없음).

## Add-on Files

- `addon/behavior_pack/items/unicorn_transform_wand.item.json`
- `addon/resource_pack/textures/items/unicorn_transform_wand.png` (16×16 아이콘) + `item_texture.json` 등록
- 로직: `addon/behavior_pack/scripts/main.js`(`TRANSFORM_ANIMALS`, `transformAnimal`)
- 생성: `blockbench/gen_item_icons.py`, `blockbench/gen_extra_items.py`

## 테스트

```
/give @s mine_structure:unicorn_transform_wand
```
동물(예: 돼지)을 우클릭 → 랜덤 동물로 변신 확인(스크립트 → behavior pack + 베타 API 실험 옵션 필요).

## Pending

- 인게임 검증(README NEXT 24번). 변신 대상/결과 풀, 쿨다운, 연출은 `TRANSFORM_ANIMALS`/스크립트에서 조정.
