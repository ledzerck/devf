import requests

class Respuestas():
    def saluda(self,sender_id):
        JSON = {"messaging_type": "RESPONSE",
        "recipient":{
          "id":1577835825621329
        },
        "message":{
          "text":"Te quiero <3"
        }
        }

        URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAACGb9y3susBAAGABRW3zyQaS2feCL86IHN6131UaojVY1U6Nusa2PhRejBRULFt8JGKT5f2qRZCjlWjTQC3xAwpS1KcvcsheT1aaqQW8OD0cmH5SF4vXACTcExU8VJMlg2ZBpn30LtgYBBhS78gmhIU94ZBtXwAt7h2SfOuw8nAaRvzqnX'
        respuesta = requests.post(URL, json = JSON)
        print(respuesta)

    def quick(self,sender_id):

        JSON = {
          "recipient":{
            "id":sender_id
          },
          "message":{
            "text": "No te entiendo campeón",
            "quick_replies":[
              {
                "content_type":"text",
                "title":"Buscar",
                "payload":"POSTBACK_IMAGE",
                "image_url":"https://www.anipedia.net/imagenes/caracteristicas-generales-de-los-gatos.jpg"
              },
              {
                "content_type":"location"
              },
              {
                "content_type":"text",
                "title":"Algo más",
                "payload":"POSTBACK_TEXT"
              }
            ]
          }
        }
        URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAACGb9y3susBAAGABRW3zyQaS2feCL86IHN6131UaojVY1U6Nusa2PhRejBRULFt8JGKT5f2qRZCjlWjTQC3xAwpS1KcvcsheT1aaqQW8OD0cmH5SF4vXACTcExU8VJMlg2ZBpn30LtgYBBhS78gmhIU94ZBtXwAt7h2SfOuw8nAaRvzqnX'
        respuesta = requests.post(URL, json = JSON)
        return True

    def generic(self,sender_id):

        JSON = {
          "recipient":{
            "id":sender_id
          },
          "message":{
            "attachment":{
              "type":"template",
              "payload":{
                "template_type":"generic",
                "elements":[

                	{'title': 'Cotizar',
        						  'image_url': "https://www.anipedia.net/imagenes/caracteristicas-generales-de-los-gatos.jpg",
        						  'subtitle': 'Cotiza tu envío',
        						  'buttons':[{'type': 'postback', 'title':'Quiero cotizar', 'payload': 220}]
        						  },
        						  {'title': 'Cotizar',
        						  'image_url': "https://www.anipedia.net/imagenes/caracteristicas-generales-de-los-gatos.jpg",
        						  'subtitle': 'Cotiza tu envío',
        						  'buttons':[{'type': 'postback', 'title':'Quiero cotizar', 'payload': 220}]
        						  }
                ]
              }
            }
          }
        }
        URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAACGb9y3susBAAGABRW3zyQaS2feCL86IHN6131UaojVY1U6Nusa2PhRejBRULFt8JGKT5f2qRZCjlWjTQC3xAwpS1KcvcsheT1aaqQW8OD0cmH5SF4vXACTcExU8VJMlg2ZBpn30LtgYBBhS78gmhIU94ZBtXwAt7h2SfOuw8nAaRvzqnX'
        respuesta = requests.post(URL, json = JSON)
        return True

    def pln(self,sender_id):
        JSON = {"messaging_type": "RESPONSE",
        "recipient":{
          "id":sender_id
        },
        "message":{
          "text":"¿Qué deseas?"
        }
        }

        URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAACGb9y3susBAAGABRW3zyQaS2feCL86IHN6131UaojVY1U6Nusa2PhRejBRULFt8JGKT5f2qRZCjlWjTQC3xAwpS1KcvcsheT1aaqQW8OD0cmH5SF4vXACTcExU8VJMlg2ZBpn30LtgYBBhS78gmhIU94ZBtXwAt7h2SfOuw8nAaRvzqnX'
        respuesta = requests.post(URL, json = JSON)
        print(respuesta)
