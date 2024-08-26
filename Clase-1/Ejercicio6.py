#Hacer un programa en Python que implemente una función que reciba
#como parámetro una lista con números enteros y como resultado debe
#devolver la suma de los números

def sumalista(listaNumeros)->int:
    suma = 0
    for numero in listaNumeros:
        suma += numero
        return suma
    
numeros = [2,6,3,2,6]

sumaNumeros = sumalista(numeros)

print(sumaNumeros)