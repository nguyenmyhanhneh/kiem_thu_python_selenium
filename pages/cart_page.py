
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    ADD_BACKPACK_BUTTON = (
        By.ID, "add-to-cart-sauce-labs-backpack"
    )

    CART_LINK = (
        By.CLASS_NAME, "shopping_cart_link"
    )

    CART_BADGE = (
        By.CLASS_NAME, "shopping_cart_badge"
    )

    CART_ITEMS = (
        By.CLASS_NAME, "cart_item"
    )

    PRODUCT_NAME = (
        By.CLASS_NAME, "inventory_item_name"
    )

    REMOVE_BACKPACK_BUTTON = (
        By.ID, "remove-sauce-labs-backpack"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def add_backpack(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_BACKPACK_BUTTON
            )
        )
        button.click()

        # Xác nhận sản phẩm đã được thêm vào giỏ
        self.wait.until(
            EC.visibility_of_element_located(
                self.CART_BADGE
            )
        )

    def cart_quantity(self):
        badge = self.wait.until(
            EC.visibility_of_element_located(
                self.CART_BADGE
            )
        )
        return badge.text

    def open_cart(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                self.CART_LINK
            )
        )
        button.click()

        self.wait.until(
            EC.url_contains("cart.html")
        )

    def cart_item_count(self):
        return len(
            self.driver.find_elements(
                *self.CART_ITEMS
            )
        )

    def product_name(self):
        element = self.wait.until(
            EC.visibility_of_element_located(
                self.PRODUCT_NAME
            )
        )
        return element.text

    def remove_backpack(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                self.REMOVE_BACKPACK_BUTTON
            )
        )
        button.click()

        # Chờ đến khi sản phẩm thực sự biến mất
        self.wait.until(
            EC.invisibility_of_element_located(
                self.CART_ITEMS
            )
        )

    def cart_is_empty(self):
        # Chờ đến khi không còn sản phẩm trong giỏ
        return self.wait.until(
            lambda driver: len(
                driver.find_elements(*self.CART_ITEMS)
            ) == 0
        )
