cuantos = int(input("¿Cuantos valores quieres introducir?"))
valor = []

if cuantos <= 0:
    print("Seas mamon")
    cuantos = int(input("¿Cuantos valores quieres introducir?"))
else:
    for i in range(cuantos):
        escribe = int(input("Escribe un valor\n"))
        valor.append(escribe)

pares = 0
impares = 0

listapares = []
listaimpares = []

for i in valor:
    if i % 2 == 0:
        listapares.append(i)
        pares +=1
    if i % 2 != 0:
        listaimpares.append(i)
        impares +=1

print("\nTienes",pares,"numeros pares y",impares,"impares")
print("\nLos pares son:",listapares)
print("\nLos impares son:",listaimpares,"\n")
