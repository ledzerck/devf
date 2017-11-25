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
        sql = text('select * from user_cinta')
        result = db.engine.execute(sql)
        names = []
        for row in result:
            names.append(row[1])
        #return jsonify({"nombres":names})
        #hola = "un textito"
        ### print(len(names))
        return render_template('get.html', hola=names)

    if request.method == 'POST':
        print(request.json)
        id_user = request.json['id']
        name = request.json['nombre']
        last_name = request.json['apellido']
        age = request.json['edad']
        sql = "insert into user_cinta(id_user,nombre,apellido,edad) values({},'{}','{}',{});".format(id_user,name,last_name,age)
        result = db.engine.execute(sql)
        return jsonify({"msg":True}),201

if __name__ == '__main__':
    app.run(debug=True,port=5001)
