
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    ERROR_MESSAGE = (
        By.CSS_SELECTOR, "[data-test='error']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def start_checkout(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                self.CHECKOUT_BUTTON
            )
        )
        button.click()

        # Xác nhận đã chuyển đến bước nhập thông tin
        self.wait.until(
            EC.url_contains("checkout-step-one.html")
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.FIRST_NAME
            )
        )

    def continue_empty_information(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                self.CONTINUE_BUTTON
            )
        )
        button.click()

        # Chờ thông báo lỗi xuất hiện
        self.wait.until(
            EC.visibility_of_element_located(
                self.ERROR_MESSAGE
            )
        )

    def error_message(self):
        element = self.wait.until(
            EC.visibility_of_element_located(
                self.ERROR_MESSAGE
            )
        )
        return element.text
