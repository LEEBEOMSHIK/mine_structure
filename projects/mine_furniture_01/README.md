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
- 최신 테스트용 패키지:
  - `dist/mine_furniture_01-20260603-213715/mine_furniture_01.mcaddon`

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
    - `/summon mine_structure:unicorn_cloud_bunk_bed` — 아래/위 두 좌석에 각각 앉는지, 좌석 높이가 매트리스에 맞는지.
    - 필요하면 좌석 위치/흔들 진폭/후광 크기/collision_box를 미세조정한다.
12. 인게임에서 펫/가챠/트램폴린/선물상자를 검증한다.
    - `/summon mine_structure:unicorn_baby_pet` — 설탕/사과/쿠키로 길들여지고, 길들인 뒤 따라오기 + 우클릭 탑승, 걸을 때 다리 애니메이션이 보이는지.
    - `/summon mine_structure:unicorn_gacha_machine` — 우클릭 시 랜덤 보상 지급(+소리).
    - `/summon mine_structure:unicorn_trampoline` — 위에 올라가 점프하면 통통 튕기는지, 웅크리면 멈추는지.
    - `/summon mine_structure:unicorn_gift_box` — 우클릭 시 뚜껑이 열리고 선물 1개 지급되는지.
    - 펫 이동 속도/콜리전, 트램폴린 바운스 세기/판정 높이, 선물상자 뚜껑 각도를 필요 시 미세조정한다.

## 6. 주의

- MCP 스크린샷이 텍스처 대신 마커색으로 보일 수 있다. 자세한 검증 방식은 루트 `../../docs/agent-guides/blockbench-mcp-rules.md`를 따른다.
- 닫힘 시 뚜껑이 1칸 앞으로 와서 시트 맨 뒤 일부가 덜 덮인다. 필요하면 뚜껑 길이를 +1 보정하고 열림 클리어런스를 재검증한다.
