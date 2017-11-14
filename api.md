## APIS
Suelen empezar como api.dominio.com/

* En python se utiliza http for humans
 * iniciamos nuestro entorno virtual
 * Se instala con:
  * pip install requests
 * En nuestro archivo .py importamos requests
  * import requests
* Podemos ver todo lo que tenemos instalado en nuestro entorno con:
 * pip freeze


---

#### JSON

Javascript Object Notation


* Formato para el intercambio de datos
* Describe datos con una sintaxis para identificar datos

---

### Características de un API
* Protocolo cliente/servidor sin estado
 * No se necesita guardar datos para ejecutar otra cosa
* Los objetos en REST siempre se manipulan a partir de URIS
* Interfaz uniforme
* Sistema de capas


#### Ventajas
* Separación entre cliente y servidor
* Visibilidad, fiabilidad y escalabilidad
* La API REST siempre es independiente del tipo de plataformas o lenguajes

---

### Ejercicio Goodreads

* Poner en postman:
 * https://goodreads-devf-aaron.herokuapp.com/api/v1/auth/

### POST
* copiamos el POST de postman
