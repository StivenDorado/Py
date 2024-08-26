# ejer 2
vegetariana = ['Pimiento', 'Tofu']
noVegetariana = ['Peperoni', 'Jamon', ' Salmón']

opcionPizza = int(
    input('Tipo de Pizzas\n1.Vegetariana\n2.No Vegetariana\n Selecione Pizza: '))

if opcionPizza == 1:
    print('Ingredientes Pizza Vegetariana: ')
    print('1. ', vegetariana[0])
    print('2. ', vegetariana[1])
    ingrediente = int(input('Seleccione Ingrediente: (1, 2): '))
    ingredientesPizza = ['Tomate', 'Mozarekka', vegetariana[ingrediente-1]]
else:
    print('Ingredientes Pizza No Vegetariana: ')
    print('1. ', vegetariana[0])
    print('2. ', vegetariana[1])
    print('3. ', vegetariana[2])
    ingrediente = int(input('Seleccione Ingrediente: (1, 2, 3): '))
    ingredientesPizza = ['Tomate', 'Mozarekka', noVegetariana[ingrediente-1]]
    
print('Ingredientes Pizza\n', ingredientesPizza)
