"""
Condicionales if:
    Evaluan exxpresiones booleanas

Estructura:
    if expresion:
        instrucciones
    if expresion:
        instrucciones
    else:
        instrucciones
"""
print("Programa que verifica si un número es positivo")
num = int(input("Ingresa un número: "))
# preguntar el numero es mayor a 0:
if num > 0:
    print("El número es positivo")
else: 
    print("El número es negativo")
print("Fin del programa")
print("Programa que verifica si un numero es par")
num = int(input("Ingresa un número: "))
if num % 2 == 0:
   print("Es un numero par")
else:
    print("Es un número impar")
