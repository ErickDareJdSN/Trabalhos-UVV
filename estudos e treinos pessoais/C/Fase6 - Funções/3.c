#include <stdio.h>
#include <string.h>

void limparEnter(char nome[])
{
    nome[strcspn(nome, "\n")] = '\0';
}

int nomeLen(char nome[])
{
    return strlen(nome);
}

int nomeVazio(char nome[])
{
    return strlen(nome) == 0;
}

void mostrarNome(char nome[101])
{
    printf("\n\nNome digitado: %s", nome);
}

int main()
{
    char nome[101];
    int tamanho;

    printf("\nDigite seu nome completo: ");
    fgets(nome, 101, stdin);

    limparEnter(nome);

    if (nomeVazio(nome == 1))
    {
        printf("\n\nNenhum nome foi digitado.");
    }

    else
    {
        tamanho = nomeLen(nome);

        mostrarNome(nome);
        printf("\nQuantidade de caracteres: %d", tamanho);
    }

    return 0;
}