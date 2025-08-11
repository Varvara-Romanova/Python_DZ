import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from page_objects import LoginPage, InventoryPage, CartPage, CheckoutPage


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

    # Переходим к оформлению
    cart_page.click_checkout()

    # Заполняем форму
    checkout_page.fill_form("Иван", "Петров", "12345")
    total_text = checkout_page.get_total()

    # Проверка итоговой суммы
    expected_total = "Total: $58.29"
    assert total_text == expected_total, (
        f"Ожидалось '{expected_total}', но получено: '{total_text}'"
    )
