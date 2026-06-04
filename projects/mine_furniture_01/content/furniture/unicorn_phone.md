# unicorn_phone

유니콘 스마트폰. 작은 받침대에 세워진 폰으로, 화면 켜기/끄기 토글이 있다.

## Registry

- Identifier: `mine_structure:unicorn_phone`
- Content type: furniture entity
- Status: add-on 파일 생성 완료, 인게임 테스트 대기.

## 구성 / 동작

- 파츠: 받침대(dock) + 킥스탠드 + 폰 바디(파스텔 핑크 케이스) + 어두운 베젤 + 카메라 + 홈버튼. **뿔/귀 없음**(파스텔 색감으로만 유니콘 느낌).
- 화면 토글(무드등과 동일한 `minecraft:variant` 방식): `light_off`(variant 0, 기본)/`light_on`(variant 1) component group을 우클릭으로 교체. 컨트롤러 `controller.animation.unicorn_phone.light`가 `q.variant`로 `off`(`glow` 본 scale 0)↔`on`(scale 1 + 맥동)을 전환.
- 켜면 베젤 앞에 밝은 **귀여운 얼굴 화면**(`glow` 본, `screen` 셀=face, north 면)이 나타나고 끄면 숨겨진다. 청크 리로드에도 상태 유지. 사운드 `random.click`.

## Add-on Files

- `../../addon/behavior_pack/entities/unicorn_phone.entity.json`
- `../../addon/resource_pack/entity/unicorn_phone.entity.json`
- `../../addon/resource_pack/models/entity/unicorn_phone.geo.json`
- `../../addon/resource_pack/render_controllers/unicorn_phone.render_controllers.json`
- `../../addon/resource_pack/animations/unicorn_phone.animation.json` + `../../addon/resource_pack/animation_controllers/unicorn_phone.animation_controllers.json`
- `../../addon/resource_pack/textures/entity/unicorn_phone/unicorn_phone_atlas.png`
- 생성: `../../blockbench/gen_phone.py` · Blockbench 원본 `../../blockbench/unicorn_phone.bbmodel`

## 테스트

```
/summon mine_structure:unicorn_phone
```
우클릭으로 화면 켜기/끄기, 켜면 얼굴 화면 표시·상태 지속 확인.

## Pending

- 인게임 검증(README NEXT 18번). 화면 위치/크기·받침대 각도 미세조정 가능.
