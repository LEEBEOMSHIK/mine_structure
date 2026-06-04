# unicorn_blocks (건축 블록 3종)

직접 쌓아서 집·길을 만들 수 있는 커스텀 블록. 지금까지의 콘텐츠는 모두 엔티티였지만 이건 진짜 블록이다.

## Registry

| Identifier | 이름 | 텍스처 |
|------------|------|--------|
| `mine_structure:unicorn_cloud_block` | 구름 블록 | `unicorn_cloud` (흰 구름) |
| `mine_structure:unicorn_candy_block` | 사탕 블록 | `unicorn_candy` (핑크/흰 줄무늬) |
| `mine_structure:unicorn_star_block` | 별 블록 | `unicorn_star` (밤하늘 + 별) |

- Content type: block (placeable)
- Menu category: construction
- Status: add-on 파일 생성 완료, 인게임 테스트 대기.

## 구조 (데이터 주도형 블록)

- behavior `blocks/<id>.block.json`: `minecraft:material_instances`의 `"*".texture`가 `terrain_texture.json`의 단축명을 가리킨다(render_method `opaque`). `destructible_by_mining`/`destructible_by_explosion`/`map_color`/`friction` 포함. 레거시 `blocks.json`은 쓰지 않는다.
- resource `textures/terrain_texture.json`: 단축명 → `textures/blocks/<name>` 매핑.
- `textures/blocks/<name>.png`: 16×16 블록 텍스처.

## Add-on Files

- `../../addon/behavior_pack/blocks/<id>.block.json` (3종)
- `../../addon/resource_pack/textures/terrain_texture.json`
- `../../addon/resource_pack/textures/blocks/<name>.png` (3종)
- 생성: `../../blockbench/gen_block_textures.py`, `../../blockbench/gen_blocks.py`

## 테스트

크리에이티브 인벤토리 **건축(construction)** 탭에서 3종이 보이고, 설치/파괴되며 텍스처가 정상인지 확인한다.

## Pending

- 인게임 검증(README NEXT 16번). 필요 시 단단함/사운드/특수 효과(예: 구름 블록 점프 부스트) 추가.
