import requests
base_url="https://ru.yougile.com/api-v2"
TOKEN = "u4NTxzUYyec3GIwvhaVcTYgKmLsBR0pBg7KvYf3-bF1Hu-GskqQhOWfXFgAanX-w"
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

# метод post
# позитивный
def test_create_project_post():
    body = {
        "title": "Компания Мечта"
    }
    resp = requests.post(base_url + '/projects', json=body, headers=HEADERS)
    assert resp.status_code == 201

# негативный
# Пустое название проекта, должна быть ошибка валидации
def test_create_project_post_negative():
    body_empty = {
    "title": ""
    }
    resp_empty = requests.post(base_url + '/projects', json=body_empty, headers=HEADERS)

    response_data = resp_empty.json()  # Сохраняем ответ для многократного использования

    assert resp_empty.status_code == 400, (
    f"Ожидался 400 для пустого названия, получен {resp_empty.status_code}"
    )
    assert "error" in response_data and response_data["error"] == "Bad Request", (
    "В ответе нет ожидаемого поля 'error': 'Bad Request'"
    )
    assert any("title" in msg.lower() for msg in response_data["message"]), (
    "В сообщении об ошибке нет упоминания поля 'title'"
    )

# метод put
# позитивный
def get_test_project_id():
    print("Создаю тестовый проект...")
    body = {"title": "Тестовый проект для обновления"}
    resp = requests.post(f"{base_url}/projects", json=body, headers=HEADERS)
    print(f"Статус создания проекта: {resp.status_code}")
    print(f"Ответ сервера: {resp.text}")
    assert resp.status_code == 201
    return resp.json()["id"]

def test_update_project_put_positive():
    project_id = get_test_project_id()
    new_title = "Обновлённое название проекта"
    body = {"title": new_title}

    # 1. Отправляем PUT-запрос
    resp = requests.put(
        f"{base_url}/projects/{project_id}",
        json=body,
        headers=HEADERS
    )
    assert resp.status_code == 200, f"Ожидался 200, получен {resp.status_code}"

    # 2. Проверяем, что обновление применилось (через GET)
    get_resp = requests.get(
        f"{base_url}/projects/{project_id}",
        headers=HEADERS
    )
    assert get_resp.status_code == 200, "Не удалось получить проект после обновления"

    updated_data = get_resp.json()

    assert updated_data["title"] == new_title, (
        f"Название не обновилось. Ожидалось: {new_title}, "
        f"получено: {updated_data.get('title', 'поле отсутствует')}"
    )

    print("Тест пройден: проект успешно обновлён.")

    # негативные
def test_update_project_put_negative():

    # 1. Невалидный ID проекта → ожидаем 404
    invalid_id = "99999"
    body_valid = {"title": "Новое название"}

    resp_404 = requests.put(
        f"{base_url}/projects/{invalid_id}",
        json=body_valid,
        headers=HEADERS
    )
    assert resp_404.status_code == 404, (
        f"Ожидался 404 для невалидного ID, получен {resp_404.status_code}"
    )

    # 2. Пустое название → ожидаем 400 (валидация)
    body_empty = {"title": ""}
    project_id = "12345"  # Замените на актуальный ID

    resp_400 = requests.put(
        f"{base_url}/projects/{project_id}",
        json=body_empty,
        headers=HEADERS
    )
    assert resp_400.status_code == 400, (
        f"Ожидался 400 для пустого названия, получен {resp_400.status_code}"
    )

    # Проверяем, что в ответе есть упоминание ошибки по полю title
    response_400 = resp_400.json()
    assert any("title" in str(err).lower() for err in response_400.get("message", [])), (
        "В ответе нет ошибки по полю 'title' при пустом значении"
    )

    # 3. Отсутствие заголовка Authorization → ожидаем 401 или 403
    resp_no_auth = requests.put(
        f"{base_url}/projects/{project_id}",
        json=body_valid,
        headers={}  # Пустые заголовки
    )
    assert resp_no_auth.status_code in [401, 403], (
        f"Ожидался 401/403 без токена, получен {resp_no_auth.status_code}"
    )

    # 4. Невалидный токен → ожидаем 401 или 403
    invalid_headers = {"Authorization": "Bearer invalid_token_123"}
    resp_invalid_token = requests.put(
        f"{base_url}/projects/{project_id}",
        json=body_valid,
        headers=invalid_headers
    )
    assert resp_invalid_token.status_code in [401, 403], (
        f"Ожидался 401/403 для невалидного токена, получен {resp_invalid_token.status_code}"
    )

    print("Негативный тест пройден: все ошибочные сценарии обработаны корректно.")

