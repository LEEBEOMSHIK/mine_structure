# CLAUDE.md — mine_structure

이 저장소는 Minecraft Bedrock 버전 패키지(add-on), 리소스팩, 행동팩, Blockbench 모델을 여러 프로젝트로 관리하는 작업 공간이다.

## 세션 시작 순서

1. 루트 `PROJECTS.md`를 먼저 읽고 현재 활성 프로젝트를 확인한다.
2. 루트 `docs/agent-guides/README.md`를 읽고 공통 Bedrock/Blockbench 지침을 확인한다.
3. 작업 대상 프로젝트 폴더의 `README.md`를 읽어 진행 상태와 다음 작업을 확인한다.
4. 작업 대상 프로젝트 폴더의 `PROJECT_CONTEXT.md`를 읽고 프로젝트별 현재 컨텍스트와 시작 순서를 확인한다.
5. 루트 지침과 프로젝트 지침이 충돌하면 더 구체적인 프로젝트 지침을 우선한다.

## 공통 구조

```text
projects/<project_id>/
├─ README.md          # 프로젝트 진행 현황, 다음 작업
├─ PROJECT_CONTEXT.md # 프로젝트별 현재 컨텍스트, 시작 순서
└─ ...                # 모델 스펙, 리소스팩, 행동팩, 산출물
```

## 현재 프로젝트 인덱스

- 공통 프로젝트 관리 문서: `PROJECTS.md`
- 공통 Bedrock/Blockbench 지침 인덱스: `docs/agent-guides/README.md`
- 현재 활성 프로젝트: `projects/mine_furniture_01/`

## 공통 작업 원칙

- 여러 패키지를 동시에 다룰 수 있으므로, 파일을 만들거나 수정하기 전에 항상 대상 프로젝트 경로를 명확히 한다.
- 개별 프로젝트의 모델링 세부 지식은 루트 문서에 중복하지 않는다.
- 새 프로젝트를 추가하면 `PROJECTS.md`에 상태, 목적, 다음 작업, 주요 문서 경로를 함께 기록한다.
- 공통 작업 환경, 핵심 원칙, MCP 주의사항은 루트 `docs/agent-guides/` 아래의 작은 문서로 분리한다.
- 프로젝트별 문서는 해당 프로젝트만의 상태, 스펙, 다음 작업을 담는다.
- Bedrock add-on 산출물은 가능하면 프로젝트 내부에서 `resource_pack/`, `behavior_pack/`, `blockbench/`, `docs/`처럼 목적별로 분리한다.
- 기존 산출물을 새로 만들기보다 현재 파일과 문서를 기준으로 이어서 작업한다.

## 작업 규칙

### 커밋 메시지 — Conventional Commits
- 형식은 `type(scope): subject` 를 따른다. (예: `feat(furniture): 주방/카페 8종 추가`)
- `type`: `feat`(기능 추가), `fix`(버그/오류 수정), `docs`(문서), `chore`(설정/잡무), `refactor`(리팩터링), `polish`(외형·품질 다듬기), `test`(검증) 등.
- `scope`: 작업 영역(프로젝트·모듈)을 소문자로. 예: `furniture`, `skins`, `wings`, `skirt`, `repo`.
- `subject`: 한 줄 요약(한국어 가능, 끝에 마침표 없이).
- 본문·푸터는 기존 규칙을 유지한다(필요 시 설명 + `Co-Authored-By`).

### 에이전트 정의 — AI 모델별 폴더
- 에이전트(agent) 정의는 각 AI 모델별 폴더에 둔다.
  - Claude: `.claude/agents/`
  - Codex: `.codex/agents/`
  - 그 외 모델도 `<model>/agents/` 규칙을 따른다.
- 같은 역할의 에이전트라도 모델별 폴더에 각각 정의(또는 링크)한다.

### 스킬 정의 — AI 모델별 폴더
- 스킬(skill) 정의는 각 AI 모델별 폴더에 둔다.
  - Claude: `.claude/skills/`
  - Codex: `.codex/skills/`
  - 그 외 모델도 `<model>/skills/` 규칙을 따른다.
