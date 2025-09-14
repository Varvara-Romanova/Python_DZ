import requests


API_KEY = "pcSu72AF9B4kp9ApAoEhaLfdxOXekVPq2X6CJRfbgOPzstxK3HaE3fk5IV5ewrsE"
PROJECT_ID = "f0e6beed-3980-4798-b7e8-c07e0e68b363"


def test_get_project_positive():
    url = f"https://ru.yougile.com/api-v2/projects/{PROJECT_ID}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")

    assert response.status_code == 200
    json_data = response.json()
    assert json_data["id"] == PROJECT_ID
    assert json_data["title"] == "Updated SkyPro"


def test_update_project_positive():
    url = f"https://ru.yougile.com/api-v2/projects/{PROJECT_ID}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {"title": "Updated SkyPro"}
    response = requests.put(url, json=data, headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")

    assert response.status_code == 200
    json_data = response.json()
    assert "id" in json_data, "Ответ должен содержать ID"
