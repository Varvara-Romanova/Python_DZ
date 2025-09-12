from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username: str):
        wait = WebDriverWait(self.driver, 15)
        field = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        field.send_keys(username)

    def enter_password(self, password: str):
        wait = WebDriverWait(self.driver, 15)
        field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
        field.send_keys(password)

    def click_login(self):
        wait = WebDriverWait(self.driver, 15)
        button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        button.click()
