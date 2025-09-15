import allure
import pytest
from pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
class TestCalculator:
    @allure.title("Сложение 7 + 8 с задержкой 45 секунд")
    @allure.description("Результат должен быть 15 после 45 секунд.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_addition_with_delay(self, driver):
        calc = CalculatorPage(driver)

        with allure.step("Открыть страницу калькулятора"):
            calc.open()

        with allure.step("Установить задержку 45 секунд"):
            calc.set_delay("45")

        with allure.step("Выполнить 7 + 8 ="):
            calc.click_button("7")
            calc.click_button("+")
            calc.click_button("8")
            calc.click_button("=")

        with allure.step("Получить результат"):
            result = calc.get_result()

        with allure.step("Проверить, что результат равен '15'"):
            assert result == "15", f"Ожидалось 15, получено {result}"
