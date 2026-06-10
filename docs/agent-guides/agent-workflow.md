# Agent Workflow — 콘텐츠 제작 파이프라인

이 저장소의 콘텐츠 작업은 **세분화 서브에이전트**를 단계별로 이어서 수행한다. 에이전트 정의는 모델별 폴더(`.claude/agents/`, `.codex/agents/`)에 있고, 품질 단계는 `quality-check` 스킬(`.claude/skills/`, `.codex/skills/`)로 묶여 있다.

## 에이전트 카탈로그

| 에이전트 | 단계 | 역할 |
|----------|------|------|
| `furniture-modeler` | 제작 | Blockbench 모델(geo/atlas/bbmodel) 생성기 작성 |
| `addon-wiring` | 제작 | behavior/resource 와이어링 + mechanic + main.js + KIDS 등록 |
| `skin-artist` | 제작 | mine_skins_01 64×64 스킨 픽셀 아트 + 미리보기 |
| `validator` | 검수 | validate/audit/node check (데이터 정합성) |
| `blockbench-reviewer` | 검수 | Blockbench 종별 렌더 시각 검수 |
| `packager` | 마무리 | embed_animations + 빌드(mcaddon/mcpack) |
| `docs-writer` | 마무리 | README/content/PROJECT_CONTEXT/PROJECTS 갱신 |
| `committer` | 마무리 | Conventional Commits 커밋 |

## 표준 파이프라인

### A. 신규 가구/의상 (mine_furniture_01)
```
furniture-modeler → addon-wiring → validator → blockbench-reviewer
        → (문제 있으면 modeler/wiring로 돌아가 수정 후 validator·reviewer 재실행)
        → packager → docs-writer → committer
```

### B. 스킨 (mine_skins_01)
```
skin-artist → blockbench-reviewer(전신 미리보기) → (수정 루프)
        → packager(skinpack) → docs-writer → committer
```

### C. 품질 점검(기존 결과물) — `quality-check` 스킬
```
validator → blockbench-reviewer(종별) → 판정 체크리스트
        → (문제 → modeler/wiring/skin-artist 수정 → 재검수)
        → packager → docs-writer → committer
```

## 단계 간 인계 규칙

- 각 에이전트는 **자기 영역만** 수정하고, 끝나면 다음 에이전트가 쓸 정보(sid/bone/mechanic/문제목록)를 요약 보고한다.
- **검수는 종(항목)마다 개별**로 한다. 배치를 한꺼번에 통과시키지 않는다(텐트 같은 누락 방지).
- 문제가 나오면 제작 에이전트로 돌아가 고치고 **검수를 다시** 거친다(OK까지 루프).

## 공통 원칙

- 중간 산출물(미리보기·임시·스크래치)은 `_workspace/`에 둔다(버전 관리 제외).
- 커밋 메시지는 Conventional Commits `type(scope): subject`.
- 새 mechanic을 추가하면 `validate`에 분기를 반드시 추가한다.
- 인게임 실행이 불가하므로 스크립트/탈것/attachable·armor 의상은 "버전 의존 → 인게임 검증 필요"로 솔직히 남긴다.
- 에이전트/스킬 정의는 모델별 폴더에 각각 둔다(`.claude/...`, `.codex/...`).
