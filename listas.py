#!/usr/bin/python
# -*- coding: utf-8 -*-

# Las listas pueden tener métodos


list1 = [2,3,1,4,5]
list2 = ["A", "B", "C", "D"]
list3 = ["MATEMÁTICAS", "HISTORIA", 1999, 8983]

print(list1)
print(list2)
print(list3)


# append agrega un item al final de la lista

frutas = ['naranja', 'manzana', 'pera', 'fresa', 'banana', 'manzana', 'kiwi']
print(frutas)

frutas.append('uva')
print("append")
print(frutas)

# extend agrega varios elementos al final de la lista

frutas.extend(list2)
print("extend")
print(frutas)

#insert agrega un elemento en la posición que indiquemos

frutas.insert(0, 'melon')
print("insert")
print(frutas)

# pop saca el último elemento de la lista o la posición que se indique

frutas.pop(3)
print("pop")
print(frutas)


# remove elimina un elemento por su valor

frutas.remove("manzana")
print("remove")
print(frutas)


# invierte los elementos de una listas

frutas.reverse()
print("reverse")
print(frutas)


# sort ordena la lista de forma ascendente alfabéticamente

frutas.sort() # frutas.sort(reverse = True)
print("sort")
print(frutas)


# count cuenta el número de elementos de una pila

frutas.count("manzana")
print("count")
print(frutas.count("manzana"))



# index devuelve en que posición de la lista se encuentra el elemento

print("index")
print(frutas.index("naranja"))
