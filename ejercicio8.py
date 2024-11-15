"""
Programa que pida dos números 'nota' y 'edad' y un caracter 'sexo'
y muestre el mensaje 'aceptada' si la nota es mayor o igual a cinco,
la edad es mayor o igual a dieciocho y el sexo es 'F'.
En caso de que se cumpla lo mismo, pero el sexo sea 'M', debe imprimir 'POSIBLE'.
Si no se cumplen dichas condiciones se debe mostrar 'no aceptada'.
"""
#Pide al usuario que ingrese dos números y un caracter
nota = int(input("Nota obtenida: "))
edad = int(input("Edad: "))
sexo = (input("Sexo(F o M): "))

#Verificar si los valores cumplen con las condiciones
if nota > 5 and edad>18:
    if sexo == "F":
        print("ACEPTADA")
    else: 
        print("POSIBLE")
else: 
    print("NO ACEPTADA")
    