import requests

'''
# Recibe varios parámetros: url,
response = requests.get('https://api.github.com/users/ledzerck')
print(response.status_code)
print(response.ok)

# Puedes pedir un elemento en específico entre corchetes []
print(response.headers['Server'])
print(response.text)
'''



response = requests.get('http://api.open-notify.org/iss-now.json')
print(response.status_code)
print(response.ok)

# Puedes pedir un elemento en específico entre corchetes []
print(response.headers)
print(response.text)

diccionario = response.json()
print(diccionario['timestamp'])
