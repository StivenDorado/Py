from alumno import Alumno
from cursos import Curso


unCurso = Curso('desarrollo web PY')

alumno1 = Alumno('maria', 16)
alumno2 = Alumno('paula', 13)
alumno3 = Alumno('diana', 20)

# Matricula alumnos
unCurso.matricularAlumno(alumno1)
unCurso.matricularAlumno(alumno2)
unCurso.matricularAlumno(alumno3)

print(f'Curso: {unCurso.getNombre()}')
print('Relacion de Alumnos Matriculados')
print(unCurso.getAlumnos())


alumnos = unCurso.getAlumnos()

for a in alumnos:
    print()

for a in alumnos:
    print(a.getNombre())
    print(a.getEdad())