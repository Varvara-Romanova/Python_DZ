import allure
import pytest
from pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
class TestCalculator:

    @allure.title("Сложение 7 + 8 с задержкой 45 секунд")
    @allure.description("Проверка, что результат 15 появляется после заданной задержки (45 секунд).")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_addition_with_delay(self, driver):
        calc = CalculatorPage(driver)

        with allure.step("Открыть страницу калькулятора"):
            calc.open()

        with allure.step("Установить значение задержки на 45 секунд"):
            calc.set_delay("45")

        with allure.step("Выполнить операцию: 7 + 8 ="):
            calc.click_button("7")
            calc.click_button("+")
            calc.click_button("8")
            calc.click_button("=")

        with allure.step("Ожидание и получение финального результата"):
            result = calc.get_result()

        with allure.step("Проверка: результат должен быть равен '15'"):
            assert result == "15", f"Ожидалось '15', получено '{result}'"
