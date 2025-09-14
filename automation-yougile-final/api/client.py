# api/client.py
import requests
from config.test_data import API_V2_URL, API_KEY, COMPANY_ID


class APIClient:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = API_V2_URL
        # Устанавливаем заголовки авторизации
        self.session.headers.update({
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        })

    def get_companies(self):
        """Получить список компаний"""
        url = f"{self.base_url}/companies"
        return self.session.get(url)

    def get_projects(self):
        """Получить проекты компании"""
        url = f"{self.base_url}/projects"
        params = {"companyId": COMPANY_ID}
        return self.session.get(url, params=params)

    def create_project(self, name):
        """Создать проект"""
        url = f"{self.base_url}/projects"
        json_data = {
            "name": name,
            "accessType": "common",
            "companyId": COMPANY_ID
        }
        return self.session.post(url, json=json_data)

    def delete_project(self, project_id):
        """Удалить проект"""
        url = f"{self.base_url}/projects/{project_id}"
        return self.session.delete(url)
