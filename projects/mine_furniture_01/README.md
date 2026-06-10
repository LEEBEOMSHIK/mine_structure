# mine_furniture_01 — Bedrock Furniture & Weapons Add-on

Minecraft Bedrock용 **여러 가구와 무기**를 묶는 add-on 프로젝트다. 현재 유니콘 테마 가구 라인으로 **무지개 유니콘 변기(`unicorn_toilet`)**, **유니콘 식탁(`unicorn_dining_table`)**, **유니콘 의자(`unicorn_chair`)**, **유니콘 barrel 수납장(`unicorn_barrel_cabinet`)**, **장식용 유니콘 인형(`decorative_unicorn_doll`)**을 관리한다.

## 1. 프로젝트 범위

- 목표: 가구와 무기를 하나의 Bedrock add-on 패키지로 관리한다.
- Pack 구성:
  - `addon/behavior_pack/` — 엔티티, 아이템, 상호작용, 스크립트
  - `addon/resource_pack/` — geometry, texture, animation, render controller, sound
- 콘텐츠 관리:
  - `content/furniture/` — 가구별 등록 문서
  - `content/weapons/` — 무기별 등록 문서
- Blockbench 작업물:
  - `blockbench/` — 원본 모델 파일을 보관할 위치

## 2. 현재 등록 콘텐츠

| ID | Type | Status | Document |
|----|------|--------|----------|
| `mine_structure:unicorn_toilet` | furniture entity | model/texture/animation ready, add-on files ready | `content/furniture/unicorn_toilet.md` |
| `mine_structure:unicorn_dining_table` | furniture entity | static model/texture ready, add-on files ready | `content/furniture/unicorn_dining_table.md` |
| `mine_structure:unicorn_chair` | furniture entity | static model/texture ready, add-on files ready | `content/furniture/unicorn_chair.md` |
| `mine_structure:unicorn_barrel_cabinet` | furniture entity | model/texture ready, Script API simple storage added | `content/furniture/unicorn_barrel_cabinet.md` |
| `mine_structure:decorative_unicorn_doll` | furniture entity | static model ready (pony rebuild), texture placeholder, no interaction | `content/furniture/decorative_unicorn_doll.md` |
| `mine_structure:unicorn_horn_blade` | weapon item (sword) | 2D icon + 3D attachable ready, in-hand pose needs in-game tuning | `content/weapons/unicorn_horn_blade.md` |
| `mine_structure:unicorn_sink_l` | furniture entity | model/texture/add-on ready, 빈손=물 토글 / 아이템=카운터 올리기, in-game test 대기 | `content/furniture/unicorn_sinks.md` |
| `mine_structure:unicorn_sink_island` | furniture entity | model/texture/add-on ready, 빈손=물 토글 / 아이템=카운터 올리기, in-game test 대기 | `content/furniture/unicorn_sinks.md` |
| `mine_structure:unicorn_sink_u` | furniture entity | model/texture/add-on ready, 빈손=물 토글 / 아이템=카운터 올리기, in-game test 대기 | `content/furniture/unicorn_sinks.md` |
| `mine_structure:unicorn_rocking_horse` | furniture entity | rideable + 흔들 애니, in-game test 대기 | `content/furniture/unicorn_kids_furniture.md` |
| `mine_structure:unicorn_night_lamp` | furniture entity | variant on/off 무드등, in-game test 대기 | `content/furniture/unicorn_kids_furniture.md` |
| `mine_structure:unicorn_ice_cream_machine` | furniture entity | Script API 간식 지급, in-game test 대기 | `content/furniture/unicorn_kids_furniture.md` |
| `mine_structure:unicorn_cloud_bunk_bed` | furniture entity | rideable 2층 침대, in-game test 대기 | `content/furniture/unicorn_kids_furniture.md` |
| `mine_structure:unicorn_baby_pet` | pet mob | 길들이기→따라오기+탑승, walk/idle 애니, in-game test 대기 | `content/furniture/unicorn_more_furniture.md` |
| `mine_structure:unicorn_gacha_machine` | furniture entity | Script 랜덤 보상(가챠), in-game test 대기 | `content/furniture/unicorn_more_furniture.md` |
| `mine_structure:unicorn_trampoline` | furniture entity | Script 점프 바운스, in-game test 대기 | `content/furniture/unicorn_more_furniture.md` |
| `mine_structure:unicorn_gift_box` | furniture entity | 뚜껑 열기 애니 + Script 선물, in-game test 대기 | `content/furniture/unicorn_more_furniture.md` |
| `mine_structure:unicorn_car` | vehicle entity | 탑승 운전(조종), 바퀴 회전, in-game test 대기 | `content/furniture/unicorn_vehicles_pets.md` |
| `mine_structure:unicorn_baby_dragon` | pet mob | 길들이기→따라오기+탑승, in-game test 대기 | `content/furniture/unicorn_vehicles_pets.md` |
| `mine_structure:unicorn_aquarium` | furniture entity | 물고기 헤엄 + 불빛 on/off, in-game test 대기 | `content/furniture/unicorn_vehicles_pets.md` |
| `mine_structure:unicorn_pegasus` | mount entity | 탑승 비행(수평 조종+점프/웅크림 상하), in-game test 대기 | `content/furniture/unicorn_vehicles_pets.md` |
| `mine_structure:unicorn_fridge` | furniture entity | 문 열기 애니 + 간식 저장/꺼내기, in-game test 대기 | `content/furniture/unicorn_vehicles_pets.md` |
| `mine_structure:unicorn_cookie` | food item | 먹으면 허기 회복 + 회복(Regeneration) 효과, in-game test 대기 | `content/foods/unicorn_cookie.md` |
| `mine_structure:unicorn_cupcake` | food item | 컵케이크, 회복 효과, in-game test 대기 | `content/foods/unicorn_treats.md` |
| `mine_structure:unicorn_lollipop` | food item | 막대사탕, 스피드, in-game test 대기 | `content/foods/unicorn_treats.md` |
| `mine_structure:unicorn_rainbow_drink` | food item | 무지개 음료, 스피드+점프, in-game test 대기 | `content/foods/unicorn_treats.md` |
| `mine_structure:unicorn_star_candy` | food item | 별사탕, 야간투시, in-game test 대기 | `content/foods/unicorn_treats.md` |
| `mine_structure:unicorn_wand` | tool item | 마법 지팡이, 우클릭 파티클+점프/스피드 부스트, 손에 3D 막대 모델, in-game test 대기 | `content/items/unicorn_wand.md` |
| `mine_structure:unicorn_cloud_block` | block | 구름 블록(건축용), in-game test 대기 | `content/blocks/unicorn_blocks.md` |
| `mine_structure:unicorn_candy_block` | block | 사탕 블록(건축용), in-game test 대기 | `content/blocks/unicorn_blocks.md` |
| `mine_structure:unicorn_star_block` | block | 별 블록(건축용), in-game test 대기 | `content/blocks/unicorn_blocks.md` |
| `mine_structure:unicorn_horn_headband` | wearable | 뿔 머리띠(머리 착용 코스튬), in-game test 대기(실험) | `content/wearables/unicorn_costume.md` |
| `mine_structure:unicorn_elytra` | wearable glider | 나비 날개(가슴 착용, 활공, 접힘/펴짐), 바닐라 elytra와 별개, in-game test 대기(실험) | `content/wearables/unicorn_costume.md` |
| `mine_structure:unicorn_rainbow_skirt` | wearable | 입체 A라인 무지개 프릴 스커트(다리 슬롯), in-game test 대기(실험) | `content/wearables/unicorn_costume.md` |
| `mine_structure:unicorn_laptop` | furniture entity | 유니콘 노트북, 뚜껑 열기/닫기 토글, 디테일 키보드, in-game test 대기 | `content/furniture/unicorn_laptop.md` |
| `mine_structure:unicorn_phone` | furniture entity | 유니콘 핸드폰(받침대 거치), 화면 켜기/끄기 토글, in-game test 대기 | `content/furniture/unicorn_phone.md` |
| `mine_structure:unicorn_phone_item` | held item | 손에 드는 핸드폰(3D attachable), in-game test 대기 | `content/items/unicorn_phone_item.md` |
| `mine_structure:unicorn_tv` | furniture entity | 유니콘 TV, 화면 켜기/끄기, in-game test 대기 | `content/furniture/unicorn_room_furniture.md` |
| `mine_structure:unicorn_arcade` | furniture entity | 아케이드 게임기, 화면 켜기/끄기, in-game test 대기 | `content/furniture/unicorn_room_furniture.md` |
| `mine_structure:unicorn_vanity` | furniture entity | 거울 화장대, 전구 켜기/끄기, in-game test 대기 | `content/furniture/unicorn_room_furniture.md` |
| `mine_structure:unicorn_king_bed` | furniture entity | 킹사이즈 침대(단층), rideable 2인, in-game test 대기 | `content/furniture/unicorn_room_furniture.md` |
| `mine_structure:unicorn_bathtub` | furniture entity | 거품 욕조, 우클릭 시 물이 **차오름**(+거품), in-game test 대기 | `content/furniture/unicorn_bath_kitchen.md` |
| `mine_structure:unicorn_oven` | furniture entity | 오븐, 불 켜기·끄기, in-game test 대기 | `content/furniture/unicorn_bath_kitchen.md` |
| `mine_structure:unicorn_microwave` | furniture entity | 전자레인지, 창 불 켜기·끄기, in-game test 대기 | `content/furniture/unicorn_bath_kitchen.md` |
| `mine_structure:unicorn_toaster` | furniture entity | 토스터, 우클릭 토스트 지급, in-game test 대기 | `content/furniture/unicorn_bath_kitchen.md` |
| `mine_structure:unicorn_robot_vacuum` | mob | 로봇청소기, 알아서 돌아다님, in-game test 대기 | `content/furniture/unicorn_bath_kitchen.md` |
| `mine_structure:unicorn_swing` | furniture entity | 그네, rideable + 흔들 애니, in-game test 대기 | `content/furniture/unicorn_playground.md` |
| `mine_structure:unicorn_slide` | furniture entity | 미끄럼틀, rideable(상단 착석), in-game test 대기 | `content/furniture/unicorn_playground.md` |
| `mine_structure:unicorn_seesaw` | furniture entity | 시소, rideable 2인, in-game test 대기 | `content/furniture/unicorn_playground.md` |
| `mine_structure:unicorn_sofa` | furniture entity | 소파, rideable 3인, in-game test 대기 | `content/furniture/unicorn_living_furniture.md` |
| `mine_structure:unicorn_fireplace` | furniture entity | 벽난로, 불 켜기/끄기, in-game test 대기 | `content/furniture/unicorn_living_furniture.md` |
| `mine_structure:unicorn_fan` | furniture entity | 선풍기, 날개 회전 on/off, in-game test 대기 | `content/furniture/unicorn_living_furniture.md` |
| `mine_structure:unicorn_bookshelf` | furniture entity | 책장, 아이템 수납, in-game test 대기 | `content/furniture/unicorn_living_furniture.md` |
| `mine_structure:unicorn_wardrobe` | furniture entity | 옷장, 아이템 수납, in-game test 대기 | `content/furniture/unicorn_living_furniture.md` |
| `mine_structure:unicorn_piano` | furniture entity | 피아노, 우클릭 연주(음 소리), in-game test 대기 | `content/furniture/unicorn_living_furniture.md` |
| `mine_structure:unicorn_cruise` | vehicle entity | 타고 모는 크루즈 보트(물 위 운전, 4인), in-game test 대기 | `content/furniture/unicorn_cruise.md` |
| `mine_structure:unicorn_transform_wand` | tool item | 변신 마법봉(동물 우클릭→랜덤 동물로 변신), 손에 3D 막대 모델, in-game test 대기 | `content/items/unicorn_transform_wand.md` |
| `mine_structure:unicorn_carousel` | furniture entity | 회전목마(탑승 4인 + 항상 회전), in-game test 대기 | `content/furniture/unicorn_amusement.md` |
| `mine_structure:unicorn_ferris_wheel` | furniture entity | 관람차(우클릭 회전 토글), in-game test 대기 | `content/furniture/unicorn_amusement.md` |
| `mine_structure:unicorn_balloon` | furniture entity | 열기구(탑승 1인 + 둥실), in-game test 대기 | `content/furniture/unicorn_amusement.md` |
| `mine_structure:unicorn_castle_tent` | furniture entity | 성 텐트(들어가 앉기), in-game test 대기 | `content/furniture/unicorn_imagination.md` |
| `mine_structure:unicorn_dollhouse` | furniture entity | 인형의 집(창문 불빛 토글), in-game test 대기 | `content/furniture/unicorn_imagination.md` |
| `mine_structure:unicorn_toy_box` | furniture entity | 장난감 상자(보관/꺼내기), in-game test 대기 | `content/furniture/unicorn_imagination.md` |
| `mine_structure:unicorn_easel` | furniture entity | 이젤(캔버스 그림 토글), in-game test 대기 | `content/furniture/unicorn_imagination.md` |

