from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """
    Page Object для страницы входа.
    """

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def open(self) -> None:
        """Открывает страницу логина."""
        self.driver.get(self.url)

    def enter_username(self, username: str) -> None:
        """Вводит имя пользователя."""
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def enter_password(self, password: str) -> None:
        """Вводит пароль."""
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self) -> None:
        """Нажимает кнопку входа."""
        self.driver.find_element(By.ID, "login-button").click()