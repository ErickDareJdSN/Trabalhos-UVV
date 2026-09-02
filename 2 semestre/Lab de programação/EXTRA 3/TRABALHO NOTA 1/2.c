#include <stdio.h>

int main(void) {
    int qtd = 0;
    int soma = 0;

    printf("=== MULTIPLOS DE 11 ===\n\n");
    printf("Intervalo: [300, 400]\n\n");
    printf("Multiplos em ordem decrescente:\n");

    for (int i = 396; i >= 300; i -= 11) {
        printf("%d ", i);
        soma += i;
        qtd++;
    }

    printf("\n\nQuantidade de multiplos: %d\n", qtd);
    printf("Soma dos multiplos: %d\n", soma);

    return 0;
}
