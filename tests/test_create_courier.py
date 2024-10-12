import requests
import allure

from helpers.generators import generate_courier_data
from constants import Url
from helpers.helpers import delete_courier, courier_login



@allure.feature("Создание курьера")
class TestCreateCourier:



    @allure.title("Создание курьера c корректными данными")
    def test_create_courier(self, create_and_delete_courier):
        payload = {
            "login": create_and_delete_courier["login"],
            "password": create_and_delete_courier["password"],
        }
        with allure.step("Создание курьера с полным набором корректных данных"):
            response = requests.post(f"{Url.SERVICE_URL}{Url.LOGIN_URL}", data=payload)
        response_json = response.json()
        courier_id = courier_login(payload["login"], payload["password"]).json()["id"]


        assert response.status_code == 200

    @allure.title("Создание курьера c существующим логином")
    def test_create_courier_duplicate_login(self, create_and_delete_courier):

        payload_1 = {
            "login": create_and_delete_courier["login"],
            "password": create_and_delete_courier["password"], "first_name": create_and_delete_courier["first_name"],
        }

        courier2_data = generate_courier_data()

        payload_2 = {
            "login": payload_1["login"],
            "password": courier2_data["password"],
            "first_name": courier2_data["first_name"],
        }
        with allure.step(
            "Создание первого курьера с полным набором корректных данных"
        ):
            requests.post(f"{Url.SERVICE_URL}{Url.CREATE_COURIER_URL}", data=payload_1)
        with allure.step(
            "Создание второго курьера с логином как у первого курьера"
        ):
            response = requests.post(
                f"{Url.SERVICE_URL}{Url.CREATE_COURIER_URL}", data=payload_2
            )
        response_json = response.json()
        courier_id = courier_login(payload_1["login"], payload_1["password"]).json()[
            "id"
        ]

        assert (
            response.status_code == 409
            and response_json["message"] == "Этот логин уже используется. Попробуйте другой."
        )


    @allure.title("Проверка создания курьера без логина")
    def test_create_courier_without_login(self):
        courier_data = generate_courier_data()
        payload = {
            "login": "",
            "password": courier_data["password"],
            "first_name": courier_data["first_name"],
        }
        with allure.step("Создание курьера с пустым логином"):
            response = requests.post(
                f"{Url.SERVICE_URL}{Url.CREATE_COURIER_URL}", data=payload
            )
        response_json = response.json()
        assert response.status_code == 400 and (
            response_json["message"]
            == "Недостаточно данных для создания учетной записи"
        )

    @allure.title("Создание курьера без пароля")
    def test_create_courier_without_password(self):
        courier_data = generate_courier_data()
        payload = {
            "login": courier_data["login"],
            "password": "",
            "first_name": courier_data["first_name"],
        }
        with allure.step("Создание курьера с пустым паролем"):
            response = requests.post(
                f"{Url.SERVICE_URL}{Url.CREATE_COURIER_URL}", data=payload
            )
        response_json = response.json()

        assert (
            response.status_code == 400
            and response_json["message"]
            == "Недостаточно данных для создания учетной записи"
        )

    @allure.title("Создание курьера без имени")
    def test_create_courier_without_first_name(self, create_and_delete_courier_without_first_without_first_name):

        payload = {
            "login": create_and_delete_courier_without_first_without_first_name["login"],
            "password": create_and_delete_courier_without_first_without_first_name["password"],
            "first_name": create_and_delete_courier_without_first_without_first_name["first_name"],
        }
        with allure.step("Создание курьера с пустым именем"):
            response = requests.post(f"{Url.SERVICE_URL}{Url.LOGIN_URL}", data=payload)
        response_json = response.json()

        courier_id = courier_login(payload["login"], payload["password"]).json()["id"]


        assert response.status_code == 200

