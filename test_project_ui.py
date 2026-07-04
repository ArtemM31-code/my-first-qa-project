# === ТВОИ АВТОТЕСТЫ ДЛЯ WEB UI (test_project_ui.py) ===
#
# Наш локальный сервер app.py работает по адресу: http://localhost:5000
#
# ==========================================
# ЗАДАНИЕ 1: Проверка отображения дефолтных задач
# 1. Импортируй requests.
# 2. Напиши тест-функцию test_ui_default_tasks_visible(page):
# 3. Перейди на адрес: http://localhost:5000
# 4. Проверь с помощью assert, что заголовок вкладки равен "Todo App".
#    (Подсказка: assert page.title() == "Todo App")
# 5. Проверь с помощью assert, что текст списка задач (селектор "#task-list") содержит "Buy milk" и "Learn Python".
#    (Подсказка: tasks_text = page.locator("#task-list").inner_text()
#               assert "Buy milk" in tasks_text)
#
# ==========================================
# ЗАДАНИЕ 2: Сквозной E2E-тест (Интеграция API и UI)
# Давай сделаем то, что делают на реальных проектах:
# 1. Напиши тест-функцию test_ui_e2e_integration(page):
# 2. Создай переменную с уникальным текстом задачи, например: "Task created by API"
# 3. Отправь POST-запрос через библиотеку requests на адрес "http://localhost:5000/api/tasks"
#    с JSON-телом: {"task": unique_task}
# 4. Открой в браузере (через page.goto) адрес "http://localhost:5000"
# 5. Проверь через assert, что созданная тобой задача отобразилась на экране (внутри "#task-list").
#
# Пиши код ниже:
import requests
def test_ui_default_tasks_visible(page):
    page.goto("http://localhost:5000/")
    assert page.title() == "Todo App"
    tasks_text = page.locator("#task-list").inner_text()
    assert "Buy milk" and "Learn Python" in tasks_text

def test_ui_e2e_integration(page):
    task = "Task created by Api"
    response = requests.post("http://localhost:5000/api/tasks", json={"task": task})
    page.goto("http://localhost:5000/")
    tasks_text = page.locator("#task-list").inner_text()
    assert task in tasks_text
