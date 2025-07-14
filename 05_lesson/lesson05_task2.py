from selenium import webdriver

# Инициализация браузера
driver = webdriver.Chrome()

try:
    # Открытие страницы
    driver.get("http://uitestingplayground.com/dynamicid")

    # Найти и кликнуть на синюю кнопку
    blue_button = driver.find_element("css selector", ".btn-primary")
    blue_button.click()

finally:
    # Закрыть браузер
    driver.quit()
