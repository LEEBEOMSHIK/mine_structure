# PROJECT_CONTEXT.md — mine_furniture_01

이 프로젝트는 Minecraft Bedrock용 여러 가구와 무기를 묶는 add-on 패키지 작업 공간이다.
현재 등록 콘텐츠는 가구/펫/탈것 21종 — **무지개 유니콘 변기(`mine_structure:unicorn_toilet`)**, **유니콘 식탁(`mine_structure:unicorn_dining_table`)**, **유니콘 의자(`mine_structure:unicorn_chair`)**, **유니콘 barrel 수납장(`mine_structure:unicorn_barrel_cabinet`)**, **장식용 유니콘 인형(`mine_structure:decorative_unicorn_doll`)**, **유니콘 싱크대 3종(`mine_structure:unicorn_sink_l` / `unicorn_sink_island` / `unicorn_sink_u`)**, **아이 친화적 가구 4종(`mine_structure:unicorn_rocking_horse` 흔들목마 / `unicorn_night_lamp` 무드등 / `unicorn_ice_cream_machine` 아이스크림 기계 / `unicorn_cloud_bunk_bed` 구름 2층침대)**, **펫/놀이 4종(`unicorn_baby_pet` 아기 유니콘 펫 / `unicorn_gacha_machine` 가챠 / `unicorn_trampoline` 트램폴린 / `unicorn_gift_box` 선물상자)**, **탈것/펫/어항 3종(`unicorn_car` 운전 자동차 / `unicorn_baby_dragon` 아기 드래곤 펫 / `unicorn_aquarium` 어항)**, **비행/주방 2종(`unicorn_pegasus` 하늘 나는 유니콘 / `unicorn_fridge` 냉장고)** — 과 무기 1종 **유니콘 뿔 검(`mine_structure:unicorn_horn_blade`)**, 음식 1종 **유니콘 쿠키(`mine_structure:unicorn_cookie`, 먹으면 허기+체력 회복)**이다.

## 세션 시작 순서

1. `README.md`에서 프로젝트 범위, 현재 등록 콘텐츠, 다음 작업을 확인한다.
2. `content/README.md`에서 가구/무기 콘텐츠 레지스트리를 확인한다.
3. 루트 `../../docs/agent-guides/README.md`를 읽고 공통 Bedrock/Blockbench 지침을 확인한다.
4. `unicorn_toilet` 모델 상세 수치가 필요하면 `unicorn_toilet_spec.md`를 기준으로 한다.

## 현재 add-on 구조

- `addon/behavior_pack/` — behavior manifest, entity/item definitions, scripts
- `addon/resource_pack/` — resource manifest, client entity, geometry, texture, animation, sound
- `content/furniture/` — 가구 콘텐츠 문서
- `content/weapons/` — 무기 콘텐츠 문서
- `blockbench/` — Blockbench 원본 모델 파일 보관 위치

## Blockbench MCP / Resource 연결

- Codex 전역 MCP 설정에는 `blockbench` 서버를 추가했다.
- 저장소 설정 예시는 루트 `../../mcp/blockbench.config.example.toml`에 있다.
- `unicorn_toilet` resource map은 `content/furniture/unicorn_toilet.resources.json`이다.
- MCP export 대상 경로는 `blockbench/export_unicorn_toilet_to_resource_pack.js`에 고정했다.
- export 산출물 상태:
  - `addon/resource_pack/models/entity/unicorn_toilet.geo.json` — 생성됨 (2026-05-31)
  - `addon/resource_pack/textures/entity/unicorn_toilet/unicorn_toilet_atlas.png` — 생성됨 (2026-05-31)
  - `blockbench/furniture.bbmodel` — 저장소에 확보됨 (2026-06-01). 현재 Blockbench에 열린 `furniture` 프로젝트를 저장소 경로로 export
  - `addon/resource_pack/sounds/flush.ogg` — 생성됨 (2026-06-01). 기본 합성 효과음이며 추후 최종 음원으로 교체 가능

### 검증 상태 (2026-05-31, 갱신)

