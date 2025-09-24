from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def open(self) -> None:
        self.driver.get(self.url)

    def set_delay(self, delay: str) -> None:
        input_field = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        input_field.clear()
        input_field.send_keys(delay)

    def click_button(self, text: str) -> None:
        button = self.driver.find_element(By.XPATH, f"//span[text()='{text}']")
        button.click()

    def get_result(self) -> str:
        """Ожидает появления результата '15' и возвращает его."""
        locator = (By.CSS_SELECTOR, ".screen")
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.text_to_be_present_in_element(locator, "15"))
        return self.driver.find_element(*locator).text
