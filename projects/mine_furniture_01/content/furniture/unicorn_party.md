# 파티/장식 6종 (배치 4)

~80종 목표 신규 가구 4차 배치. 생성기 `blockbench/gen_party.py`. 6종 모두 Blockbench로 개별 확인.

| ID | Mechanic | 설명 |
|----|----------|------|
| `mine_structure:unicorn_birthday_cake` | variant_light | 생일케이크(2단+크림+베리, 촛불 glow on/off) |
| `mine_structure:unicorn_balloon_bunch` | static | 풍선다발(색색 풍선 4개+끈+추+리본) |
| `mine_structure:unicorn_garland` | static | 가랜드(무지개 삼각 깃발 줄) |
| `mine_structure:unicorn_chandelier` | variant_light | 샹들리에(체인+4팔+초/크리스탈, 촛불 glow) |
| `mine_structure:unicorn_wall_sconce` | variant_light | 벽촛대(벽판+팔+초, 촛불 glow) |
| `mine_structure:unicorn_standing_lantern` | variant_light | 스탠드 랜턴(기둥+랜턴 등, glass glow on/off) |

## 메커니즘

- **variant_light**(birthday_cake/chandelier/wall_sconce/standing_lantern): `glow` 본(촛불/등불) 우클릭 토글.
- **static**(balloon_bunch/garland): 장식 전용.

## Add-on / 검증

- 생성: `blockbench/gen_party.py`. `KIDS` 등록, 검증 PASS. **6종 전부 Blockbench 렌더로 개별 확인**.

## 테스트

```
/summon mine_structure:unicorn_birthday_cake   (외 5종)
```
케이크/샹들리에/벽촛대/랜턴=우클릭 불빛 토글, 풍선/가랜드=장식 배치(인게임 대기).