## 3. `unicorn_toilet` 현재 상태

### 모델

- Blockbench 프로젝트 `furniture`, 포맷 **Bedrock Entity(`bedrock`)**.
- 총 ~39 큐브 / 16 그룹. 중심 `x=8`, 바닥 `y=0`, 정면=앞(낮은 `z`).
- 파츠 그룹: `unicorn_toilet` 하위에 `base_plinth`, `toilet_body`, `toilet_bowl`, `toilet_seat`, `toilet_lid_open`, `water_tank`, `tank_lid`, `unicorn_horn`, `left_ear`/`right_ear`, `rainbow_mane`, `sparkle_decorations`, `side_rainbow_sticker`, `water`, `flush_button`.

### 텍스처

- 단일 아틀라스 `unicorn_toilet_atlas` 64x64, 16x16 셀 13종.
- 각 면 UV를 해당 셀 16x16 풀범위로 고정 (`autouv=0`).

### 애니메이션

| Name | Behavior | Loop / Length |
|------|----------|---------------|
| `lid_open` | 뚜껑 0도에서 88도 위로 열림 | hold / 0.55s |
| `lid_close` | 뚜껑 88도에서 0도로 닫힘 | hold / 0.55s |
| `flush` | 버튼 눌림, 물 빠짐/소용돌이/리필, 사운드 키프레임 `flush` | once / 1.8s |

상세 좌표와 텍스처 셀은 `unicorn_toilet_spec.md`를 기준으로 한다.

## 4. Add-on 준비 상태

기본 pack 구조와 `unicorn_toilet` 등록 초안은 생성되어 있다. Blockbench MCP 등록 예시와 export 대상 경로도 추가되어 있다.

- Behavior manifest: `addon/behavior_pack/manifest.json`
- Resource manifest: `addon/resource_pack/manifest.json`
- Behavior entity: `addon/behavior_pack/entities/unicorn_toilet.entity.json`
- Client entity: `addon/resource_pack/entity/unicorn_toilet.entity.json`
- Render controller: `addon/resource_pack/render_controllers/unicorn_toilet.render_controllers.json`
- Animation scaffold: `addon/resource_pack/animations/unicorn_toilet.animation.json`
- Sound definition: `addon/resource_pack/sounds/sound_definitions.json`
- Resource map: `content/furniture/unicorn_toilet.resources.json`
- MCP export target script: `blockbench/export_unicorn_toilet_to_resource_pack.js`

실제 산출물 상태:

- `addon/resource_pack/models/entity/unicorn_toilet.geo.json` — **생성됨 (2026-05-31)**. `geometry.unicorn_toilet`, bone 16, 큐브 40.
- `addon/resource_pack/textures/entity/unicorn_toilet/unicorn_toilet_atlas.png` — **생성됨 (2026-05-31)**. 64×64 PNG.
- `blockbench/furniture.bbmodel` — **저장소에 확보됨 (2026-06-01)**. 현재 Blockbench에 열린 `furniture` 프로젝트를 저장소 경로로 export했다.
- `addon/resource_pack/sounds/flush.ogg` — **생성됨 (2026-06-01)**. 기본 합성 물내림 효과음이며, 추후 최종 제공 음원이 있으면 같은 파일명으로 교체 예정.

## 4.1 JSON 배선 검증 (2026-05-31)

resource pack 측 JSON 연결을 교차검증했다. 결과:

- **geometry identifier**: client entity가 `geometry.unicorn_toilet`을 참조 → PASS. 단 `.geo.json` 미존재로 geo 파일 내부 identifier는 export 후 재확인 필요.
- **texture path**: client entity `textures/entity/unicorn_toilet/unicorn_toilet_atlas` → resources.json과 일치, PASS. PNG 파일만 누락.
- **animation 이름**: `lid_open`/`lid_close`/`flush` 3종 모두 client entity ↔ `unicorn_toilet.animation.json` 일치 → PASS.
- **animation 내용**: 현재 animation.json은 손으로 작성한 scaffold이며 `unicorn_toilet_spec.md` 3절 수치와 일치. 실제 Blockbench export 산출물이 없어 그대로 유지(덮어쓰지 않음).
- **flush 사운드 배선**: `sound_definitions.json` `flush` → `sounds/flush`, animation `sound_effects` `flush`와 일치, PASS. `flush.ogg`는 2026-06-01 기본 합성 효과음으로 추가됨.
- **본 이름 의존성**: animation이 참조하는 `toilet_lid_open`/`flush_button`/`tank_water_grp`/`bowl_water_grp`는 향후 geo.json bone에 반드시 존재해야 한다(spec 1절 그룹과 일치 예정).

### 차단 요소 (Blocker) — 해소됨 (2026-05-31)

- ~~Blockbench MCP 미연결~~ → **연결됨**. 세션 시작 시 `furniture`(unicorn_toilet, 큐브 40/그룹 18, 64×64 atlas) 프로젝트가 이미 빌드된 채 열려 있었다(모델 재빌드 불필요).
- ~~`.bbmodel` 원본 없음~~ → `blockbench/furniture.bbmodel`로 저장소에 확보 완료.
- geometry/texture export 완료. `flush.ogg`는 기본 합성 효과음으로 확보했으며, 최종 음원이 제공되면 교체한다. `.bbmodel` 원본도 현재 저장소 경로에 확보했다.

## 4.2 Export 작업 로그 (2026-05-31)

- geometry는 `Codecs.bedrock.compile()` 결과를 `risky_eval` + `fs.writeFileSync`로 기록 → bone 16 / 큐브 40 / `geometry.unicorn_toilet` 확인.
- texture는 atlas의 PNG dataURL을 디코드해 기록(64×64, PNG 시그니처 검증).
- `.bbmodel`은 `Codecs.project.compile()`로 저장(원본 save_path가 저장소 밖이라 저장소 경로로 별도 기록).
- 프로젝트에 애니메이션은 0개 → scaffold `animations/unicorn_toilet.animation.json`이 유일 소스, 덮어쓸 export 결과 없음(유지).
- **MCP 도구 주의**: `export_model`(codec `bedrock`)이 root bone 1개짜리 **빈 geometry**를 출력하는 버그가 있었다. geo export는 `export_model` 대신 `Codecs.bedrock.compile()` 직접 호출로 우회할 것.

## 4.3 리소스 보정 / 패키징 로그 (2026-06-01)

- `addon/resource_pack/sounds/flush.ogg`를 기본 합성 OGG/Vorbis 효과음으로 추가했다. 길이 1.6초, mono, 48kHz.
- 누락돼 있던 `addon/resource_pack/textures/entity/unicorn_toilet/unicorn_toilet_atlas.png`를 `unicorn_toilet_spec.md`의 64×64 / 16px 셀 아틀라스 기준으로 생성했다.
- `unicorn_toilet.geo.json` 내부 identifier가 `geometry.unknown`이라 client entity 참조값인 `geometry.unicorn_toilet`과 불일치했다. `geometry.unicorn_toilet`로 수정했다.
- 현재 Blockbench에 열린 `furniture` 프로젝트의 save path는 `C:\project\game\mine_structure\furniture.bbmodel`였고, 저장소 작업 경로는 `C:\project\mine_structure`였다. 이 경로 차이 때문에 작업트리에서 `.bbmodel`이 보이지 않았다. 2026-06-01에 열린 프로젝트를 `projects/mine_furniture_01/blockbench/furniture.bbmodel`로 export했다.
- 리소스 검증 스크립트 `validate_unicorn_toilet_resources.py`를 추가했다.
  - 실행: `python projects/mine_furniture_01/validate_unicorn_toilet_resources.py`
  - 현재 결과: PASS
- 플레이어 상호작용 트리거 방식은 behavior component 방식으로 확정했다.
  - `minecraft:interact`가 `mine_structure:flush` 이벤트와 `flush` 사운드를 트리거한다.
  - `mine_structure:play_flush` 이벤트가 `playanimation @s animation.unicorn_toilet.flush`를 `queue_command`로 실행한다.
- 소환 테스트용 패키지를 생성했다.
  - `dist/mine_furniture_01-20260601-005635/mine_furniture_01.mcaddon`
  - 개별 pack: 같은 폴더의 `mine_furniture_01_behavior_pack.mcpack`, `mine_furniture_01_resource_pack.mcpack`
- 현재 실행 환경에는 Bedrock 기본 `com.mojang` 경로가 없어 Minecraft 앱 기반 소환 테스트는 직접 수행하지 못했다.

## 4.4 유니콘 식탁/의자 추가 로그 (2026-06-01)

- `mine_structure:unicorn_dining_table`과 `mine_structure:unicorn_chair`를 독립 furniture entity로 등록했다.
- 두 엔티티 모두 behavior/client entity, geometry, render controller, 64×64 texture atlas, resource map을 추가했다.
- Blockbench `furniture` 프로젝트에는 `unicorn_dining_table` 루트 그룹을 추가했다.
  - 그룹 구성: `table_top`, `table_legs`, `rainbow_runner`, `horn_centerpiece`, `sparkle_place_settings`
  - 큐브 수: 16
  - 배치: 기존 `unicorn_toilet` 오른쪽에 보이도록 x 21~47 범위에 배치
  - Blockbench save path를 `projects/mine_furniture_01/blockbench/furniture.bbmodel`로 맞췄다.
- Blockbench `furniture` 프로젝트에는 `unicorn_chair` 루트 그룹도 추가했다.
  - 그룹 구성: `seat`, `legs`, `backrest`, `unicorn_head_details`, `rainbow_mane`
  - 큐브 수: 16
  - 배치: 식탁 앞쪽에 보이도록 x 28~42, z -19~-4 범위에 배치
  - 텍스처: `unicorn_chair_atlas.png`
- 식탁 첫 버전 구성: 파스텔 세라믹 상판, 라벤더 다리/테두리, 무지개 러너, 유니콘 뿔 센터피스, 반짝이 플레이스 세팅.
- 의자 첫 버전 구성: 핑크 시트, 라벤더 다리/테두리, 흰색 등받이, 유니콘 귀/뿔, 등받이 뒤 무지개 갈기.
- 현재 Blockbench `furniture` 프로젝트 루트 그룹은 `unicorn_toilet`, `unicorn_dining_table`, `unicorn_chair` 3개다.
- `validate_unicorn_toilet_resources.py`를 전체 furniture resource 검증으로 확장했다.
  - 현재 결과: `PASS: furniture resource links are valid`
- 최신 테스트용 패키지:
  - `dist/mine_furniture_01-20260601-010941/mine_furniture_01.mcaddon`

## 4.5 식탁/의자 behavior 작업 로그 (2026-06-01)

- `unicorn_chair`에 `minecraft:rideable`을 추가했다.
  - `seat_count`: 1
  - `family_types`: `["player"]`
  - `seats.position`: `[0, 0.55, 0]`
