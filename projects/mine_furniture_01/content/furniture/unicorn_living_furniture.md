# unicorn_living_furniture (거실 가구 6종)

소파 · 벽난로 · 선풍기 · 책장 · 옷장 · 피아노. 파스텔, 뿔 없음.

## Registry

| Identifier | 가구 | 메커니즘 |
|------------|------|----------|
| `mine_structure:unicorn_sofa` | 소파 | `minecraft:rideable` 3인 |
| `mine_structure:unicorn_fireplace` | 벽난로 | 불 켜기/끄기(`variant_light`, `glow`=불꽃) |
| `mine_structure:unicorn_fan` | 선풍기 | 날개 회전 on/off(`variant_spin`, `blades` 본 z 360° 루프) |
| `mine_structure:unicorn_bookshelf` | 책장 | Script 수납(`script_store`) |
| `mine_structure:unicorn_wardrobe` | 옷장 | Script 수납(`script_store`) |
| `mine_structure:unicorn_piano` | 피아노 | Script 연주(`script_play`, `note.harp` 랜덤 음) |

- Content type: furniture entity
- Status: add-on 파일 생성 완료, 인게임 테스트 대기.

## 메커니즘 메모

- **소파**: rideable 좌석 3개 나란히.
- **벽난로**: 무드등과 같은 `minecraft:variant` 토글. 우클릭 시 `glow`(불꽃 cubes) 표시/숨김. 상태 지속.
- **선풍기**(새 `variant_spin`): `light_off`/`light_on` 그룹 + 컨트롤러 `controller.animation.unicorn_fan.light`가 `q.variant`로 `off`(blades 정지)↔`on`(blades z축 360° 회전 루프) 전환.
- **책장/옷장**: behavior 상호작용 없이 `scripts/main.js`가 `playerInteractWithEntity`에서 처리 → barrel 수납과 같은 `storeOrRetrieveItem`(아이템 들고=저장 / 빈손=꺼내기). dynamic property `bookshelf_items`(12칸) / `wardrobe_items`(18칸).
- **피아노**: 우클릭 시 `note.harp`를 랜덤 피치로 재생 + `note_particle`.

## Add-on Files

- 각 `<id>`: behavior/client entity, geometry, render controller, `textures/entity/<id>/<id>_atlas.png`
- 벽난로/선풍기는 `animations/<id>.animation.json` + `animation_controllers/<id>.animation_controllers.json`
- 책장/옷장/피아노 로직: `addon/behavior_pack/scripts/main.js`
- 생성: `blockbench/gen_living_furniture.py` · Blockbench 원본 `blockbench/<id>.bbmodel`

## 테스트

```
/summon mine_structure:unicorn_sofa
/summon mine_structure:unicorn_fireplace
/summon mine_structure:unicorn_fan
/summon mine_structure:unicorn_bookshelf
/summon mine_structure:unicorn_wardrobe
/summon mine_structure:unicorn_piano
```

## Pending

- 인게임 검증(README NEXT 22번). 소파 좌석 높이, 불꽃/날개 위치, 수납 칸수, 피아노 음계 조정 가능.
