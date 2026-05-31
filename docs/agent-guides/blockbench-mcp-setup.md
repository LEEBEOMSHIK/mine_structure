# Blockbench MCP Setup

Blockbench MCP는 Blockbench 데스크톱 앱을 열어 둔 상태에서 Codex/Claude가 모델, UV, 텍스처, 애니메이션을 원격 제어하기 위한 서버다.

## Repository Reference

- 설정 예시: `mcp/blockbench.config.example.toml`
- 공통 작업 규칙: `docs/agent-guides/blockbench-mcp-rules.md`

## Codex 전역 등록

`C:\Users\User\.codex\config.toml`에 아래 설정을 추가한다.

```toml
[mcp_servers.blockbench]
command = "cmd"
args = ["/c", "npx", "-y", "mcp-remote", "http://localhost:3000/bb-mcp"]
enabled = true
startup_timeout_sec = 20
tool_timeout_sec = 120
```

전역 config를 수정한 뒤 Codex 세션을 재시작해야 MCP tool 목록에 Blockbench 서버가 나타난다.

## Blockbench 쪽 준비

1. Blockbench 데스크톱 앱을 실행한다.
2. MCP 플러그인 또는 MCP 서버가 `http://localhost:3000/bb-mcp`에서 대기하도록 실행한다.
3. 현재 프로젝트 파일 `furniture`를 열어 둔다.
4. Codex/Claude에서 Blockbench MCP tool이 보이는지 확인한다.

## Export 원칙

`unicorn_toilet`의 resource pack 연결 대상은 아래 경로다.

- Geometry: `projects/mine_furniture_01/addon/resource_pack/models/entity/unicorn_toilet.geo.json`
- Texture: `projects/mine_furniture_01/addon/resource_pack/textures/entity/unicorn_toilet/unicorn_toilet_atlas.png`
- Animation: `projects/mine_furniture_01/addon/resource_pack/animations/unicorn_toilet.animation.json`

실제 export 후에는 `projects/mine_furniture_01/content/furniture/unicorn_toilet.md`의 체크리스트와 비교한다.
