#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define n 5

char primero[20], segundo[20], animal[20], color[20], nombre[20];
int Clave[n], Longitudes[n], SumaASCII[n];
int suma = 0, i, i2;

int main()
{
    // Lee los n datos
    printf("\n* Escribe tu n%cmero favorito: ", 163);
    scanf("%s", &primero);
    printf("\n* Escribe tu segundo n%cmero favorito: ", 163);
    scanf("%s", &segundo);
    printf("\n* Escribe tu animal favorito: ");
    scanf("%s", &animal);
    printf("\n* Escribe tu color favorito: ");
    scanf("%s", &color);
    printf("\n* Escribe un nombre que te guste: ");
    scanf("%s", &nombre);
    
    // Asigna los datos ingreados, al vector Datos
    char *Datos[n] = {primero, segundo, animal, color, nombre};

    // LONGITUDES
    printf("\n\n\nLONGITUDES:\n____________________\n");
    for (i = 0; i < n; i++)
    {
        Longitudes[i] = strlen(Datos[i]);
        printf("\n%i", Longitudes[i]);
    }
    printf("\n____________________");

    // SUMA ASCII
    printf("\n\n\nSUMA ASCII:\n____________________\n");
    for (i = 0; i < n; i++)
    {
        for (i2 = 0; i2 < strlen(Datos[i]); i2++)
        {
            suma += Datos[i][i2];
        }       
        SumaASCII[i] = suma;
        printf("\n%i", SumaASCII[i]);
        suma = 0;
    }
    printf("\n____________________\n");

    // Genera el vector de clave
    for (i = 0; i < n; i++)
    {
        Clave[i] = Longitudes[i] * SumaASCII[i];
        printf("\n%i", Clave[i]);
    }
    
    printf("\n\n");
    system("PAUSE");
}