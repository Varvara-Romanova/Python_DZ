# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:
    # Кнопка "Войти" на главной странице
    MAIN_LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        ".btn.btn-sm.btn-outline-primary.btn-border-radius-lg.fw-normal.ms-sm-3.ms-0.sign-in-button"
    )
    # Поля ввода email и пароля
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    # Кнопка "Войти" в форме входа
    SUBMIT_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Войти') and contains(@class, 'bg-action-default')]"
    )

    def __init__(self, driver):
        self.driver = driver

    @allure.step("1. Переход на сайт")
    def open_site(self, url):
        self.driver.get(url.strip())

    @allure.step("2. Нажатие кнопки 'Войти' на главной")
    def click_main_login_button(self):
        button = WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable(self.MAIN_LOGIN_BUTTON),
            message="Кнопка 'Войти' в шапке не найдена"
        )
        button.click()

    @allure.step("3. Ввод email")
    def enter_email(self, email):
        field = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(self.EMAIL_INPUT),
            message="Поле email не появилось"
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", field)
        field.clear()
        field.send_keys(email)

    @allure.step("4. Ввод пароля")
    def enter_password(self, password):
        field = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT),
            message="Поле пароля не появилось"
        )
        field.clear()
        field.send_keys(password)

    @allure.step("5. Отправка формы")
    def submit_login(self):
        # появление кнопки "Войти" в форме
        button = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(self.SUBMIT_BUTTON),
            message="Кнопка входа в форме не найдена"
        )
        # Прокрутка к кнопке
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        # Клик через JavaScript — обходит антибот Yougile
        self.driver.execute_script("arguments[0].click();", button)
