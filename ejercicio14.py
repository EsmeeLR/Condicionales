"""
Escribe un programa que pida un número entero entre uno y doce e imprima el 
#número de días que tiene el mes correspondiente.
# Si introducimos otro número nos da un error.
"""
meses = {
    1: 31,
    2: 28,  # No se considera el año bisiesto en este caso
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
#Solicitar número entre 1 y 12
numero_mes = int(input("Introduce un número entero entre uno y doce: "))

# Verificar si el número está en el rango válido
if numero_mes in meses:
    print(f"El mes {numero_mes} tiene {meses[numero_mes]} días.")
else:
    print("Error: El número introducido no está entre uno y doce.")
