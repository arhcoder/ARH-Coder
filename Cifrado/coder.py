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

    # Si el número de caracter actual, es par.
    if index % 2 == 0:
        ncaracter = caracter + SUMA
    else:
        divisores = 0
        for i in range (1, index):
            if index % i:
                divisores += 1

        # Si el número de caracter actual, no es primo.
        if divisores != 2:
            ncaracter = caracter + MULTI
        # Si el número de caracter actual, es primo.
        else:
            ncaracter = caracter + LEN
        print(ncaracter)
    # Modifica ncaracter, para que entre dentro del rango de síbolos (0 - total).
    # (pasos - (total - inicio)) % total.
        if ncaracter > total - 1:
            ncaracter = (ncaracter - (total - caracter)) % total

    # print(ncaracter)
    
    # Exluye los números {0, 7, ... 10, 13, 27, 128 ... 160}
            
# Genera el nuevo mensaje.