#!/usr/bin/env python
# -*- coding_ utf-8 -*-
from flask import Flask, request

app = Flask(__name__)

ACCES_TOKEN = 'EAACGb9y3susBAAGABRW3zyQaS2feCL86IHN6131UaojVY1U6Nusa2PhRejBRULFt8JGKT5f2qRZCjlWjTQC3xAwpS1KcvcsheT1aaqQW8OD0cmH5SF4vXACTcExU8VJMlg2ZBpn30LtgYBBhS78gmhIU94ZBtXwAt7h2SfOuw8nAaRvzqnX'
# Este nosotros lo especificamos como queramos
VERIFY_TOKEN = 'cintaroja'

@app.route('/')
def home():
    return 'Inicio del servidor'

@app.route('/webhook', methods = ['GET','POST'])
def webhook():
    if request.method == 'POST':
        mensaje = request.json
        print(mensaje)
        return 'True'
    elif request.method == 'GET':
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        return 'Verificar token'


if __name__ == '__main__':
    app.run(port = 5000, debug = True)