import allure
import pytest
from pages.ShopMainPageAllure import ShopMainPageAllure


@allure.feature("Интернет-магазин")
class TestShopPageAllure:

    @allure.title("Покупка трёх товаров и проверка итоговой суммы")
    @allure.description("Авторизация, добавление товаров, оформление заказа, проверка стоимости.")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_complete_purchase(self, driver):
        shop = ShopMainPageAllure(driver)

        with allure.step("Открыть сайт"):
            shop.open()

        with allure.step("Авторизоваться"):
            shop.login("standard_user", "secret_sauce")

        with allure.step("Добавить три товара"):
            shop.add_backpack()
            shop.add_bolt_tshirt()
            shop.add_onesie()

        with allure.step("Перейти в корзину"):
            shop.go_to_cart()

        with allure.step("Нажать Checkout"):
            shop.click_checkout()

        with allure.step("Заполнить форму"):
            shop.fill_personal_info("Иван", "Иванов", "123456")

        with allure.step("Получить итоговую стоимость"):
            total = shop.get_total_price()

        with allure.step("Проверить сумму $58.29"):
            assert "58.29" in total, f"Ожидалось $58.29, получено {total}"
