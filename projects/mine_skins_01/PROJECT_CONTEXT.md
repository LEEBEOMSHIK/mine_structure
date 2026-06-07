# PROJECT_CONTEXT.md — mine_skins_01

Minecraft Bedrock **스킨팩** 프로젝트. 파스텔 유니콘 소녀 캐릭터 스킨을 64×64 텍스처로
절차 생성한다(가구 add-on `mine_furniture_01`과 별개).

## 세션 시작 순서

1. `README.md`에서 스킨 목록·구조·빌드 방법 확인.
2. 참고 이미지 `../../game/mine_reference/001.png` 확인.
3. 스킨 수정은 `gen_skins.py`의 `PALETTES`/`draw_*` 함수에서 한다(직접 PNG 편집 금지 — 재생성하면 덮어씀).

## 현재 상태

- (2026-06-08) 신규 프로젝트. 스킨 2종 생성: `unicorn_pastel`(라벤더/분홍), `unicorn_pastel_mint`(민트/하늘).
  - `gen_skins.py`: classic 64×64 UV(`FACES` 맵) 기반으로 머리(머리카락+얼굴+눈/볼/입+hat 뿔 자국),
    몸(보디스+하트+무지개 스커트), 팔(퍼프 소매+손), 다리(무지개 스타킹+신발)를 그림.
  - 정면 합성 미리보기(`front_preview`)로 캐릭터 형태 확인 완료.
  - `build_skinpack.py`로 `.mcpack` 빌드(preview 제외). geometry는 `geometry.humanoid.custom`.
- 인게임 적용/검증은 대기. 솟은 뿔·꼬리·날개는 커스텀 geometry 필요(현재 평면 뿔 자국만).

## 메모

- 스킨 UV는 classic(4px 팔). slim(3px)으로 바꾸려면 `geometry.humanoid.customSlim` + 팔 폭 3 보정 필요.
- 색 팔레트만 바꿔 변형 스킨을 쉽게 추가할 수 있다(`PALETTES`에 항목 추가 → `SKIN_TITLES`도).
