# Chatbot
* Programa informático que simula una conversación humana

##### Ventajas
* No son apps y no se descargan
* La experiencia de usuario es agradable
* Asesoría y atención al cliente más eficaz y rápida
* Reducen costos de atención del cliente
* Dan atención 24/7

##### Desventajas
* Solo atienden tareas sencillas
* Se deben usar oraciones muy comprensibles
* Muchas plataformas aún no los soportan

---

## Webhooks
* Son endpoint en los servidores que reciben notificaciones
* Reciben notificaciones,
* Hace peticiones de servidor a servidor

### Arquitectura de un Chatbot


* Crear una fanpage de Facebook
* Ir a developers.facebook.com
  * Mis aplicaciones > Agregar una aplicación
  * Nombre: Chatbot
  * Identificador: 147815002518251
  * Generación de identificación > Seleccionar nuestra fanpage
    * Token: EAACGb9y3susBAAGABRW3zyQaS2feCL86IHN6131UaojVY1U6Nusa2PhRejBRULFt8JGKT5f2qRZCjlWjTQC3xAwpS1KcvcsheT1aaqQW8OD0cmH5SF4vXACTcExU8VJMlg2ZBpn30LtgYBBhS78gmhIU94ZBtXwAt7h2SfOuw8nAaRvzqnX
  * Crear una app de flask y configurarla con el token de facebook
    * Abrir ngrok con el mismo puerto de nuestra app
    * Usamos la url con Conexión segura
  * En developers.facebook: + Añadir un producto > Messenger > configurar > Webhooks
    * messages, messagin_postback, messagin_optin
    * Devolución de llamada: https://ngrok.io/webhook (ruta de nuestro webhook)
    * identificador :cintaroja (El que nosotros especificamos)
    * Elegir nuestra fanpage y suscribirnos
  * Siempre se le debe contestar 200
  * Estas URL las sacamos de la docu facebook developers: https://developers.facebook.com/docs/messenger-platform/send-messages
  * En postman en la url con POST:
      * https://graph.facebook.com/v2.6/me/messages?access_token=<PAGE_ACCESS_TOKEN>
  * En postman en el body:
    * {"messaging_type": "RESPONSE",
"recipient":{
  "id":1577835825621329
},
"message":{
  "text":"hello, world!"
}
}

---

### Respuestas rápidas
* Pasamos un json que va a esperar ciertas respuestas predefinidas
* Como lo estamos probando en el servidor de ngrok hay que cambiar la url del webhook
  * Vamos a nuestra aplicación de fb > webhook > Edit subscription
