import requests


def test_auth_valid_api_key():
    headers = {
        "Authorization": "Bearer pcSu72AF9B4kp9ApAoEhaLfdxOXekVPq2X6CJRfbgOPzstxK3HaE3fk5IV5ewrsE",
        "Content-Type": "application/json"
    }
    response = requests.get(
        "https://ru.yougile.com/api-v2/projects",
        headers=headers
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")

    assert response.status_code == 200
