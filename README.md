# mine_structure

Minecraft Bedrock 패키지(add-on), 리소스팩, 행동팩, Blockbench 모델을 여러 개 관리하기 위한 작업 저장소입니다.

## 시작 지점

Codex와 Claude는 루트의 `PROJECTS.md`를 먼저 읽고 현재 진행 중인 프로젝트와 다음 작업을 확인합니다.

- 프로젝트 인덱스: `PROJECTS.md`
- Codex 공통 지침: `AGENTS.md`
- Claude 공통 지침: `CLAUDE.md`
- 공통 Bedrock/Blockbench 세부 지침: `docs/agent-guides/README.md`
- MCP 설정 예시: `mcp/README.md`
- 개별 프로젝트: `projects/<project_id>/`

## 현재 활성 프로젝트

- `projects/mine_furniture_01/` — 여러 가구와 무기를 묶는 Minecraft Bedrock add-on. 첫 등록 콘텐츠는 `mine_structure:unicorn_toilet`

## 저장소 구조

```text
mine_structure/
├─ AGENTS.md
├─ CLAUDE.md
├─ docs/
│  └─ agent-guides/
├─ mcp/
├─ PROJECTS.md
├─ README.md
└─ projects/
   └─ mine_furniture_01/
      ├─ README.md
      ├─ PROJECT_CONTEXT.md
      ├─ addon/
      ├─ content/
      ├─ blockbench/
      └─ unicorn_toilet_spec.md
```

## 작업 원칙

1. 새 세션을 시작하면 `PROJECTS.md`를 먼저 확인합니다.
2. 루트 `docs/agent-guides/README.md`에서 공통 Bedrock/Blockbench 지침을 확인합니다.
3. 개별 프로젝트 작업을 시작하기 전에 해당 프로젝트 폴더의 `README.md`와 `PROJECT_CONTEXT.md`를 확인합니다.
4. 새 패키지를 만들 때는 `projects/<project_id>/` 아래에 격리하고, `PROJECTS.md`에 상태와 다음 작업을 추가합니다.
5. 루트 문서는 저장소 공통 규칙만 담고, 모델/애니메이션/애드온 세부 내용은 각 프로젝트 문서에 둡니다.
