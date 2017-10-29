# Programa que pida los segundos y retorne las horas, minutos y segundos

segundos = 3600

minutos = segundos / 60
moduloSegundos = segundos % 60

horas = minutos / 60
moduloMinutos = minutos % 60

print "%s : %s : %s" % (horas, moduloMinutos, moduloSegundos)
