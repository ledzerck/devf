from flask import Flask,jsonify, render_template
from flask import request
import json



# Es común llamarlo app.py
#

# Con esto creamos el objeto flask
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/')
def index():
    return "Hola Mundo"

# Para indicar una página que no existe
# Necesita la e
@app.errorhandler(404)
def page_not_found(e):
    return render_template('page.html')

# Podemos indicar que tipo de peticiones va a aceptar
@app.route('/tareas', methods = ['GET', 'POST'])
def tareas():
    if request.method == 'GET':
        return jsonify({"tareas":tasks})
    if request.method == 'POST':
        body = request.json
        lista_tareas = []
        lista_tareas.append(body['tareas'])
        return jsonify({'tareas_realiza':lista_tareas})

# Hay que hacer una confirmación:
if __name__ == '__main__':
    # Usamos debug true para que se reinicie con nuestros cambios
    # Podemos indicar otro puerto
    app.run(debug=True,port=5000)
