# PROJECT_CONTEXT.md — mine_furniture_01

이 프로젝트는 Minecraft Bedrock용 여러 가구와 무기를 묶는 add-on 패키지 작업 공간이다.
현재 등록 콘텐츠는 **무지개 유니콘 변기(`mine_structure:unicorn_toilet`)**, **유니콘 식탁(`mine_structure:unicorn_dining_table`)**, **유니콘 의자(`mine_structure:unicorn_chair`)**, **유니콘 barrel 수납장(`mine_structure:unicorn_barrel_cabinet`)**, **장식용 유니콘 인형(`mine_structure:decorative_unicorn_doll`)**이다.

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
- 현재 실행 환경에는 Bedrock 기본 `com.mojang` 경로가 없어 Minecraft 앱 기반 소환 테스트는 직접 수행하지 못했다.

## 공통 세부 지침

- `../../docs/agent-guides/environment.md` — 작업 환경 / 도구 / 좌표계
- `../../docs/agent-guides/principles.md` — 핵심 원칙
- `../../docs/agent-guides/blockbench-mcp-rules.md` — Blockbench/MCP 작업 시 반드시 지킬 주의점

## 다음 세션 시작 지점

`README.md`의 "다음 작업(NEXT)" 섹션부터 본다.
geometry/texture/`flush.ogg`/`.bbmodel`은 확보 완료. 남은 우선순위는 최신 패키지로 유니콘 변기/식탁/의자/barrel 수납장/장식용 인형 5종 인게임 소환 테스트, 변기 `flush`, 식탁 아이템 올리기, 의자 착석, barrel 저장/회수 테스트다.
