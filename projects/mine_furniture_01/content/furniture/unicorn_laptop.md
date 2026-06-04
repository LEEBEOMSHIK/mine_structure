# unicorn_laptop

유니콘 노트북. 열린 노트북 형태(키보드 + 세워진 화면)에 화면 켜기/끄기 토글이 있다.

## Registry

- Identifier: `mine_structure:unicorn_laptop`
- Content type: furniture entity
- Status: add-on 파일 생성 완료, 인게임 테스트 대기.

## 구성 / 동작

- 파츠: 베이스 deck + 트랙패드 + 힌지 + **개별 모델링한 키캡 32개 + 스페이스바** + 뚜껑(`lid`: 패널 + 베젤 + 귀여운 얼굴 화면) + 작은 하트 액센트.
- **뿔/귀 없음.** 유니콘 느낌은 파스텔 라벤더 셸 + 핑크 액센트 색감으로만 살린다.
- **뚜껑 열기/닫기 토글**(`minecraft:variant`): `lid_open`(variant 0, 기본)/`lid_closed`(variant 1) component group을 우클릭으로 교체. 리소스팩 컨트롤러 `controller.animation.unicorn_laptop.lid`가 `q.variant`로 `open`↔`closed`를 전환하고, 애니메이션이 `lid` 본을 힌지(뒤쪽) 기준으로 0°(닫힘, 키보드 위에 평평)↔100°(열림, 세워짐) 회전한다. 청크 리로드에도 상태 유지. 사운드 `random.click`.
- 화면은 뚜껑 안쪽(열면 사용자 쪽)을 향하는 `screen` 셀(face 스타일 = 귀여운 얼굴)이다.

## Add-on Files

- `../../addon/behavior_pack/entities/unicorn_laptop.entity.json`
- `../../addon/resource_pack/entity/unicorn_laptop.entity.json`
- `../../addon/resource_pack/models/entity/unicorn_laptop.geo.json`
- `../../addon/resource_pack/render_controllers/unicorn_laptop.render_controllers.json`
- `../../addon/resource_pack/animations/unicorn_laptop.animation.json` + `../../addon/resource_pack/animation_controllers/unicorn_laptop.animation_controllers.json`
- `../../addon/resource_pack/textures/entity/unicorn_laptop/unicorn_laptop_atlas.png`
- 생성: `../../blockbench/gen_laptop.py` · Blockbench 원본 `../../blockbench/unicorn_laptop.bbmodel`

## 테스트

```
/summon mine_structure:unicorn_laptop
```
우클릭으로 뚜껑이 열리고 닫히는지(상태 지속), 키보드/화면 디테일 확인.

## Pending

- 인게임 검증(README NEXT 17번). 뚜껑 열림 각도(현재 100°)·화면 위치·키캡 간격 미세조정 가능.
