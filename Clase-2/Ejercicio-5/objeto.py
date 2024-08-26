from empresa import Empresa

# Crear instancia de Empresa
elSena = Empresa('SENA')

# Agregar empleados
elSena.agregarEmpleado('Paco Rojas', 'Director Regional', 75000000)
elSena.agregarEmpleado('Pablo Ortiz', 'Instructor', 55000000)
elSena.agregarEmpleado('Cesar Chacon', 'Tesorero', 85000000)

# Imprimir detalles de la empresa y empleados
print(elSena)

# Eliminar la instancia de Empresa
del elSena
