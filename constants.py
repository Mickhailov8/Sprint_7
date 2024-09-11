class Url:
    SERVICE_URL = "https://qa-scooter.praktikum-services.ru"
    LOGIN_URL = "/api/v1/courier/login"
    CREATE_COURIER_URL = "/api/v1/courier"
    DELETE_COURIER_URL = "/api/v1/courier/"
    CANCEL_ORDER_URL = "/api/v1/orders/cancel"
    CREATE_ORDER_URL = "/api/v1/orders"




class Order:
    order_body = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [],
    }

    scooter_colors = ["[]", '["BLACK"]', '["GREY"]', '["BLACK", "GREY"]']