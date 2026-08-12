#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define PI 3.14159

int latas, custo;
double raio, altura, areatotal, litros;

int main()
{

    printf("\n\n===CALCULADORA DE LATAS DE TINTA===\n\n");
    printf("Digite o raio R do tanque em metros: ");
    scanf("%lf", &raio);

    while(raio < 1)
    {

        printf("\nTente novamente, o raio deve ser pelo menos 1: ");
        scanf("%lf", &raio);
    }
    printf("\n\nAgora digite a altura H do tanque em metros: ");
    scanf("%lf", &altura);


    while(altura < 1)
    {
        printf("\nTente novamente, a altura deve ser pelo menos 1: ");
        scanf("%lf", &altura);
    }

    raio = floor(raio);
    altura = floor(altura);
    areatotal = 2 * PI * raio * (raio + altura);
    litros = areatotal / 3;
    latas = litros / 5;
    latas = ceil(latas);
    custo = latas * 50;

    printf("\n\n===RESULTADOS===\n\n");
    printf("Valor do raio: %.0lf\n", raio);
    printf("Altura: %.0lf\n", altura);
    printf("Valor total da area: %.0lf\n\n", areatotal);
    printf("Quantidade de litros de tinta: %.0lf\n", litros);
    printf("Quantidade de latas de tinta: %d\n", latas);
    printf("Valor a pagar: %d", custo);

    return 0;

}
