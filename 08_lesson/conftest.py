import pytest
import base64
import requests


@pytest.fixture
def api_client():
    LOGIN = "super.operetta2013@mail.ru"
    PASSWORD = "29012002Vv."
    COMPANY_NAME = "SkyPro"
    BASE_URL = "https://ru.yougile.com"

    # Шаг 1: Получаем Base64 для Basic Auth
    credentials = f"{LOGIN}:{PASSWORD}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/json"
    }

    # Шаг 2: Получаем список компаний
    response = requests.get(f"{BASE_URL}/api-v2/companies", headers=headers)
    response.raise_for_status()
    companies = response.json()

    # Находим ID компании по названию
    company_id = None
    for company in companies:
        if company["name"] == COMPANY_NAME:
            company_id = company["id"]
            break

    if not company_id:
        raise Exception(f"Компания с именем '{COMPANY_NAME}' не найдена")

    # Шаг 3: Создаём API-ключ
    key_response = requests.post(
        f"{BASE_URL}/api-v2/auth/keys",
        headers=headers,
        json={"title": "Autotest Key", "companyId": company_id}
    )
    key_response.raise_for_status()
    api_key = key_response.json()["key"]

    # Возвращаем клиент с API-ключом
    from api_client import YouGileApiClient
    return YouGileApiClient(base_url=BASE_URL, api_key=api_key, company_id=company_id)


@pytest.fixture
def project_data():
    return {
        "title": "Test Project",
        "color": "#FF5733"
    }
