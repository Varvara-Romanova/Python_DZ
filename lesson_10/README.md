# Автотест для интернет-магазина

Проект содержит автоматизированный тест для сайта [https://www.saucedemo.com/](https://www.saucedemo.com/)

---

## 🛠️ Требования

- Python 3.8+
- Chrome
- `pip install selenium pytest allure-pytest webdriver-manager`

# Далее подключите пакет allure-pytest
```bash
pip install allure-pytest

---

## ▶️ Запуск теста

- Перейти в папку lesson_10
```bash
cd lesson10

```bash
pytest tests/test_02_shop_page_allure.py -v --alluredir=./allure-results

# Генерация отчёта Allure
```bash
allure serve allure-result