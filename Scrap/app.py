from bs4 import BeautifulSoup
import requests

# URL DEL sitio
URL = 'http://www.gandhi.com.mx/adolescentes'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# Muestra todos los elementos con la clase item
result_items = soup.find_all(class_='item')


print(result_items)

# itera en la lista que hicimos de result_items
for item in result_items:
    name = item.find('a')['title']
    print(name)
