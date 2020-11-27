#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char Password[];
char Mensaje[];
char Code[];
int LONG, SUMA = 0, MULTI, i, caracter, ncaracter;

int main()
{
    // Lee la contraseña
    printf("| CODIFICADOR |");
    printf("\n\nCrea una contrase%ca: ", 164);
    scanf("%s", &Password);

    // Calcula las variables principales
    LONG = strlen(Password);
    for (i = 0; i < LONG; i++)
    {
        SUMA += Password[i];
    }
    MULTI = SUMA * LONG;

    // Lee el mensaje
    printf("\n\nEscriba el mensaje:\n");
    scanf("%s", &Mensaje);

    // Codifica el mensaje
    for(i = 0; i < strlen(Mensaje); i++)
    {
        caracter = Mensaje[i];
        if(caracter%2 == 0)
        {
            ncaracter = caracter + SUMA;
        }
        else
        {
            ncaracter = caracter + MULTI;
        }

        // (pasos - (total - inicio)) % total
        if(ncaracter > 255)
        {
            ncaracter = (ncaracter - (256 - caracter))%256;
        }
        Code[i] = ncaracter;
    }
    printf("\n\n");
    printf("%s", Code);
    printf("\n\n");
    printf("\n\n");

    for (i = 0; i < 256; i++)
    {
        printf("\n%i = %c", i, i);
    }
    printf("\n\n");
    system("PAUSE");
}