# Desarrollador: Alejandro Ramos Herrera (@arhcoder).
# Licencia: Creative Commons - Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).
# Desarrollado en noviembre de 2020.
# Tiempo de desarrollo: X.
# Propósito: Práctica y Entretenimiento.

import encoder
import decoder
import coders

#def encode(password, message)
#def decode(code, password)
#def keys(password)
#def rotate(total, start, steps)

# S = {0, ..., 55295} - {0, 7, ... 10, 13, 27, 128 ... 160};
NO = [0] + list(range(7, 11)) + [13, 27] + list(range(128, 161))

# Total = 55,256;
total = 55296 - len(NO)