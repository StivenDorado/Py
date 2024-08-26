from alumno import Alumno

class Curso():
    def __init__(self, nombre: str)-> None:
        self.__nombre = nombre
        self.__alumnos = []  # Array
        
        
    def matricularAlumno(self, alumno)-> None:
        self.__alumnos.append(alumno)
        
    def anularMatricula(self, alumno)-> None:
        self._alumnos.remove(alumno)
        
        
    def getNombre(self)->str:
        return self.__nombre
    
    def getAlumnos(self)->list: #para los arrays
        return self.__alumnos