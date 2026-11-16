"""Test a local Playwright Chromium session without external network access."""
import platform
import sys


def main() -> int:
    print("Python:", platform.python_version(), "Platform:", platform.platform())
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("NOT_READY: Playwright not installed. Install in your Codex Cloud environment setup.")
        return 2
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True, timeout=15000)
            try:
                page = browser.new_page()
                page.goto("data:text/html,<title>Browser smoke</title><h1 id='status'>ready</h1>")
                if page.title() != "Browser smoke" or page.locator("#status").inner_text() != "ready":
                    print("FAIL: browser rendered unexpected content")
                    return 1
                print("PASS: Chromium launch and local page interaction")
                return 0
            finally:
                browser.close()
    except Exception as exc:
        print("FAIL: Chromium launch or interaction:", type(exc).__name__, str(exc)[:500])
        return 1


if __name__ == "__main__":
    sys.exit(main())
