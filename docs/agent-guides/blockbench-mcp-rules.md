# Blockbench/MCP 작업 시 반드시 지킬 주의점

이 문서는 Bedrock 모델링 작업에서 실제로 막혔던 문제와 검증된 해결법을 정리한다.

## 텍스처 / UV

- **Bedrock는 모델당 텍스처 1장**이 원칙이다.
  - 색을 여러 개 쓰려면 **단일 아틀라스 텍스처**에 셀로 배치하고 각 면 UV를 해당 셀로 매핑한다.
  - 텍스처 여러 장으로 만들면 인게임에서 1장만 적용되고 깨진다.
- **면 픽셀 음영이 보이려면 UV를 셀 풀범위로 고정**한다.
  - 예: `[px,py,px+16,py+16]`
  - auto-UV(box-uv)는 면 크기만큼 텍스처 일부만 샘플링해서 음영/디테일이 안 보이고 단색처럼 렌더된다.
  - `cube.autouv = 0` 후 각 면 `face.uv`를 직접 지정한다.

## Bedrock 포맷 / 애니메이션

- **`bedrock_block` 포맷은 애니메이션 불가**다.
  - 여닫기, 물, 버튼 애니메이션이 필요하면 `Formats.bedrock.convertTo()`로 **Bedrock Entity**로 전환해야 한다.
- **애니 키프레임 생성 전 `animation.select()` 필수**다.
  - 선택하지 않으면 `createKeyframe`가 `setLength` null 에러를 낸다.

```javascript
var a = new Animation({name, loop}).add(false);
a.select();
a.setLength(len);
a.getBoneAnimator(group).createKeyframe({x, y, z}, time, 'rotation', false, false);
```

사운드 키프레임은 아래 패턴을 사용한다.

```javascript
if (!a.animators.effects) a.animators.effects = new EffectAnimator(a);
a.animators.effects.createKeyframe({effect: 'flush'}, t, 'sound', false, false);
```

## 회전 / 클리어런스

- **애니 회전 부호**: 경첩이 뒤(높은 `z`)에 있을 때 **+각도 = 위로 열림**, `-`각도 = 아래로 열림이다.
  - 뚜껑은 0도에서 88도 사이로 움직인다.
- **얇은 판의 두께가 인접 파츠를 파고드는 문제**에 주의한다.
  - 뚜껑이 거의 수직으로 서면 두께(0.6~0.8)만큼 뒤로 튀어나가 탱크(`z=11`)를 침범한다.
  - 검증된 해결: 경첩 피벗을 인접 면보다 **앞으로(`z=10`)** 빼고 두께를 줄인다.
  - 검증식: `열림시 뚜껑 max z < 인접면 z`

## MCP / risky_eval

- **`risky_eval` 제약**:
  - 코드에 `//`, `/* */` 주석 사용 금지
  - `console.` 사용 금지
  - 문자열 안에서도 `//` 인접을 피한다.
- **MCP 스크린샷 한계**:
  - `capture_screenshot`/`capture_app_screenshot`가 3D 텍스처 렌더를 못 잡고 큐브 마커색으로 나올 때가 많다.
  - 실제 앱 화면에는 텍스처가 정상 표시될 수 있다.
  - **Animate 모드 + 재생 중**일 때는 텍스처가 잡히기도 한다.
  - 검증은 스크린샷보다 **`risky_eval`로 좌표/UV/텍스처명/키프레임값을 직접 읽어** 확인하는 것이 더 신뢰도 높다.
- Blockbench 애니 미리보기에서 `Timeline.setTime()`만으로는 정지 포즈가 갱신 안 될 수 있다.
  - 실제 포즈 확인은 `Timeline.start()`를 사용한다.
  - `loop: 'hold'`이면 끝 프레임이 유지된다.
