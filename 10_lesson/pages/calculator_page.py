from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """
    Page Object для страницы медленного калькулятора.
    URL: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы.

        :param driver: WebDriver instance
        """
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def open(self) -> None:
        """
        Открывает страницу калькулятора.
        """
        self.driver.get(self.url)

    def set_delay(self, delay: str) -> None:
        """
        Устанавливает значение задержки в поле ввода.

        :param delay: Значение задержки в секундах (в виде строки)
        """
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, text: str) -> None:
        """
        Нажимает кнопку калькулятора по тексту.

        :param text: Текст кнопки (например, '7', '+', '=')
        """
        button = self.driver.find_element(By.XPATH, f"//span[text()='{text}']")
        button.click()

    def get_result(self) -> str:
        """
        Ожидает, пока результат не станет равным '15', и возвращает его.

        :return: Текст результата (ожидается '15')
        """
        result_locator = (By.CSS_SELECTOR, ".screen")
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.text_to_be_present_in_element(result_locator, "15"))
        return self.driver.find_element(*result_locator).text
