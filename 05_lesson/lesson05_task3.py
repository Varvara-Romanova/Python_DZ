from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

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
