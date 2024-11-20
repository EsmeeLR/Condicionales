"""
JUEGO DE PIEDRA PAPEL O TIJERA
Progrma que lea las opciones de 2 jugadores, y muestra el resultado:
Empate, gana jugador 1 o gana jugador 2
Si introducim una opción que no coincida con piedra papel o tijera
diga que es opción incorrecta
"""
J1= input(" ¿Qué opción ejigió el jugador 1? ")
J2= input(" ¿Qué opción ejigió el jugador 2? ")
if (J1.lower() == "piedra" or J1.lower() == "papel" or J1.lower() == "tijera") \
    and (J2.lower() == "piedra" or J2.lower() == "papel" or J2.lower() == "tijera"):
    if J1 == J2:
        print("Hay un empate")
    elif J1 == "papel" and J2 == "piedra":
        print("Gana el jugador 1 gana")
    elif J1 == "piedra" and J2 == "tijera":
        print("Gana el jugador 1 gana")
    elif J1 == "tijera" and J2 == "papel":
        print("Gana el jugador 1 gana")
    else:
        print("Gana el jugador 2")
else: 
    print("Opción INCORRECTA")
