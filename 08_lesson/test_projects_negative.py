import requests


API_KEY = "pcSu72AF9B4kp9ApAoEhaLfdxOXekVPq2X6CJRfbgOPzstxK3HaE3fk5IV5ewrsE"
INVALID_ID = "invalid-id-123"


def test_create_project_negative_missing_title():
    """
    Негативный тест: создание проекта без поля title
    Ожидается: 400
    """
    url = "https://ru.yougile.com/api-v2/projects"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {"color": "#FF5733"}  # нет title
    response = requests.post(url, json=data, headers=headers)

    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")

    assert response.status_code == 400, (
        f"Ожидался 400, получен {response.status_code}"
    )
    assert "title" in str(response.json()).lower(), (
        "Должна быть ошибка по обязательному полю 'title'"
    )


def test_get_project_negative_not_found():
    """
    Негативный тест: получение несуществующего проекта
    Ожидается: 404
    """
    url = f"https://ru.yougile.com/api-v2/projects/{INVALID_ID}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)

    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")

    assert response.status_code == 404, (
        f"Ожидался 404, получен {response.status_code}"
    )


def test_update_project_negative_invalid_id():
    """
    Негативный тест: изменение проекта с невалидным ID
    Ожидается: 404
    """
    url = f"https://ru.yougile.com/api-v2/projects/{INVALID_ID}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {"title": "Fake"}
    response = requests.put(url, json=data, headers=headers)

    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")

    assert response.status_code == 404, (
        f"Ожидался 404, получен {response.status_code}"
    )
