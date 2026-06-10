# PROJECT_CONTEXT.md — mine_furniture_01

이 프로젝트는 Minecraft Bedrock용 여러 가구와 무기를 묶는 add-on 패키지 작업 공간이다.
현재 등록 콘텐츠는 가구/펫/탈것 21종 — **무지개 유니콘 변기(`mine_structure:unicorn_toilet`)**, **유니콘 식탁(`mine_structure:unicorn_dining_table`)**, **유니콘 의자(`mine_structure:unicorn_chair`)**, **유니콘 barrel 수납장(`mine_structure:unicorn_barrel_cabinet`)**, **장식용 유니콘 인형(`mine_structure:decorative_unicorn_doll`)**, **유니콘 싱크대 3종(`mine_structure:unicorn_sink_l` / `unicorn_sink_island` / `unicorn_sink_u`)**, **아이 친화적 가구 4종(`mine_structure:unicorn_rocking_horse` 흔들목마 / `unicorn_night_lamp` 무드등 / `unicorn_ice_cream_machine` 아이스크림 기계 / `unicorn_cloud_bunk_bed` 구름 2층침대)**, **펫/놀이 4종(`unicorn_baby_pet` 아기 유니콘 펫 / `unicorn_gacha_machine` 가챠 / `unicorn_trampoline` 트램폴린 / `unicorn_gift_box` 선물상자)**, **탈것/펫/어항 3종(`unicorn_car` 운전 자동차 / `unicorn_baby_dragon` 아기 드래곤 펫 / `unicorn_aquarium` 어항)**, **비행/주방 2종(`unicorn_pegasus` 하늘 나는 유니콘 / `unicorn_fridge` 냉장고)** — 과 무기 1종 **유니콘 뿔 검(`mine_structure:unicorn_horn_blade`)**, 음식 5종 **유니콘 쿠키/컵케이크/막대사탕/무지개음료/별사탕**, 도구 1종 **마법 지팡이(`unicorn_wand`)**, 건축 블록 3종 **구름/사탕/별 블록**, 입는 코스튬 2종 **뿔 머리띠(`unicorn_horn_headband`)**, **커스텀 엘리트라(`unicorn_elytra`, 활공+접힘/펴짐, 바닐라 elytra와 별개)**이다.

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
- (2026-06-06) 변신 마법봉 `unicorn_transform_wand` 추가. 들고 동물 우클릭 시 `playerInteractWithEntity`→`transformAnimal`이 대상 위치에 랜덤 동물(`TRANSFORM_ANIMALS` 16종) spawnEntity + 기존 remove(파티클/소리). 바닐라 동물만 대상. 아이콘+item_texture, `TOOLS`(script_marker transformAnimal) validate, 검증 PASS. 최신 패키지: `../../dist/mine_furniture_01-20260606-215232/mine_furniture_01.mcaddon`
- (2026-06-10) 신규 가구 2차 배치 **정원/야외 8종**(`unicorn_fountain`/`mailbox`/`birdcage`/`bench`/`parasol_table`/`campfire`/`tent`/`garden_arch`). variant_light 2(분수/모닥불), rideable 2(벤치/텐트), static 4. 텐트는 계단식 패널 ∧ A프레임. 생성기 `gen_garden.py`, `KIDS` 등록, 검증 PASS, Blockbench 확인. 누적 ~56종. 최신: `../../dist/mine_furniture_01-20260610-095738/mine_furniture_01.mcaddon`
- (2026-06-10) **~80종 목표** 시작. 신규 가구 1차 배치 **홈데코 8종**(`unicorn_coffee_table`/`rug`/`wall_clock`/`picture_frame`/`potted_plant`/`floor_lamp`/`dresser`/`nightstand`). 정적 6종은 새 `static` mechanic(`script_entity(...,"static")` + validate `static` 분기), `floor_lamp` variant_light, `dresser` script_store(main.js `DRESSER_ID` 18칸). 생성기 `gen_home_decor.py`, `KIDS` 등록, 검증 PASS, Blockbench 확인. 최신: `../../dist/mine_furniture_01-20260610-094610/mine_furniture_01.mcaddon`. 다음 배치: 주방/카페·정원/야외·파티·놀이·펫.
- (2026-06-08) 입체 A라인 무지개 스커트 의상 `unicorn_rainbow_skirt` 추가(스킨으론 불가능한 입체 스커트를 입는 attachable로). `gen_skirt.py`: player `body` 본 하위 5단 콘 큐브(위→아래 폭 증가, 핑크→라벤더 무지개, 프릴 명암), wearable(legs)+armor render controller. `WEARABLES`/`item_texture` 등록, 검증 PASS, Blockbench 확인. `mine_skins_01` 스킨은 어깨 드러난(off-shoulder) 흰 상의로 수정. 최신: `../../dist/mine_furniture_01-20260608-213919/mine_furniture_01.mcaddon`
- (2026-06-08) 커스텀 날개 `unicorn_elytra`를 **나비 날개**로 재디자인 → **4조각 구조**(참고 005.png)로 재구성. 세로 1장이라 나비 같지 않던 것을 각 쪽 forewing(위 큰 lobe)+hindwing(아래 작은 lobe) 2조각씩(총 4 cube) `right_wing`/`left_wing` 본 아래 위·아래·바깥 배치. `draw_lobe`(forewing 둥근 부채/hindwing 둥근 타원)+그라데이션/날개맥/eyespot(`spot`). atlas 128, 두께 0.05, 펴짐 ±52°. 이름 "나비 날개". Blockbench 확인, 검증 PASS. 최신 패키지: `../../dist/mine_furniture_01-20260608-134734/mine_furniture_01.mcaddon`
- (2026-06-08) (이전) 커스텀 날개를 무지개 제트 → **천사 날개**(흰/파스텔)로 재디자인, 형태는 참고 `game/mine_reference/002.png`의 **뾰족한 톱니 깃털**을 따름(부채 깃털 능선/경계 + sawtooth 끝). 색=천사, 형태=참고. `gen_custom_elytra.py` `angel_edge`/`draw_wing` 수정, 날개 11×21로 키움, 이름 "천사 날개". Blockbench 접힘/펴짐 확인. 검증 PASS. 최신 패키지: `../../dist/mine_furniture_01-20260608-095357/mine_furniture_01.mcaddon`
- (2026-06-07) 상상놀이 세트 4종 추가: `unicorn_castle_tent`(들어가 앉기 rideable_simple), `unicorn_dollhouse`(창문 불빛 variant_light/glow), `unicorn_toy_box`(보관 script_store, `toy_box_items` 12칸, main.js 분기 추가), `unicorn_easel`(캔버스 그림 variant_light/glow). 생성기 `gen_imagination.py` 신규. `KIDS` 등록, 검증 PASS, Blockbench 확인(이젤 별/뚜껑 각도 보정). 최신 패키지: `../../dist/mine_furniture_01-20260607-042819/mine_furniture_01.mcaddon`
- (2026-06-07) 놀이공원 탈것 3종 추가: `unicorn_carousel`(탑승4+항상 y회전 `spin`), `unicorn_ferris_wheel`(우클릭 회전 토글 `variant_spin`/`blades` z축, 8캐빈), `unicorn_balloon`(탑승1+둥실 `bob`). 생성기 `gen_amusement.py` 신규(`rideable_animated_wiring` + ferris는 `variant_spin_wiring` 재사용). `KIDS` 등록(carousel/balloon=rideable_simple, ferris=variant_spin), 검증 PASS, Blockbench 확인. 최신 패키지: `../../dist/mine_furniture_01-20260607-034326/mine_furniture_01.mcaddon`
- (2026-06-07) 마법봉 별 코어를 **작은 보석**(z 45도 마름모, 앞 돌출; 지팡이=청록/변신봉=자수정)으로 교체하고, **손에 든 동안 보석 반짝이 파티클** 추가. Bedrock attachable 파티클 한계로 Script 주기 spawn 채택: `main.js` `system.runInterval(...,12)`가 메인핸드 wand 보유 플레이어의 보석 위치(시선 근사)에 커스텀 파티클(`wand_sparkle_cyan`/`wand_sparkle_amethyst`, tinting 색만 다른 1장 텍스처) emit. `gen_wand_items.py` `build_particles()` 추가. Blockbench로 보석 확인(MCP 재연결). 검증 PASS. 최신 패키지: `../../dist/mine_furniture_01-20260607-031542/mine_furniture_01.mcaddon`
- (2026-06-06) 마법봉 2종(`unicorn_wand`, `unicorn_transform_wand`)에 **손에 드는 3D 막대 모델**(attachable) 추가. 막대 손잡이+그립밴드 2개+별 헤드(정사각 큐브 2개 z 45도 겹침)+발광 코어. 인벤토리 2D 아이콘/우클릭 동작은 유지. 생성기 `gen_wand_items.py` 신규, `embed_animations.py`로 1·3인칭 손 포즈 임베드. `validate` TOOLS에 `attachable:True`(attachable/geo/64×64 atlas/hand_equipped 검증) 추가, 검증 PASS. 최신 패키지: `../../dist/mine_furniture_01-20260606-220526/mine_furniture_01.mcaddon`
- (2026-06-06) 품질 패스(사용자 피드백): 욕조 물 차오름(새 `variant_fill`), 미끄럼틀 경사판(회전 큐브)+사다리, 시소 대칭+틸트, 선풍기 재설계(안전망+4날개), 로봇청소기/벽난로/책장/토스터/오븐/전자레인지/자동차 디테일↑, 킹베드 세로 연장. `blockbench/audit_gaps.py`로 떠 있는 큐브 감사·수정(머리띠만 정상 잔존), Builder에 회전 큐브 지원 추가. 검증 PASS. 최신 패키지: `../../dist/mine_furniture_01-20260606-213255/mine_furniture_01.mcaddon`
- (2026-06-06) 타고 모는 크루즈 보트 `unicorn_cruise` 추가. `minecraft:buoyant`로 부력 + `behavior.controlled_by_player`+`movement`+`navigation.generic`(amphibious)로 물 위 운전, rideable 좌석 4개(controlling_seat 0). 새 `boat` mechanic으로 validate, 검증 PASS. `gen_cruise.py`. 엔티티 충돌박스 1개라 갑판 보행 불가(타고 이동). 인게임 검증 필요. 최신 패키지: `../../dist/mine_furniture_01-20260606-115356/mine_furniture_01.mcaddon`
- (2026-06-06) 거실 가구 6종 추가: `unicorn_sofa`(rideable 3), `unicorn_fireplace`(불 토글 variant_light), `unicorn_fan`(날개 회전 토글, 새 `variant_spin`), `unicorn_bookshelf`/`unicorn_wardrobe`(Script 수납 `script_store`), `unicorn_piano`(Script 연주 `script_play`). `gen_living_furniture.py`, main.js 책장/옷장/피아노 핸들러, validate에 variant_spin/script_store/script_play 추가, 검증 PASS. 최신 패키지: `../../dist/mine_furniture_01-20260606-114713/mine_furniture_01.mcaddon`
- (2026-06-05) 욕실/주방/로봇 + 놀이터 8종 추가: `unicorn_bathtub`/`unicorn_oven`/`unicorn_microwave`(`variant_light` 토글), `unicorn_toaster`(Script 토스트 지급), `unicorn_robot_vacuum`(새 `wander` 메커니즘=자동 배회 몹), `unicorn_swing`(rideable+흔들 anim)/`unicorn_slide`/`unicorn_seesaw`(rideable). `gen_bath_kitchen.py`/`gen_playground.py`(gen_room_furniture 헬퍼 재사용), main.js 토스터 핸들러, validate에 `wander` 추가, 검증 PASS. (Blockbench MCP 세션 끊김 — 앱 로드 확인 미실시.) 최신 패키지: `../../dist/mine_furniture_01-20260605-215802/mine_furniture_01.mcaddon`
- (2026-06-05) 방 가구 4종 추가: `unicorn_tv`/`unicorn_arcade`/`unicorn_vanity`(화면·거울전구 켜기/끄기 `variant_light`), `unicorn_king_bed`(단층 킹사이즈, `minecraft:rideable` 좌석 2개, 새 `rideable_simple` mechanic). 전부 파스텔/뿔 없음. `gen_room_furniture.py`, 애니 `embed_animations.py`, validate 등록, 검증 PASS. (생성 시 Blockbench MCP 세션이 끊겨 앱 로드 확인은 미실시 — 재연결 후 bbmodel 확인.) 최신 패키지: `../../dist/mine_furniture_01-20260605-212934/mine_furniture_01.mcaddon`
- (2026-06-04) 손에 드는 핸드폰 `unicorn_phone_item`에 기능 추가: `world.afterEvents.itemUse`로 우클릭=셀카(하트/반짝 파티클+찰칵+`note.bell` 벨소리 멜로디), 웅크림 우클릭=손전등(야간투시 토글, dynamic property `phone_flashlight`). `minecraft:cooldown` 0.6초. `validate_held`에 scripted 체크 추가, 검증 PASS.
- (2026-06-04) 손에 드는 핸드폰 `unicorn_phone_item` 추가(거치형 `unicorn_phone`과 별개). 검과 같은 attachable 방식(`hand_equipped` + `controller.render.item_default` + hold 포즈 4종), 2D 아이콘 + 3D 손모델. `gen_phone_item.py`, validate `HELD_ITEMS`/`validate_held` 추가, 검증 PASS. hold 포즈는 인게임 미세조정 필요. 최신 패키지: `../../dist/mine_furniture_01-20260604-234050/mine_furniture_01.mcaddon`
- (2026-06-04) 유니콘 핸드폰(`unicorn_phone`) 추가. 받침대 거치 스마트폰(파스텔, 뿔 없음, 카메라/홈버튼), 우클릭 화면 켜기/끄기(`variant_light`, `glow` 본=얼굴 화면). `gen_phone.py`, validate 등록, 검증 PASS. 애니는 `embed_animations.py`로 bbmodel에도 임베드. 최신 패키지: `../../dist/mine_furniture_01-20260604-232908/mine_furniture_01.mcaddon`
- (2026-06-04) Blockbench Animate 탭이 비어 보이던 문제 → `blockbench/embed_animations.py`로 각 add-on 애니(`animations/*.animation.json`)를 Blockbench 내부 포맷으로 변환해 해당 `.bbmodel`에 임베드(본 이름→그룹 UUID 매핑). 생성기를 재실행하면 bbmodel 애니가 비워지므로 이 스크립트를 다시 돌린다.
- (2026-06-04) 유니콘 노트북(`unicorn_laptop`) 추가. 키캡 32개+스페이스바 개별 모델링, 트랙패드/힌지, 귀여운 얼굴 화면. **뿔 없이** 파스텔 색감 + 하트 액센트. 우클릭 토글로 뚜껑 열기/닫기(`minecraft:variant` + 컨트롤러가 `lid` 본 0°↔100° 회전, 기본 열림). mechanic `variant_lid`로 validate 추가, 검증 PASS. `gen_laptop.py`, Blockbench 원본 `unicorn_laptop.bbmodel`. 최신 패키지: `../../dist/mine_furniture_01-20260604-173735/mine_furniture_01.mcaddon`
- (2026-06-04) 날개를 elytra 바탕 **커스텀 아이템**으로 확정. 처음엔 바닐라 elytra 리텍스처(override)로 했으나 "바닐라는 그대로 두고 커스텀" 요구라 되돌리고, 별도 `mine_structure:unicorn_elytra`(wearable chest + `minecraft:glider` + 커스텀 날개 geo `body`/`left_wing`/`right_wing` + `q.is_gliding`으로 folded↔spread 컨트롤러)를 생성(`gen_custom_elytra.py`). 정적 `unicorn_wings`는 제거. `validate_elytra`를 커스텀 아이템 검증으로 교체, 검증 PASS. 머리띠/엘리트라 모두 `.bbmodel`로 Blockbench에 올림(`gen_costume_bbmodel.py`). ⚠️ 커스텀 글라이더·플레이어 부착 애니는 버전 민감 → 인게임 검증 필수. 최신 패키지: `../../dist/mine_furniture_01-20260604-154830/mine_furniture_01.mcaddon`
- (2026-06-04) 콘텐츠 카테고리 확장 — 효과 음식 4종(`unicorn_cupcake`/`unicorn_lollipop`/`unicorn_rainbow_drink`/`unicorn_star_candy`, `FOOD_EFFECTS` 맵), 마법 지팡이(`unicorn_wand`, `itemUse` 파티클+부스트), 건축 블록 3종(`unicorn_cloud_block`/`unicorn_candy_block`/`unicorn_star_block`, 데이터 주도형 + terrain_texture), 입는 코스튬 2종(`unicorn_horn_headband`/`unicorn_wings`, wearable+attachable, 플레이어 본 부착 — 실험적, 인게임 검증 필수). validate에 `FOODS`확장/`TOOLS`/`BLOCKS`/`WEARABLES` 추가, 검증 PASS. 최신 패키지: `../../dist/mine_furniture_01-20260604-141845/mine_furniture_01.mcaddon`
- (2026-06-04) 먹는 아이템 `unicorn_cookie`(유니콘 쿠키) 추가. `minecraft:food`로 허기 회복 + `scripts/main.js`의 `itemCompleteUse`가 먹는 순간 `regeneration`/`saturation` 부여로 실제 체력 회복. 16×16 아이콘 + item_texture 등록. validate에 `FOODS`/`validate_food` 추가, 검증 PASS. 최신 패키지: `../../dist/mine_furniture_01-20260604-115302/mine_furniture_01.mcaddon`
- 현재 실행 환경에는 Bedrock 기본 `com.mojang` 경로가 없어 Minecraft 앱 기반 소환 테스트는 직접 수행하지 못했다.

## 공통 세부 지침

- `../../docs/agent-guides/environment.md` — 작업 환경 / 도구 / 좌표계
- `../../docs/agent-guides/principles.md` — 핵심 원칙
- `../../docs/agent-guides/blockbench-mcp-rules.md` — Blockbench/MCP 작업 시 반드시 지킬 주의점

## 다음 세션 시작 지점

`README.md`의 "다음 작업(NEXT)" 섹션부터 본다.
geometry/texture/`flush.ogg`/`.bbmodel`은 확보 완료. 남은 우선순위는 최신 패키지로 유니콘 변기/식탁/의자/barrel 수납장/장식용 인형 5종 인게임 소환 테스트, 변기 `flush`, 식탁 아이템 올리기, 의자 착석, barrel 저장/회수 테스트다.