- behavior pack에 Script API 모듈을 추가했다.
  - manifest script entry: `scripts/main.js`
  - dependency: `@minecraft/server` `2.1.0`
- `scripts/main.js`에서 `world.afterEvents.playerInteractWithEntity`를 구독한다.
- `unicorn_dining_table` 상호작용:
  - 플레이어가 아이템을 들고 식탁과 상호작용하면 주 손 아이템 1개를 식탁 위에 `spawnItem`으로 생성한다.
  - 플레이어 주 손 스택은 1개 줄인다.
  - 빈 손이면 아무 동작도 하지 않는다.
- 현재 제한:
  - 식탁 위 아이템은 일반 dropped item entity라서 플레이어가 다시 주울 수 있다.
  - 아직 아이템을 식탁에 고정하거나 전용 display entity로 렌더링하지는 않는다.
- 최신 테스트용 패키지:
  - `dist/mine_furniture_01-20260601-015204/mine_furniture_01.mcaddon`

## 4.6 식탁 뿔 센터피스 제거 (2026-06-01)

- `unicorn_dining_table`에서 유니콘 뿔 센터피스(`horn_centerpiece` 본, 큐브 3개)를 제거했다.
- 적용: `addon/resource_pack/models/entity/unicorn_dining_table.geo.json`에서 해당 본 삭제 → 식탁 본 구성은 `table_top`, `table_legs`, `rainbow_runner`, `sparkle_place_settings`(큐브 13개).
- 텍스처 아틀라스는 그대로 둠(뿔이 쓰던 셀은 미사용 상태로 남김).
- `blockbench/furniture.bbmodel` 원본에서도 `horn_centerpiece` 그룹을 삭제했다. 이후 Blockbench에서 재export해도 식탁 센터피스가 되살아나지 않는다.

## 4.7 barrel 수납장 / 장식용 인형 추가 (2026-06-01)

- `mine_structure:unicorn_barrel_cabinet`을 독립 furniture entity로 등록했다.
  - Blockbench 루트 그룹: `unicorn_barrel_cabinet`
  - 리소스: behavior/client entity, geometry, render controller, 64×64 texture atlas, resource map
  - 동작: Script API 간이 수납. 아이템을 들고 상호작용하면 1개 저장, 빈 손으로 상호작용하면 가장 최근 저장한 아이템 1개를 꺼낸다.
  - 제한: type/amount만 저장하며, 커스텀 NBT/내구도/인챈트/전용 UI는 첫 버전에 포함하지 않는다.
- `mine_structure:decorative_unicorn_doll`을 독립 furniture entity로 등록했다.
  - Blockbench 루트 그룹: `decorative_unicorn_doll`
  - 리소스: behavior/client entity, geometry, render controller, 64×64 texture atlas, resource map
  - 동작: 순수 장식. `minecraft:interact`, Script API 핸들러, `minecraft:rideable`을 추가하지 않았다.
- 현재 Blockbench `furniture` 프로젝트 루트 그룹은 `unicorn_toilet`, `unicorn_dining_table`, `unicorn_chair`, `unicorn_barrel_cabinet`, `decorative_unicorn_doll` 5개다.
- `validate_unicorn_toilet_resources.py`를 새 가구 2종과 Blockbench 원본 동기화(`horn_centerpiece` 부재)까지 검증하도록 확장했다.
- 최신 테스트용 패키지:
  - `dist/mine_furniture_01-20260601-094146/mine_furniture_01.mcaddon`

## 4.8 장식용 인형 조랑말(포니) 재설계 (2026-06-01)

- `decorative_unicorn_doll`을 직립 박스 인형 → **네 발로 선 조랑말(포니) 실루엣**으로 다시 만들었다. 유니콘이 말로 읽히도록 형태를 전면 교체했다.
  - 몸통: 세로 박스 → 가로형 배럴(barrel) + 앞쪽 가슴(chest)
  - 다리: 배럴 네 모서리 아래 4개로 서는 자세
  - 목: 앞으로 22° 기울인 들린 목(`neck`) 신규
  - 머리: 앞으로 뻗은 주둥이(`muzzle`) + 콧구멍 2 + 입
  - 유니콘 디테일: 3단 테이퍼 뾰족 뿔(전방 기울임), 작은 곧은 귀, 이마 앞머리(forelock), 목덜미 무지개 갈기 크레스트, 뒤쪽 2단 꼬리
- 지오메트리: `geometry.decorative_unicorn_doll`, **6 bones / 27 cubes**.
- 원본 `blockbench/furniture.bbmodel`을 갱신하고, `decorative_unicorn_doll.geo.json`을 중심좌표(오프셋 `[72, 0, 7]` 차감)로 재생성했다.
- 텍스처 `decorative_unicorn_doll_atlas.png`는 여전히 플레이스홀더다. 에디터 프리뷰는 toilet 아틀라스를 빌려 쓰고, 새 큐브 UV는 기존 뿔/갈기/꼬리/분홍 영역을 재사용한다. 전용 아틀라스 페인팅은 미완.

## 4.9 유니콘 뿔 검 무기 추가 (2026-06-01)

- 첫 무기 콘텐츠 `mine_structure:unicorn_horn_blade`를 등록했다. **검으로 취급(데미지/내구도/검 인챈트)하되 외형은 유니콘 뿔**이다.
- 사양(판타지 강무기): `minecraft:damage` 9, `minecraft:durability` 1800, `minecraft:enchantable` slot `sword`(value 14), 다이아몬드 수리(+250), stack 1, menu category `equipment`.
- 외형: **2D 인벤토리 아이콘 + 3D 손모델(attachable) 둘 다**.
  - behavior 아이템: `addon/behavior_pack/items/unicorn_horn_blade.item.json`
  - 3D 모델: Blockbench 전용 프로젝트 `blockbench/unicorn_horn_blade.bbmodel`에 `unicorn_horn_blade` 루트 그룹으로 관리. 폼멜+라벤더 그립+무지개 가드+베이스 글로우+6단 테이퍼 뿔 날(Y축 12°→112° 비틀어 나선). 1 bone / 10 cubes. `geometry.unicorn_horn_blade`는 중심좌표로 직접 작성.
  - attachable `addon/resource_pack/attachables/unicorn_horn_blade.attachable.json` + hold 애니메이션 `animations/unicorn_horn_blade.animation.json`(1·3인칭 × 주손·보조손 4종).
  - 2D 아이콘 `textures/items/unicorn_horn_blade.png`(16×16), 3D 아틀라스 `textures/entity/unicorn_horn_blade/unicorn_horn_blade.png`(64×64). 생성 스크립트 `blockbench/gen_unicorn_horn_blade_textures.py`.
  - 아이콘 매핑 `textures/item_texture.json` 신규 추가(shortname `unicorn_horn_blade`).
- `validate_unicorn_toilet_resources.py`에 무기 검증(`WEAPONS`, `validate_weapon`)과 Blockbench 원본 분리/face texture binding 검증을 추가했다. 현재 결과 PASS.
- 칼날 큐브에 전용 아틀라스를 적용하고 box UV를 geo.json과 동일하게 맞춰 Blockbench 미리보기에서도 색이 보이게 했다. 뿔 칼날 스와치는 흰색을 쓰지 않는 무지개 펄 나선 패턴으로 보강했다.
- **Blockbench 저장 주의**: 이 환경의 project 저장 코덱이 모든 면 텍스처를 "선택된 텍스처" 하나로 평탄화하는 버그가 있다. 가구는 `furniture.bbmodel`, 무기는 `unicorn_horn_blade.bbmodel`로 분리해 영향 범위를 끊었다. `furniture.bbmodel` 저장 직후 가구 텍스처가 섞이면 `blockbench/fix_bbmodel_face_textures.py`를 실행한다. 인게임 리소스는 영향 없음.
- 에디터 미리보기 개선(2026-06-01): 이전에는 전 가구가 toilet 아틀라스를 공유 미리보기로 써서 식탁/의자 등이 어색하게 보였다. 각 루트 그룹을 자기 아틀라스(barrel/doll 아틀라스는 신규 임포트)에 바인딩해 에디터에서도 모델별 텍스처가 보이도록 했다.
- **미완**: 손 안에서의 정확한 포즈(위치/회전/스케일)는 보수적 기본값이라 인게임 미세조정이 필요하다(`unicorn_horn_blade.resources.json` status `in_hand_pose_tuned: false`). 텍스처도 1차 픽셀 아트다.

## 4.10 가구 아틀라스 귀여운 재제작 (2026-06-01)

- 에디터에서 전 가구가 toilet 아틀라스를 공유 미리보기로 쓰던 것을 각 모델 전용 아틀라스 바인딩으로 바꾸자, 전용 아틀라스가 단색 위주라 밋밋해 보이는 문제가 있었다.
- `blockbench/gen_cute_furniture_atlases.py`로 식탁/의자/barrel/인형 전용 아틀라스를 재제작했다. 각 16×16 셀의 기존 기본색은 유지하고, 그 위에 toilet 아틀라스 스타일의 **세로 음영 + 스파클 + 방울 speckle** 디테일을 입혔다. UV가 셀 단위라 에디터·인게임 모두 디테일이 제자리에 들어간다.
- 결과: 각 가구가 자기 색 정체성을 유지하면서 방울·스파클의 귀여운 질감을 갖는다. 인게임에서도 동일하게 적용된다(전용 아틀라스가 곧 인게임 텍스처이므로).

## 4.11 칼날 텍스처/Blockbench 바인딩 보정 (2026-06-01)

- 원인: `furniture.bbmodel` 저장 후 모든 큐브 face texture가 `unicorn_toilet_atlas.png`로 평탄화되어 있었다. 이 상태에서 칼날 텍스처를 바꾸면 가구들도 같은 텍스처를 참조해 함께 바뀌어 보인다.
- 조치: `blockbench/fix_bbmodel_face_textures.py`를 실행해 루트 그룹별 face texture binding을 복구했다.
  - 가구 5종은 각자 전용 아틀라스.
  - `unicorn_horn_blade`는 `unicorn_horn_blade.png`.
- 칼날 뿔 스와치를 흰색 없는 무지개 펄 나선 패턴으로 재생성했다.
- 추가 원인: Blockbench는 `.bbmodel` 안에도 텍스처 이미지를 base64로 임베드한다. 외부 PNG만 바꾸면 다시 열어도 내부에 박힌 예전 칼날 텍스처가 보일 수 있다.
- `blockbench/gen_unicorn_horn_blade_textures.py`가 이제 외부 resource pack PNG와 `.bbmodel` 내부 임베드 텍스처 source를 함께 갱신한다.
- `validate_unicorn_toilet_resources.py`가 `.bbmodel` face texture binding, 외부 칼날 스와치, `.bbmodel` 내부 임베드 칼날 스와치 색상까지 검증하도록 확장됐다.
- 최신 테스트용 패키지:
  - `dist/mine_furniture_01-20260601-213910/mine_furniture_01.mcaddon`

## 4.12 무기 Blockbench 프로젝트 분리 (2026-06-01)

- `unicorn_horn_blade`를 `furniture.bbmodel`에서 제거하고, 전용 원본 `blockbench/unicorn_horn_blade.bbmodel`로 분리했다.
- 현재 `furniture.bbmodel` 루트 그룹은 가구 5종만 가진다.
- `unicorn_horn_blade.bbmodel` 루트 그룹은 `unicorn_horn_blade` 1개이며, 텍스처도 `unicorn_horn_blade.png` 1개만 가진다.
- 전용 `.bbmodel`은 예전 통합 프로젝트 배치 오프셋 X=120을 제거해 원점 기준(x -2.5..2.5)으로 보정했다. Blockbench에서 다시 열면 무기가 중앙에 보여야 한다.
- 칼날 색/UV/텍스처 수정은 이제 `unicorn_horn_blade.bbmodel`만 열어서 진행한다. 가구 프로젝트의 텍스처와 섞이지 않는다.
- `blockbench/split_unicorn_horn_blade_project.py`는 이번 분리를 재현하기 위한 일회성/복구용 스크립트다.

