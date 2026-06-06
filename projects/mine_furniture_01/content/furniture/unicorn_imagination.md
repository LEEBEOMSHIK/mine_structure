# 상상놀이 세트 (성 텐트 / 인형의 집 / 장난감 상자 / 이젤)

방 안에서 노는 아이 친화 상상놀이 가구 4종. 생성기 `blockbench/gen_imagination.py`.

## unicorn_castle_tent (성 텐트)

- Identifier: `mine_structure:unicorn_castle_tent`
- Mechanic: `rideable_simple`(1인, 텐트 안에 앉기)
- 모델: 핑크 사각 벽 + 앞면 입구(보라 문기둥) + 금색 트림 + 파란 계단식 첨탑 지붕 + 무지개 깃발.

## unicorn_dollhouse (인형의 집)

- Identifier: `mine_structure:unicorn_dollhouse`
- Mechanic: `variant_light` — 우클릭으로 창문 불빛 on/off(`glow` 본).
- 모델: 크림색 2층 벽 + 분홍 박공 지붕 + 무지개 하트 용마루 + 민트 창틀 4개(창문=glow) + 문/손잡이 + 굴뚝.

## unicorn_toy_box (장난감 상자)

- Identifier: `mine_structure:unicorn_toy_box`
- Mechanic: `script_store` — 아이템 들고 우클릭=보관 / 빈손=꺼내기(최대 12칸, dynamic property `toy_box_items`). `scripts/main.js` `storeOrRetrieveItem` 재사용.
- 모델: 나무 상자 + 민트 트림(위/아래) + 활짝 열린 분홍 뚜껑(뒤로 -58° 경첩) + 무지개 별 + 삐져나온 장난감(공/블록).

## unicorn_easel (이젤)

- Identifier: `mine_structure:unicorn_easel`
- Mechanic: `variant_light` — 우클릭으로 캔버스에 그림 나타나기/지우기(`glow` 본 = 그림).
- 모델: 나무 삼각대(앞 2다리 벌어짐 + 뒤 1다리) + 트레이 + 민트 프레임 + 흰 캔버스 + 분홍 그림(glow) + 무지개 별.

## Add-on / 검증

- 각 `addon/behavior_pack/entities/<sid>.entity.json`, `addon/resource_pack/{entity,models/entity,render_controllers[,animations,animation_controllers]}/...`, `textures/entity/<sid>/<sid>_atlas.png`
- 장난감 상자 로직: `addon/behavior_pack/scripts/main.js`(`TOY_BOX_ID`, `TOY_BOX_PROPERTY`, `storeOrRetrieveItem`)
- 생성: `blockbench/gen_imagination.py`. `embed_animations.py`로 불빛 애니 임베드.
- `validate_unicorn_toilet_resources.py`의 `KIDS`에 등록(tent=`rideable_simple`, dollhouse/easel=`variant_light`, toy_box=`script_store`). 검증 PASS. Blockbench로 4종 확인.

## 테스트

```
/summon mine_structure:unicorn_castle_tent
/summon mine_structure:unicorn_dollhouse
/summon mine_structure:unicorn_toy_box
/summon mine_structure:unicorn_easel
```
성 텐트=탑승, 인형의 집/이젤=우클릭 불빛/그림 토글, 장난감 상자=아이템 보관/꺼내기 확인(인게임 대기).
