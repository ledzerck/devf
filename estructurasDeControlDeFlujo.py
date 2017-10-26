
# Python necesita identación para poder trabajar
# Para indicar que termina una línea se ponen dos puntos :
# Se utiliza elif en lugar de else if

x = 4

if x == 4:
    print("VERDADERO")
else:
    print("FALSO")



x = "ROJO"

if x == "VERDE":
    print("CRUZA")
else:
    print("ESPERA")



x = "AMARILLO"

if x == "VERDE":
    print("CRUZA")
elif x == "AMARILLO":
    print("CORRE")
else:
    print("ESPERA")
