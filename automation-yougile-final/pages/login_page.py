# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:
    MAIN_LOGIN_BUTTON = (By.XPATH, "//a[contains(text(), 'Войти')]")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Переход на сайт Yougile")
    def open_site(self, url):
        self.driver.get(url)

    @allure.step("Нажатие кнопки 'Войти' на главной")
    def click_main_login_button(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.MAIN_LOGIN_BUTTON)
        ).click()

    @allure.step("Ввод email")
    def enter_email(self, email):
        field = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )
        field.send_keys(email)

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        field = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        field.send_keys(password)

    @allure.step("Нажатие кнопки входа")
    def submit_login(self):
        button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON)
        )
        button.click()
