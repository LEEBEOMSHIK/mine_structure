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

## 6. 주의

- MCP 스크린샷이 텍스처 대신 마커색으로 보일 수 있다. 자세한 검증 방식은 루트 `../../docs/agent-guides/blockbench-mcp-rules.md`를 따른다.
- 닫힘 시 뚜껑이 1칸 앞으로 와서 시트 맨 뒤 일부가 덜 덮인다. 필요하면 뚜껑 길이를 +1 보정하고 열림 클리어런스를 재검증한다.
