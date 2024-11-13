"""
Escribe un programa que pida un nombre de usuario y una contraseña 
# y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", 
# sino se da un error.
"""
#Solicitar nombre de usuario y contraseña
usuario = input("Introduce el usuario: ")
contrasena = input("Introduce tu contraseña: ")

# Verificar si las credenciales son correctas
if usuario == "pepe" and contrasena == "asdasd":
    print("Has entrado al sistema")
else:
    print("ERROR Nombre de usuario o contraseña incorrectos")