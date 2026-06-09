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

from pages.inventory_page import InventoryPage

def test_add_to_cart(page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    inventory.add_backpack_to_cart()
    assert inventory.get_cart_count() == "1"
    page.screenshot(path="screenshots/add_to_cart.png")