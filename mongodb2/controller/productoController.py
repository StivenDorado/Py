from app import app, productos
from flask import request, jsonify, redirect, render_template, session
from werkzeug.utils import secure_filename
from bson.objectid import ObjectId
import pymongo
import pymongo.errors
import os

# Ruta principal para listar productos
@app.route("/listarProductos")
def listar_productos():
    if "user" in session:
        try:
            mensaje = ""
            listaProductos = list(productos.find())  # Convertir el cursor en lista
            if not listaProductos:
                mensaje = "No hay productos disponibles."
        except pymongo.errors.PyMongoError as error:
            mensaje = str(error)
        return render_template("listarProductos.html", productos=listaProductos, mensaje=mensaje)
    else:
        mensaje = "Debe ingresar con sus credenciales."
        return render_template("frmLogin.html", mensaje=mensaje)

# Ruta para agregar un producto
@app.route("/agregar", methods=['POST', 'GET'])
def agregar_producto():
    if "user" in session:
        mensaje = ""
        producto = None
        if request.method == 'POST':
            try:
                codigo = int(request.form['txtCodigo'])
                nombre = request.form['txtNombre']
                precio = int(request.form['txtPrecio'])
                categoria = request.form['cbCategoria']
                foto = request.files['fileFoto']
                nombreArchivo = secure_filename(foto.filename)
                extension = nombreArchivo.rsplit(".", 1)[1].lower()
                nombreFoto = f"{codigo}.{extension}"
                
                # Crear el diccionario del producto
                producto = {
                    "codigo": codigo, 
                    "nombre": nombre, 
                    "precio": precio, 
                    "categoria": categoria, 
                    "foto": nombreFoto
                }
                
                # Verificar si el producto ya existe
                if not existe_producto(codigo):
                    resultado = productos.insert_one(producto)
                    if resultado.acknowledged:
                        foto.save(os.path.join(app.config["UPLOAD_FOLDER"], nombreFoto))
                        mensaje = "Producto agregado correctamente."
                        return redirect('/listarProductos')
                    else:
                        mensaje = "Error al agregar el producto."
                else:
                    mensaje = "Ya existe un producto con ese código."
            except pymongo.errors.PyMongoError as error:
                mensaje = str(error)
            return render_template("frmAgregarProducto.html", mensaje=mensaje, producto=producto)
        else:
            return render_template("frmAgregarProducto.html", producto=producto)
    else:
        mensaje = "Debe ingresar con sus credenciales."
        return render_template("frmLogin.html", mensaje=mensaje)

# Función para verificar si el producto ya existe
def existe_producto(codigo):
    try:
        consulta = {"codigo": codigo}
        producto = productos.find_one(consulta)
        return producto is not None
    except pymongo.errors.PyMongoError as error:
        print(error)
        return False

# Ruta para consultar un producto específico
@app.route("/consultar/<string:id>", methods=["GET"])
def consultar_producto(id):
    if "user" in session:
        try:
            consulta = {"_id": ObjectId(id)}
            producto = productos.find_one(consulta)
            return render_template("frmActualizarProducto.html", producto=producto)
        except pymongo.errors.PyMongoError as error:
            mensaje = str(error)
            return redirect("/listarProductos", mensaje=mensaje)
    else:
        mensaje = "Debe ingresar con sus credenciales."
        return render_template("frmLogin.html", mensaje=mensaje)

# Ruta para actualizar un producto
@app.route("/actualizar", methods=["POST"])
def actualizar_producto():
    if "user" in session:
        try:
            codigo = int(request.form["txtCodigo"])
            nombre = request.form["txtNombre"]
            precio = int(request.form["txtPrecio"])
            categoria = request.form["cbCategoria"]
            id = ObjectId(request.form["id"])
            foto = request.files["fileFoto"]

            # Verificar si hay una foto nueva para actualizar
            if foto.filename:
                nombreArchivo = secure_filename(foto.filename)
                extension = nombreArchivo.rsplit(".", 1)[1].lower()
                nombreFoto = f"{codigo}.{extension}"
                producto = {
                    "_id": id, 
                    "codigo": codigo,
                    "nombre": nombre,
                    "precio": precio,
                    "categoria": categoria,
                    "foto": nombreFoto
                }
                foto.save(os.path.join(app.config["UPLOAD_FOLDER"], nombreFoto))
            else:
                producto = {
                    "_id": id, 
                    "codigo": codigo, 
                    "nombre": nombre,
                    "precio": precio,
                    "categoria": categoria
                }
                
            criterio = {"_id": id}
            consulta = {"$set": producto}

            # Verificar si el código ya existe en otro producto
            if productos.find_one({"codigo": codigo, "_id": {"$ne": id}}):
                mensaje = "Producto ya existe con ese código."
                return render_template("frmActualizarProducto.html", producto=producto, mensaje=mensaje)
            
            resultado = productos.update_one(criterio, consulta)
            if resultado.acknowledged:
                mensaje = "Producto actualizado correctamente."
                return redirect("/listarProductos")
        except pymongo.errors.PyMongoError as error:
            mensaje = str(error)
            return redirect("/listarProductos", mensaje=mensaje)
    else:
        mensaje = "Debe ingresar con sus credenciales."
        return render_template("frmLogin.html", mensaje=mensaje)

# Ruta para eliminar un producto
@app.route("/eliminar/<string:id>", methods=["GET"])
def eliminar_producto(id):
    if "user" in session:
        try:
            id = ObjectId(id)
            criterio = {"_id": id}
            producto = productos.find_one(criterio)
            resultado = productos.delete_one(criterio)
            if resultado.acknowledged:
                nombreFoto = producto['foto']
                rutaFoto = os.path.join(app.config['UPLOAD_FOLDER'], nombreFoto)
                if os.path.exists(rutaFoto):
                    os.remove(rutaFoto)
                mensaje = "Producto eliminado correctamente."
        except pymongo.errors.PyMongoError as error:
            mensaje = str(error)
        return redirect("/listarProductos", mensaje=mensaje)
    else:
        mensaje = "Debe ingresar con sus credenciales."
        return render_template("frmLogin.html", mensaje=mensaje)

# Función principal para correr la aplicación
if __name__ == "__main__":
    app.run(port=8000, debug=True)
