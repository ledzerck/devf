# POO
#### Programación Orientada a Objetos
Es un paradigma de programación que usa objetos para diseñar aplicaciones y programas

* Está basada en varias técnicas que incluyen:
 * Herencia, abstracción y encapsulamiento
 * Googlear SOLID (Reglas de programación)

---

### Clases
* Definición de las propiedades y comportamiento de un tipo de objeto en concreto
 * Contiene atributos y métodos
* Definir clases en Python:
  * class NombreClase:
  * Siempre empiezan con mayúsculas
  * Dentro le definimos sus atributos y métodos
  * Self se ocupa para mandarse a llamar a si mismo (los métodos)
* Para tabajar con la clase hay que instanciarlo asignándolo a una variable
* Normalmente los métodos no se deben modificar a como se definieron
* Instanciar un objeto es "crearlo" o asignarlo
* Podemos importar las clases creadas de los archivos con:
  * from clase import NombreClase

### Constructores
* Van a indicar las características específicas del objeto
* Existen en todos los lenguajes orientados a objetos
* Su sintaxis es:
  * def \_\_init\_\_ (self,caracteristicas):
* No suele accederse directamente a sus atributos, en cambio se hace definiendo los métodos
