# mine_skins_01 — 파스텔 유니콘 캐릭터 스킨팩

Minecraft Bedrock **스킨팩**(skin_pack) 프로젝트. 가구 add-on(`mine_furniture_01`)과 별개로,
캐릭터 플레이어 스킨을 64×64 텍스처로 절차 생성한다.

참고 이미지: `../../game/mine_reference/001.png`(파스텔 유니콘 소녀 — 라벤더 머리, 무지개
드레스, 별·하트, 뿔). 64×64 classic 휴머노이드 UV(4px 팔) 위에 그린 **근사본**이다.

## 현재 스킨

| 파일 | 이름 | 설명 |
|------|------|------|
| `skin_pack/unicorn_pastel.png` | Pastel Unicorn Girl | 라벤더 머리 + 분홍 드레스 + 무지개 스커트/스타킹 + 하트 |
| `skin_pack/unicorn_pastel_mint.png` | Mint Unicorn Girl | 민트 머리 + 하늘색 드레스 변형 |

- 얼굴: 큰 보라/청록 눈 + 볼홍조 + 앞머리, hat 레이어에 작은 금색 뿔 자국(평면 — 솟은 뿔은
  기본 모델 한계로 생략).
- 몸/팔/다리: 분홍 보디스 + 가슴 하트 + 무지개 스커트, 퍼프 소매 + 손, 무지개 스타킹 + 신발.

## 구조

```
projects/mine_skins_01/
├─ gen_skins.py          # 64x64 스킨 PNG + 정면 미리보기 + manifest/skins.json/texts 생성
├─ build_skinpack.py     # skin_pack/ → dist/ .mcpack (preview 제외)
└─ skin_pack/
   ├─ manifest.json      # format_version 2, type skin_pack
   ├─ skins.json         # geometry.humanoid.custom, type free
   ├─ texts/{en_US,ko_KR}.lang
   ├─ unicorn_pastel.png / unicorn_pastel_mint.png   (64x64 스킨)
   └─ preview_*.png      # 정면 합성 미리보기(확인용, 팩에는 미포함)
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
