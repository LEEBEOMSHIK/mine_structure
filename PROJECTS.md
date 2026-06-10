# PROJECTS.md — Project Index

Codex와 Claude는 새 세션을 시작할 때 이 파일을 먼저 읽고, 현재 어떤 Minecraft Bedrock 패키지 프로젝트가 진행 중인지 확인한다.

## Active Projects

### 1. `mine_furniture_01`

- 경로: `projects/mine_furniture_01/`
- 상태: 진행 중
- 목적: 여러 가구와 무기를 묶는 Minecraft Bedrock add-on 패키지. 현재 유니콘 테마 가구 라인은 변기(`mine_structure:unicorn_toilet`), 식탁(`mine_structure:unicorn_dining_table`), 의자(`mine_structure:unicorn_chair`), barrel 수납장(`mine_structure:unicorn_barrel_cabinet`), 장식용 유니콘 인형(`mine_structure:decorative_unicorn_doll`), 싱크대 3종(`mine_structure:unicorn_sink_l` / `unicorn_sink_island` / `unicorn_sink_u`, 물 on/off 토글), 아이 친화적 가구 4종(흔들목마 `unicorn_rocking_horse` / 무드등 `unicorn_night_lamp` / 아이스크림 기계 `unicorn_ice_cream_machine` / 구름 2층침대 `unicorn_cloud_bunk_bed`), 펫/놀이 4종(아기 유니콘 펫 `unicorn_baby_pet` / 가챠 `unicorn_gacha_machine` / 트램폴린 `unicorn_trampoline` / 선물상자 `unicorn_gift_box`), 탈것/펫/어항 3종(운전 자동차 `unicorn_car` / 아기 드래곤 펫 `unicorn_baby_dragon` / 어항 `unicorn_aquarium`), 비행/주방 2종(하늘 나는 유니콘 `unicorn_pegasus` / 냉장고 `unicorn_fridge`)로 구성. 무기(유니콘 뿔 검), 음식 5종(쿠키/컵케이크/막대사탕/무지개음료/별사탕), 도구(마법 지팡이), 건축 블록 3종(구름/사탕/별), 입는 코스튬(뿔 머리띠 + 커스텀 엘리트라 `unicorn_elytra`)까지 카테고리를 확장.
- 현재 산출물:
  - Blockbench Bedrock Entity 모델 스펙
  - 단일 64x64 텍스처 아틀라스 설계
  - `lid_open`, `lid_close`, `flush` 애니메이션 설계
  - behavior pack / resource pack 기본 구조
  - `mine_structure:unicorn_toilet`, `mine_structure:unicorn_dining_table`, `mine_structure:unicorn_chair`, `mine_structure:unicorn_barrel_cabinet`, `mine_structure:decorative_unicorn_doll` behavior/client entity 등록
  - `mine_structure:unicorn_horn_blade` 무기 아이템 등록(검 취급/뿔 외형, 2D 아이콘 + 3D attachable 손모델)
  - Blockbench MCP 설정 예시와 `unicorn_toilet` resource map
- 주요 문서:
  - `projects/mine_furniture_01/README.md` — 진행 현황과 다음 작업
  - `projects/mine_furniture_01/PROJECT_CONTEXT.md` — 현재 컨텍스트와 프로젝트별 시작 순서
  - `projects/mine_furniture_01/content/README.md` — 가구/무기 콘텐츠 레지스트리
  - `projects/mine_furniture_01/content/furniture/unicorn_toilet.md` — 첫 가구 콘텐츠 등록 문서
  - `projects/mine_furniture_01/content/furniture/unicorn_toilet.resources.json` — 첫 가구 resource pack 연결 맵
  - `projects/mine_furniture_01/blockbench/export_unicorn_toilet_to_resource_pack.js` — Blockbench MCP export 대상 경로
  - `projects/mine_furniture_01/unicorn_toilet_spec.md` — 상세 파츠, 텍스처, 애니메이션 스펙
- 공통 참고 문서:
  - `docs/agent-guides/README.md` — Codex/Claude 공통 Bedrock/Blockbench 지침 인덱스
  - `docs/agent-guides/environment.md` — 작업 환경 / 도구 / 좌표계
  - `docs/agent-guides/principles.md` — 핵심 원칙
  - `docs/agent-guides/blockbench-mcp-rules.md` — Blockbench/MCP 작업 시 반드시 지킬 주의점
  - `docs/agent-guides/blockbench-mcp-setup.md` — Blockbench MCP 등록과 export 절차
