from Animal import Animal

#CLASE
class Perro(Animal):

# CONTRUCTOR
    def __init__(self,raza,color,nombre):
# ATRIBUTOS
        self.raza = raza
        self.color = color
        self.nombre = nombre

# METODOS
    def vueltita(self):
        return "*da una vuelta*"

    def dar_la_mano(self):
        return "*da la mano*"

    def ladrar(self):
        return "Guau!"

    def di_te_amo(self):
        return "Te amo"