# метод get

import requests

base_url = "https://ru.yougile.com/api-v2"
# TOKEN = "u4NTxzUYyec3GIwvhaVcTYgKmLsBR0pBg7KvYf3-bF1Hu-GskqQhOWfXFgAanX-w"
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

def create_test_project():
    """Создаёт проект и возвращает его ID."""
    body = {"title": "Тестовый проект для GET-теста"}
    resp = requests.post(
        f"{base_url}/projects",
        json=body,
        headers=HEADERS,
        timeout=10
    )
    assert resp.status_code == 201, (
        f"Не удалось создать проект: {resp.status_code} {resp.text}"
    )
    return resp.json()["id"]


def test_get_project_by_id_positive():

    # 1. Создаём проект и получаем ID
    project_id = create_test_project()
    print(f"Создан проект с ID: {project_id}")

    # 2. Отправляем GET-запрос
    resp = requests.get(
        f"{base_url}/projects/{project_id}",
        headers=HEADERS,
        timeout=10
    )

    # 3. Проверяем статус
    assert resp.status_code == 200, (
        f"Ожидался 200, получен {resp.status_code}. Ответ: {resp.text}"
    )

    # 4. Парсим ответ
    response_data = resp.json()

    # 5. Проверяем обязательные поля
    assert "id" in response_data, "Нет поля 'id' в ответе"
    assert "title" in response_data, "Нет поля 'title' в ответе"
    assert "timestamp" in response_data, "Нет поля 'timestamp' в ответе"  # Исправлено!

    # 6. Проверяем соответствие ID
    assert str(response_data["id"]) == str(project_id), (
        f"ID не совпадает: ожидался {project_id}, получен {response_data['id']}"
    )

    # 7. Проверяем title
    expected_title = "Тестовый проект для GET-теста"
    assert response_data["title"] == expected_title, (
        f"title не совпадает: ожидался '{expected_title}', получен '{response_data['title']}'"
    )

    # 8. Проверяем timestamp (должен быть числом > 0)
    assert isinstance(response_data["timestamp"], int), "timestamp должен быть целым числом"
    assert response_data["timestamp"] > 0, "timestamp должен быть положительным"

    print("Позитивный тест пройден: проект успешно получен по ID.")


# негативный
def test_get_project_by_id_negative():

    # 1. Невалидный ID (проект не существует)
    invalid_id = "999999999"
    resp_404 = requests.get(
        f"{base_url}/projects/{invalid_id}",
        headers=HEADERS,
        timeout=10
    )
    assert resp_404.status_code == 404, (
        f"Ожидался 404, получен {resp_404.status_code}. Ответ: {resp_404.text}"
    )
    assert "message" in resp_404.json(), "Нет поля 'message' в ответе 404"
    assert "Проект не найден" in resp_404.json()["message"], (
        "Неверное сообщение об ошибке для 404"
    )

    # 2. Отсутствие заголовка Authorization
    resp_no_auth = requests.get(
        f"{base_url}/projects/12345",
        headers={},  # Пустые заголовки
        timeout=10
    )
    assert resp_no_auth.status_code in [401, 403], (
        f"Ожидался 401/403, получен {resp_no_auth.status_code}"
    )

    # 3. Невалидный токен
    invalid_headers = {"Authorization": "Bearer invalid_token_123"}
    resp_invalid_token = requests.get(
        f"{base_url}/projects/12345",
        headers=invalid_headers,
        timeout=10
    )
    assert resp_invalid_token.status_code in [401, 403], (
        f"Ожидался 401/403, получен {resp_invalid_token.status_code}"
    )

    # 4. Некорректный формат ID (строка вместо числа)
    malformed_id = "abcde"
    resp_400 = requests.get(
        f"{base_url}/projects/{malformed_id}",
        headers=HEADERS,
        timeout=10
    )
    assert resp_400.status_code in [400, 404], (
        f"Ожидался 400/404, получен {resp_400.status_code}"
    )

    print("Негативный тест пройден: все ошибочные сценарии обработаны.")



