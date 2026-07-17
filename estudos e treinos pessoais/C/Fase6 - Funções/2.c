#include <stdio.h>
#include <ctype.h>

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

int divisor_ok(int b)
{
    return b != 0;
}

void menu()
{
    printf("\n===== CALCULADORA USANDO FUNÇÕES =====\n");
    printf("\n1 - Somar");
    printf("\n2 - Subtrair");
    printf("\n3 - Multiplicar");
    printf("\n4 - Dividir");
    printf("\n\nEscolha uma opcao: ");
}

int main()
{
    int a;
    int b;
    int opcao;
    char loop = 'y';

    while (loop == 'y')
    {

        menu();
        scanf("%d", &opcao);
        
        while (opcao < 1 || opcao > 4)
        {
            printf("\n\nOpção inválida, selecione novamente: ");
            scanf("%d", &opcao);
        }

        printf("\n\n// Entrada de números //\n");
        printf("\nDigite o primeiro número: ");
        scanf("%d", &a);
        printf("\nDigite o segundo número: ");
        scanf("%d", &b);

        printf("\n\n=== RESULTADOS ===\n");

        if (opcao == 1)
        {
            printf("\n%d + %d = %d", a, b, somar(a, b));
        }

        else if (opcao == 2)
        {
            printf("\n%d - %d = %d", a, b, subtrair(a, b));
        }

        else if (opcao == 3)
        {
            printf("\n%d x %d = %d", a, b, multiplicar(a, b));
        }

        else
        {
            if ((divisor_ok(b)))
            {
                printf("\n%d / %d: %.2f", a, b, dividir(a, b));
            }

            else
            {
                printf("\n%d / %d: Impossível dividir por zero.", a, b);
            }
        }

        printf("\nDeseja reiniciar o programa? (Y/N): ");
        scanf(" %c", &loop);

        loop = tolower((unsigned char)loop);

        while (loop != 'y' && loop != 'n')
        {
            printf("Opção inválida, digite Y ou N: ");
            scanf(" %c", &loop);

            loop = tolower((unsigned char)loop);
        }
        getchar();
    }
    printf("Programa encerrado.");
}