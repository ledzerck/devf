import requests

def funcion():
    BASE_URL = "https://maps.googleapis.com/maps/api/directions/"
    URI = "json?origin=Marketing+Capacitacion,+MX&destination=Estela+de+luz+MX&key=AIzaSyD7SYo_K1nRimkiAbYFCpjFp5-npqINDVw"
    URL = BASE_URL + URI

    response = requests.get(URL)
    diccionario = response.json()

    print(diccionario)
    print(response.status_code)



funcion()
