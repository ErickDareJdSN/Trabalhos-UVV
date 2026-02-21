def calcula_anos(numero: int) -> int:
    """
    Verifica se um número representa um ano bissexto.

    Args:
        numero: Um número inteiro positivo maior que 400.

    Returns:
        0 se numero <= 400, 1 se é bissexto, 2 se não é bissexto.
    """
    if numero <= 400:
        return 0
    if (numero % 4 == 0 and numero % 100 != 0) or (numero % 400 == 0):
        return 1
    return 2

def valida_numero() -> int:
    """
    Solicita e valida um número inteiro positivo maior que 400.

    Returns:
        Um número inteiro maior que 400.
    """
    while True:
        try:
            numero = int(input("Digite um número inteiro positivo maior que 400: "))
            if numero > 400:
                return numero
            print("Número inválido! Deve ser maior que 400.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

def continuar_programa(repeticoes_restantes: int) -> bool:
    """
    Pergunta ao usuário se deseja continuar o programa.

    Args:
        repeticoes_restantes: Número de tentativas restantes.

    Returns:
        True se o usuário deseja continuar, False caso contrário.
    """
    resposta = input(f"Deseja continuar? Restam {repeticoes_restantes} tentativas (S/N): ").strip().upper()
    return resposta == 'S'

def main():
    """
    Função principal que executa o programa em um loop de até 100 iterações.
    Solicita um número, verifica se é bissexto e pergunta se o usuário deseja continuar.
    """
    max_repeticoes = 100
    for i in range(max_repeticoes):
        numero = valida_numero()
        resultado = calcula_anos(numero)
        
        if resultado == 1:
            print(f"{numero} é um ano bissexto.")
        elif resultado == 2:
            print(f"{numero} não é um ano bissexto.")
        else:
            print("Número inválido.")
        
        if i < max_repeticoes - 1:
            if not continuar_programa(max_repeticoes - i - 1):
                print(f"Programa encerrado após {i + 1} repetições.")
                break
        else:
            print(f"Limite de {max_repeticoes} repetições atingido. Programa encerrado.")

if __name__ == "__main__":
    main()