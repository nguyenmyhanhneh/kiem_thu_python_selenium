
from pages.login_page import LoginPage
from pages.cart_page import CartPage


def test_add_product_to_cart(driver):
    """
    Kiểm tra thêm sản phẩm vào giỏ hàng.
    """

    # Đăng nhập
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    # Khởi tạo trang giỏ hàng
    cart = CartPage(driver)
    # Thêm sản phẩm vào giỏ
    cart.add_backpack()
    # Kiểm tra số lượng trên biểu tượng giỏ hàng
    assert cart.cart_quantity() == "1"
    # Mở trang giỏ hàng
    cart.open_cart()
    # Kiểm tra sản phẩm trong giỏ
    assert cart.cart_item_count() == 1
    assert cart.product_name() == "Sauce Labs Backpack"

def test_remove_product_from_cart(driver):
    """
    Kiểm tra xóa sản phẩm khỏi giỏ hàng.
    """

    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    cart = CartPage(driver)
    # Thêm sản phẩm vào giỏ
    cart.add_backpack()
    assert cart.cart_quantity() == "1"
    # Mở giỏ hàng
    cart.open_cart()
    # Xóa sản phẩm
    cart.remove_backpack()
    # Kiểm tra giỏ hàng trống
    assert cart.cart_is_empty()
    # Kiểm tra biểu tượng giỏ hàng không còn số lượng
    assert len(driver.find_elements(*cart.CART_BADGE)) == 0
