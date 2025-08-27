import pytest


class TestProjectsAPI:

    def test_create_project_positive(self, api_client, project_data):
        response = api_client.create_project(project_data)
        assert response.status_code == 201, (
            f"Ожидался 201, получен {response.status_code}"
        )
        json_data = response.json()
        assert "id" in json_data, "Проект должен иметь ID"
        assert json_data["title"] == project_data["title"]

    def test_create_project_negative_missing_title(self, api_client):
        invalid_data = {"color": "#FF5733"}
        response = api_client.create_project(invalid_data)
        assert response.status_code == 400, (
            f"Ожидался 400, получен {response.status_code}"
        )
        assert "title" in str(response.json()), "Должна быть ошибка по обязательному полю 'title'"

    def test_update_project_positive(self, api_client, project_data):
        create_response = api_client.create_project(project_data)
        assert create_response.status_code == 201
        project_id = create_response.json()["id"]

        updated_data = {"title": "Updated Project", "color": "#33FF57"}
        response = api_client.update_project(project_id, updated_data)
        assert response.status_code == 200, (
            f"Ожидался 200, получен {response.status_code}"
        )
        assert response.json()["title"] == "Updated Project"

    def test_update_project_negative_invalid_id(self, api_client):
        response = api_client.update_project("invalid-id-123", {"title": "Fake"})
        assert response.status_code == 404, (
            f"Ожидался 404, получен {response.status_code}"
        )

    def test_get_project_positive(self, api_client, project_data):
        create_response = api_client.create_project(project_data)
        assert create_response.status_code == 201
        project_id = create_response.json()["id"]

        response = api_client.get_project(project_id)
        assert response.status_code == 200, (
            f"Ожидался 200, получен {response.status_code}"
        )
        assert response.json()["id"] == project_id

    def test_get_project_negative_not_found(self, api_client):
        response = api_client.get_project("99999999")
        assert response.status_code == 404, (
            f"Ожидался 404, получен {response.status_code}"
        )
