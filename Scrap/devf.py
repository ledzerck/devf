from bs4 import BeautifulSoup
import requests

# URL DEL sitio
URL = 'https://devf.mx'

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# Muestra todos los elementos con la clase item
result_items = soup.find_all(class_='program-item')


# print(result_items)

# itera en la lista que hicimos de result_items
for item in result_items:
    name = item.find('h3').text
    print(name)
