#include <stdio.h>

int main(void)
{
    int i, qtd = 0, soma = 0;

    printf("=== IMPARES MULTIPLOS DE 3 E NAO MULTIPLOS DE 5 ===\n\n");
    printf("Intervalo: [9, 90]\n\n");

    for(i = 9; i <= 90; i++)
    {
        if(i % 2 != 0 && i % 3 == 0 && i % 5 != 0)
        {
            soma += i;
            qtd++;
        }
    }

    printf("Quantidade de multiplos: %d\n", qtd);
    printf("Soma dos multiplos: %d\n", soma);

    return 0;
}
