# 정원/야외 8종 (배치 2)

~80종 목표 신규 가구 2차 배치. 생성기 `blockbench/gen_garden.py`.

| ID | Mechanic | 설명 |
|----|----------|------|
| `mine_structure:unicorn_fountain` | variant_light | 분수대(2단 풀+물 glow, 우클릭 물 on/off) |
| `mine_structure:unicorn_mailbox` | static | 우편함(기둥+박스+깃발+하트) |
| `mine_structure:unicorn_birdcage` | static | 새장(돔 창살+받침+작은 새) |
| `mine_structure:unicorn_bench` | rideable | 벤치(2인 착석, 등받이+팔걸이) |
| `mine_structure:unicorn_parasol_table` | static | 파라솔 테이블(둥근 테이블+무지개 캐노피) |
| `mine_structure:unicorn_campfire` | variant_light | 모닥불(돌+통나무+불꽃 glow, 우클릭 점화/끄기) |
| `mine_structure:unicorn_tent` | rideable | 캠핑텐트(∧ A프레임 + 입구 + 깃발, 들어가 앉기) |
| `mine_structure:unicorn_garden_arch` | static | 정원 아치(기둥+곡선 상단+덩굴/꽃) |

## 메커니즘

- **variant_light**(fountain/campfire): `glow` 본(물/불꽃) 우클릭 토글.
- **rideable**(bench/tent): `minecraft:rideable` 좌석(`rideable_wiring`).
- **static**: 장식 전용(`script_entity(...,"static")`).

## Add-on / 검증

- 생성: `blockbench/gen_garden.py`. `KIDS` 등록, 검증 PASS.
- Blockbench로 분수대(물)·텐트(∧ A프레임)·파라솔·모닥불 등 확인. 텐트는 **회전 경사면**으로 매끄러운 ∧형(처음 계단식에서 개선).

## 테스트

```
/summon mine_structure:unicorn_fountain   (외 7종)
```
분수/모닥불=우클릭 토글, 벤치/텐트=탑승, 나머지=장식 배치(인게임 대기).
