# mine_skins_01 — 파스텔 유니콘 캐릭터 스킨팩

Minecraft Bedrock **스킨팩**(skin_pack) 프로젝트. 가구 add-on(`mine_furniture_01`)과 별개로,
캐릭터 플레이어 스킨을 64×64 텍스처로 절차 생성한다.

참고 이미지: `../../game/mine_reference/001.png`(파스텔 유니콘 소녀 — 라벤더 머리, 무지개
드레스, 별·하트, 뿔). 64×64 classic 휴머노이드 UV(4px 팔) 위에 그린 **근사본**이다.

## 현재 스킨

| 파일 | 이름 | 설명 |
|------|------|------|
| `skin_pack/unicorn_pastel.png` | Pastel Unicorn Dress | 라벤더 머리 + 흰 원피스 + 무지개 프릴 스커트 |
| `skin_pack/unicorn_pastel_pink.png` | Pink Unicorn Dress | 분홍 머리 변형 |

상세 스펙(파스텔 유니콘 원피스):
- **머리**: 연보라/라벤더 머리(앞머리+옆머리 픽셀), 이마에 **작은 금색 뿔 자국**(평면), 작고 귀여운 얼굴 + 보라 눈.
- **상의**: 흰 원피스 + 가슴 **작은 무지개 아치 + 구름** 모티브 + 연보라 목/가슴 라인.
- **소매**: 흰색 + 끝 라벤더 프릴(소매 overlay 돌출) + 팔에 노란 별 1개.
- **스커트**: 하단 **파스텔 무지개 프릴**(위→아래: 핑크→연노랑→민트→베이비블루→라벤더), 몸통 하단 + 다리 위쪽으로 이어지고 jacket overlay로 프릴 한 겹 돌출.
- **등**: 분홍 **하트 + 세로 무지개 리본** + 무지개 프릴 유지.
- **다리**: 피부톤 다리 + 무릎 아래 흰 양말(하트/별) + 라벤더 신발.
- 색 팔레트: #FFF8FF / #CDB4F6 / #F7A7C8 / #A9D8FF / #B9F2D0 / #FFE99A / #A987D9 / #FFD75A / #FFDCC8.
- base + overlay 레이어(hat/jacket/소매/바지) 활용. 정면/후면/좌우 미리보기는 `preview_<sid>_{front,back,side}.png`.

## 구조

```
projects/mine_skins_01/
├─ gen_skins.py          # 64x64 스킨 PNG + 정면 미리보기 + manifest/skins.json/texts 생성
├─ build_skinpack.py     # skin_pack/ → dist/ .mcpack (preview 제외)
└─ skin_pack/
   ├─ manifest.json      # format_version 2, type skin_pack
   ├─ skins.json         # geometry.humanoid.custom, type free
   ├─ texts/{en_US,ko_KR}.lang
   ├─ unicorn_pastel.png / unicorn_pastel_pink.png   (64x64 스킨)
   └─ preview_<sid>_{front,back,side}.png      # 미리보기(확인용, 팩에는 미포함)
```

## 빌드 / 적용

```
python gen_skins.py        # 스킨/미리보기/메타 생성
python build_skinpack.py   # dist/mine_skins_01-<stamp>/unicorn_pastel_girls.mcpack
```
`.mcpack`을 기기에서 열거나, 압축을 풀어 PC/모바일의 `skin_packs/`에 넣으면 프로필 →
스킨 선택에서 고를 수 있다.

## 다음 작업

- 인게임에서 스킨 적용·정면/측면 확인. 색/얼굴/드레스 비율 보정.
- (옵션) 솟은 뿔·꼬리·날개가 필요하면 커스텀 geometry(별도 geo + skins.json geometry 교체)로 확장.
- (옵션) 참고 이미지의 추가 디자인(스커트 프릴, 신발 리본 등) 디테일 보강.
