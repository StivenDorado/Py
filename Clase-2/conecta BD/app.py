import pymysql as mysql

user = "root"
password = "CTPI2024*"
baseDatos = "Tienda"
host = "localhost"

miConexion = mysql.connect(
    host=host,
    user=user,
    password=password,
    db=baseDatos
)

def insertar():
    try:
        # Creando un producto en una tupla
        producto = (15, "Nevera", 2500000, "Electrodoméstico")
        cursor = miConexion.cursor()
        # Texto de la consulta
        consulta = "INSERT INTO productos (nproCodigo, proNombre, proPrecio, proCategoria) VALUES (%s, %s, %s, %s)"
        # Ejecutar la consulta
        resultado = cursor.execute(consulta, producto)
        miConexion.commit()
        if cursor.rowcount == 1:
            print('Producto Insertado')
    except mysql.MySQLError as error:
        print(str(error))
    finally:
        cursor.close()



def listar():
    try:
        # Crear el cursor
        cursor = miConexion.cursor()
        # Texto de la consulta
        consulta = 'SELECT * FROM productos'
        cursor.execute(consulta)
        productos = cursor.fetchall()
        if len(productos) > 0:
            # Imprimir
            for p in productos:
                print(f'Codigo: {p[1]}')
                print(f'Nombre: {p[2]}')
                print(f'Precio: {p[3]}')
                print(f'Categoria: {p[4]}')
                print('---')
        else:
            print('En el momento no hay productos registrados')
    except mysql.MySQLError as error:
        print(str(error))
    finally:
        cursor.close()



def consultarPorCodigo():
    try:
        cursor = miConexion.cursor()
        codigo = int(input('Ingrese código del Producto a consultar: '))
        productosConsultar = (codigo,)
        consulta = 'SELECT * FROM productos WHERE nproCodigo = %s'
        cursor.execute(consulta, productosConsultar)
        producto = cursor.fetchone()
        if producto:
            print(producto)
        else: 
            print('No hay productos con el código ingresado')
    except mysql.MySQLError as error:
        print(str(error))
    finally:
        cursor.close()
    return producto



def actualizar():
    try:
        producto = consultarPorCodigo()
        if producto:
            cursor = miConexion.cursor()
            nuevoPrecio = producto[3] * 1.20
            codigoProductoActualizar = producto[1]
            productoActualizar = (nuevoPrecio, codigoProductoActualizar)
            consulta = 'UPDATE productos SET proPrecio = %s WHERE nproCodigo = %s'
            resultado = cursor.execute(consulta, productoActualizar)
            miConexion.commit()
            if cursor.rowcount == 1:
                print('Producto actualizado con éxito')
            else:
                print('Problemas al actualizar el producto')
    except mysql.MySQLError as error:
        print(str(error))
    finally:
        cursor.close()



def eliminar():
    try:
        cursor = miConexion.cursor()
        codigo = int(input('Ingrese el código del producto a eliminar: '))
        productoEliminar = (codigo,)
        consulta = 'DELETE FROM productos WHERE nproCodigo = %s'
        cursor.execute(consulta, productoEliminar)
        miConexion.commit()
        if cursor.rowcount == 1:
            print('Producto eliminado')
        else:
            print('No hay productos con el código ingresado')
    except mysql.MySQLError as error:
        print(str(error))
    finally:
        cursor.close()

# Ejecutar funciones
# insertar()
# listar()
# consultarPorCodigo()
# actualizar()
eliminar()
