"""
Realice el código donde las claves sean nombres de estudiantes y los valores su calificaciones. 
Pida al usuario el nombre del estudiante siendo que si esta en el diccionario muestre la calificación 
y sino muestre un mensaje diciendo que no hay datos
"""

estudiantes = {
  "Juan": 4.0,
  "Pedro": 3.8,
  "Alejandro": 4.5
}

nombre = input("Ingrese el nombre del estudiante: ")

if nombre in estudiantes:
  print(estudiantes[nombre])
else:
  print("No hay datos")