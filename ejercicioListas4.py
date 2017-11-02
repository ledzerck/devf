palabras = int(input("¿Cuántas palabras tiene la lista? \n"))

nombres = []
if palabras > 0:
    for i in range(palabras):
        nombre= input("Ingresa la palabra: \n").upper()
        nombres.append(nombre)
    print(nombres)
else:
    print("No seas necio")

print("Tu lista tiene", len(nombres), "elementos")

buscar = input("Que palabra quieres buscar\n").upper() 

if nombres.count(buscar) <= 1:
    print("La palabra", buscar, "aparece", nombres.count(buscar), "vez en la lista")
else:
    print("La palabra", buscar, "aparece", nombres.count(buscar), "veces en la lista")
