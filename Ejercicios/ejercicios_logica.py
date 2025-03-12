"""
? Escribe un programa que muestre por consola (con un print) los números de 1 a 100 
 ? (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
 ? - Múltiplos de 3 por la palabra "fizz".
 ? - Múltiplos de 5 por la palabra "buzz".
 ? - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""
# Ingrese el codigo aquí

# for x in range(1, 101):
#   if x % 3 == 0 and x % 5 == 0: 
#     print("fizzbuz")
#   elif x % 5 == 0:
#     print("buzz")
#   elif x % 3 == 0:
#     print("fizz")
#   else:
#     print(x)


"""
? Crea una única función (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
  ? - La función recibirá por parámetro sólo UN polígono a la vez.
  ? - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
  ? - Imprime el cálculo del área de un polígono de cada tipo.
"""

# Ingrese el codigo aquí
def area_poligono(poligono, base, altura = None):
  if poligono == "triangulo":
    return base * altura / 2
  elif poligono == "cuadrado":
    return base * base
  elif poligono == "rectangulo":
    return base * altura
  
print(area_poligono("cuadrado", 5))