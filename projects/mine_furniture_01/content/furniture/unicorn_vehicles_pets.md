# unicorn_vehicles_pets (3종)

운전하는 자동차 · 아기 드래곤 펫 · 유니콘 어항.

## Registry

| Identifier | 종류 | 메커니즘 | 핵심 |
|------------|------|----------|------|
| `mine_structure:unicorn_car` | vehicle | rideable(조종) + 바퀴 회전 | 타고 직접 운전, 움직이면 바퀴 회전 |
| `mine_structure:unicorn_baby_dragon` | pet mob | 길들이기 → 따라오기 + 탑승 | 아기 유니콘 펫과 동일 시스템 |
| `mine_structure:unicorn_aquarium` | furniture | variant 불빛 on/off + 물고기 헤엄 | 우클릭 불빛, 물고기 2마리 루프 |

- Status: 모델/텍스처/add-on 배선 완료, 인게임 테스트 대기.

## Add-on Files (각 `<id>`)

Behavior: `../../addon/behavior_pack/entities/<id>.entity.json`
Resource: client entity / geometry / render controller / `textures/entity/<id>/<id>_atlas.png`
- (자동차) `animations/unicorn_car.animation.json`(roll) + `animation_controllers/unicorn_car.animation_controllers.json`(default↔move, 바퀴 회전)
- (드래곤) `animations/unicorn_baby_dragon.animation.json`(idle/walk) + `animation_controllers/...`(default↔move)
- (어항) `animations/unicorn_aquarium.animation.json`(fish/on/off) + `animation_controllers/...`(light off↔on)

생성: `../../blockbench/gen_more_furniture.py`, `../../blockbench/gen_more_wiring.py`
Blockbench 원본: `../../blockbench/<id>.bbmodel`
Resource maps: `<id>.resources.json`

## 메커니즘 메모

- **자동차**: `minecraft:rideable`(`controlling_seat: 0`, 좌석 `[0,0.55,0]`) + `minecraft:behavior.controlled_by_player` + `minecraft:movement`(0.3)/`navigation.walk`/`movement.basic`/`jump.static`로 플레이어가 직접 조종한다(WASD). 바퀴 4개(`wheel_*`)는 별도 본이고, `controller.animation.<id>.wheels`가 `q.modified_move_speed`로 움직일 때만 `roll`(바퀴 X축 회전 루프)을 재생한다.
- **아기 드래곤**: `gen_more_wiring.py`의 `pet_entity(sid)`를 그대로 재사용한다(아기 유니콘 펫과 동일). 길들이기 전 random_stroll/tempt, 길들이면 `mine_structure:tamed` 그룹이 `follow_owner` + `rideable` 추가. 다리 4개로 walk, 표정은 큐브(눈/볼/콧구멍/입), 등 스파이크·날개·꼬리는 무지개.
- **어항**: 무드등과 같은 `minecraft:variant` 불빛 토글(behavior `minecraft:interact` → `turn_light_on/off`, 컨트롤러 `off`(glow scale 0)↔`on`). 추가로 물고기 2마리(`fish1`/`fish2`)가 항상 좌우로 헤엄치는 `fish` 루프가 `scripts.animate: ["fish", "light_ctrl"]`로 같이 돈다.

## Pending

- 인게임 검증(README NEXT 13번). 자동차 조종감/속도, 좌석 높이, 어항 물고기 경로 미세조정.
- (참고) 자동차의 조종은 `minecraft:behavior.controlled_by_player` 동작에 의존하므로, 인게임에서 조종이 안 되면 컴포넌트 조합을 조정해야 한다.
