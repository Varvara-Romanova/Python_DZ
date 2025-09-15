# tests/test_ui.py
import pytest
import allure
from config.test_data import EMAIL, PASSWORD, BASE_URL
from pages.login_page import LoginPage


@allure.feature("UI: Авторизация")
class TestUILogin:
    @allure.story("Успешная авторизация")
    @pytest.mark.ui
    def test_successful_login(self, driver):
        driver.get(BASE_URL)
        login_page = LoginPage(driver)

        with allure.step("Ввод email"):
            login_page.enter_email(EMAIL)

        with allure.step("Ввод пароля"):
            login_page.enter_password(PASSWORD)

        with allure.step("Нажатие кнопки Войти"):
            login_page.click_login()

        assert "Проекты" in driver.title or "projects" in driver.current_url.lower()
