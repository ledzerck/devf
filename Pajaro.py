from Animal import Animal

#CLASE
class Pajaro(Animal):

# CONTRUCTOR
    def __init__(self,tipo,color,nombre):
# ATRIBUTOS
        self.tipo = tipo
        self.color = color
        self.nombre = nombre

# METODOS
    def volar(self):
        return "*vuela*"

    def cantar(self):
        return "fiuuu fuiii fi fiuuuu"
