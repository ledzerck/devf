#!/usr/bin/python
# -*- coding: utf-8 -*-

# Escribir una función que reciba una lista de tuplas de dos elementos, y que devuelva un diccionario en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los segundos.


lista = [('Buenas','tardes'),('Buenas','noches'), ('Buenos','dias')]
diccionario = {}
resultado = []

def funcion(argumento):
    for x,y in argumento:
        valor_actual = diccionario.get(x, None)
        if valor_actual:
            resultado = [valor_actual, y]
            diccionario[x] = resultado
        else:
            diccionario.update({x: y})
    return diccionario


print(funcion(lista))



'''
lista = [('Buenas','tardes'),('Buenas','noches'), ('Buenos','dias')]
diccionario = {}
resultado = []

def funcion(argumento):
    for x,y in argumento:
        current_value = diccionario.get(x, None)
        if current_value:
            if type(current_value) is list:
                current_value.append(y)
            else:
                new_list = [current_value, y]
                diccionario[x] = new_list
        else:
            diccionario.update({x: y})
    return diccionario


print(funcion(lista))

'''





'''
lista = [('Buenas','tardes'),('Buenas','noches'), ('Buenos','dias')]
diccionario = {}
resultado = []

def funcion(argumento):
    for x,y in argumento:
        actual = diccionario.get(x, None)
        diccionario[x] = resultado
        if x in argumento:
            resultado.append(y)
        else:
            diccionario.update({x:y})
    return diccionario


print(funcion(lista))
'''


'''

lista = [('Buenas','tardes'),('Buenas','noches'), ('Buenos','dias')]
diccionario = {}
resultado = []

def funcion(argumento):
    for x,y in argumento:
        diccionario[x] = resultado
        if x in argumento
            resultado.append(y)
    return diccionario


print(funcion(lista))

'''




'''
lista = [('Buenas','tardes'),('Buenas','noches'), ('Buenos','dias')]
diccionario = {}
lista_result = []

for i in lista:
        print(i[0])
        diccionario[i[0]] = lista_result
        lista_result.append(i[1])

print(diccionario)
'''
