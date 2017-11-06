palabras = int(input("¿Cuántas palabras tiene la lista? \n"))

nombres = []
if palabras > 0:
    for i in range(1,palabras+1):
        nombre= input("Ingresa la palabra " + str(i) + ": \n").upper()
        nombres.append(nombre)
    print("\n----------------------------\n")
    print(nombres)
else:
    print("No seas necio")



print("Tu lista tiene", len(nombres), "elementos")

print("\n----------------------------\n")

buscar = input("Que palabra quieres buscar\n").upper()

if nombres.count(buscar) <= 1:
    print("\n----------------------------\n")
    print("La palabra", buscar, "aparece", nombres.count(buscar), "vez en la lista")
else:
    print("\n----------------------------\n")
    print("La palabra", buscar, "aparece", nombres.count(buscar), "veces en la lista")



primera = nombres.index(buscar)

print("\n----------------------------\n")

segunda = input("¿Con que palabra quieres sustituir?\n").upper()

for i in nombres:
    if i == buscar:
        indice = nombres.index(i)
        nombres[indice] = segunda

nombres[primera] = segunda

print(nombres)
