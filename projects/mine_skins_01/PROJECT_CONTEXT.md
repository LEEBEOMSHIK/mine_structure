# PROJECT_CONTEXT.md — mine_skins_01

Minecraft Bedrock **스킨팩** 프로젝트. 파스텔 유니콘 소녀 캐릭터 스킨을 64×64 텍스처로
절차 생성한다(가구 add-on `mine_furniture_01`과 별개).

## 세션 시작 순서

1. `README.md`에서 스킨 목록·구조·빌드 방법 확인.
2. 참고 이미지 `../../game/mine_reference/001.png` 확인.
3. 스킨 수정은 `gen_skins.py`의 `PALETTES`/`draw_*` 함수에서 한다(직접 PNG 편집 금지 — 재생성하면 덮어씀).

## 현재 상태

- (2026-06-08) 신규 프로젝트. 이후 상세 스펙대로 **파스텔 유니콘 원피스** 스킨으로 전면 재작성.
  스킨 2종: `unicorn_pastel`(라벤더 머리), `unicorn_pastel_pink`(분홍 머리 변형).
  - `gen_skins.py`: classic 64×64 UV(`FACES`에 base + hat/jacket/소매/바지 overlay 포함) 기반.
    머리(라벤더+작은 얼굴+금뿔 자국), 흰 원피스 상의(가슴 무지개 아치+구름), 흰 소매(라벤더 프릴 끝동+노란 별),
    하단 무지개 프릴 스커트(핑크→연노랑→민트→블루→라벤더, jacket overlay로 프릴 돌출), 등(하트+세로 무지개 리본),
    피부 다리+흰 양말(하트/별)+라벤더 신발.
  - 색 팔레트 스펙 고정(#FFF8FF 등). 미리보기 `preview_<sid>_{front,back,side}.png` 생성, Blockbench 3D(overlay 포함)로 확인.
  - 퀄리티 보강: 가슴 무지개를 또렷한 **반원 아치(핑크/노랑/민트/블루) + 구름**으로(`rainbow_arch` math 반원), 스커트를 **명암 프릴**(`frill`: 밝은 위+본색+scallop 그림자 하단)로 다단 처리하고 jacket/소매/바지 overlay로 프릴 돌출(게임 overlay 0.5 inflate). 다리/신발 명암 추가.
  - `build_skinpack.py`로 `.mcpack` 빌드(preview 제외). geometry `geometry.humanoid.custom`. 최신: `../../dist/mine_skins_01-20260608-210830/unicorn_pastel_girls.mcpack`
- (2026-06-08) 머리/얼굴을 참고(001.png)에 맞게 보강: **큰 눈**(진보라 윗꺼풀+흰 하이라이트+보라), **M자 앞머리**, 어깨로 길게 내려오는 **옆머리**(body 양옆 라벤더), 정수리 **금뿔**(크게), 머리 명암 줄(`hair_shade`), 정수리 하트 클립.
- (2026-06-08) 상의를 **어깨 드러난(off-shoulder)** 흰 원피스로 수정(어깨/가슴 위 피부 + 퍼프 소매). 입체 A라인 스커트는 스킨(텍스처)으론 불가 → `mine_furniture_01`의 입는 의상 `unicorn_rainbow_skirt`(attachable, body 본 하위 5단 콘)로 별도 제작. 스킨+의상 세트로 착용.
- 인게임 적용/검증은 대기. 솟은 뿔·꼬리·날개는 커스텀 geometry 필요(현재 평면 금뿔 자국).

## 메모

- 스킨 UV는 classic(4px 팔). slim(3px)으로 바꾸려면 `geometry.humanoid.customSlim` + 팔 폭 3 보정 필요.
- 색 팔레트만 바꿔 변형 스킨을 쉽게 추가할 수 있다(`PALETTES`에 항목 추가 → `SKIN_TITLES`도).
