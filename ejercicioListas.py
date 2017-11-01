#Ingresa 100 valores en una lista y después imprímelo
valores = []
for i in range(1,101):
    valores.append(i)

print(valores)

print("\n-------------------------------\n")


# Pide un numero por teclado y guarda en una lista su tabla de multiplicar hasta 10

teclado = input("Dame un valor y te muestro su tabla de multiplicar")
valor = []

if teclado.isdigit():
    for i in range(1,11):
        valor.append(int(teclado) * i)
else:
    print("no seas necio")
print(valor)


# Suma los elementos de las siguientes dos listas [4,76,3,12,65,3] y [234,222,523,65]

print("\n-------------------------------\n")

lista1 = [4,76,3,12,65,3]
lista2 = [234,222,523,65]
lista1.extend(lista2)

suma = 0
for i in lista1:
    suma += i

print("La suma de las 2 listas es",suma)
