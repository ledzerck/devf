import requests

# Como buena práctica podemos separar la URL base, y la URI en variables

# Que devuelva también todos sus movimientos
#jsonEditorOnline

num_poke = str(input("Dame un número de pokemon \n"))

def tomaPokemon(pokemon):
    BASE_URL = "http://pokeapi.co/api/v2/"
    URI_POKEMON_1 = "pokemon/" + pokemon
    URL = BASE_URL + URI_POKEMON_1

    response = requests.get(URL)
    diccionario = response.json()

    resultado = diccionario['forms'][0]['name']
#    resultado = diccionario['moves'][0]['move']['name']

    for i in range(0,len(diccionario['moves'])):
        print(diccionario['moves'][i]['move']['name'])

    return resultado

x = tomaPokemon(num_poke)
print(x)

#print(diccionario['game_indices'][13]['version']['name'])
