# unicorn_kids_furniture (4종)

아이들이 좋아할 유니콘 가구 4종. 각각 검증된 상호작용 패턴을 재사용한다.

## Registry

| Identifier | 가구 | 메커니즘 | 비고 |
|------------|------|----------|------|
| `mine_structure:unicorn_rocking_horse` | 흔들목마 | `minecraft:rideable`(1인) + 항상 흔들 애니 | 안장 좌석 `[0,0.9,0]`, `rock` 본 ±7° 2.4초 루프 |
| `mine_structure:unicorn_night_lamp` | 무드등 | `minecraft:variant` on/off 토글 | 켜면 `glow` 후광 표시, 상태 지속 |
| `mine_structure:unicorn_ice_cream_machine` | 아이스크림 기계 | Script API 간식 지급 | 우클릭 시 랜덤 간식 1개 + 소리 |
| `mine_structure:unicorn_cloud_bunk_bed` | 구름 2층침대 | `minecraft:rideable`(2인) | 좌석 `[0,0.5,0]`(아래) / `[0,1.3,0]`(위) |

- Content type: furniture entity
- Status: 모델/텍스처/add-on 배선 완료, 인게임 소환/상호작용 테스트 대기.
- 공통: 파스텔 + 무지개 뿔/갈기 등 유니콘 시그니처 + 방울/스파클. 모델별 전용 아틀라스.

## Add-on Files (각 `<id>`)

Behavior pack: `../../addon/behavior_pack/entities/<id>.entity.json`
Resource pack:
- `../../addon/resource_pack/entity/<id>.entity.json`
- `../../addon/resource_pack/models/entity/<id>.geo.json`
- `../../addon/resource_pack/render_controllers/<id>.render_controllers.json`
- `../../addon/resource_pack/textures/entity/<id>/<id>_atlas.png`
- (흔들목마) `../../addon/resource_pack/animations/unicorn_rocking_horse.animation.json` — `rock` 루프
- (무드등) `../../addon/resource_pack/animations/unicorn_night_lamp.animation.json` + `../../addon/resource_pack/animation_controllers/unicorn_night_lamp.animation_controllers.json`

Script: 아이스크림 기계는 `../../addon/behavior_pack/scripts/main.js`의 `dispenseTreat` 핸들러를 사용한다.

Blockbench 원본(모델별 분리): `../../blockbench/<id>.bbmodel`
생성 스크립트: `../../blockbench/gen_kids_furniture.py`, `../../blockbench/gen_kids_wiring.py`
Resource maps: `<id>.resources.json`

## 메커니즘 메모

- **흔들목마**: rideable로 우클릭 탑승. 별도 상태 없이 `rock` 본이 항상 흔들리도록 `scripts.animate: ["rock"]`로 루프 재생(아이들이 보기에 살아있는 느낌). 안장 좌석에 1명.
- **무드등**: 싱크대 물 토글과 동일 구조. `light_off`(variant 0)/`light_on`(variant 1) component group을 우클릭으로 교체, 리소스팩 컨트롤러 `controller.animation.<id>.light`가 `q.variant`로 `off`(glow scale 0)↔`on`(glow scale 1 + 맥동)을 전환. 스폰 시 `minecraft:entity_spawned`로 off.
- **아이스크림 기계**: behavior 상호작용 없이 Script API `world.afterEvents.playerInteractWithEntity`에서 처리. 우클릭하면 `ICE_CREAM_TREATS`(cookie/sweet_berries/glow_berries/pumpkin_pie/honey_bottle) 중 랜덤 1개를 플레이어 인벤토리에 추가, 가득 차면 기계 위치에 스폰, `random.pop` 사운드 재생.
- **구름 2층침대**: rideable 좌석 2개(아래/위 칸). 두 플레이어가 각각 앉/눕는다.

## Pending

- 인게임 소환/상호작용 테스트(README NEXT 11번 참고).
- 좌석 위치/흔들 진폭/후광 크기/collision_box 미세조정.
