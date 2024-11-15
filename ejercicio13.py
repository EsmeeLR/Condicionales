"""
Realiza un programa que pida el dia de la semana (del 1 al 7) y escriba 
#el dia correspondiente. 
# Si introducimos otro número nos da un error.
"""
dia_num=int(input("Ingresa el número otenido: "))
if 1<=dia_num<=7:
    if dia_num==1:
        cadena="Lunes"
        print("El día",dia_num, "es", cadena)
    elif dia_num==2:
        cadena="Martes"
        print("El día",dia_num, "es", cadena)
    elif dia_num==3:
        cadena="Miércoles"
        print("El día",dia_num, "es", cadena)
    elif dia_num==4:
        cadena="Jueves"
        print("El día",dia_num, "es", cadena)    
    elif dia_num==5:
        cadena="Viernes"
        print("El día",dia_num, "es", cadena)
    elif dia_num==6:
        cadena="Sábado"
        print("El día",dia_num, "es", cadena)
    elif dia_num==7:
        cadena="Domingo"
        print("El día",dia_num, "es", cadena)
else: 
    print("ERROR número incorrecto")