# pages/project_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class ProjectPage:
    CREATE_PROJECT_BTN = (
        By.XPATH, "//button[contains(text(), 'Создать проект')]"
    )
    PROJECT_NAME_INPUT = (
        By.CSS_SELECTOR, "input[placeholder='Введите название проекта']"
    )
    SAVE_PROJECT_BTN = (
        By.XPATH, "//button[contains(text(), 'Сохранить')]"
    )
    PROJECT_LIST = (By.CSS_SELECTOR, ".project-card__title")
    LOADING_INDICATOR = (By.CSS_SELECTOR, ".spinner")

    def __init__(self, driver):
        self.driver = driver

    def wait_until_loaded(self):
        """Ждём исчезновения спиннера загрузки"""
        try:
            WebDriverWait(self.driver, 15).until(
                EC.invisibility_of_element_located(self.LOADING_INDICATOR)
            )
        except Exception:  # Исправлено: не используем bare 'except'
            pass

    @allure.step("Создание проекта с названием: {name}")
    def create_project(self, name):
        self.wait_until_loaded()
        create_btn = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.CREATE_PROJECT_BTN)
        )
        create_btn.click()

        name_input = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.PROJECT_NAME_INPUT)
        )
        name_input.send_keys(name)

        save_btn = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(self.SAVE_PROJECT_BTN)
        )
        save_btn.click()
        self.wait_until_loaded()

    @allure.step("Проверка наличия проекта в списке")
    def is_project_present(self, name):
        titles = WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located(self.PROJECT_LIST)
        )
        return any(name in title.text for title in titles)
