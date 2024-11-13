"""
Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
"""
#Pide al usuario que ingrese una cadena
c = input("Ingresa una cadena: ")

# Comprobar si la cadena es una letra mayúscula
if len(c) == 1 and c.isupper():
    print("La cadena es una letra mayúscula")
else:
    print("La cadena no es una letra mayúscula")