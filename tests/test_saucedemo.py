import pytest
from pages.login_page import LoginPage

def test_login_success(page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    assert "inventory" in page.url

def test_login_failed(page):
    login = LoginPage(page)
    login.goto()
    login.login("wrong_user" , "wrong_pass")
    error = page.locator("[data-test='error']")
    assert error.is_visible()