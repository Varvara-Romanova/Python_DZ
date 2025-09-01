import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_slow_calculator_with_page_object(driver):
    # Создаём объект страницы
    calc_page = CalculatorPage(driver)

    # Открываем страницу
    calc_page.open()

    # Устанавливаем задержку
    calc_page.set_delay("45")

    # Нажимаем кнопки
    calc_page.click_button_7()
    calc_page.click_button_plus()
    calc_page.click_button_8()
    calc_page.click_equals()

    # Получаем результат
    result = calc_page.get_result()

    # Проверка результата
    assert result == "15", f"Ожидалось '15', но получено: '{result}'"