- 다음 작업 요약:
  1. ~~Blockbench MCP tool 확인~~ — 완료 (2026-05-31)
  2. ~~`unicorn_toilet` geometry/texture atlas + `.bbmodel` export~~ — 완료 (2026-06-01 기준 파일 존재 확인)
  3. ~~`flush.ogg` 추가와 `sound_definitions.json` 연결 검증~~ — 완료 (2026-06-01, 기본 합성 효과음. 추후 최종 음원 교체 가능)
  4. Minecraft에서 `mine_structure:unicorn_toilet`, `mine_structure:unicorn_dining_table`, `mine_structure:unicorn_chair`, `mine_structure:unicorn_barrel_cabinet`, `mine_structure:decorative_unicorn_doll` 엔티티 소환 테스트
  5. ~~상호작용으로 `flush` 애니메이션/사운드를 트리거하는 behavior 또는 Script API 방식 확정~~ — behavior `minecraft:interact` + `queue_command` 방식으로 구현 (2026-06-01), 인게임 검증 필요
  6. ~~다음 가구 콘텐츠를 `content/`에 등록~~ — `unicorn_dining_table`, `unicorn_chair` 등록 및 정적 리소스 생성 완료 (2026-06-01)
  7. ~~식탁 아이템 올리기 / 의자 착석 behavior 구현~~ — 식탁 Script API `spawnItem`, 의자 `minecraft:rideable` 구현 (2026-06-01), 인게임 검증 필요
  8. ~~barrel 수납장 / 장식용 유니콘 인형 / 식탁 센터피스 제거 반영~~ — barrel 수납장은 Script API 간이 수납, 인형은 정적 장식, `horn_centerpiece`는 geo/Blockbench에서 제거 (2026-06-01), 인게임 검증 필요
  9. ~~첫 무기 `unicorn_horn_blade`(유니콘 뿔 검) 추가~~ — 검 컴포넌트 + 2D 아이콘 + 3D attachable 손모델 생성 (2026-06-01). 인게임에서 아이콘/손 포즈/전투 동작 검증과 hold 애니메이션 미세조정 필요
  10. ~~세련된 유니콘 싱크대 3종 추가(L자/아일랜드/ㄷ자, 물 켜기·끄기 토글)~~ — geometry/테마별 전용 아틀라스/behavior(variant)/리소스 애니메이션 컨트롤러/Blockbench 원본 생성, 검증 PASS (2026-06-03). 인게임 소환/물 토글 검증 필요
  11. ~~아이 친화적 유니콘 가구 4종 추가(흔들목마/무드등/아이스크림 기계/구름 2층침대)~~ — rideable·variant 토글·Script 지급 메커니즘 + 전용 아틀라스/Blockbench 원본 생성, 검증 PASS (2026-06-03). 인게임 소환/상호작용 검증 필요
  12. ~~펫/놀이 4종 추가(아기 유니콘 펫/가챠/트램폴린/선물상자)~~ — tameable 걷는 몹(follow+rideable), Script 랜덤 보상, runInterval 바운스, interact 뚜껑 애니+선물 + 전용 아틀라스/Blockbench 원본 생성, 검증 PASS (2026-06-03). 인게임 소환/상호작용 검증 필요
  13. ~~운전 자동차/아기 드래곤 펫/어항 추가~~ — rideable 조종(controlled_by_player)+바퀴 회전, 펫 재사용, variant 불빛+물고기 헤엄 + 전용 아틀라스/Blockbench 원본 생성, 검증 PASS (2026-06-03). 인게임 검증 필요
  14. ~~하늘 나는 유니콘/냉장고 추가~~ — 비행 탈것(rideable+controlled_by_player+fly+Script 상하 조종), 냉장고(문 열기 애니+barrel식 저장 재사용) + 전용 아틀라스/Blockbench 원본 생성, 검증 PASS (2026-06-04). 인게임 검증 필요(특히 비행 조종)
  15. ~~먹는 유니콘 쿠키 추가~~ — `minecraft:food` 음식 아이템 + Script로 먹는 순간 회복(Regeneration/Saturation) + 16×16 아이콘, 검증 PASS (2026-06-04). 인게임 검증 필요
  16. ~~효과 음식 4종 / 마법 지팡이 / 건축 블록 3종 / 입는 코스튬 추가~~ — FOOD_EFFECTS 맵, itemUse 지팡이, 데이터 주도형 커스텀 블록(terrain_texture), wearable+attachable 머리띠(실험). 검증 PASS (2026-06-04). 인게임 검증 필요(특히 코스튬)
  18. ~~유니콘 노트북 추가~~ — 디테일 키보드(키캡 32개)+힌지 뚜껑, 뿔 없이 파스텔, 우클릭 토글로 뚜껑 열기/닫기(`variant_lid`). 검증 PASS (2026-06-04). 인게임 확인 필요
  38. ~~파티/장식 6종(배치4)~~ — 생일케이크/풍선다발/가랜드/샹들리에/벽촛대/스탠드랜턴. variant_light·static. 6종 전부 Blockbench 개별 확인. `gen_party.py`. 검증 PASS (2026-06-10). 누적 ~70종. 인게임 확인 필요
  37. ~~주방/카페 8종(배치3)~~ — 커피머신/믹서기/케이크스탠드/컵케이크타워/정수기/식기건조대/제빵오븐/카페바. script_give·variant_light·static. 8종 전부 Blockbench 개별 확인. `gen_kitchen_cafe.py`. 검증 PASS (2026-06-10). 누적 ~64종. 인게임 확인 필요
  36. ~~정원/야외 8종(배치2)~~ — 분수대/우편함/새장/벤치/파라솔테이블/모닥불/캠핑텐트(∧)/정원아치. variant_light·rideable·static. `gen_garden.py`. 검증 PASS + Blockbench 확인 (2026-06-10). 누적 ~56종. 인게임 확인 필요
  35. ~~홈데코 8종(~80종 목표 배치1)~~ — 커피테이블/러그/벽시계/액자/화분/플로어램프/서랍장/협탁. 새 `static` mechanic + variant_light + script_store. `gen_home_decor.py`. 검증 PASS + Blockbench 확인 (2026-06-10). 인게임 확인 필요. 다음 배치: 주방/정원/파티/놀이/펫
  34. ~~입체 A라인 무지개 스커트 의상~~ — 스킨으론 불가한 입체 스커트를 입는 attachable(`unicorn_rainbow_skirt`)로. body 본 하위 5단 콘 큐브(허리 좁고 무릎 넓음), 무지개 프릴. `gen_skirt.py`. 스킨은 off-shoulder로 수정. 검증 PASS + Blockbench 확인 (2026-06-08). 인게임 확인 필요
  33. ~~커스텀 날개를 나비 날개로 변경(4조각)~~ — `unicorn_elytra`를 forewing+hindwing 4조각 나비 날개로(참고 005.png), 위·아래·바깥 펼침, 그라데이션/날개맥/eyespot, atlas 128. `gen_custom_elytra.py` `draw_lobe`/`spot`. Blockbench 확인. 검증 PASS (2026-06-08). 인게임 확인 필요
  32. ~~커스텀 날개를 천사 날개로 변경~~ — `unicorn_elytra`를 무지개 제트 → 흰/파스텔 천사 날개, 형태는 참고 002.png의 뾰족한 톱니 깃털. `gen_custom_elytra.py` 수정, Blockbench 확인. 검증 PASS (2026-06-08). 인게임 확인 필요
  30. ~~상상놀이 세트 4종~~ — 성 텐트(앉기), 인형의 집(불빛 토글), 장난감 상자(보관 script_store), 이젤(그림 토글). `gen_imagination.py` 신규. 검증 PASS + Blockbench 확인 (2026-06-07). 인게임 확인 필요
  29. ~~놀이공원 탈것 3종~~ — 회전목마(탑승4+회전), 관람차(회전 토글 variant_spin), 열기구(탑승1+둥실). `gen_amusement.py` 신규. 검증 PASS + Blockbench 확인 (2026-06-07). 인게임 확인 필요
  28. ~~마법봉 보석 코어 + 반짝이 파티클~~ — 별 코어를 작은 보석(45도 마름모, 청록/자수정)으로 교체, 손에 든 동안 보석에서 커스텀 반짝이 파티클(Script `runInterval`, tinting 색별). Blockbench로 확인. 검증 PASS (2026-06-07). 인게임 확인 필요
  27. ~~마법봉 2종 손에 드는 3D 막대 모델 추가~~ — `unicorn_wand`/`unicorn_transform_wand`를 attachable 3D 막대(손잡이+그립+별 헤드+발광 코어)로 보강, 2D 아이콘/우클릭 동작 유지. `gen_wand_items.py` 신규, validate TOOLS `attachable` 검증. 검증 PASS (2026-06-06). 인게임 확인 필요(손 포즈)
  26. ~~변신 마법봉 추가~~ — 들고 동물 우클릭 시 랜덤 동물로 변신(spawnEntity+remove, 바닐라 동물만). 검증 PASS (2026-06-06). 인게임 확인 필요
  25. ~~품질 패스(피드백)~~ — 욕조 물 차오름(variant_fill), 미끄럼틀 경사판/사다리, 시소 대칭+틸트, 선풍기 재설계, 로봇/벽난로/책장/토스터/오븐/전자레인지/자동차 디테일↑, 킹베드 세로 연장, 떠있는 큐브 감사(audit_gaps.py)·수정. 검증 PASS (2026-06-06). 인게임 확인 필요
  24. ~~타고 모는 크루즈 보트 추가~~ — buoyant 부력 + controlled_by_player 물 위 운전, rideable 4인(`boat` mechanic). 검증 PASS (2026-06-06). 인게임 확인 필요(조종/부력)
  23. ~~거실 가구 6종 추가(소파/벽난로/선풍기/책장/옷장/피아노)~~ — rideable·불 토글·날개 회전(`variant_spin`)·Script 수납/연주. 검증 PASS (2026-06-06). 인게임 확인 필요
  22. ~~욕실/주방/로봇청소기 + 놀이터 8종 추가~~ — 거품욕조/오븐/전자레인지(variant 토글), 토스터(Script 지급), 로봇청소기(새 `wander` 자동이동), 그네/미끄럼틀/시소(rideable). 검증 PASS (2026-06-05). 인게임 확인 필요
  21. ~~방 가구 4종 추가(TV/아케이드/화장대/킹침대)~~ — 화면·전구 토글(`variant_light`) 3종 + 단층 킹사이즈 침대(rideable 2인, `rideable_simple`). 검증 PASS (2026-06-05). 인게임 확인 필요
  20. ~~손에 드는 핸드폰 아이템 추가~~ — `unicorn_phone_item`(거치형과 별개), 검 방식 attachable 3D 손모델 + hold 포즈 4종 + 2D 아이콘, `validate_held`. 검증 PASS (2026-06-04). hold 포즈 인게임 조정 필요
  19. ~~유니콘 핸드폰 추가 + Blockbench 애니 임베드~~ — 받침대 거치 스마트폰(화면 켜기/끄기 `variant_light`), 그리고 모든 모델 애니를 `.bbmodel`에 임베드(`embed_animations.py`)해 Animate 탭에 표시. 검증 PASS (2026-06-04). 인게임 확인 필요
  17. ~~날개를 elytra 바탕 커스텀 아이템으로~~ — 바닐라 elytra는 그대로 두고 별도 `mine_structure:unicorn_elytra`(wearable chest + glider + 커스텀 날개 geo + q.is_gliding folded/spread) 생성, 정적 wings 제거. 검증 PASS (2026-06-04). ⚠️ 글라이더/부착 애니 인게임 검증 필수
  31. ~~파스텔 유니콘 캐릭터 스킨팩 신규 프로젝트~~ — `mine_skins_01` 추가. 참고 이미지 기반 64×64 플레이어 스킨 2종(`unicorn_pastel`/`unicorn_pastel_mint`) 절차 생성, `.mcpack` 빌드. 정면 미리보기 확인 (2026-06-08). 인게임 적용 확인 필요

