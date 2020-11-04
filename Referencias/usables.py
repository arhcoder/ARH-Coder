NOusables = [2, 4, 5]
total = 9 + 1 - len(NOusables)
for f in range(0, 10):
    ncaracter = int(input("Ingresa número: "))
    for i in range(0, len(NOusables)):
            if ncaracter == NOusables[i]:
                ncaracter = total + i
    print(ncaracter)