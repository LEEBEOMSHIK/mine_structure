# unicorn_toilet — 상세 스펙

Blockbench 프로젝트 `furniture` / 포맷 `bedrock`(Bedrock Entity) / 텍스처 해상도 64×64.
좌표: 16단위, 중심 x=8, 바닥 y=0, 정면=낮은 z(앞), 탱크=높은 z(뒤).

## 1. 파츠 구조 (그룹 / 큐브 / 텍스처셀)
```
unicorn_toilet
├─ base_plinth        plinth_bottom[2,0,2~14,1.5,14] / plinth_mid[3,1.5,3~13,3,13] / plinth_top[4,3,4~12,4,12]   (ceramic)
├─ toilet_body        body_column[5,4,4~11,9,11]                                                                  (ceramic)
├─ toilet_bowl        bowl_main[3,9,2~13,12,11] / bowl_front_lip[3.5,9.2,1~12.5,11.6,2] / bowl_under[4,8.4,2.5~12,9,10.5] (ceramic)
├─ toilet_seat        seat_ring[3,12,2~13,12.8,11](seat_pink) / seat_inner_line[4,12.81,3~12,12.9,10](accent)
├─ toilet_lid_open    lid_panel[3,12.9,1~13,13.5,10](seat_pink) / lid_inner_accent[4,13.5,2~12,13.62,9](accent)
│                     ※ 경첩 피벗(group.origin) = [8, 12.9, 10], 두께 0.6
├─ water_tank         tank_body[2.5,9,11~13.5,18,15](ceramic) / tank_front_deco[6,12.5,10.65~10,16.5,10.95](emblem)
├─ tank_lid           tank_lid_top[2,18,10.5~14,19,15.5](ceramic)
├─ unicorn_horn       horn_base / horn_mid / horn_tip  (모두 horn 셀, 12° 앞기울임)
├─ left_ear           left_ear(ear_white) + left_ear_inner(seat_pink)  (z+20° 바깥기울임)
├─ right_ear          right_ear(ear_white) + right_ear_inner(seat_pink) (z-20°)
├─ rainbow_mane       mane_p1..p5(앞줄) + mane_q1..q4(뒷줄)  핑크/보라/하늘/민트/노랑
├─ sparkle_decorations star_left / star_right (gold) / heart_side (heart) / sparkle_small (gold)
├─ side_rainbow_sticker sticker_pink(mp) / sticker_sky(ms) / sticker_mint(mm)  (탱크 우측면)
├─ water
│   ├─ bowl_water_grp   bowl_water[5.5,11,4~10.5,11.4,9.5](water)   pivot[8,11.2,6.7]
│   └─ tank_water_grp   tank_water[4,15.6,11.8~12,16,14.2](water)   pivot[8,15.8,13]
└─ flush_button        flush_button[10,19,11.5~12,19.8,13.5](seat_pink)  pivot[11,19.8,12.5]
```

## 2. 텍스처 아틀라스 (unicorn_toilet_atlas, 64×64, 16px 셀)
| 셀(px) | 이름 | 용도 | 베이스색 |
|--------|------|------|---------|
| (0,0)   | ceramic | 본체/볼/탱크/받침 | #EEF1F7 |
| (16,0)  | seat_pink | 시트/뚜껑/버튼/귀안쪽 | #F2A6CC |
| (32,0)  | accent_lavender | 액센트 라인 | #D9C5F2 |
| (48,0)  | ear_white | 귀 바깥 | #EFE9FB |
| (0,16)  | unicorn_horn | 뿔(사선 나선 줄무늬) | 크림#FFF7E6 + 핑크/보라/하늘 |
| (16,16) | mane_pink | 갈기 | #F2A0C4 |
| (32,16) | mane_purple | 갈기 | #BFA0EC |
| (48,16) | mane_sky | 갈기 | #A6D0F2 |
| (0,32)  | mane_mint | 갈기(채도↓) | #CFEEDD |
| (16,32) | mane_yellow | 갈기 | #F2E59E |
| (32,32) | gold_sparkle | 별/반짝이 | #FBD96A |
| (48,32) | heart_pink | 하트 | #FF96BC |
| (0,48)  | emblem | 탱크앞 별 엠블럼 | 크림+골드별+핑크하트 |
| (16,48) | water | 물 표면 | #BDE8F5 |

- 각 셀은 픽셀 음영: 상단 2px 하이라이트 / 하단 3px 그림자 / 좌1px 라이트·우1px 다크 / 스페클.
- **면 UV = `[px, py, px+16, py+16]`, `autouv=0`** (셀 풀범위 매핑 → 음영 표시됨).

## 3. 애니메이션
- `lid_open` (hold, 0.55s): `toilet_lid_open` rotation x **0 → 88**
- `lid_close` (hold, 0.55s): `toilet_lid_open` rotation x **88 → 0**
- `flush` (once, 1.8s):
  - `flush_button` position: t0(0) → t0.1(y -0.7) → t0.35(0)
  - `tank_water_grp` position: t0.1(0) → t0.5(y -3.4) → t1.0(y -3.4) → t1.8(0)
  - `bowl_water_grp` position: t0.2(0) → t0.65(y -2.3) → t1.1(y -2.3) → t1.8(0)
  - `bowl_water_grp` rotation y(소용돌이): t0.2(0) → t0.65(200) → t1.1(360) → t1.8(360)
  - `effects` sound: t0.12 effect `flush` (※ .ogg 미연결)

## 4. 검증된 클리어런스 / 수치
- 뚜껑 열림(88°) 최대 z = **10.6** < 탱크 앞면 z=11 → 겹침 없음(여유 0.4).
- 회전 부호: 경첩(뒤) 기준 **+ = 위로 열림**.
- 단일 축 회전만 사용(Bedrock OK).

## 5. 재현/수정용 메모
- 텍스처 수정: 64×64 캔버스에 13셀 재그리기 후 기존 atlas에 `atlas.fromDataURL(...)` (uuid 유지 → 면 재연결 불필요).
- 색 추가: 빈 셀 (32,48)/(48,48) 사용. UV를 해당 셀로.
- 애니 키프레임 수정: 해당 Animation `select()` 후 BoneAnimator 키프레임 `data_points[0].x/y/z` 변경.
- 스크린샷보다 `risky_eval`로 좌표/UV/키프레임 직접 읽어 검증 권장.
