from animal import Animal

class Perro(Animal):
    def __int__(self, peso: float)-> None:
        super().__int__(peso)
        
    def ladrar(self)->None:
        print('El perro ladra')