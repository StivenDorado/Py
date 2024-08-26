from persona import Persona

class Intructor(Persona):
    
    def __init__(self, especialidad: str = 'software', identificacion: str = '13453', nombre: str = 'Cesar', correo: str = 'cesar@ex.com'):
        super().__init__(identificacion, nombre, correo)
        self.__especialidad = especialidad
        
    def getEspecialidad(self)-> str:
        return self.__especialidad
    
    def setEspecialidad(self,especialidad)-> None:
        self.__especialidad = especialidad
        
    # Polomorfismo
    def __str__(self) -> str:
        print(f'Desde persona. Hola soy in objeto {type(self).__name__}')