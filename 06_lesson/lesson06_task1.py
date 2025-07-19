from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Открытие страницы
    driver.get("http://uitestingplayground.com/ajax")

    # Найти и кликнуть на синюю кнопку
    blue_button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
    blue_button.click()

    # Явное ожидание появления зелёной плашки
    green_box = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
    )

    text = green_box.text
    print(text)

    expected_text = "Data loaded with AJAX get request."
    error_message = "Текст не совпадает с ожидаемым!"
    assert text == expected_text, error_message

finally:
    driver.quit()
