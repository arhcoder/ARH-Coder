total = int(input("Total: "))
inicio = int(input("Inicio: "))
pasos = int(input("Pasos: "))
control = int(input("(Incremento = 1 | Decremento = 0): "))
final = inicio

if(control == 1):
    for i in range (1, pasos+1):
        final += 1
        if final == total:
            final = 0
    print(final)
else:
    for i in range (1, pasos+1):
        final -= 1
        if final == 0:
            final = total
    if(final == total):
        final = 0
    print(final)