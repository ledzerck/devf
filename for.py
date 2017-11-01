#!/usr/bin/python
# -*- coding: utf-8 -*-

# itera elementos como (listas, cadenas, range)



'''
var = "HOLA"
for i in var:
    print("La letras que representa i es: " + i)

print ("Se acabó")



for i in range(1,10):
    print(i)

print ("Se acabó")
'''

# Cuantos múltiplos de 2 hay en una cuenta del 1 al 100

print("----------------\n \"Contador\" Múltiplos de dos")
cuenta = 0
for i in range(1,100):
    if i % 2 == 0:
        cuenta += 1

print(cuenta)


print("----------------\n \"Acumulador\" ")
suma = 0
for i in range(1,5):
    print(i)
    suma += i

print("Resultado:", suma)
