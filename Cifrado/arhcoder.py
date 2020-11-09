from os import system
from encoder import encode
from decoder import decode

# Desarrollador: Alejandro Ramos Herrera (@arhcoder).
# Licencia: Creative Commons - Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).
# Desarrollado en noviembre de 2020.
# Tiempo de desarrollo: X.
# Propósito: Práctica y Entretenimiento.

option = 1
print("\n\t  | ARH CODER |")

while option != 0:
    print("__________________________________")
    print("\n1: Encriptar un mensaje\n2: Descifrar un mensaje\n0: Salir\n")
    option = int(input("Selecciona una opción: "))
    system("cls")

    if option == 1:
        print("\n| CIFRADOR |\n")
        password = input("| Crea una contraseña: ")
        message = input("\n| Crea un mensaje: ")
        print("\n||| Mensaje encriptado: ", encode(password, message))

    elif option == 2:
        print("\n| DESCIFRADOR |\n")
        code = input("| Ingresa el mensaje: ")
        password = input("\n| Coloca la contraseña: ")
        print("\n||| Mensaje original: ", decode(code, password))

    elif option == 0:
        print("\nAdiós...")
        
    else:
        print("\nError! Inténtalo de nuevo...")

print("__________________________________")