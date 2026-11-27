
import pytest
import time
from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")

    browser = webdriver.Chrome(options=options) 

    yield browser # bàn giao driver cho các test case
    time.sleep(3)
    browser.quit()
