# unicorn_horn_blade

## Registry

- Bedrock identifier: `mine_structure:unicorn_horn_blade`
- Content type: weapon item (sword class)
- Category: fantasy weapon
- Status: add-on files generated (2D icon + 3D in-hand attachable). In-hand pose needs in-game tuning; textures are first-pass.

## Concept

검으로 취급하지만 외형은 **유니콘 뿔**이다. 인벤토리에서는 나선형 뿔 픽셀 아이콘으로 보이고, 손에 들면 비틀린 테이퍼 뿔이 3D로 검처럼 보인다.

## Source Documents

- Progress summary: `../../README.md`
- Common Blockbench/MCP rules: `../../../../docs/agent-guides/blockbench-mcp-rules.md`
- Resource map: `unicorn_horn_blade.resources.json`

## Add-on Files

Behavior pack:

- `../../addon/behavior_pack/items/unicorn_horn_blade.item.json`

Resource pack:

- `../../addon/resource_pack/attachables/unicorn_horn_blade.attachable.json`
- `../../addon/resource_pack/models/entity/unicorn_horn_blade.geo.json`
- `../../addon/resource_pack/animations/unicorn_horn_blade.animation.json`
- `../../addon/resource_pack/textures/item_texture.json`
- `../../addon/resource_pack/textures/items/unicorn_horn_blade.png` (16×16 inventory icon)
- `../../addon/resource_pack/textures/entity/unicorn_horn_blade/unicorn_horn_blade.png` (64×64 3D model atlas)
- `unicorn_horn_blade.resources.json`

Texture generator: `../../blockbench/gen_unicorn_horn_blade_textures.py`
bbmodel 면-텍스처 교정: `../../blockbench/fix_bbmodel_face_textures.py`

## Stats (fantasy strong weapon)

| Property | Value |
|----------|-------|
| Attack damage (`minecraft:damage`) | 9 |
| Durability (`minecraft:durability`) | 1800 |
| Enchantable slot | `sword` (value 14) |
| Repair item | diamond (+250) |
| Stack size | 1 |
| Menu category | equipment |

## Model Notes

- Blockbench `furniture` 프로젝트에 `unicorn_horn_blade` 루트 그룹으로 제작. 월드 오프셋 `[120, 0, 0]`에 배치하고, `geometry.unicorn_horn_blade`는 중심좌표(오프셋 차감)로 직접 작성했다.
- 구성: 폼멜 + 라벤더 그립 + 무지개 가드 + 베이스 글로우 + 6단 테이퍼 뿔 날(각 단을 Y축으로 12°→112° 비틀어 나선 실루엣). 총 1 bone / 10 cubes.
- 뿔 날은 +Y로 솟고 그립은 -Y로 내려간다. bone pivot은 가드 위치 `[0, 0, 0]`.
- 텍스처/UV: 칼날 큐브가 작아(0.5~2.6) box UV가 거의 0폭으로 퇴화하며 뿔이 흰색으로 보이는 문제가 있었다. 그래서 **명시적 per-face UV로 단색 스와치**를 가리키게 바꿨다(geo.json도 `uv:{north:{uv,uv_size}...}` 형식). 아틀라스 스와치: 뿔=`[0,0]` 16×16(진한 분홍 펄+나선+스파클), 그립=`[16,0]` 8×8(라벤더), 폼멜=`[24,0]` 8×8(골드), 베이스글로우=`[32,0]` 8×8(시안), 가드=면별 무지개(`[40,0]`~`[56,8]`). 아틀라스 전체가 불투명이라 빈 픽셀(흰색)을 샘플하지 않는다.
- 뿔 색은 옅은 펄이 흰색처럼 보여 **진한 분홍(236,130,200)**으로 올렸다.

## Blockbench 저장 주의 (codec quirk)

이 환경의 Blockbench project 저장 코덱은 **모든 큐브 면의 텍스처 바인딩을 "현재 선택된 텍스처" 하나로 평탄화**한다. 그래서 `furniture.bbmodel`을 저장하면 모든 모델이 한 텍스처를 뒤집어쓰게 되어, 다시 열면 미리보기가 어긋난다(인게임 리소스는 별개라 영향 없음).

→ **`furniture.bbmodel`을 저장한 직후 반드시 `blockbench/fix_bbmodel_face_textures.py`를 실행**해 면 텍스처 바인딩을 모델별로 복구한다(각 루트 그룹 → 자기 아틀라스: 변기→toilet, 식탁→dining, 의자→chair, barrel→barrel, 인형→doll, 칼날→horn_blade). 루트 그룹 기준이라 멱등이며 여러 번 실행해도 안전하다.

## Held Rendering

- `unicorn_horn_blade.attachable.json`이 item identifier와 동일한 식별자로 3D 모델/텍스처/render controller(`controller.render.item_default`)를 연결한다.
- `unicorn_horn_blade.animation.json`이 1·3인칭 × 주손·보조손 4종 hold 포즈를 정의한다. 현재 값은 보수적 기본값이며 **인게임에서 손 위치/회전/스케일 미세조정 필요**(`resources.json` status `in_hand_pose_tuned: false`).

## Pending

- 인게임 소환/장착 테스트: 인벤토리 아이콘 표시, 손에 든 3D 뿔 포즈, 공격 데미지/내구도/검 인챈트 동작 확인.
- hold 애니메이션 값 미세조정.
- 전용 텍스처 디테일 보강(현재는 1차 픽셀 아트).
