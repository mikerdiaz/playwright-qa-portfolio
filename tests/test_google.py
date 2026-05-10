from playwright.sync_api import Page

def test_google_title(page: Page):
    page.goto("https://www.google.com")
    assert "Google" in page.title()

def test_google_search(page: Page):
    page.goto("https://www.google.com")
    page.locator("textarea[name='q']").fill("Playwright Python")
    page.keyboard.press("Enter")
    page.wait_for_load_state("networkidle")
    assert "Playwright" in page.title()
