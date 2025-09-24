# tests/test_ui.py
import pytest
import allure
from config.test_data import BASE_URL, EMAIL, PASSWORD
from pages.login_page import LoginPage


@allure.feature("UI: Авторизация")
class TestUILogin:
    @allure.story("Успешная авторизация в Yougile")
    @pytest.mark.ui
    def test_successful_login(self, driver):
        login_page = LoginPage(driver)

        with allure.step("1. Переход на сайт"):
            login_page.open_site(BASE_URL)

        with allure.step("2. Нажатие кнопки 'Войти' на главной"):
            login_page.click_main_login_button()

        with allure.step("3. Ввод email"):
            login_page.enter_email(EMAIL)

        with allure.step("4. Ввод пароля"):
            login_page.enter_password(PASSWORD)

        with allure.step("5. Отправка формы"):
            login_page.submit_login()

        with allure.step("6. Проверка успешного входа"):
            assert "projects" in driver.current_url.lower(), \
                f"Не удалось войти. Текущий URL: {driver.current_url}"
