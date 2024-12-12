import allure
import requests


def test_delete():
    body = {"title": "generated", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]

    response = requests.delete(f'https://todo-app-sky.herokuapp.com/{id}')

    assert response.status_code == 204


@allure.title("Удаление несуществующей задачи")
def test_delete_negative():
    with allure.step("Отправляем валидный запрос на создание задания"):
        body = {"title": "generated", "completed": False}
        response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
        id = 123123123123
    with allure.step("Отправляем валидный запрос на создание задания"):
        response = requests.delete(f'https://todo-app-sky.herokuapp.com/{id}')

    assert response.status_code == 404
