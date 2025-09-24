# api/client.py
import requests
from config.test_data import API_KEY, COMPANY_ID


class APIClient:
    def __init__(self):
        self.session = requests.Session()
        # Правильный URL из документации
        self.base_url = "https://ru.yougile.com/api-v2"
        self.session.headers.update({
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        })

    def get_projects(self):
        """GET /projects"""
        url = f"{self.base_url}/projects"
        params = {"companyId": COMPANY_ID}
        return self.session.get(url, params=params)

    def create_project(self, name):
        """POST /projects"""
        url = f"{self.base_url}/projects"
        json_data = {
            "name": name,
            "accessType": "common",
            "companyId": COMPANY_ID
        }
        return self.session.post(url, json=json_data)

    def delete_project(self, project_id):
        """DELETE /projects/{id}"""
        url = f"{self.base_url}/projects/{project_id}"
        return self.session.delete(url)
