import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Интернет-магазин")
class TestShop:
    @allure.title("Оформление заказа с проверкой итоговой суммы")
    @allure.description("Авторизация, добавление товаров, оформление заказа, проверка $58.29")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_complete_purchase(self, driver):
        login = LoginPage(driver)
        inventory = InventoryPage(driver)
        cart = CartPage(driver)
        checkout = CheckoutPage(driver)

        with allure.step("Авторизация как standard_user"):
            login.open()
            login.enter_username("standard_user")
            login.enter_password("secret_sauce")
            login.click_login()

        with allure.step("Добавить три товара в корзину"):
            inventory.add_backpack_to_cart()
            inventory.add_bolt_tshirt_to_cart()
            inventory.add_onesie_to_cart()

        with allure.step("Перейти в корзину и нажать Checkout"):
            inventory.go_to_cart()
            cart.click_checkout()

        with allure.step("Заполнить форму и нажать Continue"):
            checkout.fill_personal_info("Иван", "Иванов", "123456")
            checkout.click_continue()

        with allure.step("Проверить итоговую стоимость"):
            total = checkout.get_total_price()
            assert "58.29" in total, f"Ожидалось 58.29, получено {total}"
