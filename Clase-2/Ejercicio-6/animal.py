class Animal():
    def __init__(self, peso:float)-> None:
        self.peso = peso
        
        
    def respirar(self)->None:
        return (f'El{type(self).__name__} esta Respirando')