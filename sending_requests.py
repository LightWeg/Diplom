import requests
import configuration
import data

# создание заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         headers=data.headers,
                         json=order_body)

# получение заказа по номеру трекера
def get_order_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER + '?t=' + str(track),
                        headers=data.headers)
