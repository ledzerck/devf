#!/usr/bin/python
# -*- coding: utf-8 -*-


########################## PROBLEMA 1

print("Prógrama que pida dos numeros enteros y que calcule su division, escribiendo si la division es exacta o no\n")

x = int(input("Escribe un numero:\n"))
y = int(input("Escribe otro numero para dividir: \n"))
resultado = x/y

print("El resultado es: " + str(resultado))

residuo = x%y

if residuo == 0:
    print("Es entero")
else:
    print("Es flotante")

print("\n------------------\n")


################################### PROBLEMA 2

print("Programa que pida 2 numeros y que conteste cual es el menor y cual es el mayor o que escriba que son iguales\n")

a = int(input("Escribe un numero A: \n"))
b = int(input("Escribe otro numero B: \n"))

if a > b:
    print("El numero A es mayor")
elif a == b:
    print("Los numeros son iguales")
else:
    print("El numero B es mayor")


print("\n------------------\n")



#################################### PROBLEMA 3

print("Escriba un programa que pida el ano actual y un ano cualquiera y que escriba cuantos anos han pasado desde ese ano o cuantos anos faltan para llegar a ese ano\n")

anoactual = int(input("Escribe el anio actual: \n"))
anoviejo = int(input("Escribe otro anio: \n"))

if anoactual > anoviejo:
    operacion = anoactual-anoviejo
    print("Han pasado " + str(operacion) + " anios")
else:
    operacion = anoviejo-anoactual
    print("Faltan " + str(operacion) + " anios")





print("\n------------------\n")



###################################### PROBLEMA 4

print("Escribe un programa que pida tres numeros y que escriba si son los 3 iguales, si hay dos iguales o si los 3 son distintos\n")

f = int(input("Escribe un numero F: \n"))
g = int(input("Escribe un numero G: \n"))
h = int(input("Escribe un numero H: \n"))

if f == g and g == h:
    print("Los 3 son iguales")
elif f == g or f == h or h == f:
    print("hay 2 iguales")
else:
    print("Todos son diferentes")


print("\n------------------\n")

##################################### PROBLEMA 5

print("Pedir 3 numeros y obtener el mayor de ellos\n")

o = int(input("Escribe un numero O: \n"))
p = int(input("Escribe un numero P: \n"))
q = int(input("Escribe un numero Q: \n"))


if o > p and o > q:
    print("El numero O es el mayor")
elif p > o and p > q:
    print("El numero P es el mayor")
else:
    print("El numero Q es el mayor")
