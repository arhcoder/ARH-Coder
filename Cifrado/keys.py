def keys(password):
    LEN = len(password)
        SUMA = 0
        for i in range(0, LEN):
            SUMA += ord(password[i])
        MULTI = SUMA * LEN