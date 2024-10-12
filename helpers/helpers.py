import json
import allure
import requests
from constants import Url
from constants import Order


@allure.step("Логинимся курьером")
def courier_login(login, password):
    payload = {"login": login, "password": password}
    response = requests.post(f"{Url.SERVICE_URL}{Url.LOGIN_URL}", data=payload)
    return response


@allure.step("Удаляем курьера")
def delete_courier(id):
    requests.delete(f"{Url.SERVICE_URL}{Url.DELETE_COURIER_URL}{id}")


@allure.step("Отменяем заказ")
def cancel_order(id):
    payload = {"track": id}
    requests.put(f"{Url.SERVICE_URL}{Url.CANCEL_ORDER_URL}", data=payload)


@allure.step("Создаем заказ")
def order_create(color):
    Order.order_body["color"] = color
    payload = Order.order_body
    response = requests.post(
        f"{Url.SERVICE_URL}{Url.CREATE_ORDER_URL}", data=json.dumps(payload)
    )
    return response
