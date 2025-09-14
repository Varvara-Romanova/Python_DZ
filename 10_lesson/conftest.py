import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    # Создаём путь к временной папке
    temp_profile = os.path.join(os.getcwd(), "chrome-profile")
    if not os.path.exists(temp_profile):
        os.makedirs(temp_profile)

    options = webdriver.ChromeOptions()

    options.add_argument("--disable-password-manager")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-plugins")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-autofill-popup")
    options.add_argument(f"--user-data-dir={temp_profile}")
    options.add_argument("--start-maximized")

    # Запуск драйвера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Убираем признак автоматизации
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => false});")
    driver.execute_script("window.chrome = {runtime: {}};")
    driver.execute_script("navigator.permissions = {query: () => Promise.resolve({state: 'granted'})};")

    # Установка ожидания
    driver.implicitly_wait(10)

    yield driver
    driver.quit()