## 4.13 유니콘 싱크대 3종 추가 (2026-06-03)

- 세련된 유니콘 컨셉 싱크대 3종을 독립 furniture entity로 등록했다. 형태는 2차원 배열(1=블록, 0=빈칸, row 0=뒤쪽)로 정의한다.
  - `mine_structure:unicorn_sink_l` — `[[1,1,1],[0,0,1]]` L자. basin/수도꼭지는 가로 3칸의 **가운데(뒤-가운데 칸)**에 둬 정면에서 중앙에 보인다.
  - `mine_structure:unicorn_sink_island` — `[[1,1,1],[1,0,1],[1,0,1]]` 3×3 고리(가운데 빈 아일랜드). 앞쪽 가운데를 입구로 뚫었다. basin은 뒤-가운데 칸.
  - `mine_structure:unicorn_sink_u` — `[[1,1,1],[0,0,1],[1,1,1]]` ㄷ/C자(왼쪽 가운데 개방). basin은 뒤-가운데 칸.
- 칸 1개 = 1블록(16u). 메인 basin 1개 + 나머지는 매끈한 카운터 상판이라는 디자인 합의를 따랐다.
- 파츠: 카운터 바디 + 상판(림색 트림) + basin(림/안쪽 벽/움푹한 바닥) + 수도꼭지(post+arm+nozzle) + 수도꼭지 위 무지개 유니콘 뿔 + 물(water_stream 낙수 + basin_pool 고인물).
- **물 켜기/끄기 토글(지속 상태)**: `minecraft:variant`(0=off, 1=on)로 상태를 저장하고, 리소스팩 애니메이션 컨트롤러 `controller.animation.<id>.water`가 `q.variant`로 `off`(물 스케일 0)↔`flowing`(물 스케일 1 + 낙수 루프)을 전환한다. 청크 리로드에도 상태가 유지된다. 상호작용 시 바닐라 물소리(`bucket.fill_water`/`bucket.empty_water`)를 재생하므로 별도 음원 에셋이 필요 없다.
- 텍스처: **3종이 각각 다른 알록달록 테마의 전용 아틀라스**(64×64, 16px 셀: body/top/rim/wall/faucet/horn/water, per-face 풀셀 UV). 아이들이 좋아할 색감이며 유니콘 시그니처(무지개 뿔 + 파스텔 + 방울/스파클)는 공통 유지.
  - `unicorn_sink_l` — 딸기(핑크 바디 + 골드 림 + ♥ 하트 스파클)
  - `unicorn_sink_island` — 민트(민트 바디 + 라벤더 림 + ★ 별 스파클)
  - `unicorn_sink_u` — 레몬(버터 옐로 바디 + 핑크 림 + ○ 버블 스파클)
  - 경로: `textures/entity/unicorn_sink/<id>_atlas.png`
- Blockbench 원본은 모델별로 분리: `blockbench/unicorn_sink_l.bbmodel`, `unicorn_sink_island.bbmodel`, `unicorn_sink_u.bbmodel`. 각 파일은 자기 테마 아틀라스 1장만 임베드하므로 저장 코덱의 face-flatten 버그 영향이 모델 내부로 한정된다. 세 파일 모두 현재 Blockbench에 로드해 열림/큐브 수/테마 텍스처를 확인했다.
- 생성 스크립트: `blockbench/gen_unicorn_sinks.py`(geo + 공유 아틀라스 + 3 bbmodel), `blockbench/gen_sink_wiring.py`(behavior/client/render/animation/animation_controller/resources.json).
- `validate_unicorn_toilet_resources.py`에 `SINKS`/`validate_sink`/`validate_sink_blockbench_source`를 추가했다. variant 토글 component group, animate 컨트롤러 배선, water 본, 공유 아틀라스, bbmodel 단일 텍스처/face 인덱스까지 검증한다. 결과 PASS.
- (2026-06-03 갱신) `unicorn_sink_l`의 basin/수도꼭지를 앞-오른쪽 칸 → **가로 3칸의 가운데(뒤-가운데)**로 옮겼고, 3종 텍스처를 공유 아틀라스 → **테마별 전용 아틀라스(딸기/민트/레몬)**로 분리했다.
- (2026-06-03 갱신) 싱크대 상호작용을 **손 상태로 분기**하도록 바꿨다. 물 토글을 behavior `minecraft:interact` → **Script 처리**로 옮기고(상태는 dynamic property `sink_water_on`, `triggerEvent`로 variant 교체), **아이템을 들고 우클릭하면 basin 제외 카운터 셀 위에 1개 올리기**(`spawnItem`, 식탁과 동일 방식)를 추가했다. component group에는 `minecraft:variant`만 남기고 interact는 제거했다(이중 발동 방지). `validate_sink`도 main.js 배선 검증으로 갱신.
- 최신 테스트용 패키지:
  - `dist/mine_furniture_01-20260603-002405/mine_furniture_01.mcaddon`

## 4.14 아이 친화적 유니콘 가구 4종 추가 (2026-06-03)

- 아이들이 좋아할 유니콘 가구 4종을 독립 furniture entity로 등록했다. 각각 검증된 상호작용 패턴을 재사용한다.
  - 🐴 `mine_structure:unicorn_rocking_horse` — **흔들목마**. `minecraft:rideable`(1인 안장)로 올라타고, `rock` 본이 항상 가볍게 흔들리는 루프 애니메이션(`scripts.animate: ["rock"]`, 좌우 ±7° 2.4초).
  - 🌙 `mine_structure:unicorn_night_lamp` — **무드등(잠자는 구름 유니콘)**. 통통한 구름 몸통 + 정면에 잠든 표정(감은 눈/볼터치/미소, 텍스처 셀로 한 면만 매핑) + 귀/무지개 뿔 + 별 토퍼. 싱크대 물 토글과 같은 `minecraft:variant`(0/1) 방식이며, 켜지면 `glow` 본의 **반짝이는 별 트윙클**이 구름 주변에 스케일 0→1로 떠오른다(표정을 가리지 않도록 큰 후광 대신 작은 별로 변경). 상태 지속, 사운드 `random.click`.
  - 🍦 `mine_structure:unicorn_ice_cream_machine` — **아이스크림 기계**. 한눈에 아이스크림으로 보이도록 재설계: 투톤 둥근 본체 + 앞 트레이 위의 **와플 콘 + 흰/핑크 소프트아이스크림 스월 + 체리** + 콘 아이콘이 그려진 메뉴 간판. Script API(`scripts/main.js`)가 우클릭 시 간식 1개(쿠키/딸기/발광열매/호박파이/꿀병 중 랜덤)를 인벤토리에 지급(가득 차면 바닥에 스폰)하고 `random.pop` 소리를 낸다. behavior 상호작용 컴포넌트는 쓰지 않는다(식탁과 동일 방식).
  - ☁️ `mine_structure:unicorn_cloud_bunk_bed` — **구름 2층침대**. `minecraft:rideable` 좌석 2개(아래/위 칸, position `[0,0.5,0]` / `[0,1.3,0]`)로 두 명이 앉/눕는다.
- 텍스처: 각 모델 전용 아틀라스 `textures/entity/<id>/<id>_atlas.png`(64×64, per-face 풀셀 UV). 모두 파스텔 + 무지개 뿔/갈기 등 유니콘 시그니처 + 방울/스파클.
- Blockbench 원본: `blockbench/<id>.bbmodel` 4개(각 단일 텍스처). 네 파일 모두 Blockbench에 로드해 큐브 수/텍스처를 확인했다.
- 생성 스크립트: `blockbench/gen_kids_furniture.py`(geo + 아틀라스 + bbmodel, 범용 atlas/assembler), `blockbench/gen_kids_wiring.py`(behavior/client/render/animation/animation_controller/resources.json).
- `validate_unicorn_toilet_resources.py`에 `KIDS`/`validate_kids`/`validate_single_texture_bbmodel`를 추가했다. mechanic별(rideable / rideable_bunk seat 2 / variant_light 토글+컨트롤러 / script_give main.js) 검증 + bbmodel 단일 텍스처까지 본다. 결과 PASS.
- (2026-06-03 갱신) 무드등을 잠자는 구름 유니콘(표정 + 반짝 별 트윙클)으로, 아이스크림 기계를 콘+소프트 스월+체리+간판으로 재디자인했다. `gen_kids_furniture.py`에 면별 텍스처 셀(face/sign)과 cone/face/sign 그리기를 추가했다.
- 최신 테스트용 패키지:
  - `dist/mine_furniture_01-20260603-005119/mine_furniture_01.mcaddon`

## 4.15 아이 친화 콘텐츠 4종 추가 (펫/가챠/트램폴린/선물상자) (2026-06-03)

- 새 메커니즘 포함 4종을 추가했다.
  - 🦄 `mine_structure:unicorn_baby_pet` — **아기 유니콘 펫(걷는 몹)**. `minecraft:tameable`(설탕/사과/쿠키로 길들이기) + 걷기 세트(`navigation.walk`, `movement(.basic)`, `jump.static`, `behavior.float/tempt/random_stroll/look_at_player`). 길들이면 `mine_structure:tamed` 그룹이 `behavior.follow_owner` + `minecraft:rideable`(안장 1인)을 추가해 따라다니고 탈 수 있다. 다리 4개/머리를 별도 본으로 분리해 `controller.animation.<id>.move`가 `q.modified_move_speed`로 idle↔walk를 전환. 얼굴은 머리 정면 면에 표정 셀로 표현.
  - 🎰 `mine_structure:unicorn_gacha_machine` — **가챠 뽑기**. 캡슐(가챠) 글로브 외형. Script API가 우클릭 시 랜덤 보상(케이크/에메랄드/이름표/디스크/다이아 등) 1개 지급 + `random.orb` 소리.
  - 🛝 `mine_structure:unicorn_trampoline` — **트램폴린**. 위에 서면(매트 콜리전) `scripts/main.js`의 `system.runInterval`(3틱)이 매트 위 플레이어를 감지해 하강/정지 순간 `applyKnockback`으로 위로 통통 튕긴다(웅크리면 멈춤).
  - 🎁 `mine_structure:unicorn_gift_box` — **선물상자**. `minecraft:interact`가 `mine_structure:open_gift`를 호출해 `lid`(경첩 본) 열기 애니메이션을 `playanimation`으로 재생하고, 동시에 Script가 랜덤 선물 1개 지급 + `random.orb`.
- 텍스처: 각 전용 아틀라스 `textures/entity/<id>/<id>_atlas.png`. 가챠용 캡슐 패턴 그리기(`draw_capsule`)를 추가.
- 생성 스크립트: `blockbench/gen_more_furniture.py`(gen_kids_furniture 헬퍼 재사용, 첫 배치 bbmodel 미변경), `blockbench/gen_more_wiring.py`. `scripts/main.js`에 가챠/선물 지급 + 트램폴린 바운스 추가(`node --check` 통과).
- `validate_unicorn_toilet_resources.py`에 mechanic `pet`/`script_bounce`/`interact_give` 검증을 추가하고 `script_give`를 범용화했다. 결과 PASS.
- (2026-06-03 갱신) **펫 얼굴**: 머리 정면 표정이 주둥이에 가려져 안 보이던 문제를 작은 큐브(눈/볼/콧구멍/입)로 바꿔 해결. **2층침대 혼자 칸 선택**: 좌석 순서만 다른 component group(`order_bottom`/`order_top`) + `scripts/main.js`로 그냥 우클릭=아래칸 / 웅크림 우클릭=위칸. 빈 침대는 runInterval이 `order_bottom`으로 리셋(`bunk_seatlock`로 전환 중 보호). 검증 PASS.
- 최신 테스트용 패키지:
  - `dist/mine_furniture_01-20260603-224431/mine_furniture_01.mcaddon`

