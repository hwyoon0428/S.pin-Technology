# S.pin-Technology

초기 단계의 저장소입니다. 애플리케이션의 목적·기술 스택·실행 방법은 추후 정의하며, 저장소 문서와 자동화 설정의 검증을 위한 Python 기반 CI만 구성되어 있습니다.

- [에이전트 작업 지침](AGENTS.md)
- [프로젝트 문서](docs/README.md)
- [설계 결정 기록](docs/decisions/README.md)
- [자가개선 루프](docs/self-improvement.md)

## 저장소 검증 및 Codex Cloud

- [Repository validation CI](.github/workflows/repository-validation.yml) — PR/`main` 푸시에서 Python 테스트와 문서·병합 안전장치 검사
- [Codex Cloud 브라우저 검증](docs/codex-cloud-browser.md) — Playwright 오프라인 스모크 및 CUA 장애 분리 진단
- [자가개선과 안전한 PR 병합](docs/self-improvement.md) — CI 통과 확인·수동 관리자 설정·증거 기반 개선

로컬 검사: `python3 -m unittest discover -s tests -v` 및 `python3 scripts/validate_repo.py`. 브라우저 스모크는 실제 Codex Cloud 환경에서 별도로 수행합니다.
