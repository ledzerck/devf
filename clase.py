#CLASE
class Auto:

# CONTRUCTOR
    def __init__(self,nombre_cons,color,motor):
# ATRIBUTOS
        self.nombre = nombre_cons
        self.color = color
        self.ruedas = "4"
        self.motor = motor

# METODOS
    def arranca(self):
        print("RRRUUNNN el", self.nombre)

    def frena(self):
        print("frenando el", self.nombre)

    def get_color(self):
        print(self.color)

    def set_color(self,new_color):
        self.color = new_color


mustang = Auto('MUSTANG','ROJO', '5.5')
mustang.arranca()
mustang.frena()
mustang.set_color('azul')
mustang.get_color()

jetta = Auto('JETTA','BLANCO', '2.5')
jetta.arranca()
jetta.frena()
jetta.get_color()
