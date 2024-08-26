from animal import Animal

class Gato(Animal):
    def __int__(self, peso: float)-> None:
        super().__int__(peso)
        
    def maullar(self)->None:
        print('El gato maulla')