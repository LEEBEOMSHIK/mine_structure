# unicorn_room_furniture (방 가구 4종)

TV · 아케이드 게임기 · 거울 화장대 · 킹사이즈 침대. 모두 파스텔, 뿔 없음.

## Registry

| Identifier | 가구 | 메커니즘 |
|------------|------|----------|
| `mine_structure:unicorn_tv` | 유니콘 TV(스탠드형) | 화면 켜기/끄기(`variant_light`) |
| `mine_structure:unicorn_arcade` | 아케이드 게임기 | 화면 켜기/끄기(`variant_light`) |
| `mine_structure:unicorn_vanity` | 거울 화장대 | 거울 전구 켜기/끄기(`variant_light`, `glow`=전구) |
| `mine_structure:unicorn_king_bed` | 킹사이즈 침대(단층) | `minecraft:rideable` 좌석 2개(`rideable_simple`) |

- Content type: furniture entity
- Status: add-on 파일 생성 완료, 인게임 테스트 대기.

## 메커니즘 메모

- **화면/전구 토글**(TV/아케이드/화장대): 무드등과 동일한 `minecraft:variant` 방식. `light_off`(0)/`light_on`(1) component group을 우클릭으로 교체, 컨트롤러 `controller.animation.<id>.light`가 `q.variant`로 `off`(`glow` 본 scale 0)↔`on`(scale 1 + 맥동) 전환. TV/아케이드는 `glow`가 얼굴 화면 패널, 화장대는 `glow`가 거울 둘레 전구 묶음. 상태 지속, 사운드 `random.click`.
- **킹침대**: `minecraft:rideable` 좌석 2개(`[-0.5,0.55,0]`/`[0.5,0.55,0]`)로 두 명이 나란히 눕/앉는다. (riding은 앉는 자세 — 바닐라엔 눕는 포즈 없음.)

## Add-on Files (각 `<id>`)

- `../../addon/behavior_pack/entities/<id>.entity.json`
- `../../addon/resource_pack/entity/<id>.entity.json`
- `../../addon/resource_pack/models/entity/<id>.geo.json`
- `../../addon/resource_pack/render_controllers/<id>.render_controllers.json`
- 토글형은 `animations/<id>.animation.json` + `animation_controllers/<id>.animation_controllers.json`
- `../../addon/resource_pack/textures/entity/<id>/<id>_atlas.png`
- 생성: `../../blockbench/gen_room_furniture.py` · Blockbench 원본 `../../blockbench/<id>.bbmodel`

## 테스트

```
/summon mine_structure:unicorn_tv
/summon mine_structure:unicorn_arcade
/summon mine_structure:unicorn_vanity
/summon mine_structure:unicorn_king_bed
```
토글형은 우클릭 켜기/끄기, 침대는 좌석 2개 탑승 확인.

## Pending

- 인게임 검증(README NEXT 20번). 화면 위치/크기, 전구 배치, 침대 좌석 높이 미세조정 가능.
- Blockbench MCP 세션이 끊겨 있던 동안 생성됨 → 재연결 후 bbmodel 열어 확인 권장.
