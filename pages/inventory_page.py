
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    TITLE = (By.CLASS_NAME, "title")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def page_title(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.TITLE)
        )
        return element.text

    def product_count(self):
        elements = self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCT_ITEMS)
        )
        return len(elements)

    def product_names(self):
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [element.text for element in elements]

    def product_prices(self):
        elements = self.driver.find_elements(*self.PRODUCT_PRICES)
        return [element.text for element in elements]
