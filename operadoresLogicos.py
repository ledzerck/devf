# Se pueden llamar compuertas lógicas
# Python usa && como and y | como or

x = int(input("Ingresa un numero x: \n"))
y = int(input("Ingresa un numero y: \n"))

print(type(x))

# Ejemplo AND

if x == 3 and y == 2:
    print("Se cumplio AND")
else:
    print("NO")

# Ejemplo OR

if x == 3 or y == 2:
    print("Se cumplio OR")
else:
    print("NO")
