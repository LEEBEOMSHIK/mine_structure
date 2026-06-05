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
| `mine_structure:unicorn_wand` | tool item | 마법 지팡이(파티클+부스트), in-game test 대기 | `items/unicorn_wand.md` |
| `mine_structure:unicorn_cloud_block` 외 2종 | block | 건축 블록(구름/사탕/별), in-game test 대기 | `blocks/unicorn_blocks.md` |
| `mine_structure:unicorn_laptop` | furniture entity | 노트북(뚜껑 열기/닫기, 디테일 키보드), in-game test 대기 | `furniture/unicorn_laptop.md` |
| `mine_structure:unicorn_phone` | furniture entity | 핸드폰(받침대 거치, 화면 켜기/끄기), in-game test 대기 | `furniture/unicorn_phone.md` |
| `mine_structure:unicorn_phone_item` | held item | 손에 드는 핸드폰(3D attachable), in-game test 대기 | `items/unicorn_phone_item.md` |
| `mine_structure:unicorn_tv` / `unicorn_arcade` / `unicorn_vanity` | furniture entity | TV/아케이드/화장대(화면·전구 토글), in-game test 대기 | `furniture/unicorn_room_furniture.md` |
| `mine_structure:unicorn_king_bed` | furniture entity | 킹사이즈 침대(단층, rideable 2인), in-game test 대기 | `furniture/unicorn_room_furniture.md` |
| `mine_structure:unicorn_bathtub` 외 | furniture/mob | 욕조/오븐/전자레인지/토스터/로봇청소기, in-game test 대기 | `furniture/unicorn_bath_kitchen.md` |
| `mine_structure:unicorn_swing` 외 | furniture entity | 놀이터(그네/미끄럼틀/시소), in-game test 대기 | `furniture/unicorn_playground.md` |
| `mine_structure:unicorn_horn_headband` | wearable | 입는 코스튬(뿔 머리띠), in-game test 대기(실험) | `wearables/unicorn_costume.md` |
| `mine_structure:unicorn_elytra` | wearable glider | 커스텀 엘리트라(바닐라 별개, 활공+접힘/펴짐), in-game test 대기(실험) | `wearables/unicorn_costume.md` |

새 콘텐츠를 추가할 때는 이 표에 ID, 분류, 상태, 상세 문서 경로를 먼저 등록한다.
