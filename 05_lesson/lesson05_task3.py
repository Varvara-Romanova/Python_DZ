from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Инициализация браузера Firefox
driver = webdriver.Firefox()

try:
    # Открытие страницы
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Небольшая пауза для загрузки страницы
    time.sleep(2)

    # Найти поле ввода
    input_field = driver.find_element(By.TAG_NAME, "input")

    # Ввести текст "Sky"
    input_field.send_keys("Sky")
    time.sleep(1)

    # Очистить поле ввода
    input_field.clear()
    time.sleep(1)

    # Ввести текст "Pro"
    input_field.send_keys("Pro")
    time.sleep(1)

finally:
    # Закрыть браузер
    driver.quit()
