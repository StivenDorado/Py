from flask import Flask
import pymongo
from flask_cors import CORS
# crear objeto de tipo flask
app = Flask(__name__)
CORS(app)


app.config["UPLOAD_FOLDER"]="./Static/img"

miConexion = pymongo.MongoClient("mongodb://localhost:27017/")

# Crear una base de datos
baseDatos = miConexion['Tienda']
#  Crear una colección Productos
productos = baseDatos['Productos']
# Crear una colección Usuarios
usuarios = baseDatos['Usuarios']

if __name__=="__main__":
    from controller.productoController import *
    from controller.usuarioController import *
    #arrancar el servidor en el pueerto 8000
    app.run(port=8000,debug=True)