from flask import Flask, jsonify, render_template
from flask import request, redirect
import json
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Hola Mundo"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html')

@app.route('/usuarioGET', methods = ['GET', 'POST'])
def usuarioget():
    if request.method == 'GET':
        sql = text('select * from user_cinta')
        result = db.engine.execute(sql)
        names = []
        for row in result:
            names.append(row[1])
        #return jsonify({"nombres":names})
        #hola = "un textito"
        return render_template('get.html', hola=names[0])

    if request.method == 'POST':
        return "Hola desde POST"

@app.route('/usuarioPOST')
def usuariopost():
    return render_template('post.html')

@app.route('/resultadoPOST', methods = ['GET', 'POST'])
def resultadopost():
    if request.method == 'GET':
        return render_template('post.html')
    if request.method == 'POST':
        id_user = request.form['id_user']
        name = request.form['nombre']
        last_name = request.form['apellido']
        age = request.form['edad']
        result = request.form

        return render_template('resultadopost.html', result = result, id_user = id_user)

if __name__ == '__main__':
    app.run(debug=True,port=5000)