## 4.16 운전 자동차 / 아기 드래곤 / 어항 추가 (2026-06-03)

- 🚗 `mine_structure:unicorn_car` — **운전하는 자동차**. `minecraft:rideable`(controlling_seat 0) + `minecraft:behavior.controlled_by_player` + `movement`/`navigation.walk`/`movement.basic`로 플레이어가 직접 몰고 다닌다. 바퀴 4개를 별도 본으로 분리해 `controller.animation.<id>.wheels`가 `q.modified_move_speed`로 움직일 때만 회전(`roll`). 보닛에 무지개 뿔 + 전조등 눈.
- 🐉 `mine_structure:unicorn_baby_dragon` — **아기 드래곤 펫**. 아기 유니콘 펫과 같은 메커니즘(`pet_entity` 재사용): tameable(설탕/사과/쿠키) → 길들이면 follow_owner + rideable, idle/walk 컨트롤러. 등 스파이크/날개/꼬리(무지개) + 큐브 얼굴.
- 🐠 `mine_structure:unicorn_aquarium` — **유니콘 어항**. 무드등과 같은 `minecraft:variant` 불빛 on/off(우클릭) + 물고기 2마리(`fish1`/`fish2`)가 항상 좌우로 헤엄치는 루프(`scripts.animate: ["fish", "light_ctrl"]`). 켜면 수면 글로우 바가 나타난다.
- 생성: `gen_more_furniture.py`(build_car/baby_dragon/aquarium), `gen_more_wiring.py`(pet_entity 일반화 + car/aquarium). `validate`에 `drive` mechanic 추가, 드래곤=pet/어항=variant_light 재사용. 결과 PASS.
- 최신 테스트용 패키지:
  - `dist/mine_furniture_01-20260603-233947/mine_furniture_01.mcaddon`

## 4.17 하늘 나는 유니콘 / 냉장고 추가 (2026-06-04)

- 🦄 `mine_structure:unicorn_pegasus` — **하늘 나는 유니콘(날개 달린 유니콘)**. `minecraft:rideable`(controlling_seat 0) + `behavior.controlled_by_player` + `movement.fly`/`navigation.fly`/`flying_speed`로 수평 비행, `has_gravity:false`로 공중 호버. 상하 조종은 `scripts/main.js` runInterval이 탑승한 플레이어의 입력을 읽어 처리(점프=상승 `applyImpulse` +y / 웅크림=하강). 날개 2개(`wing_l`/`wing_r`)는 항상 펄럭임(`scripts.animate: ["flap"]`).
- 🧊 `mine_structure:unicorn_fridge` — **냉장고**. `minecraft:interact`가 `mine_structure:open_fridge`를 호출해 경첩 `door` 본의 문 열기 애니메이션을 `playanimation`으로 재생하고, 동시에 Script가 barrel 수납장과 같은 저장 로직(아이템 들고=저장 / 빈손=꺼내기, dynamic property `fridge_items`, 최대 18칸)을 처리한다. barrel의 `storeOrRetrieveItem`을 property/maxSlots 인자형으로 일반화해 재사용.
- 생성: `gen_more_furniture.py`(build_pegasus/build_fridge), `gen_more_wiring.py`(pegasus/fridge). `validate`에 `fly`/`fridge` mechanic 추가. 결과 PASS.
- 비행 조종(특히 상하)은 Bedrock 네이티브 한계로 Script 보조이며, **인게임 검증이 가장 필요한 항목**이다.
- 최신 테스트용 패키지:
  - `dist/mine_furniture_01-20260604-094821/mine_furniture_01.mcaddon`

## 4.18 유니콘 쿠키(먹는 아이템) 추가 (2026-06-04)

- 🍪 `mine_structure:unicorn_cookie` — **먹을 수 있는 음식 아이템**. 엔티티가 아니라 검(sword)과 같은 아이템 방식이다.
  - `minecraft:food`(nutrition 6, saturation "good", can_always_eat) + `minecraft:use_animation: "eat"` + `minecraft:use_modifiers`로 실제로 먹을 수 있고 허기를 채운다(허기 → 자연 체력 재생).
  - **실제 체력 회복**: `scripts/main.js`의 `world.afterEvents.itemCompleteUse`가 쿠키를 다 먹은 순간 플레이어에게 `regeneration`(amplifier 1, 5초)과 `saturation`을 부여하고 하트 파티클을 띄운다.
  - 아이콘: `textures/items/unicorn_cookie.png`(16×16, 무지개 초코칩 + 작은 뿔), `item_texture.json`에 shortname 등록. 생성 스크립트 `blockbench/gen_unicorn_cookie_texture.py`.
- `validate_unicorn_toilet_resources.py`에 `FOODS`/`validate_food`(food 컴포넌트·아이콘·item_texture·heal 스크립트 배선) 추가. 결과 PASS.
- 최신 테스트용 패키지:
  - `dist/mine_furniture_01-20260604-115302/mine_furniture_01.mcaddon`

## 4.19 효과 음식 세트 / 마법 지팡이 / 블록 세트 / 입는 코스튬 추가 (2026-06-04)

- 🌈 **효과 음식 4종**(`unicorn_cupcake`/`unicorn_lollipop`/`unicorn_rainbow_drink`/`unicorn_star_candy`) — `minecraft:food` + `scripts/main.js`의 `FOOD_EFFECTS` 맵으로 먹을 때 효과 부여(컵케이크=회복, 막대사탕=스피드, 무지개음료=스피드+점프, 별사탕=야간투시). 쿠키도 이 맵으로 통합.
- 🪄 **마법 지팡이**(`unicorn_wand`) — 아이템. 우클릭(`itemUse`) 시 토템 파티클 + 점프/스피드 부스트 + 소리, `minecraft:cooldown` 2초.
- 🧱 **건축 블록 3종**(`unicorn_cloud_block`/`unicorn_candy_block`/`unicorn_star_block`) — **직접 쌓을 수 있는 커스텀 블록**(엔티티가 아님). 데이터 주도형: behavior `blocks/*.block.json`의 `material_instances`가 `terrain_texture.json` 단축명을 가리킨다. 16×16 블록 텍스처.
- 👑 **입는 코스튬**(`unicorn_horn_headband` 머리 슬롯) — `minecraft:wearable` + attachable. geometry 본 이름을 플레이어 `head`에 맞춰 착용 시 머리에 3D로 보이게 했다. **⚠️ 플레이어 부착 커스텀은 버전 민감 → 인게임 검증 필수.**
- 🪽 (2026-06-04 갱신) **날개는 elytra 바탕 커스텀 아이템으로 변경**: 정적 가슴 부착 날개(`unicorn_wings`)는 제거하고, **바닐라 elytra는 그대로 둔 채** 별도 커스텀 글라이더 `mine_structure:unicorn_elytra`를 만들었다.
  - item: `minecraft:wearable`(chest) + `minecraft:glider`(활공) + `minecraft:durability`.
  - attachable + 커스텀 날개 geometry(`body`/`left_wing`/`right_wing` 본) + 애니메이션 컨트롤러가 `q.is_gliding`으로 `folded`(접힘)↔`spread`(펴짐)를 전환.
  - (2026-06-04 추가) 날개가 블록처럼 끊겨 보이던 문제 → **얇은 평면 1장 + 알파 컷아웃 텍스처**(바닐라 elytra 방식)로 바꿔 가장자리를 부드럽게. 생성 `gen_custom_elytra.py`가 geo/텍스처/`.bbmodel`을 함께 출력.
  - 생성 `gen_custom_elytra.py`, Blockbench 원본 `blockbench/unicorn_elytra.bbmodel`.
  - **⚠️ 커스텀 글라이더 + 플레이어 부착 애니메이션은 Bedrock에서 가장 버전 민감 → 인게임 검증 필수**(glider 컴포넌트 지원 여부, attachable에서 `q.is_gliding` 동작, `controller.render.armor`로 커스텀 geo 렌더, 접힘 포즈 각도).
- 생성 스크립트: `gen_item_icons.py`(음식/지팡이 아이콘), `gen_extra_items.py`(음식/지팡이 item + item_texture), `gen_block_textures.py`/`gen_blocks.py`(블록), `gen_costume.py`(코스튬 아이콘/아틀라스/geo/item/attachable).
- `validate`에 `FOODS` 확장, `TOOLS`/`BLOCKS`/`WEARABLES` 검증 추가. 결과 PASS.
- 최신 테스트용 패키지:
  - `dist/mine_furniture_01-20260604-141845/mine_furniture_01.mcaddon`

## 4.20 유니콘 노트북 추가 (2026-06-04)

- 💻 `mine_structure:unicorn_laptop` — 디테일한 노트북(키캡 32개 + 스페이스바 개별 모델링 + 트랙패드 + 힌지 + 귀여운 얼굴 화면). **뿔 없이** 파스텔 라벤더/핑크 색감 + 작은 하트 액센트로 유니콘 느낌만 살림.
  - 우클릭 토글로 **뚜껑(화면) 열기/닫기**: `minecraft:variant`(0=open/1=closed) + 애니메이션 컨트롤러가 `lid` 본을 힌지 기준으로 0°↔100° 회전. 기본은 열린 상태, 상태 지속.
  - geo/atlas/bbmodel은 `gen_kids_furniture` 헬퍼 재사용(`gen_laptop.py`). `validate`엔 `variant_lid` mechanic으로 등록(검증 PASS).
  - 최신 테스트용 패키지:
    - `dist/mine_furniture_01-20260604-173735/mine_furniture_01.mcaddon`

## 4.21 유니콘 핸드폰 추가 (2026-06-04)

- 📱 `mine_structure:unicorn_phone` — 작은 받침대에 세워진 스마트폰(파스텔 핑크 케이스 + 카메라 + 홈버튼, **뿔 없음**). 무드등과 같은 `minecraft:variant` 토글로 **화면 켜기/끄기**: 켜면 어두운 베젤 앞에 밝은 **귀여운 얼굴 화면**(`glow` 본)이 나타나고, 끄면 숨겨진다. 우클릭 토글, 상태 지속.
- geo/atlas/bbmodel은 `gen_kids_furniture` 헬퍼 재사용(`gen_phone.py`). `validate`엔 `variant_light`로 등록(검증 PASS). 애니메이션은 `embed_animations.py`로 `.bbmodel`에도 임베드.
- 최신 테스트용 패키지:
  - `dist/mine_furniture_01-20260604-232908/mine_furniture_01.mcaddon`

## 4.22 손에 드는 핸드폰 아이템 추가 (2026-06-04)

- 📱 `mine_structure:unicorn_phone_item` — **들고 다니는 3D 핸드폰**(거치형 `unicorn_phone`과 별개 아이템). 검과 같은 attachable 방식: `minecraft:hand_equipped` 아이템 + attachable(`controller.render.item_default`) + 1·3인칭 × 주손·보조손 hold 포즈 4종. 화면은 귀여운 얼굴.
- 📲 (2026-06-04 추가) **핸드폰 기능**(Script, `world.afterEvents.itemUse`): 그냥 우클릭=**셀카**(하트+반짝 파티클+찰칵+짧은 벨소리 멜로디), 웅크리고 우클릭=**손전등**(야간투시 on/off 토글). `minecraft:cooldown` 0.6초.
- geo/atlas/bbmodel은 `gen_kids_furniture` 헬퍼 재사용(`gen_phone_item.py`). `validate`에 `HELD_ITEMS`/`validate_held` 추가(검증 PASS). hold 애니는 `.bbmodel`에도 임베드.
- **hold 포즈(위치/회전/스케일)는 보수적 기본값 → 인게임 미세조정 필요**(`resources.json` status `in_hand_pose_tuned: false`).
- 최신 테스트용 패키지:
  - `dist/mine_furniture_01-20260604-234050/mine_furniture_01.mcaddon`