### 2. `mine_skins_01`

- 경로: `projects/mine_skins_01/`
- 상태: 진행 중
- 목적: Minecraft Bedrock **스킨팩**. 파스텔 유니콘 소녀 캐릭터 플레이어 스킨(64×64)을 절차 생성. 참고 이미지 `game/mine_reference/001.png` 기반 근사본. 현재 `unicorn_pastel`(라벤더/분홍), `unicorn_pastel_mint`(민트/하늘) 2종.
- 현재 산출물:
  - `gen_skins.py` — 64×64 스킨 PNG + 정면 미리보기 + manifest/skins.json/texts 생성
  - `build_skinpack.py` — `skin_pack/` → `dist/` `.mcpack`(preview 제외)
  - `skin_pack/` — manifest(format_version 2, skin_pack) + skins.json(geometry.humanoid.custom) + 스킨 2종 + texts
- 주요 문서:
  - `projects/mine_skins_01/README.md` — 스킨 목록·구조·빌드
  - `projects/mine_skins_01/PROJECT_CONTEXT.md` — 현재 컨텍스트·시작 순서
- 다음 작업: 인게임 스킨 적용/정면·측면 확인, 색·비율 보정. (옵션) 솟은 뿔/꼬리/날개는 커스텀 geometry로 확장.

## 새 프로젝트 추가 규칙

새 패키지를 시작할 때는 아래 형식을 따른다.

```text
projects/<project_id>/
├─ README.md
├─ PROJECT_CONTEXT.md
└─ docs-or-assets
```

그리고 이 파일의 `Active Projects` 또는 `Backlog Projects` 섹션에 다음 정보를 추가한다.

- 경로
- 상태
- 목적
- 주요 문서
- 다음 작업

## Backlog Projects

현재 없음.
