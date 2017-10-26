#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import database
from flask import Flask, request, jsonify
import requests
import json, pprint
from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient("")
db = client.devf

app = Flask(__name__)

#¿Cómo parsear argumentos del Querystring?
@app.route('/multiply')
def multiply():
  a = request.args.get('a')
  a = int(a)
  b = request.args.get('b')
  b = int(b)
  return str(a*b)

#Consumo de la API de NASA
@app.route('/asknasa')
def nasa():
  lat = request.args.get('lat')
  lon = request.args.get('lon')
  date = '2016-02-01'
  payload = {'lat':lat, 'lon':lon, 'date':date, 'api_key':'DEMO_KEY'}
  r = requests.get('https://api.nasa.gov/planetary/earth/imagery', params=payload).json()['url']
  return r

#Snippet para IFTTT
@app.route('/test')
def pruebilla():
    report = check_server_status()
    print requests.post("https://maker.ifttt.com/trigger/test_flask/with/key/b617PtNYUr2GjUQUoKF1U9", data=report)
    return '1'
    
def check_server_status():
  return {"value1":"OK"}

#Messenger Chatbot
@app.route('/facebook', methods=['POST','GET'])
def facebook():
  #print request.get_json()['status']['result']
  #pprint(request.data)
  location_data= json.loads(request.data)['originalRequest']['data']['postback']['data']
  lat= location_data['lat'] #Parses the user's latitude
  lon= location_data['long'] #Parses the user's longitude
  
  #Given the context's list structure, we look for the one dictionary element where the 'name' key's value is 'generic', and parse both sabor and tamano
  for x in json.loads(request.data)['result']['contexts']:
    if x.get('name')=='generic':
      sabor= x.get('parameters')['Sabor'].encode('ascii', 'ignore').decode('ascii')
      tamano= x.get('parameters')['Tamano'].encode('ascii', 'ignore').decode('ascii')
  
  #Prints out to terminal the order's info
  print('Cliente con coordenadas ({},{}) acaba de pedir una pizza de {}, tamano {}'.format(lat, lon, sabor, tamano))
  
  #Declares a dictionary to hold the current order and pushes it to Mongo
  data= {
    'coordenadas':{'lat':lat,'lon':lon},
    'sabor': sabor,
    'tamano': tamano,
    'status': 'orden recibida'
  }
  db['ordenes'].insert_one(data)
  
  return 'x'

#Checar documentos de Mongo
@app.route('/orders')
def check_orders():
  datos = db.ordenes.find()
  print datos
  orders = {'orders':[]}

  for documento in datos:
    documento['_id'] = str(documento['_id'])
    orders['orders'].append(documento)
    
  return jsonify(orders)
  

#Cambiar el status de una orden recibida a una orden completada
@app.route('/change_order_status')
def change_order_status():
  identifier = request.args.get('id')
  print identifier
  order = db['ordenes'].find_one_and_update(
    {'_id': ObjectId(identifier)},
    {"$set": {"status": "orden completada"}})
  print order
  return '1'












