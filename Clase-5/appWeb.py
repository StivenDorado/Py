from flask import Flask, request, render_template, redirect
from werkzeug.utils import secure_filename
import os
import pymongo
import pymongo.errors

# Crear objeto de tipo Flask
app = Flask(__name__)

# Configurar la carpeta donde se guardarán las imágenes
app.config['UPLOAD_FOLDER'] = './static/imagenes'

# Conexión a la base de datos MongoDB
miConexion = pymongo.MongoClient("mongodb://localhost:27017")
baseDatos = miConexion['Tienda']
productos = baseDatos['Productos']

# Ruta para la página principal
@app.route("/")
def inicio():
    try:
        listaProductos = productos.find()
        mensaje = ""
    except Exception as e:
        mensaje = str(e)
    return render_template("Index.html", productos=listaProductos, mensaje=mensaje)




# Ruta para agregar productos
@app.route('/agregar', methods=['POST', 'GET'])
def agregar():
    if request.method == 'POST':
        try:
            codigo = int(request.form['txtCodigo'])
            nombre = request.form['txtNombre']
            precio = int(request.form['txtPrecio'])
            categoria = request.form['cbCategoria']
            foto = request.files['fileFoto']

            nombreArchivo = secure_filename(foto.filename)
            listaNombreArchivo = nombreArchivo.rsplit(".", 1)
            extension = listaNombreArchivo[1].lower()
            nombreFoto = f"{codigo}.{extension}"

            producto = {
                "codigo": codigo,
                "nombre": nombre,
                "precio": precio,
                "categoria": categoria,
                "foto": nombreFoto
            }

            # Verificar si el producto ya existe
            existe = existeProducto(codigo)

            if not existe:
                resultado = productos.insert_one(producto)
                if resultado.acknowledged:
                    foto.save(os.path.join(app.config["UPLOAD_FOLDER"], nombreFoto))
                    mensaje = "Producto Agregado Correctamente"
                else:
                    mensaje = "Error al agregar el producto"
            else:
                mensaje = "Ya existe un producto con ese código"
        except Exception as e:
            mensaje = str(e)

    return render_template("frmAgregarProducto.html", mensaje=mensaje, producto=producto)


def existeProducto(codigo):
    try:
        consulta = {'codigo': codigo}
        producto = producto.find_one(consulta)
        if(producto is not None):
            return True
        else:
            return False 
    
    except pymongo.errors as error:
        print(error)
        return False


# Función para verificar si un producto ya existe
def existeProducto(codigo):
    return productos.find_one({"codigo": codigo}) is not None








# Iniciar la aplicación
if __name__ == '__main__':
    app.run(port=5000, debug=True)