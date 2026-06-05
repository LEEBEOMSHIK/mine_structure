# unicorn_bath_kitchen (욕실/주방/로봇)

거품 욕조 · 오븐 · 전자레인지 · 토스터 · 로봇청소기. 모두 파스텔, 뿔 없음.

## Registry

| Identifier | 종류 | 메커니즘 |
|------------|------|----------|
| `mine_structure:unicorn_bathtub` | 거품 욕조 | 물/거품 켜기·끄기(`variant_light`, `glow`=물+거품) |
| `mine_structure:unicorn_oven` | 오븐 | 불 켜기·끄기(`variant_light`, `glow`=내부 불빛) |
| `mine_structure:unicorn_microwave` | 전자레인지 | 창 불 켜기·끄기(`variant_light`) |
| `mine_structure:unicorn_toaster` | 토스터 | Script: 우클릭 시 `minecraft:bread` 지급(+pop) |
| `mine_structure:unicorn_robot_vacuum` | 로봇청소기(몹) | 알아서 돌아다님(`wander`) |

- Content type: furniture entity (로봇청소기는 이동 몹)
- Status: add-on 파일 생성 완료, 인게임 테스트 대기.

## 메커니즘 메모

- **켜기/끄기 토글**(욕조/오븐/전자레인지): 무드등과 동일한 `minecraft:variant` 방식. `light_off`/`light_on` 그룹 교체, 컨트롤러가 `q.variant`로 `glow` 본 scale 0↔1 전환. 욕조는 `glow`가 물+거품, 오븐/전자레인지는 불빛 패널.
- **토스터**: behavior 상호작용 없이 `scripts/main.js`가 `playerInteractWithEntity`에서 처리 → 우클릭 시 `giveItem(... minecraft:bread ...)` + `random.pop`.
- **로봇청소기**(새 `wander` 메커니즘): `minecraft:physics`(중력) + `movement`(0.16, 느릿) + `navigation.walk` + `movement.basic` + `jump.static` + `behavior.float` + `behavior.random_stroll`로 바닥을 알아서 배회한다. 탑승 불가, 순수 자동 이동 + 귀여운 얼굴.

## Add-on Files

- 각 `<id>`: behavior/client entity, geometry, render controller, `textures/entity/<id>/<id>_atlas.png`
- 토글형은 `animations/<id>.animation.json` + `animation_controllers/<id>.animation_controllers.json`
- 토스터 로직: `addon/behavior_pack/scripts/main.js`(`TOASTER_ID`)
- 생성: `blockbench/gen_bath_kitchen.py` · Blockbench 원본 `blockbench/<id>.bbmodel`

## 테스트

```
/summon mine_structure:unicorn_bathtub
/summon mine_structure:unicorn_oven
/summon mine_structure:unicorn_microwave
/summon mine_structure:unicorn_toaster
/summon mine_structure:unicorn_robot_vacuum
```

## Pending

- 인게임 검증(README NEXT 21번). 로봇 이동속도/콜리전, 욕조 물 높이, 토스터 보상 종류 조정 가능.
