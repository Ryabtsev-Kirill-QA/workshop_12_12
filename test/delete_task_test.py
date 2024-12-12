import allure
import requests


@allure.title('Удаление задачи')
def test_delete():
    body = {"title": "generated", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)

    response.json().get("id")
    response = requests.delete(f'https://todo-app-sky.herokuapp.com/{id}')
    assert response.status_code == 204