- resource pack JSON 배선 교차검증 완료 → geometry identifier / texture path / animation 이름 3종 모두 PASS. 상세는 `README.md` 4.1절.
- **차단 해소**: Blockbench MCP 연결됨. 세션 시작 시 `furniture`(unicorn_toilet) 모델이 이미 빌드된 채 열려 있어 재빌드 불필요. geometry/texture/`.bbmodel` export 완료. 상세 로그는 `README.md` 4.2절.
- **MCP 주의**: `export_model`(codec `bedrock`)이 빈 geometry를 내는 버그가 있어 geo는 `Codecs.bedrock.compile()` 직접 호출로 export했다.
- 다음 세션은 인게임 소환/상호작용 테스트부터 진행한다. `flush.ogg`는 기본 합성 효과음으로 확보했으며, 최종 음원이 제공되면 같은 경로에 교체한다.
- 소환/상호작용 테스트용 최신 패키지: `../../dist/mine_furniture_01-20260601-094146/mine_furniture_01.mcaddon`
- `unicorn_dining_table`, `unicorn_chair`, `unicorn_barrel_cabinet`, `decorative_unicorn_doll`은 독립 furniture entity로 등록했다. 각 항목은 behavior/client entity, geometry, render controller, 64×64 texture atlas, resource map을 가진다.
- Blockbench `furniture` 프로젝트에는 `unicorn_dining_table`, `unicorn_chair`, `unicorn_barrel_cabinet`, `decorative_unicorn_doll` 루트 그룹이 있다. 현재 루트 그룹은 `unicorn_toilet`, `unicorn_dining_table`, `unicorn_chair`, `unicorn_barrel_cabinet`, `decorative_unicorn_doll` 5개다.
- `unicorn_dining_table`의 `horn_centerpiece`는 geo/`.bbmodel` 양쪽에서 제거했다.
- 상호작용 방식은 behavior component 방식으로 확정했다. `minecraft:interact`가 `mine_structure:flush`와 `flush` 사운드를 트리거하고, 이벤트에서 `playanimation @s animation.unicorn_toilet.flush`를 queue_command로 실행한다.
- 식탁 behavior는 Script API 방식이다. `scripts/main.js`가 `world.afterEvents.playerInteractWithEntity`를 구독하고, `unicorn_dining_table`과 상호작용할 때 플레이어 주 손 아이템 1개를 식탁 위에 `spawnItem`으로 생성한다.
- 의자 behavior는 `minecraft:rideable` 방식이다. 플레이어 1명이 `[0, 0.55, 0]` 좌석에 앉는다.
- barrel 수납장 behavior는 Script API 간이 수납 방식이다. 아이템을 들고 상호작용하면 1개 저장, 빈 손으로 상호작용하면 가장 최근 저장 아이템 1개를 꺼낸다.
- 장식용 유니콘 인형은 순수 정적 장식이다. `minecraft:interact`, Script API 핸들러, `minecraft:rideable`을 사용하지 않는다.
- (2026-06-01) `decorative_unicorn_doll`을 직립 박스 인형 → 네 발로 선 조랑말(포니) 체형으로 재설계했다. 가로형 배럴 몸통 + 들린 목 + 주둥이 + 3단 뿔/앞머리/갈기/꼬리. `geometry.decorative_unicorn_doll` 6 bones / 27 cubes. `furniture.bbmodel`과 `decorative_unicorn_doll.geo.json` 갱신. 전용 텍스처는 아직 플레이스홀더다. 상세는 `README.md` 4.8절.
- (2026-06-01) 첫 무기 콘텐츠 `mine_structure:unicorn_horn_blade`(유니콘 뿔 검)를 추가했다. 검 취급(데미지 9/내구도 1800/검 인챈트)이며 외형은 유니콘 뿔이다. 2D 아이콘 + 3D attachable 손모델. hold 포즈는 인게임 미세조정 필요. 상세는 `README.md` 4.9절.
- (2026-06-01) `furniture.bbmodel`의 face texture binding이 저장 코덱 문제로 전부 toilet 아틀라스에 평탄화되어 칼날 수정이 가구 텍스처까지 바꾸는 문제가 있었다. 최종 조치로 `unicorn_horn_blade`를 `furniture.bbmodel`에서 제거하고 전용 `blockbench/unicorn_horn_blade.bbmodel`로 분리했다. 현재 `furniture.bbmodel`은 가구 5종만, `unicorn_horn_blade.bbmodel`은 무기 1종만 가진다. 전용 무기 프로젝트는 통합 프로젝트 오프셋 X=120을 제거해 원점 기준으로 보정했다. 칼날 뿔 스와치는 무지개 펄 나선 패턴이다. 최신 패키지: `../../dist/mine_furniture_01-20260601-213910/mine_furniture_01.mcaddon`
- (2026-06-03) 세련된 유니콘 싱크대 3종(`unicorn_sink_l` L자, `unicorn_sink_island` 아일랜드 고리, `unicorn_sink_u` ㄷ자)을 독립 furniture entity로 추가했다. 형태는 2D 배열로 정의하고 칸 1개=1블록(16u)이며 메인 basin 1개 + 매끈한 카운터. 세 모델 모두 basin/수도꼭지는 가로 3칸의 가운데(뒤-가운데)에 둔다. 물 켜기/끄기는 `minecraft:variant`(0/1) + 리소스팩 애니메이션 컨트롤러(`q.variant`로 off↔flowing)로 지속 상태를 유지한다. 상호작용 사운드는 바닐라 물소리라 별도 음원 불필요. 텍스처는 3종 각각 다른 알록달록 테마의 전용 아틀라스(딸기/민트/레몬, `textures/entity/unicorn_sink/<id>_atlas.png`)이며 무지개 뿔 등 유니콘 시그니처는 공통. Blockbench 원본은 모델별 분리(`blockbench/unicorn_sink_*.bbmodel`, 각 자기 테마 텍스처 1장)이며 세 파일 모두 Blockbench에 로드 확인. 생성 스크립트 `gen_unicorn_sinks.py`/`gen_sink_wiring.py`. 검증(`validate_sink`) PASS. 최신 패키지: `../../dist/mine_furniture_01-20260603-002405/mine_furniture_01.mcaddon`
- (2026-06-03) 아이 친화적 유니콘 가구 4종을 추가했다. 흔들목마(`unicorn_rocking_horse`, rideable 1인 + `rock` 본 항상 흔들 루프), 무드등(`unicorn_night_lamp`, 싱크대와 같은 `minecraft:variant` 토글 + 컨트롤러로 `glow` 후광 표시/숨김, 상태 지속), 아이스크림 기계(`unicorn_ice_cream_machine`, Script API `dispenseTreat`로 우클릭 시 랜덤 간식 1개 지급), 구름 2층침대(`unicorn_cloud_bunk_bed`, rideable 좌석 2개). 각 모델 전용 아틀라스(`textures/entity/<id>/<id>_atlas.png`)와 모델별 분리 bbmodel(`blockbench/<id>.bbmodel`, 단일 텍스처). 생성 스크립트 `gen_kids_furniture.py`/`gen_kids_wiring.py`. 검증(`validate_kids`) PASS. 최신 패키지: `../../dist/mine_furniture_01-20260603-003610/mine_furniture_01.mcaddon`
- (2026-06-03) 새 메커니즘 포함 4종 추가: 아기 유니콘 펫(`unicorn_baby_pet`, tameable 걷는 몹 → 길들이면 follow_owner + rideable, idle/walk 애니 컨트롤러), 가챠(`unicorn_gacha_machine`, Script 랜덤 보상), 트램폴린(`unicorn_trampoline`, Script `runInterval`+`applyKnockback` 바운스), 선물상자(`unicorn_gift_box`, interact 뚜껑 열기 애니 + Script 선물). 생성 스크립트 `gen_more_furniture.py`/`gen_more_wiring.py`, `scripts/main.js` 확장(node --check 통과). 검증(`pet`/`script_bounce`/`interact_give` mechanic) PASS. 최신 패키지: `../../dist/mine_furniture_01-20260603-213715/mine_furniture_01.mcaddon`
- (2026-06-03) 싱크대 상호작용을 손 상태로 분기: 빈손 우클릭=물 토글(behavior interact → Script `triggerEvent`+dynamic property `sink_water_on`으로 이전), 아이템 들고 우클릭=basin 제외 카운터 셀에 1개 올리기(`spawnItem`, yaw 회전 오프셋). component group은 `minecraft:variant`만 유지. 검증/문서 갱신, 검증 PASS. 최신 패키지: `../../dist/mine_furniture_01-20260603-221322/mine_furniture_01.mcaddon`
- (2026-06-03) 펫 얼굴이 주둥이에 가려지던 문제를 작은 큐브(눈/볼/콧구멍/입)로 교체해 해결. 2층침대는 혼자서도 칸 선택 가능하게 변경(좌석 순서만 다른 `order_bottom`/`order_top` component group + `scripts/main.js` `rideBunkTop`: 웅크림 우클릭=위칸, 빈 침대는 runInterval로 `order_bottom` 리셋, `bunk_seatlock`로 전환 보호). 검증 PASS. 최신 패키지: `../../dist/mine_furniture_01-20260603-224431/mine_furniture_01.mcaddon`
- (2026-06-03) 운전 자동차(`unicorn_car`, rideable controlling_seat + behavior.controlled_by_player + 바퀴 회전 컨트롤러), 아기 드래곤 펫(`unicorn_baby_dragon`, `pet_entity` 재사용), 어항(`unicorn_aquarium`, variant 불빛 토글 + 물고기 헤엄 루프) 3종 추가. `gen_more_furniture.py`/`gen_more_wiring.py` 확장, validate에 `drive` mechanic 추가, 검증 PASS. 최신 패키지: `../../dist/mine_furniture_01-20260603-233947/mine_furniture_01.mcaddon`
- (2026-06-04) 하늘 나는 유니콘(`unicorn_pegasus`, rideable+controlled_by_player+fly 컴포넌트, has_gravity false 호버, Script로 점프=상승/웅크림=하강 applyImpulse, 날개 flap)과 냉장고(`unicorn_fridge`, interact 문 열기 애니 + barrel식 저장 로직 일반화 재사용, dynamic property `fridge_items` 18칸) 2종 추가. validate에 `fly`/`fridge` mechanic 추가, 검증 PASS. 비행 상하 조종은 네이티브 한계로 Script 보조라 인게임 튜닝 필요. 최신 패키지: `../../dist/mine_furniture_01-20260604-094821/mine_furniture_01.mcaddon`
- (2026-06-04) 먹는 아이템 `unicorn_cookie`(유니콘 쿠키) 추가. `minecraft:food`로 허기 회복 + `scripts/main.js`의 `itemCompleteUse`가 먹는 순간 `regeneration`/`saturation` 부여로 실제 체력 회복. 16×16 아이콘 + item_texture 등록. validate에 `FOODS`/`validate_food` 추가, 검증 PASS. 최신 패키지: `../../dist/mine_furniture_01-20260604-115302/mine_furniture_01.mcaddon`
- 현재 실행 환경에는 Bedrock 기본 `com.mojang` 경로가 없어 Minecraft 앱 기반 소환 테스트는 직접 수행하지 못했다.

## 공통 세부 지침

- `../../docs/agent-guides/environment.md` — 작업 환경 / 도구 / 좌표계
- `../../docs/agent-guides/principles.md` — 핵심 원칙
- `../../docs/agent-guides/blockbench-mcp-rules.md` — Blockbench/MCP 작업 시 반드시 지킬 주의점

## 다음 세션 시작 지점

`README.md`의 "다음 작업(NEXT)" 섹션부터 본다.
geometry/texture/`flush.ogg`/`.bbmodel`은 확보 완료. 남은 우선순위는 최신 패키지로 유니콘 변기/식탁/의자/barrel 수납장/장식용 인형 5종 인게임 소환 테스트, 변기 `flush`, 식탁 아이템 올리기, 의자 착석, barrel 저장/회수 테스트다.
