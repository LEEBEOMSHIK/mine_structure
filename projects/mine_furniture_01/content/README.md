# Content Registry

이 폴더는 add-on에 들어갈 가구와 무기 콘텐츠를 관리한다.

## 분류

- `furniture/` — 배치형/상호작용형 가구
- `weapons/` — 무기 아이템, 장비, 전투용 엔티티
- `foods/` — 먹는 아이템
- `items/` — 도구/지팡이 등 일반 아이템
- `blocks/` — 직접 쌓는 커스텀 블록
- `wearables/` — 입는 코스튬(방어구 슬롯)

## 등록 상태

| ID | Type | Status | Docs |
|----|------|--------|------|
| `mine_structure:unicorn_toilet` | furniture entity | model ready, add-on scaffold ready | `furniture/unicorn_toilet.md` |
| `mine_structure:unicorn_dining_table` | furniture entity | planned static unicorn dining furniture | `furniture/unicorn_dining_table.md` |
| `mine_structure:unicorn_chair` | furniture entity | planned static unicorn dining furniture | `furniture/unicorn_chair.md` |
| `mine_structure:unicorn_barrel_cabinet` | furniture entity | Script API simple storage furniture | `furniture/unicorn_barrel_cabinet.md` |
| `mine_structure:decorative_unicorn_doll` | furniture entity | static decorative unicorn doll | `furniture/decorative_unicorn_doll.md` |
| `mine_structure:unicorn_horn_blade` | weapon item (sword) | 2D icon + 3D attachable ready, in-hand pose needs tuning | `weapons/unicorn_horn_blade.md` |
| `mine_structure:unicorn_sink_l` | furniture entity | L자 싱크대, 물 on/off 토글, in-game test 대기 | `furniture/unicorn_sinks.md` |
| `mine_structure:unicorn_sink_island` | furniture entity | 아일랜드(고리) 싱크대, 물 on/off 토글, in-game test 대기 | `furniture/unicorn_sinks.md` |
| `mine_structure:unicorn_sink_u` | furniture entity | ㄷ자 싱크대, 물 on/off 토글, in-game test 대기 | `furniture/unicorn_sinks.md` |
| `mine_structure:unicorn_rocking_horse` | furniture entity | 흔들목마, rideable + 흔들 애니, in-game test 대기 | `furniture/unicorn_kids_furniture.md` |
| `mine_structure:unicorn_night_lamp` | furniture entity | 무드등, variant on/off, in-game test 대기 | `furniture/unicorn_kids_furniture.md` |
| `mine_structure:unicorn_ice_cream_machine` | furniture entity | 아이스크림 기계, Script 간식 지급, in-game test 대기 | `furniture/unicorn_kids_furniture.md` |
| `mine_structure:unicorn_cloud_bunk_bed` | furniture entity | 구름 2층침대, rideable 2인, in-game test 대기 | `furniture/unicorn_kids_furniture.md` |
| `mine_structure:unicorn_baby_pet` | pet mob | 아기 유니콘, 길들이기+따라오기+탑승, in-game test 대기 | `furniture/unicorn_more_furniture.md` |
| `mine_structure:unicorn_gacha_machine` | furniture entity | 가챠 뽑기(랜덤 보상), in-game test 대기 | `furniture/unicorn_more_furniture.md` |
| `mine_structure:unicorn_trampoline` | furniture entity | 트램폴린(점프 바운스), in-game test 대기 | `furniture/unicorn_more_furniture.md` |
| `mine_structure:unicorn_gift_box` | furniture entity | 선물상자(뚜껑 열기+선물), in-game test 대기 | `furniture/unicorn_more_furniture.md` |
| `mine_structure:unicorn_car` | vehicle entity | 운전하는 자동차(조종+바퀴 회전), in-game test 대기 | `furniture/unicorn_vehicles_pets.md` |
| `mine_structure:unicorn_baby_dragon` | pet mob | 아기 드래곤(길들이기+따라오기+탑승), in-game test 대기 | `furniture/unicorn_vehicles_pets.md` |
| `mine_structure:unicorn_aquarium` | furniture entity | 어항(물고기 헤엄+불빛), in-game test 대기 | `furniture/unicorn_vehicles_pets.md` |
| `mine_structure:unicorn_pegasus` | mount entity | 하늘 나는 유니콘(탑승 비행), in-game test 대기 | `furniture/unicorn_vehicles_pets.md` |
| `mine_structure:unicorn_fridge` | furniture entity | 냉장고(문 열기+저장/꺼내기), in-game test 대기 | `furniture/unicorn_vehicles_pets.md` |
| `mine_structure:unicorn_cookie` | food item | 유니콘 쿠키(허기 회복 + 체력 회복), in-game test 대기 | `foods/unicorn_cookie.md` |
| `mine_structure:unicorn_cupcake` 외 3종 | food item | 효과 음식 세트(컵케이크/막대사탕/무지개음료/별사탕), in-game test 대기 | `foods/unicorn_treats.md` |
| `mine_structure:unicorn_wand` | tool item | 마법 지팡이(파티클+부스트, 손에 3D 막대 모델), in-game test 대기 | `items/unicorn_wand.md` |
| `mine_structure:unicorn_cloud_block` 외 2종 | block | 건축 블록(구름/사탕/별), in-game test 대기 | `blocks/unicorn_blocks.md` |
| `mine_structure:unicorn_laptop` | furniture entity | 노트북(뚜껑 열기/닫기, 디테일 키보드), in-game test 대기 | `furniture/unicorn_laptop.md` |
| `mine_structure:unicorn_phone` | furniture entity | 핸드폰(받침대 거치, 화면 켜기/끄기), in-game test 대기 | `furniture/unicorn_phone.md` |
| `mine_structure:unicorn_phone_item` | held item | 손에 드는 핸드폰(3D attachable), in-game test 대기 | `items/unicorn_phone_item.md` |
| `mine_structure:unicorn_tv` / `unicorn_arcade` / `unicorn_vanity` | furniture entity | TV/아케이드/화장대(화면·전구 토글), in-game test 대기 | `furniture/unicorn_room_furniture.md` |
| `mine_structure:unicorn_king_bed` | furniture entity | 킹사이즈 침대(단층, rideable 2인), in-game test 대기 | `furniture/unicorn_room_furniture.md` |
| `mine_structure:unicorn_bathtub` 외 | furniture/mob | 욕조/오븐/전자레인지/토스터/로봇청소기, in-game test 대기 | `furniture/unicorn_bath_kitchen.md` |
| `mine_structure:unicorn_swing` 외 | furniture entity | 놀이터(그네/미끄럼틀/시소), in-game test 대기 | `furniture/unicorn_playground.md` |
| `mine_structure:unicorn_sofa` 외 | furniture entity | 거실(소파/벽난로/선풍기/책장/옷장/피아노), in-game test 대기 | `furniture/unicorn_living_furniture.md` |
| `mine_structure:unicorn_cruise` | vehicle entity | 타고 모는 크루즈 보트(물 위 운전, 4인), in-game test 대기 | `furniture/unicorn_cruise.md` |
| `mine_structure:unicorn_transform_wand` | tool item | 변신 마법봉(동물→랜덤 동물, 손에 3D 막대 모델), in-game test 대기 | `items/unicorn_transform_wand.md` |
| `mine_structure:unicorn_carousel` | furniture entity | 회전목마(탑승 4인 + 항상 회전), in-game test 대기 | `furniture/unicorn_amusement.md` |
| `mine_structure:unicorn_ferris_wheel` | furniture entity | 관람차(우클릭 회전 토글), in-game test 대기 | `furniture/unicorn_amusement.md` |
| `mine_structure:unicorn_balloon` | furniture entity | 열기구(탑승 1인 + 둥실), in-game test 대기 | `furniture/unicorn_amusement.md` |
| `mine_structure:unicorn_castle_tent` | furniture entity | 성 텐트(들어가 앉기, 1인), in-game test 대기 | `furniture/unicorn_imagination.md` |
| `mine_structure:unicorn_dollhouse` | furniture entity | 인형의 집(창문 불빛 토글), in-game test 대기 | `furniture/unicorn_imagination.md` |
| `mine_structure:unicorn_toy_box` | furniture entity | 장난감 상자(보관/꺼내기), in-game test 대기 | `furniture/unicorn_imagination.md` |
| `mine_structure:unicorn_easel` | furniture entity | 이젤(캔버스 그림 토글), in-game test 대기 | `furniture/unicorn_imagination.md` |
| `mine_structure:unicorn_horn_headband` | wearable | 입는 코스튬(뿔 머리띠), in-game test 대기(실험) | `wearables/unicorn_costume.md` |
| `mine_structure:unicorn_elytra` | wearable glider | 나비 날개(커스텀 글라이더, 바닐라 별개, 활공+접힘/펴짐), in-game test 대기(실험) | `wearables/unicorn_costume.md` |
| `mine_structure:unicorn_rainbow_skirt` | wearable | 입체 A라인 무지개 프릴 스커트(다리 슬롯, 허리 좁고 아래로 넓어짐), in-game test 대기(실험) | `wearables/unicorn_costume.md` |
| `mine_structure:unicorn_coffee_table` 외 7종 | furniture entity | 홈데코 8종(커피테이블/러그/벽시계/액자/화분/플로어램프/서랍장/협탁), in-game test 대기 | `furniture/unicorn_home_decor.md` |
| `mine_structure:unicorn_fountain` 외 7종 | furniture entity | 정원/야외 8종(분수대/우편함/새장/벤치/파라솔테이블/모닥불/텐트/정원아치), in-game test 대기 | `furniture/unicorn_garden.md` |

새 콘텐츠를 추가할 때는 이 표에 ID, 분류, 상태, 상세 문서 경로를 먼저 등록한다.
