# unicorn_playground (놀이터 3종)

그네 · 미끄럼틀 · 시소. 모두 파스텔, 뿔 없음.

## Registry

| Identifier | 놀이기구 | 메커니즘 |
|------------|----------|----------|
| `mine_structure:unicorn_swing` | 그네 | rideable(1) + 항상 흔들 애니(`rock`) |
| `mine_structure:unicorn_slide` | 미끄럼틀 | rideable(1, 상단 착석) |
| `mine_structure:unicorn_seesaw` | 시소 | rideable(2, 양끝) |

- Content type: furniture entity
- Status: add-on 파일 생성 완료, 인게임 테스트 대기.

## 메커니즘 메모

- **그네**: A-프레임(정적) + 줄/시트는 `rock` 본. `scripts.animate: ["rock"]`로 항상 ±22° 흔들린다. `minecraft:rideable` 1인.
- **미끄럼틀**: 계단 + 계단식 미끄럼판 + 상단 플랫폼. rideable 1인(상단 착석). (활강 물리는 없음 — 착석/장식.)
- **시소**: 받침점 + 긴 널 + 양끝 좌석/손잡이. rideable 2인.
- (참고) riding은 앉는 자세이고, 좌석은 엔티티 기준 고정이라 그네/시소 애니메이션과 함께 플레이어가 움직이지는 않는다(시각 연출). 바닐라 한계.

## Add-on Files

- 각 `<id>`: behavior/client entity, geometry, render controller, `textures/entity/<id>/<id>_atlas.png`
- 그네는 `animations/unicorn_swing.animation.json`(rock)
- 생성: `blockbench/gen_playground.py` · Blockbench 원본 `blockbench/<id>.bbmodel`

## 테스트

```
/summon mine_structure:unicorn_swing
/summon mine_structure:unicorn_slide
/summon mine_structure:unicorn_seesaw
```
탑승, 그네 흔들림, 좌석 위치 확인.

## Pending

- 인게임 검증(README NEXT 21번). 좌석 높이/그네 진폭/미끄럼틀 각도 조정 가능.
