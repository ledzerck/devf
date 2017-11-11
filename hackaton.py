#!/usr/bin/python
# -*- coding: utf-8 -*-

print('----------------------------------------')
# Función que retorne los números primos del 0 al 100

for i in range(1,100):
    if i % 2 != 0:
        print(i)

print('----------------------------------------')
# Calcular el área de un triángulo equilátero de 5mts de altura y 10.3 mts de base
base = 10.3
altura = 5
area = (base*altura) / 2
print(area)


print('----------------------------------------')
# Cual es la palabra más larga y la más corta y cuántas letras tienen “Electroencefalografista”,”Electrodoméstico” , “Arteriosclerosis”,”Otorrinolaringólogo”

lista = ['Electroencefalografista', 'Electrodoméstico', 'Arteriosclerosis', 'Otorrinolaringólogo']

mayor = 0
for i in range(0, len(lista)):
    if len(lista[i]) > mayor:
        textoMayor = lista[i]
        mayor = len(lista[i])
print("La palabra más larga es:")
print(textoMayor, "y tiene", mayor, "letras")


menor = mayor
for i in range(0, len(lista)):
    if len(lista[i]) < menor:
        textoMenor = lista[i]
        menor = len(lista[i])
print("La palabra más corta es:")
print(textoMenor, "y tiene", menor, "letras")


print('----------------------------------------')
# Cuales son palabras palíndromas? -Anita lava la tina, -A mi me mima, - Mi mama masa la masa en la mesa

palabras = ['Anita lava la tina', 'A mi me mima', 'Mi mama masa la masa en la mesa']

cadena = "Anita lava la tina"
cadena = cadena.replace(' ', '')
cadena = cadena.lower()
longitudCadena = len(cadena) // 2


if cadena == cadena[::-1]:
    print(cadena, "es palíndromo")
