# === ТВОИ АВТОТЕСТЫ ДЛЯ API (test_project_api.py) ===
#
# Наш локальный сервер app.py работает по адресу: http://localhost:5000
# Он имеет эндпоинт GET и POST по адресу: http://localhost:5000/api/tasks
#
# ==========================================
# ЗАДАНИЕ 1: Проверка получения списка задач (GET)
# 1. Импортируй requests.
# 2. Напиши тест-функцию test_api_get_tasks():
# 3. Отправь GET-запрос на адрес: http://localhost:5000/api/tasks
# 4. Проверь с помощью assert, что статус-код ответа равен 200.
# 5. Переведи ответ в JSON: data = response.json()
# 6. Проверь с помощью assert, что ключ "tasks" есть в словаре data.
#
# ==========================================
# ЗАДАНИЕ 2: Проверка создания задачи (POST)
# 1. Напиши тест-функцию test_api_create_task():
# 2. Создай словарь с данными задачи payload: {"task": "My test task"}
# 3. Отправь POST-запрос на адрес: http://localhost:5000/api/tasks, передав json=payload.
# 4. Проверь с помощью assert, что статус-код ответа равен 201.
# 5. Проверь, что в JSON-ответе (response.json()) статус ("status") равен "success".
#
# Пиши код ниже:
import pytest
import requests

def test_api_get_tasks():
    response = requests.get("http://localhost:5000/api/tasks")
    assert response.status_code == 200
    data = response.json()
    assert "tasks" in data

def test_api_create_task():
    payload = {"task": "My test task"}
    response = requests.post("http://localhost:5000/api/tasks", json=payload)
    assert response.status_code == 201
    assert (response.json()["status"] == "success")
