# unicorn_costume (입는 코스튬)

캐릭터에 착용하면 보이는 드레스업. **머리띠**는 커스텀 attachable(실험적), **날개**는 바닐라 elytra와 별개인 커스텀 글라이더(**나비 날개** 외형)로 처리한다.

## Registry

| Identifier | 이름 | 방식 |
|------------|------|------|
| `mine_structure:unicorn_horn_headband` | 유니콘 뿔 머리띠 | wearable(head) + attachable, 본 `head` |
| `mine_structure:unicorn_elytra` | 나비 날개 | wearable(chest) + glider + 커스텀 나비 날개 모델 (바닐라 elytra와 별개) |

- Content type: wearable item
- Status: add-on 파일 생성 완료, **인게임 검증 대기(실험적)**.

## 날개 = elytra 바탕 커스텀 (바닐라는 그대로!)

바닐라 elytra는 **건드리지 않고**, elytra를 바탕으로 한 **별도 커스텀 글라이더** `mine_structure:unicorn_elytra`를 만들었다.

- item: `minecraft:wearable`(slot.armor.chest) + `minecraft:glider`(활공) + `minecraft:durability`(432) + 아이콘/이름.
- attachable(`attachables/unicorn_elytra.attachable.json`): 커스텀 geometry/texture + `render_controllers: ["controller.render.armor"]` + `scripts.animate: ["glide"]`.
- geometry(`models/entity/unicorn_elytra.geo.json`): `body`(플레이어 몸 본) 하위에 `left_wing`/`right_wing` 본. **각 날개는 큐브 더미가 아니라 얇은 평면 1장**이고, 날개 모양은 텍스처에 **알파 컷아웃(투명 가장자리)**으로 그린다. 외형은 **나비 날개**: 둥근 forewing(분홍→라벤더 그라데이션) + hindwing(하늘→민트), 몸통에서 방사하는 진보라 **날개맥**, 각 lobe의 **eyespot(눈알 무늬)**, 가장자리 진한 띠 + 연노랑 점박이. 해상도 32×64(atlas 128). `gen_custom_elytra.py`의 `butterfly_edge` 실루엣 + `draw_wing`(그라데이션/날개맥/점)+ `spot`(eyespot). 옆면 슬리버 면은 투명 픽셀로 매핑해 보이지 않게 했다. Blockbench 원본 `../../blockbench/unicorn_elytra.bbmodel`.
- 애니메이션: `controller.animation.unicorn_elytra.glide`가 `q.is_gliding`으로 `folded`(접힘, 등에 붙음)↔`spread`(펴짐)를 전환.
- 생성: `../../blockbench/gen_custom_elytra.py`

### ⚠️ 리스크 (가장 불확실)

커스텀 글라이더 + 플레이어 부착 애니메이션은 Bedrock에서 매우 버전 민감하다. 인게임에서 다음을 확인/보정해야 한다.
- `minecraft:glider` 컴포넌트가 해당 버전에서 활공을 실제로 부여하는지(미지원이면 착용·외형만 되고 활공 불가).
- attachable 컨텍스트에서 `q.is_gliding`이 동작해 접힘/펴짐이 전환되는지.
- `controller.render.armor`로 커스텀 geometry가 렌더되는지(안 되면 커스텀 RC 필요).
- 접힘 포즈 회전 각도(`folded`)와 날개 위치/피벗.

## 구조

## 머리띠 구조

- item: `minecraft:wearable`(slot.armor.head) + `minecraft:icon` + `minecraft:display_name` + max_stack 1.
- attachable(`attachables/unicorn_horn_headband.attachable.json`): geometry/texture/materials + `render_controllers: ["controller.render.armor"]`.
- geometry(`models/entity/unicorn_horn_headband.geo.json`): 루트 본 이름을 플레이어 `head` 본으로 맞춰, 착용 시 머리를 따라 렌더된다. 머리(y24..32) 둘레에 밴드+뿔+귀.
- 텍스처: 아이콘 16×16 + 3D 아틀라스 64×64. 생성 `../../blockbench/gen_costume.py`, Blockbench 원본 `../../blockbench/unicorn_horn_headband.bbmodel`.

## 테스트 / 리스크

```
/give @s mine_structure:unicorn_horn_headband
/give @s mine_structure:unicorn_elytra
```
머리띠는 머리 슬롯 착용 시 머리에 보이는지, 엘리트라는 가슴 착용 후 점프+활공·접힘/펴짐이 되는지 확인한다(바닐라 elytra는 영향 없음).

- **알려진 리스크**: 커스텀 방어구 attachable은 버전에 따라 안 보이거나 위치/스케일이 어긋날 수 있다. 문제가 있으면 다음을 조정한다.
  - render controller(`controller.render.armor`) ↔ 커스텀 RC 교체
  - geometry 본 이름/피벗이 플레이어 스켈레톤과 일치하는지
  - 텍스처 해상도와 geo의 texture_width/height 일치

## Pending

- 인게임 검증(README NEXT 16번). 표시되면 위치/크기 미세조정, 안 되면 attachable 방식 보정.
