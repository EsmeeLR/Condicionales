"""
La política de cobro de una compañía telefónica es: cuando se realiza una 
#llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros 
#cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos,
#los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
#Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno
#de mañana, 15 %, y en turno de tarde, 10 %. 
#Realice un programa para determinar cuánto debe pagar por cada concepto 
#una persona que realiza una llamada.
"""
t = int(input("Ingresa el tiempo total de la llamada en minutos: "))

#condiciones segun el tiempo de la llamada
if t <=5:
    c=t*1
elif t <= 8:
    c = 5 * 1.0 + (t - 5) * 0.8
elif t <= 10:
    c = 5 * 1.0 + 3 * 0.8 + (t - 8) * 0.7
else:
    c = 5 * 1.0 + 3 * 0.8 + 2 * 0.7 + (t - 10) * 0.5

#condiciones segun el dia y el turno
dia = input("Ingresa el dia de la llamada: ")
turno = input("¿Turno? (mañana o tarde)")
if dia.lower() == "domingo":
    impuesto = c * 0.03
elif turno.lower() == "mañana":
    impuesto = c * 0.15
else: # turno de tarde
    impuesto = c * 0.10
costo_total = c + impuesto
print("El costo total por la llamada realizada es de",costo_total,"euros")