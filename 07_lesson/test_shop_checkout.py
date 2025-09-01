import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Импортируем каждый класс из его файла
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_shop_checkout_with_page_object(driver):
    # Создаём объекты страниц
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Открываем сайт и авторизуемся
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Добавляем товары в корзину
    inventory_page.add_products()
    inventory_page.go_to_cart()

    # Переходим к оформлению заказа
    cart_page.click_checkout()

    # Заполняем форму
    checkout_page.fill_form("Иван", "Петров", "12345")

    # Получаем итоговую сумму
    total_text = checkout_page.get_total()

    # Проверка результата
    expected = "Total: $58.29"
    assert total_text == expected, (
        f"Ожидалось '{expected}', но получено: '{total_text}'"
    )
