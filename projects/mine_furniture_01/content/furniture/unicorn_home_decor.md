# 홈데코 8종 (배치 1)

~80종 목표의 신규 가구 1차 배치. 생성기 `blockbench/gen_home_decor.py`.

| ID | Mechanic | 설명 |
|----|----------|------|
| `mine_structure:unicorn_coffee_table` | static | 커피테이블(상판+다리4+하단선반+하트) |
| `mine_structure:unicorn_rug` | static | 러그(납작, 동심 무지개 링+별) |
| `mine_structure:unicorn_wall_clock` | static | 벽시계(원형 프레임+시침/분침+숫자점) |
| `mine_structure:unicorn_picture_frame` | static | 액자(금 프레임+매트+그림) |
| `mine_structure:unicorn_potted_plant` | static | 화분(흙+줄기+잎4+분홍 꽃) |
| `mine_structure:unicorn_floor_lamp` | variant_light | 플로어램프(우클릭 갓 불빛 on/off) |
| `mine_structure:unicorn_dresser` | script_store | 서랍장(아이템 보관/꺼내기, 18칸 `dresser_items`) |
| `mine_structure:unicorn_nightstand` | static | 협탁(서랍+다리4) |

## 메커니즘

- **static**: 장식 전용 엔티티(상호작용 없음). `script_entity(sid, "static", w, h)` — common_components + static_client + resources. validate에 `static` 분기 추가(파일/identifier만 검증).
- **variant_light**(floor_lamp): `glow` 본 우클릭 토글.
- **script_store**(dresser): `scripts/main.js` `DRESSER_ID`/`DRESSER_PROPERTY` + `storeOrRetrieveItem`(18칸).

## Add-on / 검증

- 각 `addon/behavior_pack/entities/<sid>.entity.json`, `addon/resource_pack/{entity,models/entity,render_controllers[,animations,animation_controllers]}/...`, `textures/entity/<sid>/<sid>_atlas.png`
- 생성: `blockbench/gen_home_decor.py`. `KIDS` 등록, 검증 PASS. Blockbench로 화분/플로어램프 등 확인.

## 테스트

```
/summon mine_structure:unicorn_coffee_table   (외 7종)
```
정적 가구는 소환 후 배치, 플로어램프=우클릭 불빛, 서랍장=아이템 보관/꺼내기 확인(인게임 대기).
