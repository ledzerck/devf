#!/usr/bin/python
# -*- coding: utf-8 -*-

# Programa que calcule cuantas letras y cuantos digitos tiene una palabra

cadena = str(input("Dame una cadena alfanumérica \n")).lower()

numeros = ["0","1","2","3","4","5","6","7","8","9"]
letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
especiales = numeros + letras

numero = 0
for i in cadena:
    if i in numeros:
        numero += 1

letra = 0
for i in cadena:
    if i in letras:
        letra += 1

especial = 0
for i in cadena:
    if i not in especiales:
        especial += 1

print("Tu cadena tiene ")
print(str(numero) + " numeros")
print(str(letra) + " letras")
print("y " + str(especial) + " caracteres especiales")
