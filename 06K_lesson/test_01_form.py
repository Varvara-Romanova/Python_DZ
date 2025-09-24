import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Инициализация драйвера Chrome
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_form_highlighting(driver):
    # Открытие страницы
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(url)

    # Заполнение формы
    first_name = driver.find_element(By.NAME, "first-name")
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.NAME, "last-name")
    last_name.send_keys("Петров")

    address = driver.find_element(By.NAME, "address")
    address.send_keys("Ленина, 55-3")

    email = driver.find_element(By.NAME, "e-mail")
    email.send_keys("test@skypro.com")

    phone = driver.find_element(By.NAME, "phone")
    phone.send_keys("+7985899998787")

    zip_code = driver.find_element(By.NAME, "zip-code")
    zip_code.send_keys("")  # Оставить пустым

    city = driver.find_element(By.NAME, "city")
    city.send_keys("Москва")

    country = driver.find_element(By.NAME, "country")
    country.send_keys("Россия")

    job_position = driver.find_element(By.NAME, "job-position")
    job_position.send_keys("QA")

    company = driver.find_element(By.NAME, "company")
    company.send_keys("SkyPro")

    # Нажать кнопку Submit
    submit_button = driver.find_element(By.TAG_NAME, "button")
    submit_button.click()

    # Ожидание подсветки полей
    wait = WebDriverWait(driver, 10)

    # Проверка: Zip code подсвечен красным
    zip_code_field = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
    zip_class = zip_code_field.get_attribute("class")
    assert "alert-danger" in zip_class, "Поле Zip code должно быть красным"

    # Список остальных полей
    field_ids = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    # Проверка: все остальные поля — зелёные
    for field_id in field_ids:
        field = driver.find_element(By.ID, field_id)
        field_class = field.get_attribute("class")
        assert "alert-success" in field_class, f"Поле {field_id} должно быть зелёным"
