from animal import Animal

class Pez(Animal):
    def __int__(self, peso: float)-> None:
        super().__int__(peso)
        
    def nadar(self)->None:
        print('El pez nada')
        
    