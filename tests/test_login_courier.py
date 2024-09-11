import requests
import allure

from constants import Url


@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Проверка авторизации")
    def test_login(self, create_and_delete_courier):
        payload = {
            "login": create_and_delete_courier["login"],
            "password": create_and_delete_courier["password"],
        }
        with allure.step("Авторизация с полным набором данных"):
            response = requests.post(f"{Url.SERVICE_URL}{Url.LOGIN_URL}", data=payload)

        assert response.status_code == 200 and "id" in response.text

    @allure.title("Авторизация без логина")
    def test_login_without_login(self, create_and_delete_courier):
        payload = {"login": "", "password": create_and_delete_courier["password"]}
        with allure.step("Авторизация с пустым логином"):
            response = requests.post(f"{Url.SERVICE_URL}{Url.LOGIN_URL}", data=payload)
        response_json = response.json()

        assert (
            response.status_code == 400
            and response_json["message"] == "Недостаточно данных для входа"
        )

    @allure.title("Авторизация без пароля")
    def test_login_without_password(self, create_and_delete_courier):
        payload = {
            "login": create_and_delete_courier["login"],
            "password": "",
        }
        with allure.step("Авторизация с пустым паролем"):
            response = requests.post(f"{Url.SERVICE_URL}{Url.LOGIN_URL}", data=payload)
        response_json = response.json()

        assert (
            response.status_code == 400
            and response_json["message"] == "Недостаточно данных для входа"
        )

    @allure.title("Авторизация несуществующего пользователя")
    def test_login_non_existent_user(self, create_and_delete_courier):
        payload = {
            "login": create_and_delete_courier["login"],
            "password": create_and_delete_courier["login"],
        }
        with allure.step("Авторизация несуществующим пользователем"):
            response = requests.post(f"{Url.SERVICE_URL}{Url.LOGIN_URL}", data=payload)
        response_json = response.json()

        assert (
            response.status_code == 404
            and response_json["message"] == "Учетная запись не найдена"
        )
