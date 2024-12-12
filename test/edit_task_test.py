import requests
import allure


@allure.title('Редактирование задачи')
def test_edit():
    body = {"title": "generated", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response.json().get("id")

    body = {"title": "generated-1"}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)  # noqa: E501
    assert response.status_code == 200

    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
    assert response.status_code == 200
    assert response.json()['title'] == "generated-1"
