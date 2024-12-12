import requests
import allure


@allure.title("Добавление задания ")
def test_add():
    with allure.step("Отправляем валидный запрос на создание задания"):
        body = {"title": "generated", "completed": False}
        response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)  # noqa: E501
        response_body = response.json()
    with allure.step("Проверяем статус код и тело ответа"):
        assert response.status_code == 201
        assert response_body['completed'] is False
        assert response_body['completed'] == False

@allure.title("Добавление задания с пустым телом")
def test_add_negative():
    with allure.step("Отправляем запрос на создание задания с пустым телом"):
        body = {"title": "", "completed": False}
        response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
        response_body = response.json()
    with allure.step("Проверяем статус код и тело ответа"):
        assert response.status_code == 200
        assert response_body['completed'] == None
