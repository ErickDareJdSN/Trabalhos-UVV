#include <stdio.h>
#include <string.h>
#include <ctype.h>

void limparEnter(char nick[])
{
    nick[strcspn(nick, "\n")] = '\0';
}

int tamanhoNick(char nick[])
{
    return strlen(nick);
}

int nickVazio(char nick[], int vazio)
{
    if (strlen(nick) == 0)
    {
        vazio = 1;
    }

    else
    {
        vazio = 0;
    }
}

int tamanhoInvalido(char nick[], int invalido)
{
    if (strlen(nick) < 3 || strlen(nick) > 15)
    {
        invalido = 1;
    }

    else
    {
        invalido = 0;
    }
}

int comecaComEspaco(char nick[], int espacoComeco)
{
    if (nick[0] == ' ')
    {
        espacoComeco = 1;
    }

    else
    {
        espacoComeco = 0;
    }
}

int terminaComEspaco(char nick[], int espacoFinal, int tamanho)
{
    tamanho = strlen(nick);

    if (nick[tamanho - 1] == ' ')
    {
        espacoFinal = 1;
    }

    else
    {
        espacoFinal = 0;
    }
}

int apelidoValido(int vazio, int invalido, int espacoComeco, int espacoFinal, int valido)
{
    if (vazio == 0 && invalido == 0 && espacoComeco == 0 && espacoFinal == 0)
    {
        valido = 1;
    }
    else
    {
        valido = 0;
    }
}

int tipoErro(int vazio, int invalido, int espacoComeco, int espacoFinal, int erro)
{
    if (vazio == 0 && invalido == 0 && espacoComeco == 0 && espacoFinal == 1)
    {
        erro = 1;
    }

    else if (vazio == 0 && invalido == 0 && espacoComeco == 1 && espacoFinal == 0)
    {
        erro = 2;
    }

    else if (vazio == 0 && invalido == 1 && espacoComeco == 0 && espacoFinal == 0)
    {
        erro = 3;
    }

    else if (vazio == 0 && invalido == 0 && espacoComeco == 1 && espacoFinal == 1)
    {
        erro = 4;
    }

    else if (vazio == 0 && invalido == 1 && espacoComeco == 0 && espacoFinal == 1)
    {
        erro = 5;
    }

    else if (vazio == 0 && invalido == 1 && espacoComeco == 1 && espacoFinal == 1)
    {
        erro = 6;
    }

    else if (vazio == 1)
    {
        erro = 7;
    }
}

void mensagemErro(int erro)
{
    if (erro == 1)
    {
        printf("\n\nMotivo: O usuário possui espaço no final.\n\n");
    }

    else if (erro == 2)
    {
        printf("\n\nMotivo: O usuário possui espaço no começo.\n\n");
    }

    else if (erro == 3)
    {
        printf("\n\nMotivo: O usuário deve ter entre 3 e 15 caracteres.\n\n");
    }

    else if (erro == 4)
    {
        printf("\n\nMotivo: O usuário possui espaço no começo e no final.\n\n");
    }

    else if (erro == 5)
    {
        printf("\n\nMotivo: O usuário deve ter entre 3 e 15 caracteres e não deve ter espaço no final.\n\n");
    }

    else if (erro == 6)
    {
        printf("\n\nMotivo:. O usuário deve ter entre 3 e 15 caracteres e não deve ter espaço nem no começo e nem no final\n\n");
    }

    else
    {
        printf("\n\nMotivo: O usuário não pode estar vazio.\n\n");
    }
}

void mostrarResultado(int valido, char nick[])
{
    if (valido == 1)
    {
        printf("\n\nUsuário válido. Olá %s\n\n!", nick);
    }

    else
    {
        printf("\n\nUsuário inválido.");
    }
}

int main()
{
    char nick[51];
    char loop = 'y';

    int vazio = 0;
    int invalido;
    int espacoComeco;
    int espacoFinal;
    int erro;
    int tamanho;
    int valido;

    while (loop == 'y')
    {
        printf("Vazio: %d", vazio);

        printf("Digite seu apelido de jogador: ");
        fgets(nick, 51, stdin);

        limparEnter(nick);

        apelidoValido(vazio, invalido, espacoComeco, espacoFinal, erro);

        mostrarResultado(valido, nick);

        mensagemErro(erro);

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