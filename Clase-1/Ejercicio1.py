# obtener salario
salario = int(input('ingrese su salario'))

# obtener impuesto

if (salario < 1000000):
    impuesto = salario * 1/100
elif(salario >=  1000000 and salario < 2000000):
    impuesto = salario * 3/100
elif(salario >=  2000000 and salario < 3000000):
    impuesto = salario * 5/100
elif(salario >=  4000000 and salario < 10000000):
    impuesto = salario * 7/100
else: 
    impuesto = salario * 10/100
    
# Mostrar resultados
print(f'Deacuerdo a su salario: {salario} El impuesto a pagar es: {impuesto}')  # Mostrar el imp


