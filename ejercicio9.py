"""
Programa que pida tres números y los muestre ordenados (de mayor a menor);
"""
#Pide al usuario que ingrese tres números
num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Tercer número: "))

numeros = [num1, num2, num3]

# Ordenar la lista de mayor a menor
numeros.sort(reverse=True)

# Imprimir los números ordenados
print("Números de mayor a menor:")
for numero in numeros:
    print(numero)