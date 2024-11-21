"""
El director de una escuela está organizando un viaje de estudios, y requiere 
determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de 
viajes por el servicio. La forma de cobrar es la siguiente: 
si son 100 alumnos o más, el costo por cada alumno es de 65 euros; 
de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, 
y si son menos de 30, el costo de la renta del autobús es de 4000 euros, 
sin importar el número de alumnos. 
Realice un programa que permita determinar el pago a la compañía de autobuses 
y lo que debe pagar cada alumno por el viaje.
"""
#Pedir al usuario que ingrese el número de alumnos asistiran
alumnos = int(input("Ingrese la cantidad de alumnos que irán al viaje de estudios: "))

#Calcular el costo si son 100 alumnos o más
if alumnos >= 100:
    c_alumno = 65
    ser_compañia = alumnos * c_alumno
    print("Se cobrará por alumno",c_alumno,"euros y se le pagará a la compañia por el servicio",ser_compañia, "euros")

#Calcular el costo si son entre 50 a 99 alumnos
elif 50<=alumnos<=99:
    c_alumno = 70
    ser_compañia = alumnos * c_alumno
    print("Se cobrará por alumno",c_alumno,"euros y se le pagará a la compañia por el servicio",ser_compañia, "euros")
#Calcular el costo si son entre 30 a 49 alumnos  
elif 30<=alumnos<=49:
    c_alumno = 95
    ser_compañia = alumnos * c_alumno
    print("Se cobrará por alumno",c_alumno,"euros y se le pagará a la compañia por el servicio",ser_compañia, "euros")
#Indicar que si son menos de 30 alumnos, el costo del autobús es de 4000 euros
elif alumnos<30:
    c=4000
    print("El costo de la renta del autobús es de",c,"euros")
    print("Fin del programa")