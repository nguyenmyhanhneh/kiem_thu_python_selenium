
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory_products_displayed(driver):
    """Kiểm tra danh sách sản phẩm."""

    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)

    assert inventory.page_title() == "Products"

    assert inventory.product_count() > 0

    names = inventory.product_names()
    prices = inventory.product_prices()

    assert len(names) > 0
    assert len(prices) > 0
    assert all(name.strip() for name in names)
    assert all(price.strip() for price in prices)

