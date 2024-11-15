"""Realiza un programa que pida por teclado el resultado (dato entero) obtenido 
#al lanzar un dado de seis caras y muestre por pantalla el número en letras 
#(dato cadena) de la cara opuesta al resultado obtenido.
#* Nota 1: En las caras opuestas de un dado de seis caras están los números: 
#1-6, 2-5 y 3-4.
#* Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, 
#se mostrará el mensaje: "ERROR: número incorrecto."
"""
res_obt=int(input("Ingresa el número otenido: "))
if 1<=res_obt<=6:
    if res_obt==1:
        cadena="seis"
        print("El número en la cara opuesta del resultado obtenido es:", cadena)
    elif res_obt==2:
        cadena="cinco"
        print("El número en la cara opuesta del resultado obtenido es:", cadena)
    elif res_obt==3:
        cadena="cuatro"
        print("El número en la cara opuesta del resultado obtenido es:", cadena)
    elif res_obt==4:
        cadena="tres"
        print("El número en la cara opuesta del resultado obtenido es:", cadena)
    elif res_obt==5:
        cadena="dos"
        print("El número en la cara opuesta del resultado obtenido es:", cadena)
    elif res_obt==6:
        cadena="uno"
        print("El número en la cara opuesta del resultado obtenido es:", cadena)
else: 
    print("ERROR número incorrecto")