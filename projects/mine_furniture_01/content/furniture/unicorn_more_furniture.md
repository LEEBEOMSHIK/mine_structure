# unicorn_more_furniture (4종)

아이들이 좋아할 콘텐츠 4종 (새 메커니즘 포함).

## Registry

| Identifier | 종류 | 메커니즘 | 핵심 |
|------------|------|----------|------|
| `mine_structure:unicorn_baby_pet` | pet mob | 길들이기 → 따라오기 + 탑승 | 설탕/사과/쿠키로 길들임, walk/idle 애니 |
| `mine_structure:unicorn_gacha_machine` | furniture | Script 랜덤 보상 | 우클릭 시 랜덤 아이템 1개 + 소리 |
| `mine_structure:unicorn_trampoline` | furniture | Script 점프 바운스 | 매트 위에서 통통 튕김 |
| `mine_structure:unicorn_gift_box` | furniture | interact 애니 + Script 선물 | 우클릭 시 뚜껑 열림 + 선물 1개 |

- Status: 모델/텍스처/add-on 배선 완료, 인게임 테스트 대기.

## Add-on Files (각 `<id>`)

Behavior pack: `../../addon/behavior_pack/entities/<id>.entity.json`
Resource pack:
- `../../addon/resource_pack/entity/<id>.entity.json`
- `../../addon/resource_pack/models/entity/<id>.geo.json`
- `../../addon/resource_pack/render_controllers/<id>.render_controllers.json`
- `../../addon/resource_pack/textures/entity/<id>/<id>_atlas.png`
- (펫) `animations/unicorn_baby_pet.animation.json`(idle/walk) + `animation_controllers/unicorn_baby_pet.animation_controllers.json`(default↔move)
- (선물상자) `animations/unicorn_gift_box.animation.json`(lid_open)

Script: 가챠/선물 지급과 트램폴린 바운스는 `../../addon/behavior_pack/scripts/main.js`.
생성 스크립트: `../../blockbench/gen_more_furniture.py`, `../../blockbench/gen_more_wiring.py`
Blockbench 원본: `../../blockbench/<id>.bbmodel`
Resource maps: `<id>.resources.json`

## 메커니즘 메모

- **아기 유니콘 펫**: 일반 걷는 몹 컴포넌트(`physics`/`movement`/`navigation.walk`/`movement.basic`/`jump.static`/`behavior.float`)에 `minecraft:tameable`(tame_items: 설탕/사과/쿠키, `minecraft:on_tame` 이벤트)을 더했다. 길들이기 전엔 `behavior.tempt`로 먹이를 따라오고 `random_stroll`/`look_at_player`로 돌아다닌다. 길들이면 `mine_structure:tamed` 그룹이 `behavior.follow_owner`와 `minecraft:rideable`(좌석 `[0,0.6,0]`)을 추가한다. 다리 4개(`leg_*`)와 머리(`head`)를 별도 본으로 분리해 `controller.animation.<id>.move`가 `q.modified_move_speed`로 idle↔walk 전환(`scripts.animate: ["move"]`).
- **가챠 뽑기**: behavior 상호작용 없이 Script API에서 처리. 우클릭 시 `GACHA_REWARDS`(cake/cookie/emerald/slime_ball/name_tag/music_disc_cat/golden_apple/diamond/firework_rocket/painting) 중 1개를 인벤토리에 추가(가득 차면 바닥 스폰), `random.orb` 소리.
- **트램폴린**: 매트(`mat`)에 콜리전이 있어 위에 설 수 있다. `system.runInterval`(3틱)이 모든 차원에서 트램폴린을 찾아 매트 위(높이 0.2~1.1) 플레이어 중 하강/정지(velocity.y ≤ 0.08)·비웅크림 상태면 `applyKnockback({x:0,z:0}, 0.9)`로 위로 튕긴다 → 연속 바운스. 웅크리면 멈춘다.
- **선물상자**: `minecraft:interact`가 `mine_structure:open_gift`를 호출 → `queue_command`로 `playanimation @s animation.<id>.lid_open`(경첩 `lid` 본이 열렸다 닫힘). 동시에 Script가 `GIFT_REWARDS` 중 1개 지급 + `random.orb`.

## Pending

- 인게임 소환/상호작용 테스트(README NEXT 12번).
- 펫 속도/콜리전, 트램폴린 바운스 세기·판정, 선물상자 뚜껑 각도 미세조정.
- (참고) 스크립트형(가챠/선물/트램폴린)·펫은 behavior pack 스크립트 모듈과 `@minecraft/server` 2.1.0 호환 버전 + 실험 옵션이 필요하다.
