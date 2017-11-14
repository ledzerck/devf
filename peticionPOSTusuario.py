import requests

BASE_URL = "https://goodreads-devf-aaron.herokuapp.com/api/v1"

def mi_peticion_post(email,passW):
    URI = "/users/"
    URL = BASE_URL + URI
    json_send = {
        "email": email,
        "password": passW
    }

    response = requests.post(URL,json=json_send)

    return response

respuesta = mi_peticion_post("Aldo", "siQueSi")
print(respuesta.status_code)
print(respuesta.json())
