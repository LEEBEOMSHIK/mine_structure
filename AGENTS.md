# AGENTS.md — mine_structure

이 저장소는 Codex와 Claude가 함께 Minecraft Bedrock 패키지(add-on), 리소스팩, 행동팩, Blockbench 모델을 만드는 작업 공간입니다.

## 필수 시작 절차

1. 먼저 `PROJECTS.md`를 읽고 현재 활성 프로젝트를 확인합니다.
2. 루트 `docs/agent-guides/README.md`를 읽고 공통 Bedrock/Blockbench 지침을 확인합니다.
3. 작업 대상 프로젝트의 `README.md`를 읽어 현재 상태와 다음 작업을 확인합니다.
4. 작업 대상 프로젝트의 `PROJECT_CONTEXT.md`를 읽고 프로젝트별 현재 컨텍스트와 시작 순서를 확인합니다.
5. 루트 지침보다 프로젝트별 지침이 더 구체적이면 프로젝트별 지침을 우선합니다.

## 프로젝트 구조

```text
projects/<project_id>/
├─ README.md
├─ PROJECT_CONTEXT.md
└─ project-specific files
```

현재 활성 프로젝트 목록과 우선순위는 `PROJECTS.md`가 단일 기준입니다.

## Codex 작업 원칙

- 파일 이동, 생성, 수정 전 대상 프로젝트를 명확히 확인합니다.
- 여러 프로젝트가 생겨도 루트에는 공통 문서만 두고, 개별 패키지 세부 내용은 `projects/<project_id>/` 아래에 둡니다.
- 공통 작업 환경, 핵심 원칙, Blockbench/MCP 주의사항은 루트 `docs/agent-guides/` 아래의 작은 문서로 분리해 참조합니다.
- 프로젝트 폴더에는 해당 프로젝트만의 상태, 스펙, 산출물, 프로젝트별 예외 사항만 둡니다.
- Minecraft Bedrock 관련 작업에서는 resource pack, behavior pack, geometry, animation, texture, sound의 책임을 문서와 폴더에서 분리합니다.
- 기존 문서에 기록된 좌표, UV, 애니메이션, Blockbench/MCP 주의사항을 임의로 무시하지 않습니다.
- 변경 후에는 `rg --files` 또는 동등한 명령으로 구조를 확인하고, 관련 문서 링크가 새 경로와 맞는지 점검합니다.

## 작업 규칙

### 콘텐츠 작업 워크플로 — 서브에이전트 파이프라인
- 콘텐츠 제작은 단계별 서브에이전트(`.codex/agents/`)를 이어서 수행합니다. 표준 흐름:
  - 가구/의상: `furniture-modeler → addon-wiring → validator → blockbench-reviewer →`(문제 시 수정 루프)`→ packager → docs-writer → committer`
  - 스킨: `skin-artist → blockbench-reviewer → packager → docs-writer → committer`
- **제작(가구/스킨/의상 생성·수정)을 마치면 커밋 전에 반드시 `quality-check` 스킬을 거칩니다**(검증+종별 시각검수+빌드+문서+커밋이 묶여 있음). 기존 결과물 점검도 같은 스킬을 씁니다.
- **검수는 종(항목)마다 개별**로 하고, 문제가 있으면 제작 에이전트로 돌아가 고친 뒤 재검수합니다. **재수정(redo)은 한 항목당 최대 2회**까지만 하고, 그 후 남는 경미한 문제는 보고만 하고 통과시킵니다.
- 상세는 `docs/agent-guides/agent-workflow.md`를 따릅니다.

### 커밋 메시지 — Conventional Commits
- 형식은 `type(scope): subject` 를 따릅니다. (예: `feat(furniture): 주방/카페 8종 추가`)
- `type`: `feat`(기능 추가), `fix`(버그/오류 수정), `docs`(문서), `chore`(설정/잡무), `refactor`(리팩터링), `polish`(외형·품질 다듬기), `test`(검증) 등.
- `scope`: 작업 영역(프로젝트·모듈)을 소문자로 적습니다. 예: `furniture`, `skins`, `wings`, `skirt`, `repo`.
- `subject`: 한 줄 요약(한국어 가능, 끝에 마침표 없이).
- 본문·푸터는 기존 규칙을 유지합니다(필요 시 설명 + `Co-Authored-By`).

### 에이전트 정의 — AI 모델별 폴더
- 에이전트(agent) 정의는 각 AI 모델별 폴더에 둡니다.
  - Claude: `.claude/agents/`
  - Codex: `.codex/agents/`
  - 그 외 모델도 `<model>/agents/` 규칙을 따릅니다.
- 같은 역할의 에이전트라도 모델별 폴더에 각각 정의(또는 링크)합니다.

### 스킬 정의 — AI 모델별 폴더
- 스킬(skill) 정의는 각 AI 모델별 폴더에 둡니다.
  - Claude: `.claude/skills/`
  - Codex: `.codex/skills/`
  - 그 외 모델도 `<model>/skills/` 규칙을 따릅니다.

### 중간 산출물 — `_workspace/`
- 미리보기 모델, 임시 텍스처, 스크래치 등 **중간 산출물은 `_workspace/`에 둡니다**(루트 또는 프로젝트별 `_workspace/`).
- 정식 산출물(스킨/모델/리소스팩 등)과 섞지 않으며, `_workspace/`는 버전 관리에서 제외합니다.
