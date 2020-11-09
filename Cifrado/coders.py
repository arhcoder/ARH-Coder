def keyLEN(password):
    return len(password)

def keySUMA(password):
    SUMA = 0
    for i in range(0, len(password)):
        SUMA += ord(password[i])
    return SUMA

def keyMULTI(LEN, SUMA):
    return LEN * SUMA