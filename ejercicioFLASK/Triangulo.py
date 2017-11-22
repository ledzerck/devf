from Figura import Figura

class Triangulo(Figura):

    def area(self):
        areaT = (self.base * self.altura) / 2
        return areaT
