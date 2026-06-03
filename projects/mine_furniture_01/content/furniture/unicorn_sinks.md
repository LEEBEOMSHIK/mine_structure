# unicorn_sinks (3종)

세련된 유니콘 컨셉 싱크대 3종. 형태는 2차원 배열로 정의한다(1=블록, 0=빈칸, row 0 = 뒤쪽, 칸 1개 = 1블록 16u).

## Registry

| Identifier | 형태(2D 배열) | 설명 | basin 위치 | 테마 |
|------------|---------------|------|-----------|------|
| `mine_structure:unicorn_sink_l` | `[[1,1,1],[0,0,1]]` | L자 | 가로 3칸 가운데(뒤-가운데) | 딸기(핑크 + ♥) |
| `mine_structure:unicorn_sink_island` | `[[1,1,1],[1,0,1],[1,0,1]]` | 3×3 고리(아일랜드), 앞쪽 가운데가 입구 | 뒤-가운데 칸 | 민트(민트 + ★) |
| `mine_structure:unicorn_sink_u` | `[[1,1,1],[0,0,1],[1,1,1]]` | ㄷ/C자(왼쪽 가운데 개방) | 뒤-가운데 칸 | 레몬(버터옐로 + ○) |

- Content type: furniture entity (multi-block)
- Status: 모델/텍스처/add-on 배선 완료, 물 토글 완료. 인게임 소환/상호작용 테스트 대기.

## Concept / Design 합의

- 메인 basin(세면대 볼) 1개 + 나머지 칸은 매끈한 카운터 상판. 물은 그 basin에서만 나온다.
- 2번(아일랜드)은 닫힌 고리이므로 앞쪽 가운데 한 칸을 입구로 비웠다(가운데 공간으로 진입 가능).
- 유니콘 컨셉: 파스텔 바디 + 림 트림 + 수도꼭지 위 무지개 유니콘 뿔 + 방울/스파클 디테일.
- 3종은 각각 다른 알록달록 테마(아이 친화적): 딸기(핑크/♥) · 민트(민트/★) · 레몬(버터옐로/○). 무지개 뿔 등 유니콘 시그니처는 공통.

## Add-on Files (각 `<id>` = sink_l / sink_island / sink_u)

Behavior pack:
- `../../addon/behavior_pack/entities/<id>.entity.json`

Resource pack:
- `../../addon/resource_pack/entity/<id>.entity.json`
- `../../addon/resource_pack/models/entity/<id>.geo.json`
- `../../addon/resource_pack/render_controllers/<id>.render_controllers.json`
- `../../addon/resource_pack/animations/<id>.animation.json`
- `../../addon/resource_pack/animation_controllers/<id>.animation_controllers.json`
- `../../addon/resource_pack/textures/entity/unicorn_sink/<id>_atlas.png` (테마별 전용, 64×64)

Blockbench 원본(모델별 분리):
- `../../blockbench/unicorn_sink_l.bbmodel`
- `../../blockbench/unicorn_sink_island.bbmodel`
- `../../blockbench/unicorn_sink_u.bbmodel`

생성 스크립트:
- `../../blockbench/gen_unicorn_sinks.py` — geo + 공유 아틀라스 + 3 bbmodel
- `../../blockbench/gen_sink_wiring.py` — behavior/client/render/animation/animation_controller/resources.json

Resource maps: `unicorn_sink_l.resources.json`, `unicorn_sink_island.resources.json`, `unicorn_sink_u.resources.json`

## Model Notes

- 본 구성: `<id>`(root) → `cabinet`(바디/상판/basin 림·벽), `faucet`(post/arm/nozzle/뿔), `water`(부모) → `water_stream`(낙수), `basin_pool`(고인물).
- basin 칸: 하단 솔리드 블록(0~8) + 4면 안쪽 벽(8~12) + 골드 림 프레임(12~13.5)으로 움푹한 10×10 우물을 만든다. 일반 칸은 바디(0~12) + 상판(12~13.5).
- 좌표는 발치(0,0,0) 기준으로 풋프린트를 X/Z 중앙 정렬했다. per-face 풀셀(16×16) UV, 회전 큐브 없음.
- 아틀라스 셀: body(0,0) / top(16,0) / rim(32,0) / wall(48,0) / faucet(0,16) / horn(16,16) / water(32,16).

## 상호작용 (손 상태로 구분)

우클릭 한 번을 손 상태로 나눠 처리한다(전부 `scripts/main.js`).

- **빈손 + 우클릭 → 물 켜기/끄기** (아래 토글)
- **아이템 들고 + 우클릭 → basin(물 나오는 곳) 제외 카운터 위에 그 아이템 1개 올리기** (`spawnItem`, 식탁과 동일 방식). 올릴 위치는 싱크대별 카운터 셀 로컬 오프셋(`SINK_COUNTER_OFFSET`)을 엔티티 yaw로 회전해 계산한다.

물 토글은 더 이상 behavior `minecraft:interact`가 아니라 Script가 처리한다. 상태는 엔티티 dynamic property `sink_water_on`으로 기억하고, `entity.triggerEvent("mine_structure:turn_water_on"/"off")`로 variant component group을 교체한다(시각은 그대로 애니메이션 컨트롤러가 담당). component group에는 `minecraft:variant`만 남기고 interact는 제거했다(이중 발동 방지).

## 물 켜기/끄기 (지속 상태)

- 상태 저장: `minecraft:variant` — `mine_structure:water_off`(value 0) / `mine_structure:water_on`(value 1) component group.
- 토글: Script가 빈손 우클릭 때 dynamic property `sink_water_on`을 뒤집고 `triggerEvent`로 `mine_structure:turn_water_on` / `turn_water_off` 이벤트를 호출해 두 그룹을 교체한다. 스폰 시 `minecraft:entity_spawned`로 `water_off` 적용.
- 표시: 리소스팩 애니메이션 컨트롤러 `controller.animation.<id>.water`가 `q.variant`로 `off`(water 본 scale 0)↔`flowing`(scale 1 + 낙수 위치 루프)을 전환한다. `scripts.animate`에 연결.
- 소리: 빈손 토글 시 Script가 바닐라 `bucket.fill_water`/`bucket.empty_water` 사운드를 재생. 별도 음원 에셋 불필요.
- 청크 리로드에도 variant 값이 유지되므로 물 on/off 상태가 지속된다.

## Pending

- 인게임 소환 테스트: 3종 형태/텍스처 정상 표시, collision_box(현재 width 3.0 / height 1.0) 적정성.
- 우클릭 물 토글: 낙수/고인물 표시·숨김, 상태 지속, 사운드 확인.
- 필요 시 물 위치/수도꼭지 포즈/collision 미세조정.
