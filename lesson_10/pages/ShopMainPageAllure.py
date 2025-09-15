from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class ShopMainPageAllure:
    """
    Page Object для интернет-магазина https://www.saucedemo.com/
    """

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def open(self) -> None:
        """Открывает сайт."""
        self.driver.get(self.url)

    def login(self, username: str, password: str) -> None:
        """Авторизация."""
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def add_backpack(self) -> None:
        """Добавить рюкзак."""
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    def add_bolt_tshirt(self) -> None:
        """Добавить футболку."""
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    def add_onesie(self) -> None:
        """Добавить комбинезон."""
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    def go_to_cart(self) -> None:
        """Перейти в корзину."""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def click_checkout(self) -> None:
        """Нажать Checkout."""
        self.driver.find_element(By.ID, "checkout").click()

    def fill_personal_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        """Заполнить форму."""
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    def get_total_price(self) -> str:
        """Получить итоговую стоимость."""
        total_locator = (By.CLASS_NAME, "summary_total_label")
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located(total_locator))
        return self.driver.find_element(*total_locator).text
