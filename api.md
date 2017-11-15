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

### Cabeceras
* Permite enviar información no visible, como:
 * tokens, clave de país, información del dispositivo

### GET
* Con este obtenemos informaión de la API

### POST
* Permite pasarle/crear información a la API

### PULL
* Parecido a POST

---

#### Ejercicio Google Maps
* https://developers.google.com/maps/documentation/directions/
* Hay que crear una llave
 * Ledzer
 * AIzaSyD7SYo_K1nRimkiAbYFCpjFp5-npqINDVw
* Pegamos en postman la url de la API + nuestra key
 * https://maps.googleapis.com/maps/api/directions/json?origin=Marketing+Capacitacion,+MX&destination=Estela+de+luz+MX&key=AIzaSyD7SYo_K1nRimkiAbYFCpjFp5-npqINDVw
 * Podemos cambiar en la URI el inicio y el destino
* Instalamos googlemaps con pip
 * pip install googlemaps
* Con este cliente podemos hacer peticiones más fácilmente
* Hay que iniciar el cliente con googlemaps.Client()
* Usamos googlemaps.Directions() que recibe 3 parametros (origen,destino, modo)
* Importamos datetime para que nos devuelva el tiempo que va a tardar
* buscar googlemaps python
