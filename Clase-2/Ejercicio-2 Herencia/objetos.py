# main.py

from persona import Persona
from aprendiz import Aprendiz

# Persona Instances
persona1 = Persona('11', 'Carlitos', 'carlitos@ex.com')
print(persona1.getIdentificacion())
persona1.setIdentificacion('111')
print(persona1.getIdentificacion())

persona2 = Persona('22', 'Diana', 'Diana@ex.com')
print(persona2.getNombre())
persona2.setNombre('12')  # Update name if needed
persona2.setNombre('111')

persona3 = Persona(identificacion='324', nombre='rosa', correo='rous@ex.com')

# Aprendiz Instance
aprendiz1 = Aprendiz(222, '39', 'Eddie', 'eddie@ex.com')
print(aprendiz1.getIdentificacion())
aprendiz1.setIdentificacion("100")
print(aprendiz1.getIdentificacion())

aprendiz1.setPuntajeIcfes(380)
print(aprendiz1.getPuntajeIcfes())
