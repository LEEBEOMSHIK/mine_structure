---
name: quality-check
description: 만들어진 가구/스킨/의상 결과물의 품질을 검증·시각검수하고 최대한 끌어올리는 워크플로. 데이터 검증 + Blockbench 종별 렌더 검수로 문제를 찾아 수정 에이전트로 고치고 OK까지 재검수한 뒤 빌드·문서·커밋. "퀄리티 확인", "품질 점검", "검수", "결과물 확인", "QA" 등에 사용.
---

# quality-check — 결과물 품질 확인 & 향상 워크플로

만든 콘텐츠(가구/스킨/의상)의 품질을 **검증 → 시각검수 → 수정 → 재검수**로 끌어올린다. 각 단계는 세분화 서브에이전트를 활용한다. **종(항목)마다 개별로** 확인해 누락(과거 텐트 케이스)을 막는다.

## 입력 파악
- 무엇을 확인할지(특정 sid / 배치 / 프로젝트 전체)와 어느 프로젝트인지(`mine_furniture_01` 가구·의상 / `mine_skins_01` 스킨) 먼저 정한다.

## 워크플로

1. **데이터 검증 — `validator` 에이전트**
   - `python validate_unicorn_toilet_resources.py` (PASS/FAIL), `python blockbench/audit_gaps.py`(떠있는 큐브), `node --check addon/behavior_pack/scripts/main.js`.
   - FAIL/의심 항목을 "무엇·왜·어느 파일"로 정리받는다.

2. **시각 검수 — `blockbench-reviewer` 에이전트**
   - 대상 `.bbmodel`을 **하나씩** Blockbench로 띄워 렌더/스크린샷 확인(스킨은 `gen_preview.py`로 전신).
   - 토글/애니가 있으면 양극단 포즈도 확인.

3. **판정 — 아래 체크리스트로 OK/문제 분류**
   - [ ] 떠있는/어긋난 큐브 없음(회전 파츠 false positive 구분)
   - [ ] 실루엣이 의도대로 읽힘(예: 텐트=매끄러운 ∧, 스커트=A라인, 날개=나비)
   - [ ] 비율 자연스러움(허리/손 라인 등 기준 일치)
   - [ ] 파스텔 색 일관 + 약간의 명암 대비(너무 흐리게 날아가지 않음)
   - [ ] 텍스처 면 매핑 정확(얼굴 방향, eyespot, 무지개 등)
   - [ ] mechanic 구조 정상(variant=glow/blades bone, rideable=좌석, script=main.js 핸들러+KIDS 등록)
   - [ ] `validate` PASS

4. **수정 루프 (OK 될 때까지 반복)**
   - 형태/텍스처 문제 → `furniture-modeler`(가구) 또는 `skin-artist`(스킨)
   - 와이어링/면 매핑/등록 문제 → `addon-wiring`
   - 수정 후 **1~3을 다시** 돌려 재검수한다.

5. **마무리**
   - `packager` → embed_animations + 빌드, 패키지 파일 포함 확인.
   - `docs-writer` → README/content/PROJECT_CONTEXT/PROJECTS 갱신(인게임 미검증 명시).
   - `committer` → Conventional Commits(`fix(scope): ...`/`polish(scope): ...`) 커밋, 무관 bbmodel 노이즈 제외.

## 원칙
- **종별 개별 확인**을 건너뛰지 않는다(배치 일괄 통과 금지).
- 중간 산출물(미리보기 등)은 `_workspace/`에 둔다.
- 인게임 실행이 불가하므로, 스크립트/탈것/attachable·armor 의상은 "버전 의존 → 인게임 검증 필요"로 솔직히 보고한다.
- Blockbench MCP가 "Session expired"면 사용자에게 재연결을 요청한다.
