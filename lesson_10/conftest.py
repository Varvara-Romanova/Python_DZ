import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    # Настройка Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-password-manager")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-plugins")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--user-data-dir=C:/temp/chrome-profile")
    options.add_argument("--start-maximized")

    # Запуск драйвера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Убираем признак автоматизации
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => false});")

    yield driver
    driver.quit()
