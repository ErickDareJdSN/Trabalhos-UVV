#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Remove o '\n' que o fgets costuma guardar no final da string.
void limparEnter(char nick[])
{
    nick[strcspn(nick, "\n")] = '\0';
}

// Retorna o tamanho do nick.
int tamanhoNick(char nick[])
{
    return strlen(nick);
}

// Verifica se o nick está vazio.
// Retorna 1 se estiver vazio, 0 se não estiver.
int nickVazio(char nick[])
{
    return strlen(nick) == 0;
}

// Verifica se o tamanho está fora do intervalo permitido.
// Retorna 1 se for inválido, 0 se for válido.
int tamanhoInvalido(char nick[])
{
    int tamanho = tamanhoNick(nick);

    return tamanho < 3 || tamanho > 15;
}

// Verifica se o primeiro caractere é espaço.
// Retorna 1 se começar com espaço, 0 se não começar.
int comecaComEspaco(char nick[])
{
    return nick[0] == ' ';
}

// Verifica se o último caractere é espaço.
int terminaComEspaco(char nick[])
{
    int tamanho = tamanhoNick(nick);

    if (tamanho == 0)
    {
        return 0;
    }

    return nick[tamanho - 1] == ' ';
}

// Junta todas as regras de validação.
// O nick só é válido se nenhuma das funções de erro retornar 1.
int apelidoValido(char nick[])
{
    return !nickVazio(nick) &&
           !tamanhoInvalido(nick) &&
           !comecaComEspaco(nick) &&
           !terminaComEspaco(nick);
}

// Mostra todos os motivos de erro encontrados.
// Assim evitamos criar um código para cada combinação possível de erros.
void mensagemErro(char nick[])
{
    if (nickVazio(nick))
    {
        printf("\nMotivo: o usuario nao pode estar vazio.");
    }

    if (tamanhoInvalido(nick))
    {
        printf("\nMotivo: o usuario deve ter entre 3 e 15 caracteres.");
    }

    if (comecaComEspaco(nick))
    {
        printf("\nMotivo: o usuario nao pode comecar com espaco.");
    }

    if (terminaComEspaco(nick))
    {
        printf("\nMotivo: o usuario nao pode terminar com espaco.");
    }

    printf("\n");
}

// Mostra se o nick foi aprovado ou recusado.
// Ela chama apelidoValido() para decidir o resultado.
void mostrarResultado(char nick[])
{
    if (apelidoValido(nick))
    {
        printf("\nUsuario valido. Ola, %s!\n", nick);
    }
    else
    {
        printf("\nUsuario invalido.");
        mensagemErro(nick);
    }
}

int main()
{
    char nick[51];
    char loop = 'y';

    while (loop == 'y')
    {
        printf("Digite seu apelido de jogador: ");
        fgets(nick, 51, stdin);

        limparEnter(nick);

        mostrarResultado(nick);

        printf("\nDeseja reiniciar o programa? (Y/N): ");
        scanf(" %c", &loop);

        loop = tolower((unsigned char)loop);

        // Valida a resposta do usuário.
        while (loop != 'y' && loop != 'n')
        {
            printf("Opcao invalida, digite Y ou N: ");
            scanf(" %c", &loop);

            loop = tolower((unsigned char)loop);
        }

        // Limpa o ENTER que sobrou do scanf antes do próximo fgets.
        getchar();

        printf("\n");
    }

    printf("Programa encerrado.\n");

    return 0;
}