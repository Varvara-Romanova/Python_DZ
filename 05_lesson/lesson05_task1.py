from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time  # Используется для time.sleep()

# Инициализация браузера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Открытие страницы
    driver.get("http://uitestingplayground.com/classattr")

    # Небольшая пауза для загрузки страницы
    time.sleep(2)

    # Найти и кликнуть на синюю кнопку
    blue_button = driver.find_element("css selector", ".btn-primary")
    blue_button.click()

    # Пауза для визуального подтверждения результата
    time.sleep(2)

finally:
    # Закрыть браузер
    driver.quit()