## 4.23 방 가구 4종 추가 (TV / 아케이드 / 화장대 / 킹침대) (2026-06-05)

- 📺 `unicorn_tv` — 스탠드형 와이드 TV. 우클릭 **화면 켜기/끄기**(귀여운 얼굴 화면, `variant_light`).
- 🎮 `unicorn_arcade` — 아케이드 게임기 캐비닛(조이스틱+버튼+마퀴). 우클릭 **화면 켜기/끄기**(`variant_light`).
- 🎀 `unicorn_vanity` — 거울 화장대(서랍+거울+향수). 우클릭 **거울 전구 켜기/끄기**(Hollywood 전구, `glow` 본, `variant_light`).
- 🛏️ `unicorn_king_bed` — **단층 킹사이즈 침대**(헤드보드+베개 2+무지개 이불). `minecraft:rideable` **좌석 2개**(나란히 눕기/앉기, `rideable_simple`).
- 전부 파스텔, **뿔 없음**. geo/atlas/bbmodel은 `gen_room_furniture.py`. `validate`에 `variant_light`(TV/아케이드/화장대) + 새 `rideable_simple`(킹침대) 등록. 애니는 `embed_animations.py`로 bbmodel에도 임베드. 검증 PASS.
- ⚠️ Blockbench MCP 세션이 끊겨 이번 4종은 앱 로드 확인은 못 함(파일은 생성·검증 완료). 재연결 후 `blockbench/unicorn_tv|arcade|vanity|king_bed.bbmodel`을 열면 된다.
- 최신 테스트용 패키지:
  - `dist/mine_furniture_01-20260605-212934/mine_furniture_01.mcaddon`

## 4.24 욕실/주방/로봇청소기 + 놀이터 추가 (2026-06-05)

- 🛁 `unicorn_bathtub` — 거품 욕조. 우클릭 **물/거품 켜기·끄기**(`variant_light`, `glow` 본 = 물+거품).
- 🍳 `unicorn_oven` / `unicorn_microwave` — 우클릭 **불/창 켜기·끄기**(`variant_light`).
- 🍞 `unicorn_toaster` — Script로 우클릭 시 토스트(`minecraft:bread`) 지급(+pop 소리). main.js `TOASTER_ID` 핸들러.
- 🤖 `unicorn_robot_vacuum` — **알아서 바닥을 돌아다니는 작은 로봇**(새 `wander` 메커니즘: physics+movement+navigation.walk+behavior.random_stroll). 귀여운 얼굴.
- 🛝 놀이터: `unicorn_swing`(rideable + 항상 흔들 `rock` 애니), `unicorn_slide`(rideable 상단 착석), `unicorn_seesaw`(rideable 2인).
- 전부 파스텔/뿔 없음. `gen_bath_kitchen.py` + `gen_playground.py`(gen_room_furniture 헬퍼 재사용). `validate`에 `wander` mechanic 추가 + 나머지는 기존 mechanic 재사용. 애니 `embed_animations.py` 임베드. 검증 PASS.
- ⚠️ Blockbench MCP 세션이 끊긴 상태라 이번 분도 앱 로드 확인은 미실시(파일 생성·검증 완료).
- 최신 테스트용 패키지:
  - `dist/mine_furniture_01-20260605-215802/mine_furniture_01.mcaddon`

## 4.25 거실 가구 6종 추가 (2026-06-06)

- 🛋️ `unicorn_sofa` — `minecraft:rideable` 3인 착석.
- 🔥 `unicorn_fireplace` — 우클릭 **불 켜기/끄기**(`variant_light`, `glow`=불꽃).
- 🌀 `unicorn_fan` — 우클릭 **날개 회전 on/off**(새 `variant_spin` mechanic: `light_ctrl`가 `blades` 본을 z축 360° 회전 루프↔정지 전환).
- 📚 `unicorn_bookshelf` / 👕 `unicorn_wardrobe` — Script 수납(아이템 들고=저장, 빈손=꺼내기, barrel 로직 재사용; `script_store`).
- 🎹 `unicorn_piano` — 우클릭 시 랜덤 음(`note.harp`) + 노트 파티클(`script_play`).
- 전부 파스텔/뿔 없음. `gen_living_furniture.py`(room/bath_kitchen 헬퍼 재사용). main.js에 책장/옷장/피아노 핸들러 추가. validate에 `variant_spin`/`script_store`/`script_play` mechanic 추가. 검증 PASS.
- 최신 테스트용 패키지:
  - `dist/mine_furniture_01-20260606-114713/mine_furniture_01.mcaddon`

## 4.26 타고 모는 크루즈 보트 추가 (2026-06-06)

- 🛳️ `mine_structure:unicorn_cruise` — 물 위를 직접 모는 크루즈 보트(자동차 운전의 물 버전). `minecraft:buoyant`로 물에 뜨고, `behavior.controlled_by_player` + `movement` + `navigation.generic`(amphibious)로 조종. `minecraft:rideable` 좌석 4개(controlling_seat 0=운전석 + 승객 3). 갑판·선실·2단 굴뚝·현창·승객 쿠션 + 뱃머리 무지개 깃발(`flag` 본, 흔들림 애니).
- 새 `boat` mechanic으로 validate(rideable controlling_seat 0 + controlled_by_player + movement + buoyant). 생성 `gen_cruise.py`. 검증 PASS.
- ⚠️ 플레이어가 직접 모는 물 위 탈것은 버전 민감 → 인게임 검증 필수(조종/부력/좌석). 엔티티 충돌박스가 하나라 갑판 위를 자유롭게 걸어다니진 못함(타고 이동).
- 최신 테스트용 패키지:
  - `dist/mine_furniture_01-20260606-115356/mine_furniture_01.mcaddon`

## 4.27 디테일 보강 / 틈 수정 / 욕조 물 차오름 (2026-06-06)

사용자 피드백으로 품질 패스를 진행했다.
- 🛁 **욕조**: 토글 시 물이 즉시 뜨던 것 → **바닥부터 차오르는** 애니(`glow` y스케일 0→1, 새 `variant_fill` mechanic) + 클로풋 다리/수전 디테일.
- 🛝 **미끄럼틀**: 계단형 → **경사진 미끄럼판**(회전 큐브) + 사다리 가로대로 발판 연결.
- ⚖️ **시소**: 좌우 대칭 보정 + `plank` 본이 살짝 시소 운동(틸트 애니).
- 🌀 **선풍기**: 형편없던 것 → 둥근 안전망(촘촘한 링+십자 스포크) + 4날개(피치) + 받침/기둥/모터로 재설계.
- 🤖 **로봇청소기**: 브러시/바퀴/센서/안테나/버튼/범퍼/얼굴 추가.
- 🔥 **벽난로**: 벽돌 줄눈 + 장작 3단 + 화로 받침 + 멘틀 장식 + 다층 불꽃.
- 📚 **책장**: 측판/상단 몰딩/4단 선반/책 높이 다양화 + 화분·시계.
- 🍞 **토스터** / 🍳 **오븐** / 📟 **전자레인지**: 토스트 슬라이스/다이얼/레버/얼굴, 다이얼·버튼·디스플레이·손잡이 등 디테일.
- 🚗 **자동차**: 펜더/범퍼/그릴/미등/스포일러/도어라인/번호판/스티어링휠/허브캡.
- 🛏️ **킹베드**: 세로(깊이)가 짧던 것 → 25칸으로 길게 + 발판/베개 위치 보정.
- 🧰 틈 감사 도구 `blockbench/audit_gaps.py`로 "떠 있는 큐브"를 잡아 수정(현재 남은 건 머리띠뿐 = 플레이어 머리에 씌우는 정상 케이스). Builder에 회전 큐브 지원 추가.
- 검증 PASS. 최신 패키지: `dist/mine_furniture_01-20260606-213255/mine_furniture_01.mcaddon`

## 4.28 변신 마법봉 추가 (2026-06-06)

- 🪄 `mine_structure:unicorn_transform_wand` — **동물 변신 마법봉**. 들고 **동물을 우클릭**하면 그 동물을 **랜덤으로 다른 동물**로 바꾼다. Bedrock은 엔티티 형태를 직접 못 바꾸므로, `scripts/main.js`(`world.afterEvents.playerInteractWithEntity` + `transformAnimal`)가 대상 위치에 랜덤 동물(`TRANSFORM_ANIMALS` 16종)을 `spawnEntity`하고 기존 동물을 `remove`하며 totem 파티클 + 소리로 변신 연출.
  - 대상은 **바닐라 동물만**(플레이어·몬스터·우리 가구/탈것 엔티티 제외)이라 안전. `minecraft:cooldown` 1초.
  - 2D 아이콘(별 마법봉) + `item_texture.json` 등록. 생성 `gen_item_icons.py`/`gen_extra_items.py`.
- `validate`에 `TOOLS` 항목 추가(스크립트 마커 `transformAnimal`). 검증 PASS.
- 최신 테스트용 패키지:
  - `dist/mine_furniture_01-20260606-215232/mine_furniture_01.mcaddon`

## 4.29 마법봉 2종 손에 드는 3D 막대 모델 추가 (2026-06-06)

- `unicorn_wand`(마법 지팡이)와 `unicorn_transform_wand`(변신 마법봉)을 2D 아이콘만 있던 상태에서 **손에 들면 3D 막대로 보이는 attachable**로 보강. 핸드폰 아이템(`unicorn_phone_item`)과 같은 attachable 방식.
  - 모델: 슬림한 막대 손잡이 + 그립 밴드 2개 + **별 헤드(정사각 큐브 2개를 z축 45도로 겹쳐 별 실루엣)** + 가운데 발광 코어. 색상은 아이콘과 맞춤(지팡이=라벤더 손잡이+금색 별, 변신봉=보라 손잡이+분홍·하늘 무지개 별).
  - 1·3인칭 main/off hand 손 포즈 애니메이션 포함(포즈 값은 인게임 튜닝 대기).
  - 인벤토리 2D 아이콘과 우클릭 동작(부스트/변신)은 그대로 유지.
  - 생성기 `blockbench/gen_wand_items.py` 신규. `.bbmodel`(별 헤드 포함) + geo + atlas + attachable + animation 출력, `embed_animations.py`로 손 포즈를 bbmodel Animate 탭에 임베드.
- `validate`의 `TOOLS`에 `attachable: True` 플래그 추가 → attachable/geo/64×64 atlas/`hand_equipped`까지 검증. 검증 PASS.
- 최신 테스트용 패키지:
  - `dist/mine_furniture_01-20260606-220526/mine_furniture_01.mcaddon`

## 4.30 마법봉 보석 코어 + 손에 든 동안 반짝이 파티클 (2026-06-07)

- Blockbench로 모델을 띄워 확인한 뒤(MCP 재연결), 별 중앙의 큰 흰 코어를 **작은 보석(z 45도 마름모, 별 앞으로 돌출)** 으로 교체. 지팡이=청록, 변신봉=자수정 보라. 정면=별 가운데 작은 보석, 측면=입체 돌출로 확인.
- **손에 든 동안 보석이 반짝이도록** 커스텀 파티클 추가. Bedrock attachable 파티클은 버전 의존이 커서 **Script 주기 spawn** 방식 채택: `scripts/main.js`에 `system.runInterval(...,12)`(약 0.6초)로 메인핸드에 wand가 있는 플레이어의 보석 위치(시선 기준 근사)에 색별 파티클 emit.
  - 커스텀 파티클 `mine_structure:wand_sparkle_cyan`(청록) / `wand_sparkle_amethyst`(자수정) — 흰색 4점 반짝이 텍스처(`textures/particle/wand_sparkle.png`) 1장을 `particle_appearance_tinting`으로 색만 다르게. 위로 떠오르며 0.9초 후 소멸.
  - 생성기 `gen_wand_items.py`에 `build_particles()` 추가. RP `particles/` 폴더는 매니페스트 자동 인식.
