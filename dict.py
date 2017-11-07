#!/usr/bin/python
# -*- coding: utf-8 -*-

separador = '------------------------------------'

diccionario = {'nombre': 'Carlos', 'edad': 22, 'cursos': ['Python','Django']}

print(diccionario)

print(diccionario['nombre'])
print(diccionario['edad'])
print(diccionario['cursos'])
print(diccionario['cursos'][0])

# Iterar Diccionarios
# Podemos usar dos variables para que traiga la llave y su valor

print(separador)
for key,value in diccionario.items():
    print(key + ': '+ str(value))


# Otra forma de declarar diccionarios
print(separador)
dic = dict(nombre='Néstor', apellido='Juárez', edad=22)
print(dic)


# Devuelve el número de elementos en el diccionario
print(separador)
print(len(diccionario))


# Mostrar solo todas las llaves en el diccionario
print(separador)
print(diccionario.keys())


# Mostrar solo los valores del diccionario
print(separador)
print(diccionario.values())


# Devuelve el valor del elemento con su clave. Y si no lo encuentra, trae un valor por default
print(separador)
print(diccionario.get('nombre'))
print(diccionario.get('nombreBLE', 'JUANITO'))


# Inserta un elemento al diccionario con su clave:valor
print(separador)
diccionario['key'] = 'value'
print(diccionario)


# Eliminar un elemento del diccionario
print(separador)
diccionario.pop('key')
print(diccionario)


# Obtener una lista
print(separador)
lista_cursos = diccionario['cursos']
lista_cursos.append('Java')
print(diccionario)


# Devuelve la copia de un diccionario
print(separador)
diccionario2 = diccionario.copy()
print(diccionario2)


# Añade los elementos de un diccionario a otro
diccionario.update(dic)
print(diccionario)
