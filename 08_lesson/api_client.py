import requests


class YouGileApiClient:
    def __init__(self, base_url, api_key, company_id):
        self.base_url = base_url.rstrip("/")
        self.company_id = company_id
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        })

    def create_project(self, data):
        url = f"{self.base_url}/api-v2/projects"
        params = {"companyId": self.company_id}
        response = self.session.post(url, json=data, params=params)
        return response

    def update_project(self, project_id, data):
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        params = {"companyId": self.company_id}
        response = self.session.put(url, json=data, params=params)
        return response

    def get_project(self, project_id):
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        params = {"companyId": self.company_id}
        response = self.session.get(url, params=params)
        return response
