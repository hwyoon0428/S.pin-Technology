# 0002. 검증 우선 PR 병합 및 Codex Cloud 브라우저 분리 점검

- 상태: 적용 대기(브랜치 보호 및 CI 검증).
- 배경: `main`은 보호되지 않았고 기존 자가개선 `pull_request_target` 워크플로가 필수 검사 없이 병합할 수 있었다.
- 결정: 저장소 검증 CI를 읽기 권한으로 실행한다. 자가개선 PR 병합은 성공한 CI의 `workflow_run` 후, 동일 저장소·소유자·브랜치 접두사·PR 최신 커밋 일치 조건을 확인한다.
- 안전 게이트: `ENABLE_SELF_IMPROVEMENT_AUTOMERGE` 저장소 변수가 명시적으로 `true`가 되기 전까지 자동 병합을 비활성화한다. 변수는 `main` 보호와 필수 검사 적용·검증 후에만 설정한다.
- 분리: 브라우저 진단은 Codex Cloud 실행 환경에서 독립적으로 수행한다. GitHub Actions CI 통과를 브라우저 복구의 증명으로 사용하지 않는다.
- 남은 작업: GitHub 관리자 UI에서 `main` 보호/필수 CI 검사 구성, 실제 Cloud 브라우저 테스트, 자가개선 자동 병합 E2E 검증.
