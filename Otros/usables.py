NO = [2, 4, 5]
total = 9 + 1 - len(NO)

for f in range(0, 10):
    ncaracter = int(input("Ingresa número: "))
    for i in range(0, len(NO)):
            if ncaracter == NO[i]:
                ncaracter = total + i
    print(ncaracter)