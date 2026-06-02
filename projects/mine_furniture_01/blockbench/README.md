# Blockbench Sources

Blockbench 원본 모델 파일을 이 폴더에 보관한다.

## Source files

- `furniture.bbmodel` — 가구 5종 원본. 무기는 포함하지 않는다.
- `unicorn_horn_blade.bbmodel` — 유니콘 뿔 검 전용 원본. 칼날 텍스처 수정은 이 파일에서만 진행한다. 무기 큐브 좌표는 원점 기준(x -2.5..2.5)으로 보정되어 Blockbench에서 바로 보인다.

내보낸 Bedrock 산출물은 `../addon/resource_pack/` 아래에 둔다.

## 주의

- `furniture.bbmodel` 저장 후 가구 텍스처가 섞이면 `fix_bbmodel_face_textures.py`를 실행한다.
- `unicorn_horn_blade`는 별도 프로젝트라 `furniture.bbmodel`에 다시 추가하지 않는다.
