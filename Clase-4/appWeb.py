from flask import Flask, request, render_template, redirect
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# variable de rutas 
app.config['UPLOAD_FOLDER'] = './static/img'

# Lista de array global para agregar arrays 
contactos = [['Maria', 'Rojas', 'wenm@'], 
            ['Juan', 'Pérez', 'juan@example.com'],
            ['Stiven', 'Salas', 'golds9013.com'],
            ['Juan', 'Pérez', 'juan@example.com']]

@app.route('/')
def index():
    mensaje = "hola mundo..."
    return render_template("index.html", mensaje=mensaje)

# Definir una ruta para mostrar la tabla
@app.route('/tabla')
def mostrarTabla():
   
    return render_template('tabla.html', contactos=contactos) #HTML QUE SE USA, y la variable que recibe los datos que van en la tabla 

# Definir ruta de formulario
@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
        return render_template('formulario.html')

# Agregar nuevo Contacto
@app.route('/agregarContacto', methods=['POST'])
def agregarContacto():
    if request.method == 'POST':
        nombre = request.form['textNombre']
        apellido = request.form['textApellido']
        correo = request.form['textCorreo']
        contacto = [nombre, apellido, correo]
        contactos.append(contacto)
        
        # Datos del archivo 
        archivo = request.files['fileFoto']
        nombreArchivo = secure_filename(archivo.filename)
        listaNombreArchivo = nombreArchivo.rplit('.', 1)
        extension = listaNombreArchivo[1].lower()()
        # Obtener la posición del contacto agregado
        pocicionUltimoAgregado = len(contactos)-1
        # Crear nombre de Foto
        nombreFoto = str(pocicionUltimoAgregado) + '.' + str(extension)
        # Sube el Archivo al servidor
        archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], nombreFoto))
        
        mensaje = 'contacto agregado correctamente'
        
        # return render_template('formulario.html', mensaje = mensaje) # se quita para que se pueda redireccionar
        return redirect('/tabla') # Redireccionar a al index de tabla 

# Ruta de saludo
@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f"Bienvenido, {nombre}! Dios de las artes de la borrachera y el arte de alcoholizarse."

# Otra ruta de saludo con un mensaje
@app.route('/mensaje/<mensaje>')
def mensaje(mensaje):
    return f'El mensaje es: {mensaje}'

# Ruta para productos (ejemplo para edad, ajustar según necesidad)
@app.route('/producto/<nombreProducto>')
def producto(nombreProducto):
    return f'El producto es: {nombreProducto}'

if __name__ == '__main__':
    app.run(port=3000, debug=True)
