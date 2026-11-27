from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    PAGE_TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.visibility_of_element_located(self.USERNAME))

    def login(self, username="", password=""): 
        user_input = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        )
        password_input = self.driver.find_element(*self.PASSWORD)

        user_input.clear()
        password_input.clear()

        if username:
            user_input.send_keys(username)
        if password:
            password_input.send_keys(password)

        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def error_message(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return element.text

    def page_title(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.PAGE_TITLE)
        )
        return element.text
