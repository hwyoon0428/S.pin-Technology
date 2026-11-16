"""Unit tests for the repository validator; no network or browsers required."""
import tempfile
import unittest
from pathlib import Path

from scripts.validate_repo import ROOT, local_markdown_targets, validate


class RepositoryValidationTests(unittest.TestCase):
    def test_local_links_ignore_external_and_fragments(self):
        source = ROOT / "README.md"
        actual = list(local_markdown_targets(
            "[doc](docs/self-improvement.md) [web](https://example.com) [section](#test)", source))
        self.assertEqual(actual, [(ROOT / "docs/self-improvement.md").resolve()])

    def test_local_link_includes_fragmentless_target(self):
        source = ROOT / "docs/self-improvement.md"
        actual = list(local_markdown_targets("[README](../README.md#top)", source))
        self.assertEqual(actual, [(ROOT / "README.md").resolve()])

    def test_repo_validation_passes(self):
        self.assertEqual(validate(ROOT), [])

    def test_missing_files_detected(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            problems = validate(Path(temp_dir))
            self.assertTrue(any("Missing required file" in p for p in problems))


if __name__ == "__main__":
    unittest.main()
