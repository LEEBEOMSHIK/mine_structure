# unicorn_cookie

먹을 수 있는 유니콘 쿠키 (음식 아이템). 가구/엔티티가 아니라 검과 같은 아이템이다.

## Registry

- Identifier: `mine_structure:unicorn_cookie`
- Content type: food item
- Menu category: nature
- Status: add-on 파일 생성 완료, 인게임 테스트 대기.

## 효과

- `minecraft:food` (nutrition 6, saturation_modifier "good", can_always_eat) → 먹으면 허기 회복(허기 → 자연 체력 재생).
- **실제 체력 회복**: 다 먹는 순간 `scripts/main.js`의 `world.afterEvents.itemCompleteUse`가 `regeneration`(amplifier 1, 5초) + `saturation`을 부여하고 하트 파티클을 띄운다.
- 스택 64, 먹는 애니메이션(`use_animation: eat`), 먹는 동안 이동 감속(`use_modifiers.movement_modifier 0.35`).

## Add-on Files

- `../../addon/behavior_pack/items/unicorn_cookie.item.json`
- `../../addon/resource_pack/textures/items/unicorn_cookie.png` (16×16 아이콘)
- `../../addon/resource_pack/textures/item_texture.json` (shortname `unicorn_cookie`)
- 회복 스크립트: `../../addon/behavior_pack/scripts/main.js` (`itemCompleteUse` 핸들러)
- 아이콘 생성: `../../blockbench/gen_unicorn_cookie_texture.py`

## 사용 / 테스트

```
/give @s mine_structure:unicorn_cookie
```
받아서 먹으면 허기가 차고 먹은 직후 체력이 회복돼야 한다(스크립트 효과 → behavior pack + Beta API 실험 옵션 필요).

## Pending

- 인게임 검증(README NEXT 15번). 회복량/지속시간(현재 Regeneration II 5초)·영양치 밸런스는 필요 시 조정.
