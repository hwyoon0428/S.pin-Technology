# Codex Cloud 브라우저 실행·오류 진단

## 목적과 범위

- Codex Cloud의 작업 환경에서 Playwright/Chromium이 실제로 실행되는지 **로컬 테스트 페이지**만으로 확인합니다.
- 이 검사는 Playwright 기반 브라우저 사용 가능 여부만 검증합니다. ChatGPT Work의 클라우드 브라우저나 `cua.getState()`·`gaas-browser` NodeREPL 정상 동작을 증명하지 않습니다.
- 기존 오류 `the gaas-browser node_repl sandbox cannot be disabled`는 첫 `cua.getState()` 이전 단계에서 발생했으며 원인은 미확정입니다.

## 준비

1. Codex Cloud에서 이 저장소를 연결한 실행 환경을 구성합니다. 설치 과정은 환경 설정 단계에서 진행하고, 네트워크 정책은 꼭 필요한 패키지 도메인만 허용합니다.
2. Python 3.9 이상을 사용합니다.
3. 환경의 공식 설치 단계에서 다음 명령을 실행합니다(Playwright 설치가 승인된 경우).

```bash
python -m pip install playwright
python -m playwright install chromium
```

4. 해당 Codex Cloud 환경에서 아래의 오프라인 스모크 테스트를 실행합니다.

```bash
python scripts/browser_smoke.py
```

- `PASS`: Chromium 시작 및 DOM 조작 성공. 이것은 Playwright 검증에만 해당합니다.
- `NOT_READY`: Playwright Python 패키지가 없습니다. 설치 환경과 네트워크 접근 정책을 확인합니다.
- `FAIL`: Chromium 실행 또는 로컬 DOM 검증 실패. 의존 라이브러리, 디스플레이/샌드박스 및 정책을 진단합니다. 보호 기능을 끄거나 우회하지 않습니다.

## 기존 CUA / NodeREPL 오류 별도 진단

1. 실패한 Codex Cloud 작업과 **동일한 환경 ID**인지 먼저 확인합니다.
2. 가능하다면 해당 환경의 상태와 진단 기록 메타데이터를 공식 도구로 확인합니다.
3. `cua.getState()`를 문서화된 방식으로 한 번 호출하고 응답 화면·오류를 기록합니다. 이 호출의 성공이 확인되지 않는 한 CUA 복구 완료라고 보고하지 않습니다.
4. 문제가 지속되면 환경 ID·발생 시각·진단 ID와 정확한 오류 문구를 지원팀에 전달합니다. 쿠키·토큰·민감한 원시 로그는 별도 승인이 없으면 수집·공유하지 않습니다.

## 동작 경계

- GitHub Actions의 저장소 검증 CI는 Codex Cloud 내부 브라우저를 실행하지 않습니다.
- 저장소의 스크립트를 추가하거나 CI를 통과해도 Codex Cloud의 설치·런타임 정책이나 CUA 호스트 문제를 직접 고치지는 못합니다.
- 인증된 업무 UI 조작은 우선 공식 커넥터/API를 사용하고, 불가하면 해당 실행 환경에서 허용된 브라우저를 사용합니다. 인증·권한 확인 및 변경 후 재검증이 필요합니다.

참고: [Codex Cloud 공식 안내](https://help.openai.com/en/articles/20001545-using-codex-cloud), [Notion gaas-browser 진단 기록](https://app.notion.com/p/419392ba3f5c81e992abc9fc4eaf5822).
