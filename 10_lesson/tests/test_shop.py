import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Интернет-магазин")
class TestShop:

    @allure.title("Покупка трёх товаров и проверка итоговой суммы")
    @allure.description("Добавление товаров в корзину, оформление заказа, проверка стоимости.")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_complete_purchase(self, driver):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        with allure.step("Открыть сайт и авторизоваться"):
            login_page.open()
            login_page.enter_username("standard_user")
            login_page.enter_password("secret_sauce")
            login_page.click_login()

        with allure.step("Добавить три товара в корзину"):
            inventory_page.add_backpack_to_cart()
            inventory_page.add_bolt_tshirt_to_cart()
            inventory_page.add_onesie_to_cart()

        with allure.step("Перейти в корзину и нажать Checkout"):
            inventory_page.go_to_cart()
            cart_page.click_checkout()

        with allure.step("Заполнить форму доставки"):
            checkout_page.fill_personal_info("Иван", "Иванов", "123456")

        with allure.step("Получить итоговую стоимость"):
            total_text = checkout_page.get_total_price()

        with allure.step("Проверить, что итоговая сумма равна $58.29"):
            assert "58.29" in total_text, f"Итог не совпадает: {total_text}"
