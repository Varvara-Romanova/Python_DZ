from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация браузера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Открытие страницы
    driver.get("http://uitestingplayground.com/textinput")

    # Ввод текста в поле
    input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
    input_field.send_keys("SkyPro")

    # Нажатие на синюю кнопку
    blue_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
    blue_button.click()

    # Явное ожидание обновления текста на кнопке
    locator = (By.CSS_SELECTOR, "#updatingButton")
    expected_text = "SkyPro"

    updated_text = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(locator, expected_text)
    )

    # Получение и вывод текста кнопки
    button_text = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
    print(button_text)

finally:
    driver.quit()
