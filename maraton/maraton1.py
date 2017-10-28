# Programa que pida los segundos y retorne las horas, minutos y segundos

segundos = 5980

minutos = segundos / 60
segundosRestantes = segundos % 60

horas = minutos / 60

if minutos > 60:
    minutosRestantes = minutos % 60


print(horas)
print(minutos)
print(segundosRestantes)
