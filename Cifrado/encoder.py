# S = {0, ..., 55295} - {0, 7, ... 10, 13, 27, 128 ... 160};
NOusables = [0, 13, 27] + list(range(7, 11)) + list(range(128, 161))
# Total = 55,256;
total = 55296 - len(NOusables)
MENSAJE = ""

print("\n| CIFRADOR |\n")
password = input("| Crea una contraseña: ")

LEN = len(password)
SUMA = 0
for i in range(0, LEN):
    SUMA += ord(password[i])
MULTI = SUMA * LEN

# Lee el mensaje.
mensaje = input("\n| Ingrese el mensaje: ")

# Ciclo que analiza todos los caracteres del mensaje.
for index in range(0, len(mensaje)):
    caracter = ord(mensaje[index])

    # Si el número de caracter actual, es primo.
    divisores = 0
    for i in range (1, index+1):
        if index % i == 0:
            divisores += 1

    # Si el número de caracter actual, es primo.
    if divisores == 2 or index == 2:
        pasos = LEN
    # Si el número de caracter actual, no es primo.
    else:
        # Si es par.
        if index % 2 == 0:
            pasos = SUMA
        # Si es impar.
        else:
            pasos = MULTI

    # // Avanza la cantidad de pasos necesarios.
    ncaracter = caracter
    for i in range (1, pasos+1):
        ncaracter += 1
        if ncaracter == total:
            ncaracter = 0 

    # Exluye los números {0, 7, ... 10, 13, 27, 128 ... 160}
    for i in range(0, len(NOusables)):
        if ncaracter == NOusables[i]:
            ncaracter = total + i
    
    # Genera el mensaje encriptado.
    MENSAJE += chr(ncaracter)
print("\n\n| Mensaje cifrado:\n")
print(MENSAJE+"\n\n")