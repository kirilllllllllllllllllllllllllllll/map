import sys
from io import BytesIO

import requests
from PIL import Image


def load_map(name, spn=0.003, index=False, mode='map'):
    toponym_to_find = name
    delta = spn

    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        # обработка ошибочной ситуации
        pass

    # Преобразуем ответ в json-объект
    json_response = response.json()
    # Получаем первый топоним из ответа геокодера.
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    org_point = "{0},{1}".format(toponym_coodrinates[0], toponym_coodrinates[1])

    toponym_index = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
    if index:
        toponym_index = toponym_index + ', ' + toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([str(delta), str(delta)]),
        "l": mode,
        "pt": "{0},pm2dgl".format(org_point)
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    return (BytesIO(response.content), toponym_index)
