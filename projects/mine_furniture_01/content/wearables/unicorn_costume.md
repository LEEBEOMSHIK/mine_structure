# unicorn_costume (입는 코스튬 2종)

캐릭터에 착용하면 보이는 드레스업 아이템. **플레이어 부착 커스텀은 Bedrock에서 가장 버전 민감한 부분이라 인게임 검증이 필수다(실험적).**

## Registry

| Identifier | 이름 | 슬롯 | 부착 본 |
|------------|------|------|---------|
| `mine_structure:unicorn_horn_headband` | 유니콘 뿔 머리띠 | `slot.armor.head` | `head` |
| `mine_structure:unicorn_wings` | 유니콘 날개 | `slot.armor.chest` | `body` |

- Content type: wearable item (방어구 슬롯, protection 0 = 순수 코스튬)
- Status: add-on 파일 생성 완료, **인게임 검증 대기(가장 불확실)**.

## 구조

- item: `minecraft:wearable`(slot) + `minecraft:icon` + `minecraft:display_name` + max_stack 1.
- attachable(`attachables/<id>.attachable.json`): geometry/texture/materials + `render_controllers: ["controller.render.armor"]`.
- geometry(`models/entity/<id>.geo.json`): 루트 본 이름을 **플레이어 본**(머리띠=`head`, 날개=`body`)으로 맞춰, 착용 시 해당 신체 부위를 따라 렌더된다. 머리띠는 머리(y24..32) 둘레에 밴드+뿔+귀, 날개는 등(z>2)에 무지개 날개.
- 텍스처: 아이콘 16×16(`textures/items/<id>.png`) + 3D 아틀라스 64×64(`textures/entity/<id>/<id>.png`).
- 생성: `../../blockbench/gen_costume.py`

## 테스트 / 리스크

```
/give @s mine_structure:unicorn_horn_headband
/give @s mine_structure:unicorn_wings
```
머리/가슴 슬롯에 착용 후 캐릭터에 3D로 보이는지 확인한다.

- **알려진 리스크**: 커스텀 방어구 attachable은 버전에 따라 안 보이거나 위치/스케일이 어긋날 수 있다. 문제가 있으면 다음을 조정한다.
  - render controller(`controller.render.armor`) ↔ 커스텀 RC 교체
  - geometry 본 이름/피벗이 플레이어 스켈레톤과 일치하는지
  - 텍스처 해상도와 geo의 texture_width/height 일치

## Pending

- 인게임 검증(README NEXT 16번). 표시되면 위치/크기 미세조정, 안 되면 attachable 방식 보정.
