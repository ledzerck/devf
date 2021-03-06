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




@app.route('/api', methods = ['GET'])
def api():
    if request.method == 'GET':
        print(request.json)
        sql = text('select * from user_cinta')
        result = db.engine.execute(sql)
        items = []
        for row in result:
            an_item = dict(ids=row['id_user'], nombre=row['nombre'], edad=row['edad'], apellido=row['apellido'] )
            items.append(an_item)

        return jsonify(usuario=items)

    if request.method == 'POST':
        return "Hola desde POST"



@app.route('/usuarioGET', methods = ['GET', 'POST'])
def usuarioget():
    if request.method == 'GET':
        print(request.json)
        sql = text('select * from user_cinta')
        result = db.engine.execute(sql)
        items = []
        api = json.dumps(items)
        for row in result:
            an_item = dict(ids=row['id_user'], names=row['nombre'], edad=row['edad'], apellido=row['apellido'] )
            items.append(an_item)

        return render_template('get.html', items=items)

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
        # Autoincremento feo :(
        sql = text('select id_user from user_cinta')
        result = db.engine.execute(sql)
        names = 0
        for i in result:
            names +=1
        id_user = names + 1

        name = request.form['nombre']
        last_name = request.form['apellido']
        age = request.form['edad']
        result = request.form
        sql = "insert into user_cinta(id_user,nombre,apellido,edad) values({},'{}','{}',{});".format(id_user,name,last_name,age)
        nuevo = db.engine.execute(sql)
        return render_template('resultadopost.html', result = result, id_user = id_user)

if __name__ == '__main__':
    app.run(debug=True,port=5000)
