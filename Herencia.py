from Perro import Perro
from Pajaro import Pajaro

perrito = Perro('Pug','blanco', 'Pugtato')
ladrar = perrito.ladrar()
print(ladrar)

comiendo = perrito.comer()
print(comiendo)

color = perrito.get_color()
print(color)

print("------------------")

pajarito = Pajaro('Quetzal','azul', 'Dimitri')
volar = pajarito.volar()
comiendo_pajarito = pajarito.comer()
color_pajarito = pajarito.get_color()


print(volar)
print(comiendo_pajarito)
print(color_pajarito)

# Liskov sustitution

def jauria(Animal):
    return Animal.comer()

print(jauria(perrito))
