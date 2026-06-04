# unicorn_treats (효과 음식 4종)

쿠키에 이어 추가한 효과 음식 세트. 먹으면 허기 회복 + 각자 다른 효과가 붙는다.

## Registry

| Identifier | 이름 | 효과(먹을 때) |
|------------|------|---------------|
| `mine_structure:unicorn_cupcake` | 유니콘 컵케이크 | Regeneration II 7초 + 포만 |
| `mine_structure:unicorn_lollipop` | 유니콘 막대사탕 | Speed I 30초 |
| `mine_structure:unicorn_rainbow_drink` | 무지개 음료 | Speed I + Jump Boost I 30초 (마시기 모션) |
| `mine_structure:unicorn_star_candy` | 별사탕 | Night Vision 60초 + 약간 포만 |

- Content type: food item / 2D 아이콘
- Status: add-on 파일 생성 완료, 인게임 테스트 대기.

## 동작

- `minecraft:food`(nutrition/saturation, can_always_eat)로 먹을 수 있고 허기를 채운다.
- 효과는 `scripts/main.js`의 `FOOD_EFFECTS` 맵으로 부여한다. `world.afterEvents.itemCompleteUse`가 다 먹은 순간 해당 아이템의 `[효과, 지속틱, 증폭]` 목록을 `addEffect`로 적용하고 하트 파티클을 띄운다(쿠키도 같은 맵).

## Add-on Files

- `../../addon/behavior_pack/items/<id>.item.json` (4종)
- `../../addon/resource_pack/textures/items/<id>.png` (16×16 아이콘)
- `../../addon/resource_pack/textures/item_texture.json` (shortname 등록)
- 효과 로직: `../../addon/behavior_pack/scripts/main.js` (`FOOD_EFFECTS`, `itemCompleteUse`)
- 생성: `../../blockbench/gen_item_icons.py`(아이콘), `../../blockbench/gen_extra_items.py`(item + item_texture)

## 테스트

```
/give @s mine_structure:unicorn_cupcake
/give @s mine_structure:unicorn_lollipop
/give @s mine_structure:unicorn_rainbow_drink
/give @s mine_structure:unicorn_star_candy
```
먹어서 각 효과가 붙는지 확인(스크립트 효과 → behavior pack + Beta API 실험 옵션 필요).

## Pending

- 인게임 검증(README NEXT 16번). 효과 종류/지속시간/영양치 밸런스는 필요 시 조정.
