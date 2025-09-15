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
    url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html "
    driver.get(url)

    # Ждём появления третьего изображения
    third_image = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "image3"))
    )

    # Функция для ожидания непустого src
    def wait_for_src(element):
        def condition(driver):
            src = element.get_attribute("src")
            return src is not None and len(src) > 10
        return condition

    # Ждём, пока src будет загружен
    WebDriverWait(driver, 10).until(wait_for_src(third_image))

    # Получаем и выводим значение src
    src_value = third_image.get_attribute("src")
    print("src третьей картинки:")
    print(src_value)

finally:
    driver.quit()
