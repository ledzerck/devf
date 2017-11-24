from flask import Flask, jsonify, render_template
from flask import request, redirect
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Hola Mundo"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('page.html')

@app.route('/usuario', methods = ['GET', 'POST'])
def usuario():
    if request.method == 'GET':
        return "Hola desde GET"

    if request.method == 'POST':
        return "Hola desde POST"

if __name__ == '__main__':
    app.run(debug=True,port=5000)
