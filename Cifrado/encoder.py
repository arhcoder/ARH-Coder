# S = {0, ..., 55295} - {0, 7, ... 10, 13, 27, 128 ... 160}

total = 256

password = input("Crea una contraseña: ")

LEN = len(password)
SUMA = 0
for i in range(0, LEN):
    SUMA += ord(password[i])
MULTI = SUMA * LEN

# Lee el mensaje.
mensaje = input("Ingrese el mensaje: ")

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
        ncaracter = caracter + LEN
    # Si el número de caracter actual, no es primo.
    else:
        # Si es par.
        if index % 2 == 0:
            ncaracter = caracter + SUMA
        # Si es impar.
        else:
            ncaracter = caracter + MULTI  

    # Modifica ncaracter, para que entre dentro del rango de síbolos (0 - total).
    # (pasos - (total - inicio)) % total.
    if ncaracter > total - 1:
        ncaracter = (ncaracter - (total - caracter)) % total
    
    print(ncaracter)
    # Exluye los números {0, 7, ... 10, 13, 27, 128 ... 160}
    

    # Genera el mensaje encriptado.
    # mensaje = str(mensaje.replace(mensaje[index], chr(ncaracter)))
    
print(mensaje)