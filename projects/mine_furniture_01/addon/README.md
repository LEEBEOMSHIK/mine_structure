# Add-on Package Layout

이 폴더는 `mine_furniture_01` 프로젝트의 Minecraft Bedrock add-on 산출물을 담는다.

## Pack 구조

- `behavior_pack/` — 엔티티/아이템 동작, 상호작용, 스크립트
- `resource_pack/` — geometry, texture, animation, render controller, sound, client entity

## 현재 등록 준비 콘텐츠

- `mine_structure:unicorn_toilet` — 첫 번째 가구 엔티티. 모델/텍스처/애니메이션은 Blockbench에서 내보낸 뒤 resource pack 경로에 연결한다.

## 다음 연결 작업

1. Blockbench에서 `../blockbench/export_unicorn_toilet_to_resource_pack.js`에 기록된 경로를 기준으로 geometry를 `resource_pack/models/entity/unicorn_toilet.geo.json`로 내보낸다.
2. 텍스처 아틀라스를 `resource_pack/textures/entity/unicorn_toilet/unicorn_toilet_atlas.png`로 저장한다.
3. 실제 Blockbench animation export가 있으면 `resource_pack/animations/unicorn_toilet.animation.json`을 덮어쓴다.
4. 물내림 사운드를 `resource_pack/sounds/flush.ogg`로 추가한다.
5. Minecraft에서 behavior pack/resource pack을 함께 활성화해 엔티티 소환과 애니메이션을 검증한다.
