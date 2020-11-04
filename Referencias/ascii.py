# S = {0, ..., 55295} - {0, 7, ... 10, 13, 27, 128 ... 160}

for i in range(0, 55296):
    symbol = chr(i)
    print(i, " = ", symbol)