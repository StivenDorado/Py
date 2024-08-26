# Programa que diga si un numero es entero y mostrar su binario

numero = int(input('Ingrese un valor para obtener su binario: '))

binario = ''
numeroIngresado = numero


while(True):
    resultado = numero //2 # operador para division entera
    residuo = numero % 2 # division para residuo
    binario = binario + str(residuo)
    if(resultado == 1):
        binario = binario + str(resultado)
        break
    numero = resultado #en la misma linea tabuladora del if 
    
print('el binario resultante: ') 
# print(binario[::-1]) retrocede el numero de atras hacia adelante

# for para impl¿rimir el numero binario de atras hacia adelante
for i in range(len(binario) -1, -1, -1):
    print(binario[i],  end='')

    

    