- 사용 시(우클릭) 파티클은 기존대로 유지(지팡이=토템, 변신=토템). 검증 PASS.
- 최신 테스트용 패키지:
  - `dist/mine_furniture_01-20260607-031542/mine_furniture_01.mcaddon`

## 4.31 놀이공원 탈것 3종 추가 (회전목마 / 관람차 / 열기구) (2026-06-07)

- 🎠 `unicorn_carousel` — 탑승 4인 + **항상 회전**(`spin` 본 y축). 계단식 분홍 지붕 + 금색 기둥 + 유니콘 말 4마리(파란 안장·무지개 뿔). 좌석 고정이라 모델이 회전(Bedrock seat 한계).
- 🎡 `unicorn_ferris_wheel` — **우클릭 회전 토글**(`variant_spin`, `blades` 본 z축). 8살 방사형 + 색색 캐빈 8개 + 무지개 허브 + A자 다리. 감상용.
- 🎈 `unicorn_balloon` — 탑승 1인(바구니) + **둥실 bob**(y 위아래). 줄무늬 풍선 + 무지개 꼭대기 + 로프 + 바구니.
- 생성기 `blockbench/gen_amusement.py` 신규(공용 `rideable_animated_wiring` + ferris는 `variant_spin_wiring` 재사용). `embed_animations.py` 임베드.
- `validate` `KIDS`에 3종 등록(carousel/balloon=`rideable_simple`, ferris=`variant_spin`). 검증 PASS. Blockbench로 3종 모양 확인.
- 최신 테스트용 패키지:
  - `dist/mine_furniture_01-20260607-034326/mine_furniture_01.mcaddon`

## 4.32 상상놀이 세트 4종 추가 (성 텐트 / 인형의 집 / 장난감 상자 / 이젤) (2026-06-07)

- 🏰 `unicorn_castle_tent` — 들어가 앉기(`rideable_simple`). 핑크 벽 + 입구 + 파란 첨탑 + 무지개 깃발.
- 🏠 `unicorn_dollhouse` — 창문 불빛 토글(`variant_light`/`glow`). 크림 2층 + 분홍 지붕 + 무지개 하트 + 창틀 4개.
- 🧸 `unicorn_toy_box` — 아이템 보관/꺼내기(`script_store`, `toy_box_items` 12칸). 활짝 열린 뚜껑 + 무지개 별 + 삐져나온 장난감.
- 🎨 `unicorn_easel` — 캔버스 그림 토글(`variant_light`/`glow`). 나무 삼각대 + 캔버스 + 분홍 그림 + 별.
- 생성기 `blockbench/gen_imagination.py` 신규(`variant_light_wiring`/`rideable_wiring`/`script_entity` 재사용). `main.js`에 toy_box 수납 분기 추가. `KIDS` 등록, 검증 PASS. Blockbench로 4종 확인(이젤 별 띄움/장난감 상자 뚜껑 각도 보정).
- 최신 테스트용 패키지:
  - `dist/mine_furniture_01-20260607-042819/mine_furniture_01.mcaddon`

## 4.33 커스텀 날개를 천사 날개(뾰족 깃털 형태)로 변경 (2026-06-08)

- `unicorn_elytra`(커스텀 글라이더, 바닐라 elytra는 그대로)를 무지개 제트/매미 날개 → **흰 깃털 천사 날개**로 재디자인.
  - 색: 흰색 베이스 + 연한 라벤더 음영(깃털 능선=흰 하이라이트, 경계=라벤더).
  - **형태(참고 `game/mine_reference/002.png`)**: 한 면 실루엣이 사각형이 아니라 **부채형 날개**가 되도록 `angel_edge`를 위(어깨) 좁고 아래로 넓어지다 끝점으로 모이게 바꾸고, **외곽 전체를 날카로운 톱니(sawtooth) 뾰족 깃털 끝**으로 처리. 색은 천사(흰), 형태만 참고 이미지의 부채/뾰족 깃털을 따름.
  - 텍스처: `gen_custom_elytra.py`의 `angel_edge` 실루엣 + `draw_wing`(부채 깃털 능선/경계 + sawtooth 끝). 아이콘: 흰 날개 한 쌍(톱니) + 금색 후광 점. 표시 이름 "천사 날개".
  - **퀄리티 향상(2026-06-08 추가)**: 텍스처 해상도 2배(16×32 → **32×64**, atlas 64→128). 깃털 셰이딩을 002식 결정 깃털처럼 **앞 가장자리 밝은 하이라이트→뒤로 어두워지는 그라데이션**(`lerp` 보간) + 뾰족 끝 + 음영 대비 강화로 깃털 결을 선명하게.
  - 날개를 약간 키움(11×21). 평면 두께를 0.3→**0.05**로 줄여 옆에서 앞/뒷면 2면 겹침이 거의 안 보이게(양면 텍스처는 유지 — 앞뒤 모두 날개 보임). 글라이더/접힘·펴짐(`q.is_gliding`) 구조는 유지.
  - Blockbench로 접힘/펴짐(spread) 모두 확인. (참고: 평면 날개라 north/south UV가 같아 mirror는 spine 좌우에 영향 없음 — spine 위치는 인게임 확인 후 필요 시 텍스처 좌우 반전으로 보정.)
- 검증 PASS. 최신 패키지:
  - `dist/mine_furniture_01-20260608-130716/mine_furniture_01.mcaddon`

## 4.34 커스텀 날개를 나비 날개로 변경 → 4조각 나비 날개 재구성 (2026-06-08)

- `unicorn_elytra`(커스텀 글라이더)를 천사 깃털 → **나비 날개**로 재디자인.
- **4조각 구조(참고 `game/mine_reference/005.png`)**: 기존엔 세로로 긴 평면 1장이라 나비 같지 않고 "한 면"으로 보였다. 등에 펼쳐진 진짜 나비처럼, 각 쪽을 **forewing(위, 큰 lobe) + hindwing(아래, 작은 lobe)** 2조각으로 나눠 `right_wing`/`left_wing` 본 아래에 두고 위·아래·바깥으로 펼쳤다(총 4 cube).
  - `draw_lobe`: forewing은 둥근 부채(위 둥글게), hindwing은 둥근 타원 lobe. **아이 친화 무지개색** — 각 날개가 안쪽(분홍/주황)→바깥(노랑/초록/파랑/보라) 무지개 그라데이션(`rainbow()`), **흰 날개맥/테두리**로 스테인드글라스처럼 구분, 분홍 **eyespot**(흰 ring), 진보라 몸통.
  - UV 영역 분리(forewing/hindwing), atlas 128. 평면 두께 0.05. 표시 이름 "나비 날개".
  - 글라이더/접힘·펴짐 유지(접힘 ±12°). **글라이딩 중(`q.is_gliding`) 날개가 나비처럼 펄럭임** — `spread` 애니를 `hold` → **loop**로 바꿔 날개를 아래로 펼침(z≈-2)↔위로 모음(z≈-30) 0.7초 주기 왕복(`right_wing`/`left_wing` 본 회전). Blockbench로 두 극단 확인.
  - ⚠️ attachable의 q.is_gliding loop 재생은 버전 의존 — 인게임 검증 필요.
- 검증 PASS. 최신 패키지:
  - `dist/mine_furniture_01-20260608-135908/mine_furniture_01.mcaddon`

## 4.35 입체 A라인 무지개 스커트 의상 추가 (2026-06-08)

- 스킨(텍스처)으론 불가능한 **입체 A라인 스커트**를 입는 attachable `unicorn_rainbow_skirt`로 제작(파스텔 유니콘 스킨 `mine_skins_01`과 세트).
  - `gen_skirt.py`: 플레이어 `body` 본 하위 **5단 콘 큐브**(위→아래 폭 증가: 핑크→연노랑→민트→블루→라벤더), 각 단 위 하이라이트+아래 scallop 그림자로 프릴 명암. wearable(slot.armor.legs) + `controller.render.armor`.
  - 허리 좁고 무릎으로 넓어지는 튜튜 A라인. Blockbench로 확인.
- `WEARABLES`/`item_texture` 등록, 검증 PASS.
- 최신 패키지: `dist/mine_furniture_01-20260608-213919/mine_furniture_01.mcaddon`
- ⚠️ armor-slot attachable + 커스텀 geometry는 버전 의존 — 인게임 검증 필요.

## 4.36 홈데코 8종 추가 (~80종 목표 배치 1) (2026-06-10)

- 신규 가구 ~40종(→총 ~80종) 로드맵의 **1차 배치 8종**: 커피테이블·러그·벽시계·액자·화분·플로어램프·서랍장·협탁.
  - 정적 6종(`static` mechanic 신규 — `script_entity(sid,"static",..)`, validate에 `static` 분기 추가), 플로어램프(`variant_light`), 서랍장(`script_store`, `main.js` `DRESSER_ID` 18칸).
  - 생성기 `blockbench/gen_home_decor.py` 신규. `KIDS` 등록, 검증 PASS. Blockbench로 확인(화분/플로어램프 등).
- 최신 패키지: `dist/mine_furniture_01-20260610-094610/mine_furniture_01.mcaddon`
- 다음 배치 예정: 주방/카페, 정원/야외, 파티/장식, 놀이, 펫/기타.

## 4.37 정원/야외 8종 추가 (배치 2) (2026-06-10)

- 2차 배치 8종: 분수대·우편함·새장·벤치·파라솔테이블·모닥불·캠핑텐트·정원아치.
  - variant_light 2(분수 물/모닥불 불꽃 glow 토글), rideable 2(벤치 2인/텐트 1인), static 4.
  - 텐트는 회전 경사면으로 매끄러운 ∧ A프레임(+입구+깃발) 제작(계단식에서 개선).
  - 생성기 `blockbench/gen_garden.py` 신규. `KIDS` 등록, 검증 PASS. Blockbench로 분수/텐트 확인.
- 최신 패키지: `dist/mine_furniture_01-20260610-095738/mine_furniture_01.mcaddon`
- 누적 ~56종. 남은 배치: 주방/카페·파티·놀이·펫.

## 4.38 주방/카페 8종 추가 (배치 3, 종별 확인) (2026-06-10)

- 3차 배치 8종: 커피머신·믹서기·케이크스탠드·컵케이크타워·정수기·식기건조대·제빵오븐·카페바.
  - script_give 2(커피머신→무지개음료, 오븐→쿠키, `main.js` giveItem), variant_light 2(믹서기/정수기), static 4.
  - **8종 전부 Blockbench 렌더로 개별 확인**(사용자 요청 — 텐트 케이스 재발 방지). 커피머신/오븐은 디스플레이/창에 귀여운 얼굴.
  - 생성기 `blockbench/gen_kitchen_cafe.py` 신규. `KIDS` 등록, 검증 PASS.
- 최신 패키지: `dist/mine_furniture_01-20260610-103918/mine_furniture_01.mcaddon`
- 누적 ~64종. 남은 배치: 파티/장식·놀이·펫.

## 5. 다음 작업 (NEXT)

- ~~1. Blockbench MCP 연결 및 tool 확인~~ — 완료 (2026-05-31).
- ~~2. `.bbmodel` 원본을 `blockbench/furniture.bbmodel`로 확보~~ — 완료.
- ~~3. geometry/texture atlas를 resource pack에 export (geo identifier `geometry.unicorn_toilet` 확인)~~ — 완료.
- ~~4. export animation 덮어쓰기~~ — 해당 없음(프로젝트에 애니 0개, scaffold 유지).

남은 작업:

1. Minecraft에서 유니콘 가구 5종 엔티티 소환을 테스트한다.
   - `dist/mine_furniture_01-20260601-094146/mine_furniture_01.mcaddon`을 Minecraft Bedrock으로 가져온다.
   - behavior pack/resource pack을 같은 테스트 월드에 활성화한다.
   - 치트가 켜진 월드에서 `/summon mine_structure:unicorn_toilet`, `/summon mine_structure:unicorn_dining_table`, `/summon mine_structure:unicorn_chair`, `/summon mine_structure:unicorn_barrel_cabinet`, `/summon mine_structure:decorative_unicorn_doll`을 실행한다.
   - 기대 결과: 다섯 엔티티가 깨진 텍스처 없이 보이고, 충돌 박스가 각 가구 크기에 맞게 동작한다.
