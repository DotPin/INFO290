#define L 15
#include <string.h>
typedef struct arreglo
{
    char *id;
    int arr[8];
    struct arreglo *next;
} arreglo;
int largo = 0;
arreglo *aux[L];

arreglo *nuevo_arreglo()
{
    arreglo *a = (arreglo *)malloc(sizeof(arreglo));
    a->next = NULL;
    return a;
}

int buscar(char *id, int option);
void ordenar(int index);
void meter(char *id, int val, int pos);
void mirar(char *id);
void dato(char *id, int pos);
void sacar(char *id, int pos);

void iniciar(char *id, int e1, int e2, int e3, int e4, int e5, int e6, int e7, int e8)
{
    //primero busca si existe previamente el identificador
    int index = buscar(id, 2);
    if (index == -1)
    {
        aux[largo] = nuevo_arreglo();
        aux[largo]->arr[0] = e1;
        aux[largo]->arr[1] = e2;
        aux[largo]->arr[2] = e3;
        aux[largo]->arr[3] = e4;
        aux[largo]->arr[4] = e5;
        aux[largo]->arr[5] = e6;
        aux[largo]->arr[6] = e7;
        aux[largo]->arr[7] = e8;
        aux[largo]->id = id;

        largo++;

        printf(">> Identificador %s ha sido inicializado\n", id);
    }
}
int buscar(char *id, int option)
{
    for (int i = 0; i < largo; i++)
    {
        if (strcmp(aux[i]->id, id) == 0)
        {
            if (option == 2)
            {
                printf(">> El identificador %s ya se encuentra en los registros\n", id);
            }
            return i;
        }
    }
    if (option == 1)
    {
        printf(">> El identificador %s no se encuentra en los registros\n", id);
    }
    return -1;
}
void ordenar(int index)
{
    int ceros = 0;
    int arr2[8] = {0, 0, 0, 0, 0, 0, 0, 0};
    for (int i = 0; i < 8; i++)
    {
        if (aux[index]->arr[i] == 0)
        {
            ceros++;
        }
        else
        {
            arr2[i - ceros] = aux[index]->arr[i];
        }
    }
    for (int i = 0; i < 8; i++)
    {
        aux[index]->arr[i] = arr2[i];
    }
}
void meter(char *id, int val, int pos) //como estaba no empujaba los valores siguientes hacia la derecha como deberia
{
    int index = buscar(id, 1);
    if (pos > 8 && pos < 1)
    {
        printf(">> La posicion %d no pertenece al intervalo correcto de indices\n", pos);
        printf("del arreglo. Debe ser entre 1 a 8, intente nuevamente... \n");
    }
    else
    {
        for (int i = 7; i > pos - 1; i--)
        {
            aux[index]->arr[i] = aux[index]->arr[i - 1];
        }
        aux[index]->arr[pos - 1] = val;
        ordenar(index);
        printf(">> Digito %d agregado a %s en posicion %d\n", val, id, pos);
    }
}
/*
PARTIR
INICIAR(L1,2,4,6,0,0,0,0,0)
METER(L1,5,3)
MIRAR(L1)
INICIAR(L2,9,3,5,7,0,0,0,0)
SACAR(L2,1)
DATO(L2,2)
METER(L2,6,3)
MIRAR(L2)

*/
void mirar(char *id)
{
    int index = buscar(id, 1);
    if (index > -1)
    {
        printf(">> ");
        for (int j = 0; j <= 7; j++)
        {
            printf("%d ", aux[index]->arr[j]);
        }
        printf("\n");
    }
}
void dato(char *id, int pos)
{
    int index = buscar(id, 1);
    if (index > -1)
    {
        if (pos > 0 && pos <= 8)
        {
            printf(">> %d\n", aux[index]->arr[pos - 1]);
        }
        else
        {
            printf(">> La posicion %d no pertenece al intervalo correcto de indices\n", pos);
            printf("del arreglo. Debe ser entre 1 a 8, intente nuevamente... \n");
        }
    }
}
void sacar(char *id, int pos)
{
    int index = buscar(id, 1);
    if (index > -1)
    {
        if (pos > 0 && pos <= 8)
        {
            printf(">> Sacando de %s elemento en posicion %d\n", id, pos);
            aux[index]->arr[pos - 1] = 0;
            ordenar(index);
        }
        else
        {
            printf(">> La posicion %d no pertenece al intervalo correcto de indices\n", pos);
            printf("del arreglo. Debe ser entre 1 a 8, intente nuevamente... \n");
        }
    }
}
