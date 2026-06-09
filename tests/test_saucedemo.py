import pytest
from pages.login_page import LoginPage

def test_login_success(page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    page.screenshot(path="screenshots/login_success.png")
    assert "inventory" in page.url

def test_login_failed(page):
    login = LoginPage(page)
    login.goto()
    login.login("wrong_user", "wrong_pass")
    page.screenshot(path="screenshots/login_failed.png")
    error = page.locator("[data-test='error']")
    assert error.is_visible()