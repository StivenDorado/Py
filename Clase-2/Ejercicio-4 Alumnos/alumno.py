class Alumno():
    def __init__(self, nombre: str, edad: int) -> None:
        self.__nombre = nombre # Privado
        self.__edad = edad
        
    # Metodos get
    def getnombre(self)->str:
        return self.__nombre
    
    def getnombre(self)->str:
        return self.__edad
     
    # Metodos set
    def setnombre(self, nombre)->None:
        self.__nombre = nombre
        
    def setnombre(self, edad)->None:
        self.__nombre = edad
        
    ############Metodos guardados por defecto PY#############
        
    def __str__(self)-> str:
        return self.__nombre