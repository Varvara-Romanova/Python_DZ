from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    # Открытие страницы
    driver.get("http://the-internet.herokuapp.com/login")

    # Небольшая пауза для загрузки страницы
    time.sleep(2)

    # Найти поле username и ввести значение
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    # Найти поле password и ввести значение
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    # Найти кнопку Login и кликнуть по ней
    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
    login_button.click()

    # Пауза для отображения результата
    time.sleep(2)

    # Найти текст с зеленой плашки и вывести его в консоль
    success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
    print("Текст с зеленой плашки:")
    print(success_message.text)

finally:
    # Закрыть браузер
    driver.quit()
