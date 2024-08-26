from empleado import Empleado

class Empresa:
    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre
        self.__empleados = []

    def agregarEmpleado(self, nombre: str, cargo: str, sueldo: int) -> None:
        empleado = Empleado(nombre=nombre, cargo=cargo, sueldo=sueldo)
        self.__empleados.append(empleado)

    def getNombre(self) -> str:
        return self.__nombre

    def getEmpleados(self):
        return self.__empleados

    def __str__(self) -> str:
        empleados_str = "\n".join(str(emp) for emp in self.__empleados)
        return f'Empresa: {self.__nombre}\nEmpleados:\n{empleados_str}'

    def __del__(self):
        print('Empresa ha sido eliminada')
