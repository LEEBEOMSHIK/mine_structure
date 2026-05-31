# 작업 환경 / 도구

이 저장소의 Bedrock 모델링 프로젝트는 기본적으로 **Blockbench + MCP**로 Minecraft Bedrock 스타일 오브젝트를 제작한다.

## 기본 작업 대상

- 프로젝트별 현재 작업물과 모델 파일명은 `PROJECTS.md`와 해당 프로젝트 `README.md`를 따른다.
- 애니메이션이 필요한 모델은 **Bedrock Entity (`bedrock`)** 포맷을 우선한다.
- 정적 블록 모델로 충분한 경우에만 프로젝트 문서에 명시하고 `bedrock_block`을 사용한다.

## 도구

- **Blockbench** 데스크톱 앱
- **blockbench MCP 서버**
  - 기본 포트: `3000`
  - 원격 제어로 모델, UV, 텍스처, 애니메이션을 수정한다.
  - Codex 등록 예시는 `mcp/blockbench.config.example.toml`을 따른다.

## 좌표계

- 16단위 블록 기준
- 중심: `x=8`
- 바닥: `y=0`
- 정면: 낮은 `z`
- 탱크/뒤쪽: 높은 `z`
