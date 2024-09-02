import sqlite3

baseDatos = 'negocio.db'


miConexion = sqlite3.connect(baseDatos)

def insetarCategorias():
    try:
        nombre = 'Calzado'
        cursor = miConexion.cursor()
        categoria = (nombre,)
        consulta = 'INSERT INTO Categorias VALUES(NULL, ?)'
        cursor.execute(consulta, categoria)
        miConexion.commit()
        if(cursor.rowcount == 1):
            print(f'Categoria agregada con id {cursor.lastrowid}')
            
    except miConexion.Error as error:
        print(str(error))
        
        
#insetarCategorias()

def listarCatrgoria():
    try:
        # Crear el cursor
        cursor = miConexion.cursor()
        # Texto de la consulta
        consulta = 'SELECT * FROM Categorias'
        cursor.execute(consulta)
        productos = cursor.fetchall()
        if len(productos) > 0:
            # Imprimir
            for c in productos:
                print(c)
        else:
            print('En el momento no hay categorias registradas')
    
    except miConexion.Error as error:
        print(str(error))
        
# listarCatrgoria()

def insertarProducto():
    try:
        cursor = miConexion.cursor()

        codigo = int(input("Ingrese Código de Producto: "))
        
        nombre = input("Nombre de Producto: ")
        precio = int(input("Precio del Producto: "))
        categoria = int(input("Seleccione categoria ingresando numero de categoria: "))
        producto = (codigo, nombre, precio, categoria)
        consulta = "insert into Productos values (null,?,?,?,?)"
        cursor.execute(consulta, producto)
        miConexion.commit()

        if(cursor.rowcount==1):
            print(f"Producto insertado con id {cursor.lastrowid}")

    except miConexion.Error as error:
        miConexion.rollback()
        print(str(error))

insertarProducto()

def listarProductos():
    try:
        cursor = miConexion.cursor()
        consulta = """
        select p.proCodigo, p.proNombre, p.proPrecio, c.catNombre
        from Productos p inner join Categorias c
        on p.proCategoria = c.idCategoria
        """
        cursor.execute(consulta)
        productos = cursor.fetchall()
        for p in productos:
            print(p)
    except miConexion.Error as error:
        print(str(error))


# actividad realizar operaciones 
# consultar por categoria 
# actualizar  Producto
# eliminar producto





def eliminarProductos():
    try:
        cursor = miConexion.cursor()
        codigo = int(input('Ingrese el id de la Productos a eliminar: '))
        productosEliminar = (codigo,)
        consulta = 'DELETE FROM Productos WHERE nproCodigo = ?'
        cursor.execute(consulta, productosEliminar)
        miConexion.commit()
        if cursor.rowcount == 1:
            print('Productos eliminado')
        else:
            print('No hay CProductos con el código ingresado')
            
    except miConexion.Error as error:
        print(str(error))
    finally:
        cursor.close()
        
# eliminarProductos()