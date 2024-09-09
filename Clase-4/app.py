import pymongo
import pymongo.errors
import os

miConexion = pymongo.MongoClient("mongodb+srv://golds9013:B9RWB2pFvNGk2K8P@cluster0.gup76.mongodb.net/Tienda?retryWrites=true&w=majority&appName=Cluster0")

#obtener acceso a la base de datos

baseDatos = miConexion["Tienda"]
print(type(baseDatos))

#crear objeto para acceder a la colección productos

productos = baseDatos["Productos"]
print(type(productos))

#tareas del crud a la base de datos

def agregar():
    """_summary_: Agrega un producto a la colección
    productos de la base de datos
    """
    try:
        os.system("cls")
        codigo=int(input("Ingrese código del producto: "))
        nombre=input("Ingrese nombre del producto: ")
        precio=int(int(input("Ingrese precio del producto: ")))
        categoria=input("Ingrese categoria del producto[Electrodomestico, Ropa, Calzado]: ")
        producto={
            "codigo":codigo,
            "nombre":nombre,
            "precio":precio,
            "categoria":categoria
        }
        resultado = productos.insert_one(producto)
        if(resultado.acknowledged):
            print(f"Producto agregado correctamente con id {resultado.inserted_id}")
    except pymongo.errors as error:
        print(str(error))
        
def consultarPorCodigo():
    try:
        os.system("cls")
        codigoAConsultar = int(input("Ingrese código del producto a consultar: "))
        consulta = {"codigo": codigoAConsultar}
        producto = productos.find_one(consulta)
        print(producto)
        if(producto):
            print(f"Código : {producto['codigo']}")
            print(f"Nombre : {producto['nombre']}")
            print(f"Precio : {producto['precio']}")
            print(f"Categoría : {producto['categoria']}")
        else:
            print("No se encontró el producto")        
    except pymongo.errors as error:
        print(str(error))
        
def listar():
    try:
        os.system("cls")
        listaProductos = productos.find()
        print(type(listaProductos))
        for p in listaProductos:
            print(f"Código : {p['codigo']}")
            print(f"Nombre : {p['nombre']}")
            print(f"Precio : {p['precio']}")
            print(f"Categoría : {p['categoria']}")
            print("*" * 50)            
    except pymongo.errors as error:
        print(str(error))
        
def actualizar():
    try:
        os.system('cls')
        codigo = int(input("Ingrese código del producto a Eliminar: "))
        criterio = {"codigo": codigo}
        precio = int(input(f"Ingrese nuevo precio del producto con código {codigo}: "))
        datosActualizar = {
            "precio":   precio,          
        }
        consulta = {"$set" :  datosActualizar}
        resultado = productos.update_one(criterio, consulta)
        if(resultado.acknowledged):
            print("Producto actualizado correctamente")
        else:
            print("No existo producto con ese código")
    except pymongo.errors as error:
        print(str(error))

def eliminar():
    try:
        os.system('cls')
        codigo = int(input("Ingrese código del producto a Eliminar: "))
        criterio = {"codigo": codigo}
        resultado = productos.delete_one(criterio)
        if(resultado.deleted_count > 0):
            print("Producto eliminado correctamente")
        else:
            print("No existo producto con ese código")        
    except pymongo.errors as error:
        print(str(error))   
       
       
def agregarVariosProductos():
    try:
        os.system('cls')
        listaProductosAgregar=[]
        cantidad = int(input("Cuantos desea agregar: "))
        for i in range(cantidad):
            codigo=int(input("Ingrese código del producto: "))
            nombre=input("Ingrese nombre del producto: ")
            precio=int(int(input("Ingrese precio del producto: ")))
            categoria=input("Ingrese categoria del producto[Electrodomestico, Ropa, Calzado]: ")
            producto={
                "codigo":codigo,
                "nombre":nombre,
                "precio":precio,
                "categoria":categoria
            }
            listaProductosAgregar.append(producto)
              
        resultado = productos.insert_many(listaProductosAgregar)
        if(resultado.acknowledged):
            print(f"Productos agregados correctamente con los ids {resultado.inserted_ids}")
            
    except pymongo.errors as error:
        print(str(error))      
        
def menu():    
    while True:
        os.system('cls')
        print("\nMenu de opciones")
        print("1. Agregar producto")
        print("2. Buscar producto por Código")
        print("3. Eliminar producto")
        print("4. Listar todos los Productos")
        print("5. Actualizar Producto")
        print("6. Agregar varios productos")
        print("7. Salir")
        opcion = int(input("Ingrese opcion (1-7): "))
        match (opcion):
            case 1: agregar()                    
            case 2: consultarPorCodigo()
            case 3: eliminar()
            case 4: listar()
            case 5: actualizar()
            case 6: agregarVariosProductos()
            case 7: 
                print("Salir") 
                break
            case _otro: print("opcion fuera de rango")
            
        input("Presione enter para continuar")
        
     
    
#agregar()
#consultarPorCodigo()
#listar()
#actualizar()
#eliminar()4
#agregarVariosProductos()
menu()