## DialogFlow
* Create new agent
 * Pide pizza


#### Intent
* Trabajar con el intent por defecto

* Borrar el default welcome intent
 * Quedarnos con eldefault fallback intent
 * Add follow up intent - Custom

* Deben quedar 4 intents como escalera

###### Response
* Agregar con el botón de + la opción de fb
 * Text Response
 * Lo guardamos para que se conecte a fb messenger

* Tenemos que ir a developer.facebook.como
* En integrations vamos a la parte de Facebook messenger
  * Nos va a dar una url de callback
* En la parte de mfacebook vamos a la parte de messenger y generamos un token (Después de pedir el token refrescamos)
  * Para eso hay que crear una página
  * Con eso obtenemos el identificador
  * Lo pegamos en PageAccessToken
  * En verify ponemos una palabra sin caracteres especiales

* En DialogFlow también configuramos los datos de la app de fb

* En los webhooks seleccionamos nuestra página

* Crear tarjetas en add Message content > cad hasta tener 3 tarjetas

* Llenar las tarjetas con la info de pizzas
 * Buscar imágenes de pizza y copiar su URL para la tarjeta

* Podemos llenar una tarjeta con quickreplies para respuestas rápidas

* En entities
 * Aquí es donde el bot reconoce las palabras
 * Se especifican los sabores de la pizza

* En los intent preguntamos el sabor y tamaño
* El tamaño lo hacemos con un quick reply





gist,github.com/anonymous/8746e61e24d994a6358f02c0a91a5e1d
