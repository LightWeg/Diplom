# Соломахина Ирина, 35-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import sending_requests

# запрос на получения заказа по треку заказа.
def get_order_track_status_code():
    response_code = sending_requests.post_new_order(data.order_body)
    track = response_code.json()["track"]
    return sending_requests.get_order_track(track).status_code

# Проверка, что код ответа равен 200.
def test_get_order_track_code_200():
    assert get_order_track_status_code() == 200
