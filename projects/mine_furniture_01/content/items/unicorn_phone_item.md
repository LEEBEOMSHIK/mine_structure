# unicorn_phone_item

손에 들고 다니는 3D 유니콘 핸드폰. 바닥에 놓는 거치형 `unicorn_phone`(엔티티)과는 **별개의 아이템**이다.

## Registry

- Identifier: `mine_structure:unicorn_phone_item`
- Content type: held item (3D attachable)
- Menu category: equipment
- Status: add-on 파일 생성 완료, 인게임 테스트 대기(hold 포즈 미세조정 필요).

## 구성 / 동작

- 검(`unicorn_horn_blade`)과 같은 방식: `minecraft:hand_equipped` 아이템 + attachable.
- attachable(`attachables/unicorn_phone_item.attachable.json`): `controller.render.item_default` + `scripts`(item_slot/first_person 분기) + 1·3인칭 × 주손·보조손 hold 애니 4종.
- 외형: 파스텔 핑크 케이스 + 어두운 베젤 + 카메라 + 홈버튼 + 귀여운 얼굴 화면(항상 표시). 2D 인벤토리 아이콘 + 3D 손모델.
## 기능 (Script, 우클릭)

- 📸 **셀카** (그냥 우클릭): 하트 + 반짝(`villager_happy`) 파티클 + 찰칵 소리 + 짧은 벨소리 멜로디(`note.bell` 4음).
- 🔦 **손전등** (웅크리고 우클릭): 야간투시 on/off 토글(플레이어 dynamic property `phone_flashlight`로 상태 기억).
- 🎵 벨소리/음악은 셀카에 함께 묶여 재생된다.
- `minecraft:cooldown`(0.6초)으로 연타 방지. 로직은 `scripts/main.js`의 `phoneSelfie`/`phoneFlashlight` + `world.afterEvents.itemUse`.
- (거치형 폰과 달리 화면 on/off 토글은 없음 — 손에 든 모델 + 위 기능.)

## Add-on Files

- `../../addon/behavior_pack/items/unicorn_phone_item.item.json`
- `../../addon/resource_pack/attachables/unicorn_phone_item.attachable.json`
- `../../addon/resource_pack/models/entity/unicorn_phone_item.geo.json`
- `../../addon/resource_pack/animations/unicorn_phone_item.animation.json` (hold 포즈 4종)
- `../../addon/resource_pack/textures/items/unicorn_phone_item.png` (16×16 아이콘, `item_texture.json` 등록)
- `../../addon/resource_pack/textures/entity/unicorn_phone_item/unicorn_phone_item_atlas.png` (3D 아틀라스)
- 생성: `../../blockbench/gen_phone_item.py` · Blockbench 원본 `../../blockbench/unicorn_phone_item.bbmodel`

## 테스트

```
/give @s mine_structure:unicorn_phone_item
```
손에 들었을 때 1·3인칭에서 3D 핸드폰이 보이는지, **우클릭=셀카(플래시+찰칵+멜로디)**, **웅크리고 우클릭=손전등(야간투시) on/off**가 되는지 확인. (스크립트 효과 → behavior pack + Beta API 실험 옵션 필요.)

## Pending

- hold 포즈(위치/회전/스케일) 인게임 미세조정(`resources.json` `in_hand_pose_tuned: false`). 값은 `animations/unicorn_phone_item.animation.json`에서 조정.
