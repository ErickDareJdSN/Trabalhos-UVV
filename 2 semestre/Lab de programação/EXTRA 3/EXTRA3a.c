#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int pontox1, pontoy1, pontox2, pontoy2;
double distancia;

int main()
{
    printf("==CALCULADORA DE DISTÂNCIA ENTRE DOIS PONTOS===\n\n");
    printf("Digite a coordenada X do ponto 1: ");
    scanf("%d", &pontox1);

    while ((scanf("%d", &pontox1) != 1))
    {
        printf("Digite um número inteiro válido: ");
        scanf("%d", &pontox1);
        while (getchar() != '\n');
    }
    

    printf("\nDigite a coordenada Y do ponto 1: ");
    scanf("%d", &pontoy1);

    while ((scanf("%d", &pontoy1) != 1))
    {
        printf("Digite um número inteiro válido: ");
        scanf("%d", &pontoy1);
        while (getchar() != '\n');
    }

    printf("PRIMEIRA COORDENADA REGISTRADA: (%d, %d)", pontox1, pontoy1);
    printf("\n\nDigite a coordenada X do ponto 2: ");
    scanf("%d", &pontox2);

    while ((scanf("%d", &pontox2) != 1))
    {
        printf("Digite um número inteiro válido: ");
        scanf("%d", &pontox2);
        while (getchar() != '\n');
    }

    printf("\nDigite a coordenada Y do ponto 2: ");
    scanf("%d", &pontoy2);

    while ((scanf("%d", &pontoy2) != 1))
    {
        printf("Digite um número inteiro válido: ");
        scanf("%d", &pontoy2);
        while (getchar() != '\n');
    }

    distancia = sqrt(pow(pontox2 - pontox1, 2) + pow(pontoy2 - pontoy1, 2));

    printf("\n\n===RESULTADOS===\n\n");
    printf("Ponto 1: (%d, %d)", pontox1, pontoy1);
    printf("\nPonto 2: (%d, %d)", pontox2, pontoy2);
    printf("\n\nDistância entre os dois pontos: %.2lf", distancia);

    return 0;
}