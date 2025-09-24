from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def fill_personal_info(self, first_name: str, last_name: str, postal_code: str):
        wait = WebDriverWait(self.driver, 10)
        first_name_field = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
        last_name_field = self.driver.find_element(By.ID, "last-name")
        postal_code_field = self.driver.find_element(By.ID, "postal-code")

        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        postal_code_field.send_keys(postal_code)

    def get_total_price(self) -> str:
        wait = WebDriverWait(self.driver, 15)
        total_locator = (By.CLASS_NAME, "summary_total_label")
        wait.until(EC.visibility_of_element_located(total_locator))
        return self.driver.find_element(*total_locator).text
