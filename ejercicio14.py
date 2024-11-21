"""
Escribe un programa que pida un número entero entre uno y doce e imprima el 
#número de días que tiene el mes correspondiente.
# Si introducimos otro número nos da un error.
"""
# Solicitamos al usuario queingrese un número entero entre 1 y 12
mes = int(input("Ingrese un número entero entre 1 y 12: "))

# Determinamos el número de días del mes correspondiente usando condicionales
if mes == 1:
    dias = 31
elif mes == 2:
    dias = 28
elif mes == 3:
    dias = 31
elif mes == 4:
    dias = 30
elif mes == 5:
    dias = 31
elif mes == 6:
    dias = 30
elif mes == 7:
    dias = 31
elif mes == 8:
    dias = 31
elif mes == 9:
    dias = 30
elif mes == 10:
    dias = 31
elif mes == 11:
    dias = 30
elif mes == 12:
    dias = 31
if (mes>=1 and mes<=12):
    print("El mes" ,mes, "tiene",dias, "dias")
else:
    print("ERROR, el número ingresado no es válido. debe ser un número entero entre 1 y 12.")