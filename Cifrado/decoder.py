from coders import keyLEN, keySUMA, keyMULTI

# S = {0, ..., 55295} - {0, 7, ... 10, 13, 27, 128 ... 160};
NO = [0] + list(range(7, 11)) + [13, 27] + list(range(128, 161))
total = 55296 - len(NO) # Total = 55,256;

def decode(code, password):
    message = ""

    LEN = keyLEN(password)
    SUMA = keySUMA(password)
    MULTI = keyMULTI(LEN, SUMA)

    # Ciclo que analiza todos los caracteres del mensaje.
    for index in range(0, len(code)):
        caracter = ord(code[index])

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

        # Considera los valores exclusivos {0, 7, ... 10, 13, 27, 128 ... 160}
        for i in range(0, len(NO)):
            if caracter == total + i:
                ncaracter = NO[i]
            else:
                # Avanza la cantidad de pasos necesarios.
                ncaracter = caracter
                for i in range (1, pasos+1):
                    ncaracter -= 1
                    if ncaracter == 0:
                        ncaracter = total
                if(ncaracter == total):
                    ncaracter = 0
        
        # Genera el mensaje encriptado.
        message += chr(ncaracter)
    return message