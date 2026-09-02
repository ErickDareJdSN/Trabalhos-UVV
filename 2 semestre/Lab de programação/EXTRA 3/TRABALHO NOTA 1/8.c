#include <stdio.h>
#include <ctype.h>

int main(void)
{
    char novamente;
    int opcao;
    int mix1, mix2, mix3, total;

    do {
        mix1 = 0;
        mix2 = 0;
        mix3 = 0;

        printf("\n=== VOTACAO DE MIX DE SABORES ===\n\n");
        printf("1 - Mix 1\n");
        printf("2 - Mix 2\n");
        printf("3 - Mix 3\n");
        printf("0 - Encerrar esta votacao e ver porcentagens\n\n");

        do {
            printf("Digite sua opcao: ");
            if (scanf("%d", &opcao) != 1) {
                printf("Digite um numero (1, 2, 3 ou 0).\n");
                while (getchar() != '\n') { }
                opcao = -1;
                continue;
            }

            if (opcao == 1) {
                mix1++;
            } else if (opcao == 2) {
                mix2++;
            } else if (opcao == 3) {
                mix3++;
            } else if (opcao != 0) {
                printf("Opcao invalida. Use 1, 2, 3 ou 0.\n");
            }
        } while (opcao != 0);

        total = mix1 + mix2 + mix3;

        printf("\n=== RESULTADO ===\n");
        if (total == 0) {
            printf("Nenhum voto registrado.\n");
        } else {
            printf("Total de clientes: %d\n\n", total);
            printf("Mix 1: %d voto(s) - %.2f%%\n", mix1, (mix1 * 100.0) / total);
            printf("Mix 2: %d voto(s) - %.2f%%\n", mix2, (mix2 * 100.0) / total);
            printf("Mix 3: %d voto(s) - %.2f%%\n", mix3, (mix3 * 100.0) / total);
        }

        while (getchar() != '\n') { }

        do {
            printf("\nDeseja iniciar outra votacao? (Y/N): ");
            if (scanf(" %c", &novamente) != 1) {
                novamente = ' ';
            }
            novamente = tolower((unsigned char)novamente);

            if (novamente != 'y' && novamente != 'n') {
                printf("Opcao invalida. Digite Y ou N.\n");
                while (getchar() != '\n') { }
            }
        } while (novamente != 'y' && novamente != 'n');

    } while (novamente == 'y');

    printf("Programa encerrado.\n");
    return 0;
}
