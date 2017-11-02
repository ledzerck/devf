# Programa que permite crear una lista de palabras. El programa tiene que pedir


palabras = int(input("¿Cuántas palabras tiene la lista? \n"))

nombres = []
if palabras > 0:
    for i in range(palabras):
        nombre = input("Ingresa la palabra: \n")
        nombres.append(nombre)
    print(nombres)
else:
    print("No seas necio")


print("Tu lista tiene", len(nombres), "elementos")
