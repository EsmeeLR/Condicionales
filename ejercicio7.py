"""
Realiza un algoritmo que calcule la potencia, para ello pide por teclado 
# la base y el exponente. Pueden ocurrir tres cosas:
# * El exponente sea positivo, sólo tienes que imprimir la potencia.
# * El exponente sea 0, el resultado es 1.
# * El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
"""
#Pide al usuario la base y la potencia
a = int(input("Ingresa el número base:"))
b = int(input("Ingresa la exponente:"))
 
 #Verifica que el exponente sea positivo para imprimir supotencia
if b > 0:
    c=a**b
    print("El resultado es: ",c) 

#Verificar que el exponente no sea 0
elif b == 0:
    c=1
    print("El resultado de elevar el número ingresdo a la 0 potencia siempre es: ",c)

#Si el exponente es negativo, el resultado será 1/potencia con el exponente positivo
else:
    c=1/2**(-1*b) 
    print("El resultado de elevar a por el exponente negativo dado es: ", c)