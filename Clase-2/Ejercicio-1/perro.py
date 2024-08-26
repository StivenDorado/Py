class Perro():
    def __init__(self, nombre, raza):
        self.name = nombre # no hay necesidad de que el self se llame de la misma forma quue el atributo de la clase 
        self.raza = raza
        
    def ladrar(self): # las variables deben ir todas en la misma linea de tabulacion
            print("Woof")
            
    def caminar(self, pasos):
            print(f"{self.name} caminando {pasos} pasos") 