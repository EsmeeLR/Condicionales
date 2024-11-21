"""
Programa que pida tres números y los muestre ordenados (de mayor a menor);
"""
#Pide al usuario que ingrese tres números
num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Tercer número: "))

# Comparar y ordenar los números usando condicionales
if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        ordenados = (num1, num2, num3)
    else:
        ordenados = (num1, num3, num2)
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        ordenados = (num2, num1, num3)
    else:
        ordenados = (num2, num3, num1)
else:
    if num1 >= num2:
        ordenados = (num3, num1, num2)
    else:
        ordenados = (num3, num2, num1)

# Mostrar los números ordenados de mayor a menor
print("Los números ordenados de mayor a menor quedan de la siguiente manera:", ordenados)