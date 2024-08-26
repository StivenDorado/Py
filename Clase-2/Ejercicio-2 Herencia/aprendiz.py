from persona import Persona

class Aprendiz(Persona):
    def __init__(self, puntajesIcfes: int = 0, identificacion: str = '15', nombre: str = 'Pepe', correo: str = 'pepito@ex.com') -> None:
        super().__init__(identificacion, nombre, correo)
        self.__puntajeIcfes = puntajesIcfes

    def getPuntajeIcfes(self) -> int:
        return self.__puntajeIcfes

    def setPuntajeIcfes(self, puntaje: int) -> None:
        self.__puntajeIcfes = puntaje
