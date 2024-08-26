class Persona():
    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.__identificacion = identificacion # __ atributos privados
        self.__nombre = nombre
        self.__correo = correo 
        
    # Metodods gent para guardar valores
    def getIdentificacion(self) -> str:
        return self.__identificacion
    
    def getNombre(self) -> str:
        return self.__nombre
    
    def getCorreo(self) -> str:
        return self.__correo
    
    
    # Metodos set para cmabiar valores
    def setIdentificacion(self, identificacion: str) -> None:
        self.__identificacion = identificacion
    
    def setNombre(self, nombre: str) -> None:
        self.__nombre = nombre
        
    def setCorreo(self, correo: str) -> None:
        self.__correo = correo
        
        
    # Polomorfismo
    def __str__(self) -> str:
        print(f'Desde persona. Hola soy in objeto {type(self).__name__}')