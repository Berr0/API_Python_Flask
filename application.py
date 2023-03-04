# . .venv/bin/activate
# flask --app application.py --debug run

# Que servicio de amazon web services sirve para crear usuarios

# IAM = Identity and access management

# Al usuario root se le da administrator access de forma predeterminada

# Comando para meter el access key y el secret key = aws configure

#Segundo servicio para las bases de datos: RDS

#Sección 0/40

#Como usuario de AWS tu solo quieres saber la zonas de disponibilidad, los datacenter no te importan

#Secrets Manager es un servicio que nos permitirá guardar y recuperar las credenciales del usuario de forma separada como un 

#Para final de curso tenemos que hacer la api y la documentación


from flask import Flask, jsonify, request
from flask import render_template
from flask_cors import CORS
from flask import request

#Importamos las librerias necesarias para usar la base de datos
import mysql.connector

#Sacamos estos datos de la base de datos que tengamos en produccion
credentials = {
    "user": "root",
    "password": "root",
    "database": "db_amazon",
    "host": "RDS -> "
    }

#4 metodos básicos, conexión a base de datos 

#funcion que crea los usuarios en la base de datos
def create_users():
    cnx = mysql.connector.connect(**credentials)
    cursor = cnx.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS db_amazon")
    cursor.execute("USE db_amazon")
    cursor.execute("CREATE USER IF NOT EXISTS root@localhost IDENTIFIED BY 'root'")
    cursor.execute("GRANT ALL PRIVILEGES ON *.* TO root@localhost")
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))")
    cursor.execute("INSERT INTO users (username, password) VALUES ('root', 'root')")
    cnx.commit()
    cursor.close()
    cnx.close()
    return "ok"

def get_all_users():
    cnx = mysql.connector.connect(**credentials)
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    cursor.close()
    cnx.close()
    return rows

application = Flask(__name__)

CORS(application)

# @ == decorators 
# Define routes of the application
@application.route('/usuarios')
def hello_world():
    print(request.method)
    return "<div><h1>Alejandro</h1></div>"

@application.post('/') 
def hello_world_post():
    return "hola desde post"

@application.route('/usuarios/<username>')
def hello(username):
    return render_template('hello.html', username=username)

@application.post('/create-todo')
def create_todo():
    #add new li item to the list
    data = request.data
    print(data)
    return "ok"

@application.route('/get-todos')
def get_todo():
    todo = [[1,"todo",True],[4,"todo",True],[7,"todo",False]]
    diccionario = {}
    for i in range(len(todo)):
        diccionario[todo[i][0]] = todo[i][:]
    return jsonify(diccionario)

@application.put('/list-todos')
def complete_todo():
    pass







#
ammo = {
    "5.45x39mm": {
        "PS": {"penetration": 18, "damage": 34, "armor_damage": 31},
        "PP": {"penetration": 28, "damage": 20, "armor_damage": 24},
        "PRS": {"penetration": 20, "damage": 34, "armor_damage": 31},
        "BP": {"penetration": 37, "damage": 16, "armor_damage": 28},
        "BT": {"penetration": 33, "damage": 25, "armor_damage": 27},
        "BS": {"penetration": 51, "damage": 14, "armor_damage": 27},
        "Igolnik": {"penetration": 62, "damage": 14, "armor_damage": 26},
        "SB193": {"penetration": 28, "damage": 20, "armor_damage": 24},
        "FMJ": {"penetration": 22, "damage": 31, "armor_damage": 29},
        "HP": {"penetration": 7, "damage": 54, "armor_damage": 42},
        "T": {"penetration": 7, "damage": 47, "armor_damage": 40},
        "US": {"penetration": 7, "damage": 47, "armor_damage": 40},
        "PS gs": {"penetration": 18, "damage": 34, "armor_damage": 31},
        "PP gs": {"penetration": 28, "damage": 20, "armor_damage": 24},
        "PRS gs": {"penetration": 20, "damage": 34, "armor_damage": 31},
        "BS gs": {"penetration": 51, "damage": 14, "armor_damage": 27},
        "BP gs": {"penetration": 37, "damage": 16, "armor_damage": 28},
        "BT gs": {"penetration": 33, "damage": 25, "armor_damage": 27},
        "Igolnik gs": {"penetration": 62, "damage": 14, "armor_damage": 26},
        "FMJ gs": {"penetration": 22, "damage": 31, "armor_damage": 29},
        "HP gs": {"penetration": 7, "damage": 54, "armor_damage": 42},
        "T gs": {"penetration": 7, "damage": 47, "armor_damage": 40},
        "US gs": {"penetration": 7, "damage": 47, "armor_damage": 40}
    },"7.62x39mm": {
        "PS": {"penetration": 25, "damage": 57, "armor_damage": 49},
        "HP": {"penetration": 13, "damage": 67, "armor_damage": 55},
        "US": {"penetration": 15, "damage": 56, "armor_damage": 46},
        "BP": {"penetration": 42, "damage": 50, "armor_damage": 53},
        "T45M": {"penetration": 27, "damage": 54, "armor_damage": 50},
        "gs": {"penetration": 25, "damage": 57, "armor_damage": 49},
        "HP gs": {"penetration": 13, "damage": 67, "armor_damage": 55},
        "US gs": {"penetration": 15, "damage": 56, "armor_damage": 46},
        "BP gs": {"penetration": 42, "damage": 50, "armor_damage": 53},
        "T45M gs": {"penetration": 27, "damage": 54, "armor_damage": 50}
},
"5.56x45mm": {
    "M855": {"penetration": 29, "damage": 40, "armor_damage": 35},
    "M856": {"penetration": 16, "damage": 58, "armor_damage": 44},
    "M855A1": {"penetration": 37, "damage": 43, "armor_damage": 36},
    "M856A1": {"penetration": 20, "damage": 60, "armor_damage": 46},
    "M995": {"penetration": 53, "damage": 35, "armor_damage": 40},
    "55 FMJ": {"penetration": 20, "damage": 60, "armor_damage": 46},
    "55 HP": {"penetration": 5, "damage": 72, "armor_damage": 54},
    "55 AP": {"penetration": 39, "damage": 41, "armor_damage": 38},
    "6.5 mm CT": {"penetration": 32, "damage": 50, "armor_damage": 44},
    "55 HP gs": {"penetration": 5, "damage": 72, "armor_damage": 54},
    "55 AP gs": {"penetration": 39, "damage": 41, "armor_damage": 38},
    "M856A1 tracer": {"penetration": 20, "damage": 60, "armor_damage": 46},
    "M856A1 gs": {"penetration": 20, "damage": 60, "armor_damage": 46},
    "M995 gs": {"penetration": 53, "damage": 35, "armor_damage": 40},
    "M855A1 gs": {"penetration": 37, "damage": 43, "armor_damage": 36}
},
"7.62x51mm": {
    "M80": {"penetration": 41, "damage": 80, "armor_damage": 62},
    "M62": {"penetration": 47, "damage": 79, "armor_damage": 64},
    "M61": {"penetration": 68, "damage": 70, "armor_damage": 62},
    "BPZ FMJ": {"penetration": 42, "damage": 80, "armor_damage": 62},
    "TPZ SP": {"penetration": 43, "damage": 79, "armor_damage": 63},
    "HPBT": {"penetration": 22, "damage": 93, "armor_damage": 72},
    "AP": {"penetration": 51, "damage": 78, "armor_damage": 70},
    "FMJ": {"penetration": 41, "damage": 80, "armor_damage": 62},
    "M993": {"penetration": 65, "damage": 75}
    }}