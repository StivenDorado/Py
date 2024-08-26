edades = []

for i in range(5): # cantidad maxima de valores que acepta el Array 
    edad = int(input(f"Introduce edad de  la persona: "))
    edades.append(edad)
    
    
#print(edades)    

menor = min(edades)
mayor = max(edades)
print(f'La edad Mayor es: {mayor}')
print(f'La edad Menor es: {menor}')