2. 인게임에서 플레이어 상호작용으로 `flush` 애니메이션/사운드가 트리거되는지 검증한다.
3. 인게임에서 식탁 상호작용으로 들고 있는 아이템 1개가 식탁 위에 생성되는지 검증한다.
4. 인게임에서 의자 상호작용으로 플레이어가 앉는지 검증한다.
5. 인게임에서 barrel 수납장 상호작용으로 아이템 1개 저장/빈 손 회수가 되는지 검증한다.
6. 인게임에서 장식용 유니콘 인형이 상호작용 없이 정적으로 보이는지 검증한다.
7. 추후 최종 제작/제공 음원이 생기면 `addon/resource_pack/sounds/flush.ogg`를 교체하고 사운드 검증을 다시 실행한다.
8. 필요하면 lid_open/lid_close/flush 애니메이션을 Blockbench 모델 안에도 빌드해 scaffold와 일원화할지 결정한다.
9. 인게임에서 `mine_structure:unicorn_horn_blade`를 지급해 인벤토리 아이콘, 손에 든 3D 뿔 포즈, 공격 데미지/내구도/검 인챈트 동작을 테스트하고 hold 애니메이션 값을 미세조정한다.
10. 인게임에서 싱크대 3종(`/summon mine_structure:unicorn_sink_l`, `unicorn_sink_island`, `unicorn_sink_u`)을 소환해 형태/텍스처를 확인하고, **빈손 우클릭=물 토글**(낙수 + 고인물 표시/숨김, 상태 지속), **아이템 들고 우클릭=카운터에 올리기**가 동작하는지 검증한다. 카운터 올리는 위치(`SINK_COUNTER_OFFSET`)가 basin 아닌 카운터 셀 위에 정확히 놓이는지, 회전(yaw)된 상태에서도 맞는지 확인하고 필요하면 오프셋/물 위치/collision을 미세조정한다.
11. 인게임에서 아이 친화적 가구 4종을 검증한다.
    - `/summon mine_structure:unicorn_rocking_horse` — 흔들 애니메이션이 보이고 우클릭으로 올라타지는지, 안장 좌석 위치가 맞는지.
    - `/summon mine_structure:unicorn_night_lamp` — 우클릭으로 켜기/끄기, 후광 표시/숨김과 상태 지속.
    - `/summon mine_structure:unicorn_ice_cream_machine` — 우클릭 시 간식 1개 지급(+소리), 인벤토리 가득 찼을 때 바닥 스폰.
    - `/summon mine_structure:unicorn_cloud_bunk_bed` — 그냥 우클릭=아래칸 / 웅크리고 우클릭=위칸으로 혼자서도 칸을 고를 수 있는지, 좌석 높이가 매트리스에 맞는지.
    - 필요하면 좌석 위치/흔들 진폭/후광 크기/collision_box를 미세조정한다.
12. 인게임에서 펫/가챠/트램폴린/선물상자를 검증한다.
    - `/summon mine_structure:unicorn_baby_pet` — 얼굴(눈/볼/콧구멍/입)이 보이는지, 설탕/사과/쿠키로 길들여지고, 길들인 뒤 따라오기 + 우클릭 탑승, 걸을 때 다리 애니메이션이 보이는지.
    - `/summon mine_structure:unicorn_gacha_machine` — 우클릭 시 랜덤 보상 지급(+소리).
    - `/summon mine_structure:unicorn_trampoline` — 위에 올라가 점프하면 통통 튕기는지, 웅크리면 멈추는지.
    - `/summon mine_structure:unicorn_gift_box` — 우클릭 시 뚜껑이 열리고 선물 1개 지급되는지.
    - 펫 이동 속도/콜리전, 트램폴린 바운스 세기/판정 높이, 선물상자 뚜껑 각도를 필요 시 미세조정한다.
13. 인게임에서 자동차/드래곤/어항을 검증한다.
    - `/summon mine_structure:unicorn_car` — 타고 직접 몰고 다녀지는지(WASD 조종), 바퀴가 움직일 때 회전하는지, 좌석 위치가 맞는지.
    - `/summon mine_structure:unicorn_baby_dragon` — 얼굴이 보이고 길들이기/따라오기/탑승이 되는지.
    - `/summon mine_structure:unicorn_aquarium` — 물고기가 헤엄치는지, 우클릭으로 불빛 on/off가 되는지.
    - 자동차 속도/조종감, 좌석 높이, 어항 물고기 경로를 필요 시 미세조정한다.
14. 인게임에서 하늘 나는 유니콘/냉장고를 검증한다.
    - `/summon mine_structure:unicorn_pegasus` — 타고 수평 비행이 되는지, 점프=상승/웅크림=하강이 동작하는지, 날개가 펄럭이는지, 좌석 높이가 맞는지. (비행 조종이 매끄럽지 않으면 컴포넌트/Script 보정 필요.)
    - `/summon mine_structure:unicorn_fridge` — 우클릭 시 문이 열리고, 아이템 들고=저장 / 빈손=꺼내기가 되는지.
    - 비행 상하 세기/속도, 냉장고 문 각도를 필요 시 미세조정한다.
15. 인게임에서 유니콘 쿠키를 검증한다.
    - `/give @s mine_structure:unicorn_cookie` 로 받아서 먹어 본다. 먹는 애니메이션이 나오고, 허기가 차고, 먹은 직후 체력이 회복(Regeneration)되는지 확인한다. (스크립트 효과이므로 behavior pack + Beta API 실험 옵션 필요.)
16. 인게임에서 음식 세트/지팡이/블록/코스튬을 검증한다.
    - 음식 4종(`/give` 컵케이크/막대사탕/무지개음료/별사탕) — 먹으면 각 효과(회복/스피드/스피드+점프/야간투시)가 붙는지.
    - `/give @s mine_structure:unicorn_wand` — 우클릭 시 파티클 + 점프/스피드 부스트 + 쿨다운.
    - 블록 3종 — 크리에이티브 "건축" 탭에 나오는지, 설치/파괴되고 텍스처가 맞는지.
    - **코스튬(가장 불확실)**: `/give` 뿔 머리띠를 받아 머리 슬롯에 착용 시 캐릭터에 3D로 보이는지. 안 보이거나 위치가 어긋나면 attachable/지오메트리(본 이름·피벗·render controller) 보정 필요.
    - **커스텀 elytra**(`/give @s mine_structure:unicorn_elytra`): 가슴에 착용되는지, 높은 곳에서 점프+활공이 되는지(glider), 활공 시 날개가 펴지고 평소엔 접히는지. 바닐라 elytra는 영향 없이 그대로인지. 안 되면 glider 지원/`q.is_gliding`/render controller/본 이름·피벗을 보정.
17. 인게임에서 `/summon mine_structure:unicorn_laptop` — 우클릭으로 뚜껑(화면)이 열리고 닫히는지(힌지 회전, 상태 지속), 키보드/화면 디테일이 정상인지 확인한다.
18. 인게임에서 `/summon mine_structure:unicorn_phone` — 우클릭으로 화면 켜기/끄기(얼굴 화면 표시/숨김, 상태 지속)가 되는지 확인한다.
19. 인게임에서 `/give @s mine_structure:unicorn_phone_item` — 손에 들면 3D 핸드폰이 보이는지(1·3인칭), hold 포즈가 자연스러운지 확인하고, **우클릭=셀카(플래시/찰칵/멜로디)**, **웅크리고 우클릭=손전등(야간투시) on/off**가 동작하는지 검증한다(스크립트 → behavior pack + 베타 API 필요).
20. 인게임에서 방 가구 4종을 검증한다.
    - `/summon mine_structure:unicorn_tv` / `unicorn_arcade` / `unicorn_vanity` — 우클릭으로 화면(또는 거울 전구) 켜기/끄기, 상태 지속.
    - `/summon mine_structure:unicorn_king_bed` — 좌석 2개에 각각 올라가지는지, 좌석 높이가 매트리스에 맞는지.
21. 인게임에서 욕실/주방/로봇/놀이터를 검증한다.
    - `/summon mine_structure:unicorn_bathtub` / `unicorn_oven` / `unicorn_microwave` — 우클릭 켜기/끄기.
    - `/summon mine_structure:unicorn_toaster` — 우클릭 시 토스트 지급(스크립트 → behavior pack + 베타 API).
    - `/summon mine_structure:unicorn_robot_vacuum` — 알아서 돌아다니는지(이동/길찾기).
    - 놀이터 `unicorn_swing`/`unicorn_slide`/`unicorn_seesaw` — 탑승, 그네 흔들림, 좌석 위치 확인.
22. 인게임에서 거실 가구 6종을 검증한다.
    - `/summon mine_structure:unicorn_sofa` — 3인 착석.
    - `unicorn_fireplace`(불 토글), `unicorn_fan`(날개 회전 토글) — 우클릭.
    - `unicorn_bookshelf`/`unicorn_wardrobe` — 아이템 들고=저장 / 빈손=꺼내기.
    - `unicorn_piano` — 우클릭 시 음 소리/노트 파티클.
23. 인게임에서 `/summon mine_structure:unicorn_cruise`(물 위) — 타고 직접 모는지(WASD 조종), 물에 뜨는지(부력), 좌석 4개 탑승, 깃발 흔들림 확인. 안 되면 navigation/movement/buoyant/controlled_by_player 조합·좌석 위치 보정.
24. 인게임에서 `/give @s mine_structure:unicorn_transform_wand` — 동물(돼지/소/양 등)을 우클릭하면 랜덤 동물로 바뀌는지(+파티클/소리) 확인(스크립트 → behavior pack + 베타 API). 변신 대상/결과 동물 목록은 `TRANSFORM_ANIMALS`에서 조정.
25. 인게임에서 두 마법봉을 손에 들어 **3D 막대 모델**이 보이는지(별 헤드+보석 코어), 1·3인칭 손 포즈가 자연스러운지, **들고 있는 동안 보석에서 반짝이 파티클**(청록/자수정)이 약 0.6초마다 손 근처에 뜨는지 확인. 손 포즈는 `gen_wand_items.py`의 `pose(...)`, 파티클 위치/주기는 `main.js`의 sparkle `runInterval`(오프셋·`12`틱)로 보정.
26. 인게임에서 놀이공원 탈것 3종을 확인한다.
    - `/summon mine_structure:unicorn_carousel` — 탑승(4인) + 모델 회전, 좌석 위치 확인.
    - `/summon mine_structure:unicorn_ferris_wheel` — 우클릭 회전 on/off(`blades`).
    - `/summon mine_structure:unicorn_balloon` — 탑승(1인) + 둥실(`bob`). 좌석/높이 보정 필요 시 `gen_amusement.py`.
27. 인게임에서 상상놀이 세트 4종을 확인한다.
    - `/summon mine_structure:unicorn_castle_tent` — 들어가 앉기, 좌석 위치 확인.
    - `/summon mine_structure:unicorn_dollhouse` / `unicorn_easel` — 우클릭 불빛/그림 토글(`glow`).
    - `/summon mine_structure:unicorn_toy_box` — 아이템 들고=보관 / 빈손=꺼내기.

## 6. 주의

- MCP 스크린샷이 텍스처 대신 마커색으로 보일 수 있다. 자세한 검증 방식은 루트 `../../docs/agent-guides/blockbench-mcp-rules.md`를 따른다.
- 닫힘 시 뚜껑이 1칸 앞으로 와서 시트 맨 뒤 일부가 덜 덮인다. 필요하면 뚜껑 길이를 +1 보정하고 열림 클리어런스를 재검증한다.
