
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_with_empty_information(driver):
    """
    Kiểm tra bỏ trống thông tin thanh toán.
    """
    # Đăng nhập
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    # Thêm sản phẩm vào giỏ
    cart = CartPage(driver)
    cart.add_backpack()
    cart.open_cart()
    # Thực hiện thanh toán
    checkout = CheckoutPage(driver)
    checkout.start_checkout()
    checkout.continue_empty_information()
    # Kiểm tra thông báo lỗi
    message = checkout.error_message()

    assert "First Name is required" in message
