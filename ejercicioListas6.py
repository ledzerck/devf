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

print("\n----------------------------\n")

buscar = input("¿Que palabra quieres eliminar?\n").upper()



while buscar in nombres:
    nombres.remove(buscar)


'''
for i in nombres:
    if i not in nombres:
        nombres.remove(buscar)
'''



print(nombres)
