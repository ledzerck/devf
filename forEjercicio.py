contar = 0
for i in range(0,1001):
    contar += 1
    print(i)

print("\n-------------------------------------------\n")

cuenta = 0
for i in range(0,1001):
    if i % 2 == 0:
        cuenta += 1
        print(i)

print("\n-------------------------------------------\n")

palabra = "ELEFANTE"

cuentaP = 0
for i in palabra:
    if i == "E":
        cuentaP += 1
        if cuentaP == 3:
            print("Encontraste la 3era E")
