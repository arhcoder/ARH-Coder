m = input("Aquí: ")
print(len(m))

print("\n| CIFRADOR |\n")
    password = input("| Crea una contraseña: ")

    LEN = len(password)
    SUMA = 0
    for i in range(0, LEN):
        SUMA += ord(password[i])
    MULTI = SUMA * LEN

    # Lee el mensaje.
    message = input("\n| Ingrese el mensaje: ")