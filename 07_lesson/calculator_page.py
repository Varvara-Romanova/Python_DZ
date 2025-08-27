from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_equals = (By.XPATH, "//span[text()='=']")
        self.result_screen = (By.CSS_SELECTOR, ".screen")

    def open(self):
        url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.driver.get(url)

    def set_delay(self, value):
        field = self.driver.find_element(*self.delay_input)
        field.clear()
        field.send_keys(value)

    def click_button_7(self):
        self.driver.find_element(*self.button_7).click()

    def click_button_plus(self):
        self.driver.find_element(*self.button_plus).click()

    def click_button_8(self):
        self.driver.find_element(*self.button_8).click()

    def click_equals(self):
        self.driver.find_element(*self.button_equals).click()

    def get_result(self):
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element(self.result_screen, "15")
        )
        return self.driver.find_element(*self.result_screen).text
