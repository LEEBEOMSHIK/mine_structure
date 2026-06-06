# 놀이공원 탈것 (회전목마 / 관람차 / 열기구)

아이들이 좋아할 유니콘 테마 놀이공원 탈것 3종. 생성기 `blockbench/gen_amusement.py`.

## unicorn_carousel (회전목마)

- Identifier: `mine_structure:unicorn_carousel`
- Mechanic: `rideable_simple`(4인) + 항상 회전(`spin` 본, y축 0→360, 6초 루프)
- 모델: 라벤더 바닥 + 민트 플랫폼 + 금색 중앙 기둥 + 계단식 분홍 캐노피 지붕 + 무지개 꼭대기, 4방향 흰 유니콘 말(파란 안장 + 무지개 뿔) — 말은 기둥에 매달린 금색 폴에 연결.
- 좌석은 엔티티 로컬 고정이라 플레이어는 제자리에 앉고 **모델(말·지붕)이 주위로 회전**한다(Bedrock seat 한계).

## unicorn_ferris_wheel (관람차)

- Identifier: `mine_structure:unicorn_ferris_wheel`
- Mechanic: `variant_spin` — 우클릭으로 바퀴 회전 on/off(`blades` 본, z축 360°). `gen_living_furniture.variant_spin_wiring` 재사용.
- 모델: 라벤더 A자 다리 + 바닥 + 무지개 허브, 8개 금색 살(spoke)이 방사형으로 뻗고 끝에 색색 캐빈 8개(분홍/하늘/노랑) + 8각 림 조각. 장식/감상용(탑승 없음).

## unicorn_balloon (열기구)

- Identifier: `mine_structure:unicorn_balloon`
- Mechanic: `rideable_simple`(1인, 바구니 탑승) + 둥실 `bob` 본(y 위아래, 4초 루프)
- 모델: 줄무늬 풍선(분홍/하늘/노랑 계단식 물방울) + 무지개 꼭대기 + 금색 로프 4개 + 갈색 바구니(+금색 림).

## Add-on / 검증

- 각 `addon/behavior_pack/entities/<sid>.entity.json`, `addon/resource_pack/{entity,models/entity,render_controllers,animations}/...`, `textures/entity/<sid>/<sid>_atlas.png`
- 생성: `blockbench/gen_amusement.py`(carousel/ferris/balloon). `embed_animations.py`로 애니 임베드.
- `validate_unicorn_toilet_resources.py`의 `KIDS`에 등록(carousel/balloon=`rideable_simple`, ferris=`variant_spin`). 검증 PASS.
- Blockbench로 3종 모두 모양 확인(MCP).

## 테스트

```
/summon mine_structure:unicorn_carousel
/summon mine_structure:unicorn_ferris_wheel
/summon mine_structure:unicorn_balloon
```
회전목마=탑승+회전, 관람차=우클릭 회전 토글, 열기구=탑승+둥실 확인(인게임 대기).
