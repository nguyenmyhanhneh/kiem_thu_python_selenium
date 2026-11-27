from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"
#kiem tra login voi tai khoan hop le
def test_login_with_valid_account(driver):
    page = LoginPage(driver)
    page.open()
    page.login(VALID_USERNAME, VALID_PASSWORD)

    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
    assert driver.current_url.endswith("/inventory.html")
#kiem tra login voi mat khau sai
def test_login_with_wrong_password(driver):
    page = LoginPage(driver)
    page.open()
    page.login(VALID_USERNAME, "wrong_password")

    message = page.error_message()
    assert "Username and password do not match" in message
#kiem tra login voi mat khau rong
def test_login_with_empty_fields(driver):
    page = LoginPage(driver)
    page.open()
    page.login("", "")

    message = page.error_message()
    assert "Username is required" in message
#kiem tra login voi tai khoan hop le
def test_inventory_page_after_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login(VALID_USERNAME, VALID_PASSWORD)

    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
    assert page.page_title() == "Products"
    assert driver.current_url.endswith("/inventory.html")
    # assert driver.current_url.endswith("/wrong.html")
#kiem tra login voi tai khoan khong ton tai
def test_login_with_invalid_username(driver):
    """TC_LOGIN_05: Đăng nhập với username không tồn tại."""
    page = LoginPage(driver)
    page.open()

    page.login("invalid_user", "secret_sauce")

    message = page.error_message()
    assert "Username and password do not match" in message
#kiem tra login voi tai khoan bi khoa
def test_login_with_locked_out_account(driver):
    """TC_LOGIN_06: Đăng nhập bằng tài khoản bị khóa."""
    page = LoginPage(driver)
    page.open()

    page.login("locked_out_user", "secret_sauce")

    message = page.error_message()
    assert "locked out" in message.lower()
