# tests/test_api.py
import pytest
import allure
from api.client import APIClient
from config.test_data import PROJECT_NAME


@allure.feature("API: Проекты")
class TestAPIProjects:
    @pytest.fixture(scope="class")
    def api_client(self):
        return APIClient()

    @allure.story("Получение списка проектов")
    @pytest.mark.api
    def test_get_projects_list(self, api_client):
        with allure.step("Отправка GET /projects"):
            response = api_client.get_projects()

        with allure.step("Проверка успешного ответа (200 OK)"):
            assert response.status_code == 200, \
                f"Ожидался 200, получен {response.status_code}. " \
                f"Ответ: {response.text}"

    @allure.story("Создание проекта")
    @pytest.mark.api
    def test_create_project(self, api_client):
        project_name = f"{PROJECT_NAME}_test"

        with allure.step(f"Создание проекта: {project_name}"):
            response = api_client.create_project(project_name)

        with allure.step("Проверка успешного создания (201 Created)"):
            assert response.status_code == 201, \
                f"Ожидался 201, получен {response.status_code}. " \
                f"Ответ: {response.text}"
            data = response.json()
            assert data["name"] == project_name, \
                f"Имя проекта не совпадает: ожидаемое '{project_name}', фактическое '{data['name']}'"

    @allure.story("Удаление проекта")
    @pytest.mark.api
    def test_delete_project(self, api_client):
        # Создаём временный проект
        create_resp = api_client.create_project("ToDelete")
        if create_resp.status_code != 201:
            allure.attach(
                create_resp.text,
                "Ошибка создания",
                allure.attachment_type.TEXT
            )
            assert False, f"Не удалось создать проект для удаления. " \
                          f"Статус: {create_resp.status_code}, Ответ: {create_resp.text}"
        project_id = create_resp.json()["id"]

        with allure.step(f"Удаление проекта {project_id}"):
            delete_resp = api_client.delete_project(project_id)

        with allure.step("Проверка успешного удаления (200 или 204)"):
            assert delete_resp.status_code in [200, 204], \
                f"Ошибка удаления: статус {delete_resp.status_code}, Ответ: {delete_resp.text}"
