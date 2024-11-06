"""
Programa que pide al usuario dos números
y muestra su division. Si el segundo no es cero, 
o un mensaje de aviso en caso contrario.
"""
a = int(input("Ingresa el dividendo: "))
b = int(input("Ingresa el divisor: "))
if b!=0:
    c=a/b
    print("El resultado es: ",c)
else:
    print("ERROR MATEMÁTICO:")
