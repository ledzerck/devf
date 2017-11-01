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
print(frutas)

# extend agrega varios elementos al final de la lista

frutas.extend(list2)
print(frutas)

#insert agrega un elemento en la posición que indiquemos

frutas.insert(0, 'melon')
print(frutas)
