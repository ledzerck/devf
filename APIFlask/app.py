from flask import Flask, jsonify, render_template
from flask import request, redirect
import json
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
# Le indicamos un archivo de configuración
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
print(db)

@app.route('/')
def index():
    return "Hola Mundo"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('page.html')

@app.route('/usuario', methods = ['GET', 'POST'])
def usuario():
    if request.method == 'GET':
        hola = "un textito"
        return render_template('get.html', hola=hola)

    if request.method == 'POST':
        return "Hola desde POST"

if __name__ == '__main__':
    app.run(debug=True,port=5000)
