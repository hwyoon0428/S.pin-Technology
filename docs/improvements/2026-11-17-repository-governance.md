# GitHub 저장소 CI·브라우저 검증·자가개선 통제

- 날짜: 2026-11-17
- 문제와 근거: `main` 브랜치 보호·필수 검사가 없고 이전 자동 병합에 별도 CI 게이트가 없었다. Codex Cloud 브라우저 검증 문서 및 스크립트도 없었다.
- 변경 전 기준선: main `4ee7f8ececf46f909ee794a809bcd261ec628ddb`, 보호 false, Rulesets 없음, 열린 PR 0건.
- 완료 조건: 저장소 CI 통과, 자동 병합 기본 비활성 및 커밋 일치 검증, Codex Cloud 브라우저 스모크 절차 문서화, Notion/AGENTS 지침 정합화.
- 변경 내용: CI, Python 저장소 검증, 브라우저 스모크, PR 템플릿, 검증 후 자동 병합 안전 게이트, 운영 문서.
- 검증: GitHub PR의 `Repository validation / validate` 실행 결과 확인 예정. 실제 테스트 결과 확인 전에는 완료로 간주하지 않음.
- 미실행 검증과 이유: Codex Cloud 런타임의 `cua.getState()`와 Chromium 실제 시작은 이 GitHub 연결에서 직접 실행할 수 없음.
- 남은 위험: GitHub의 브랜치 보호와 저장소 변수 변경은 이 연결로 지원되지 않으므로 관리자 UI 설정 필요.
- 후속 후보: 보호 규칙 적용 후 E2E 자동 병합 시험, Codex Cloud 실제 환경 재진단.
