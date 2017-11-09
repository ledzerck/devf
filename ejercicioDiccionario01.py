#!/usr/bin/python
# -*- coding: utf-8 -*-

# Escribir una función que reciba una lista de tuplas de dos elementos, y que devuelva un diccionario en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los segundos.


lista = [('Buenas','tardes'),('Buenas','noches'), ('Buenos','dias')]
diccionario = {}
lista_result = []

for i in lista:
        print(i[0])
        diccionario[i[0]] = lista_result
        lista_result.append(i[1])

#def tuplas_a_diccionario(holi):
    # No se que hacer :(

print(diccionario)
