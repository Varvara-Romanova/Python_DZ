from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Инициализация браузера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Открытие страницы
    driver.get("http://uitestingplayground.com/dynamicid")

    # Найти и кликнуть на синюю кнопку
    blue_button = driver.find_element("css selector", ".btn-primary")
    blue_button.click()

finally:
    # Закрыть браузер
    driver.quit()
