palabras = []

for i in range(10):
    palabra = input("Ingrese una palabra: ")
    palabras.append(palabra)
    
palabrasABuscar = input('Ingrese Palabra que quiere buscar: ')

# Buscar la palabra en la lista de palabras

cantidad = palabras.count(palabrasABuscar)

print(f'La palabra {palabra} se repite {cantidad} en la lista\n {palabras}')

