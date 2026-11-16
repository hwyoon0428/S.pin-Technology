"""Dependency-free repository checks run on pull requests and pushes."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
DOCS = ("README.md", "AGENTS.md", "docs/README.md",
        "docs/self-improvement.md", "docs/codex-cloud-browser.md")
REQUIRED = ("AGENTS.md", "docs/self-improvement.md",
            ".github/workflows/repository-validation.yml",
            ".github/workflows/self-improvement-merge.yml",
            "scripts/browser_smoke.py", "tests/test_repo_validation.py")
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def local_markdown_targets(text: str, source: Path):
    """Find local file links while ignoring HTTP/mail/fragment links."""
    for match in LINK.finditer(text):
        target = match.group(1).strip().split("#", 1)[0].split("?", 1)[0]
        if not target or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
            continue
        yield (source.parent / unquote(target)).resolve()


def validate(root: Path = ROOT):
    problems = []
    for name in REQUIRED:
        if not (root / name).is_file():
            problems.append("Missing required file: " + name)
    for name in DOCS:
        source = root / name
        if not source.is_file():
            problems.append("Missing documentation: " + name)
            continue
        for target in local_markdown_targets(source.read_text(encoding="utf-8"), source):
            if not target.is_relative_to(root.resolve()) or not target.exists():
                problems.append("Broken local link in " + name + ": " + str(target))
    merge_path = root / ".github/workflows/self-improvement-merge.yml"
    if merge_path.is_file():
        content = merge_path.read_text(encoding="utf-8")
        for guard in ("workflow_run:", "Repository validation",
                      "ENABLE_SELF_IMPROVEMENT_AUTOMERGE",
                      "conclusion == 'success'", "--match-head-commit"):
            if guard not in content:
                problems.append("Missing safe-merge guard: " + guard)
        if "pull_request_target:" in content:
            problems.append("Do not run privileged auto-merge on pull_request_target")
    return problems


if __name__ == "__main__":
    errors = validate()
    for error in errors:
        print("FAIL:", error, file=sys.stderr)
    if errors:
        sys.exit(1)
    print("PASS: required files, documentation links, and merge safeguards")
