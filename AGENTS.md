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
