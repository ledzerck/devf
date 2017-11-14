import requests

BASE_URL = "https://goodreads-devf-aaron.herokuapp.com/api/v1"

def mi_peticion_post(nombre,apellidos,bio,edad):
    URI = "/authors/"
    URL = BASE_URL + URI
    json_send = {
        "name": nombre,
        "last_name": apellidos,
        "nacionalidad": "MX",
        "biography": bio,
        "gender": "M",
        "age": edad
    }

    response = requests.post(URL,json=json_send)

    return response

respuesta = mi_peticion_post("Wasol", "González", "Oh baby I love your way", 36)
print(respuesta.status_code)
print(respuesta.json())
