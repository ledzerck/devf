import requests

def tomaAutores():

    BASE_URL = "https://goodreads-devf-aaron.herokuapp.com"
    URI = "/api/v1/authors/"
    URL = BASE_URL + URI

    response = requests.get(URL)

    diccionario = response.json()

    resultado = diccionario[0]['name']

    for i in range(0, len(diccionario)):
        print (diccionario[i]['name'], diccionario[i]['last_name'])
        print (diccionario[i]['biography'])
        print ('------------------------------------------------')


    return resultado

x = tomaAutores()
print(x)



'''
def tomaAutores():

    BASE_URL = "https://goodreads-devf-aaron.herokuapp.com"
    URI = "/api/v1/authors/"
    URL = BASE_URL + URI

    response = requests.get(URL)
    lista_jsons = response.json()
    for i in lista_jsons:
        print(i)

tomaAutores()
'''
