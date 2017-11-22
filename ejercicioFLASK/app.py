from flask import Flask, jsonify, render_template
from flask import request, redirect
from Rectangulo import Rectangulo
from Triangulo import Triangulo
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Hola Mundo"


@app.errorhandler(404)
def page_not_found(e):
    return render_template('page.html')

# Podemos indicar que tipo de peticiones va a aceptar

@app.route('/rectangulo', methods = ['GET', 'POST'])
def rectangulo():
    if request.method == 'GET':
        baseG = request.args.get('base','valor por default')
        alturaG = request.args.get('altura','valor por default')
        rectangulo = Rectangulo(int(baseG),int(alturaG))
        areaRectangulo = rectangulo.area()
        return "El parametro es: {}".format(areaRectangulo)

    if request.method == 'POST':
        body = request.json
        baseJ = body['base']
        alturaJ = body['altura']
        rectangulo = Rectangulo(baseJ,alturaJ)
        areaRectangulo = rectangulo.area()
        return jsonify(dict(area=areaRectangulo))


@app.route('/triangulo', methods = ['GET', 'POST'])
def triangulo():
    if request.method == 'POST':
        body = request.json
        baseJ = body['base']
        alturaJ = body['altura']
        triangulo = Triangulo(baseJ,alturaJ)
        areaTriangulo = triangulo.area()
        return jsonify(dict(area=areaTriangulo))

if __name__ == '__main__':
    app.run(debug=True,port=5001)
