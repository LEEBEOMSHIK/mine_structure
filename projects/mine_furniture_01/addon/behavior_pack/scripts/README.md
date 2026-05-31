# Scripts

Minecraft Bedrock Script API를 사용할 경우 스크립트를 이 폴더에 둔다.

## 현재 스크립트

- `main.js`

## 동작

- `mine_structure:unicorn_dining_table` 상호작용:
  - 플레이어 주 손의 아이템 1개를 복제해 식탁 위 위치에 `dimension.spawnItem`으로 생성한다.
  - 플레이어 주 손 스택은 1개 줄인다.
  - 빈 손이면 아무 동작도 하지 않는다.

`unicorn_toilet`의 flush 트리거는 behavior entity의 `minecraft:interact` + `queue_command` 방식이다.
`unicorn_chair`의 착석은 behavior entity의 `minecraft:rideable` 방식이다.
