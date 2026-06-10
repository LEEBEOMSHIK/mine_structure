# 주방/카페 8종 (배치 3)

~80종 목표 신규 가구 3차 배치. 생성기 `blockbench/gen_kitchen_cafe.py`. 8종 모두 Blockbench로 개별 확인.

| ID | Mechanic | 설명 |
|----|----------|------|
| `mine_structure:unicorn_coffee_machine` | script_give | 커피머신(우클릭→무지개음료 지급, 디스플레이 얼굴) |
| `mine_structure:unicorn_blender` | variant_light | 믹서기(작동 juice glow on/off) |
| `mine_structure:unicorn_cake_stand` | static | 케이크 스탠드(받침+케이크+크림+베리) |
| `mine_structure:unicorn_cupcake_tower` | static | 컵케이크 타워(3단+컵케이크 다수+체리) |
| `mine_structure:unicorn_water_dispenser` | variant_light | 정수기(물통 glow on/off+탭) |
| `mine_structure:unicorn_dish_rack` | static | 식기건조대(거치대+세운 접시+컵) |
| `mine_structure:unicorn_bakery_oven` | script_give | 제빵오븐(우클릭→쿠키 지급, 창 얼굴+굴뚝) |
| `mine_structure:unicorn_cafe_bar` | static | 카페 바(카운터+상판+jar/사인+무지개 하트) |

## 메커니즘

- **script_give**(coffee_machine→`unicorn_rainbow_drink`, bakery_oven→`unicorn_cookie`): `scripts/main.js` `COFFEE_MACHINE_ID`/`BAKERY_OVEN_ID` + `giveItem`(toaster 패턴).
- **variant_light**(blender/water_dispenser): `glow` 본 우클릭 토글.
- **static**: 장식 전용.

## Add-on / 검증

- 생성: `blockbench/gen_kitchen_cafe.py`. `KIDS` 등록, 검증 PASS. **8종 전부 Blockbench 렌더로 개별 확인**.

## 테스트

```
/summon mine_structure:unicorn_coffee_machine   (외 7종)
```
커피머신/오븐=우클릭 지급, 믹서기/정수기=불빛 토글, 나머지=장식 배치(인게임 대기).
