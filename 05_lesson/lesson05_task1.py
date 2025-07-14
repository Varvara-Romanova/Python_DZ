from selenium import webdriver
import time

# Инициализация браузера Google Chrome
driver = webdriver.Chrome()

try:
    # Открытие страницы
    driver.get("http://uitestingplayground.com/classattr")

    # Небольшая пауза для загрузки страницы
    time.sleep(2)

    # Поиск и клик по синей кнопке
    blue_button = driver.find_element(
        "css selector",
        ".btn-primary"
    )
    blue_button.click()

    # Пауза для визуального подтверждения результата
    time.sleep(2)

finally:
    # Закрытие браузера
    driver.quit()
