from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_checkout(self):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        button.click()
