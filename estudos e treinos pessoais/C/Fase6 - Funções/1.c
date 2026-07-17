#include <stdio.h>

int somar(int a, int b)
{
    return a + b;
}

int subtrair(int a, int b)
{
    return a - b;
}

int multiplicar(int a, int b)
{
    return a * b;
}

float dividir(int a, int b)
{
    return (float)a / b;
}

int main()
{
    int a;
    int b;
    int a_mais_b;
    int a_menos_b;
    int a_x_b;
    int a_div_b;

    printf("Digite o primeiro número: ");
    scanf("%d", &a);

    printf("\n\nAgora digite o segundo número: ");
    scanf("%d", &b);

    a_mais_b = somar(a, b);
    a_menos_b = subtrair(a, b);
    a_x_b = multiplicar(a, b);

    if (b != 0)
    {
        a_div_b = dividir(a, b);
    }

    printf("\n\n=== RESULTADOS ===\n");
    printf("\n%d + %d: %d", a, b, a_mais_b);
    printf("\n%d - %d: %d", a, b, a_menos_b);
    printf("\n%d x %d: %d", a, b, a_x_b);

    if (b != 0)
    {
        printf("\n%d / %d: %.2f", a, b, a_div_b);
    }

    else
    {
        printf("\n%d / %d: Impossível dividir por 0", a, b);
    }

    return 0;
}
