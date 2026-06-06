# unicorn_cruise

타고 직접 모는 유니콘 크루즈 보트. 물 위를 운전하는 탈것(자동차 운전 메커니즘의 물 버전).

## Registry

- Identifier: `mine_structure:unicorn_cruise`
- Content type: vehicle entity
- Status: add-on 파일 생성 완료, 인게임 테스트 대기(실험적).

## 구성 / 동작

- 외형: 테이퍼 선체(뱃머리 -Z) + 갑판 + 선실/브리지 + 2단 굴뚝 + 현창 + 승객 쿠션 + 뱃머리 무지개 깃발. 파스텔, 뿔 없음.
- **물에 뜸**: `minecraft:buoyant`(water/flowing_water).
- **조종**: `minecraft:behavior.controlled_by_player` + `minecraft:movement`(0.3) + `minecraft:navigation.generic`(is_amphibious, can_swim, can_walk) + `minecraft:movement.amphibious`. 운전석에서 WASD로 이동(물/땅 양쪽).
- **탑승**: `minecraft:rideable` 좌석 4개, `controlling_seat: 0`(운전석) + 승객 3.
- 깃발은 `flag` 본이 `scripts.animate: ["wave"]`로 살랑인다.

## Add-on Files

- `addon/behavior_pack/entities/unicorn_cruise.entity.json`
- `addon/resource_pack/entity/unicorn_cruise.entity.json`
- `addon/resource_pack/models/entity/unicorn_cruise.geo.json`
- `addon/resource_pack/render_controllers/unicorn_cruise.render_controllers.json`
- `addon/resource_pack/animations/unicorn_cruise.animation.json` (flag wave)
- `addon/resource_pack/textures/entity/unicorn_cruise/unicorn_cruise_atlas.png`
- 생성: `blockbench/gen_cruise.py` · Blockbench 원본 `blockbench/unicorn_cruise.bbmodel`

## 테스트 / 한계

```
/summon mine_structure:unicorn_cruise   (물가에서)
```
타고 WASD로 물 위 운전, 물에 뜨는지, 좌석 4개 탑승 확인.

- **한계**: 엔티티는 충돌박스가 하나라 **갑판 위를 자유롭게 걸어다닐 수는 없다**(타고 이동하는 방식). 걸어다니는 대형 크루즈는 구조물(.mcstructure) 방식이 필요하다.
- 플레이어가 직접 모는 물 위 탈것은 Bedrock에서 버전 민감 → 조종/부력이 어색하면 컴포넌트 조합 보정 필요.

## Pending

- 인게임 검증(README NEXT 23번). 속도/조종감/부력/좌석 위치 미세조정.
