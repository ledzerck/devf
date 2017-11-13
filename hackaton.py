#!/usr/bin/python
# -*- coding: utf-8 -*-

print('----------------------------------------')
# 1. Función que retorne los números primos del 0 al 100

listaPrimos = []
for i in range(2,101):
    if (i%2!=0 or i==2) and (i%3!=0 or i==3) and (i%5!=0 or i==5) and (i%7!=0 or i==7):
        listaPrimos.append(i)
print(listaPrimos)

print('----------------------------------------')
# 2. Calcular el área de un triángulo equilátero de 5mts de altura y 10.3 mts de base
base = 10.3
altura = 5
area = (base*altura) / 2
print(area)


print('----------------------------------------')
# 3. Cual es la palabra más larga y la más corta y cuántas letras tienen “Electroencefalografista”,”Electrodoméstico” , “Arteriosclerosis”,”Otorrinolaringólogo”

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
# 4. Cuales son palabras palíndromas? -Anita lava la tina, -A mi me mima, - Mi mama masa la masa en la mesa

palabras = ['Anita lava la tina', 'A mi me mima', 'Mi mama masa la masa en la mesa']
palindromos = []

for i in range(0,len(palabras)):
    cadena = palabras[i]
    cadena = cadena.replace(' ', '')
    cadena = cadena.lower()
    if cadena == cadena[::-1]:
        palindromos.append(cadena)

print(palindromos)


print('----------------------------------------')
# 5. En el año 2009 viajé a Europa y a Estados Unidos. Voy a Europa cada 5 años y a Estados Unidos cada 2 años. ¿Cuál será el próximo año que realizaré ambos viajes?


viaje = 2009
europa = 2
eua = 4

if europa > eua:
    mayorNum = europa
else:
    mayorNum = eua

if mayorNum % europa == 0 and mayorNum % eua == 0:
    comun = mayorNum
else:
    while mayorNum % europa != 0 or mayorNum % eua != 0:
        mayorNum += 1

viaje += mayorNum

print("Realizarás ambos viajes en:")
print(viaje)




print('----------------------------------------')
# 6. Tengo 1 ½ litros de leche para servir en vasitos de  1/8 litro cada uno, la misma cantidad de leche en cada vasito. ¿Cuántos vasitos necesito?

litros = 1+(1/2)
vasitos = 1/8

cuantosVasos = int(litros // vasitos)
print("El número de vasitos que necesitas es:")
print(cuantosVasos)



print('----------------------------------------')
# 7. Una piscina olímpica de 2,5 millones de litros de agua está llena al 95% de su capacidad. Se calcula que se evaporará una cantidad de agua correspondiente al 5% de su capacidad total. Calcular cuántos litros se van a evaporar.

# se hace el cálculo sobre la capacidad total, es lo que dice el problema...
evaporada = int(2500000 * .05)
print("Los litros que se van a evaporar son:")
print(evaporada)


print('----------------------------------------')
# 8. ¿Cuál es la respuesta a
# El sentido de la vida, el universo y todo lo demás?

pi= 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550522317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091

sentido = int(pi) * 2 * 7
universo = int(round(pi,1) * 360)
dias_sin_ella = 1060 + len("Valiendo verga")
demas = dias_sin_ella
sentido = universo - demas

if sentido != 42:
    print("Estás chavo, vete a comer buebito con catsu")
else:
    print(sentido)


print('----------------------------------------')
# 9. La fecha y hora actual de Bucarest, Rumania con formato ‘YYYY-MM-DD HH:mm’

import time

hora = time.strftime("%y-%m-%d %H:%M")
print(hora)
