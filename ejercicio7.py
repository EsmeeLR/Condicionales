"""
Realiza un algoritmo que calcule la potencia, para ello pide por teclado 
# la base y el exponente. Pueden ocurrir tres cosas:
# * El exponente sea positivo, sólo tienes que imprimir la potencia.
# * El exponente sea 0, el resultado es 1.
# * El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
"""
a = int(input("Ingresa el término base: "))
b = int(input("Ingresa la potencia: "))
if b>0:
    r = (a**b)
    print("El resultado es:", r)
elif b==0:
    r=1
    print("El resultado es:", r)
else: 
    p_pos= -1*b
    r= "1""/"+a+"^"+p_pos
    print("El resultado es:",r )
