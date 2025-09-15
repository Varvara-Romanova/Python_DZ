from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CSS_SELECTOR, ".summary_total_label")

    def fill_personal_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.first_name_input))

        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)

    def click_continue(self) -> None:
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable(self.continue_button))
        button.click()

    def get_total_price(self) -> str:
        wait = WebDriverWait(self.driver, 20)
        total_element = wait.until(EC.visibility_of_element_located(self.total_label))
        return total_element.text
