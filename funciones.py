#!/usr/bin/python
# -*- coding: utf-8 -*-

separador = "------------------------------------"

def mi_funcion():
    print("Baia baia")

mi_funcion()

########################################
print(separador)

# Parámetro y parámetro con un valor por default
def sumando(num1,num2):
    suma = num1 + num2
    print(str(suma))

sumando(3,5)


#############################################
print(separador)


def funcion_return():
    palabra = "HOLA, ESTO RETORNÓ"
    return palabra

frase = funcion_return()
print(frase)

####################################################
print(separador)

def multiplicacion(num1,num2):
    multi = num1 * num2
    return multi

multiplicar = multiplicacion(2,2)
print(multiplicar)


##################################################
print(separador)

def funcion_numeros(num1):
    if num1 == 2:
        return "Tu número es 2"
    else:
        return "Tu número no es 2"

numero = funcion_numeros(1)
print(numero)
