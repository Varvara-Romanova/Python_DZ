from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    """
    Page Object для главной страницы магазина (https://www.saucedemo.com/inventory.html)
    """

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def add_backpack_to_cart(self) -> None:
        """Добавляет товар 'Sauce Labs Backpack' в корзину."""
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    def add_bolt_tshirt_to_cart(self) -> None:
        """Добавляет товар 'Sauce Labs Bolt T-Shirt' в корзину."""
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    def add_onesie_to_cart(self) -> None:
        """Добавляет товар 'Sauce Labs Onesie' в корзину."""
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    def go_to_cart(self) -> None:
        """Переходит в корзину."""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
