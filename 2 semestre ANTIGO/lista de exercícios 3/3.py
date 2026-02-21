def calcular_primos(numero: int) -> bool:
    """
    Verifica se um número é primo.

    Args:
        numero: Um número inteiro positivo maior que 2.

    Returns:
        True se o número é primo, False caso contrário.
    """
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def valida_numero() -> int:
    """
    Solicita e valida um número inteiro positivo maior que 2.

    Returns:
        Um número inteiro maior que 2.
    """
    while True:
        try:
            numero = int(input("Digite um número inteiro positivo maior que 2: "))
            if numero > 2:
                return numero
            print("Número inválido! Deve ser maior que 2.")
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
    Função principal que executa o programa em um loop de até 500 iterações.
    Solicita um número, verifica se é primo e pergunta se o usuário deseja continuar.
    """
    max_repeticoes = 500
    for i in range(max_repeticoes):
        numero = valida_numero()
        resultado = calcular_primos(numero)
        
        if resultado:
            print(f"{numero} é um número primo.")
        else:
            print(f"{numero} não é um número primo.")
        
        if i < max_repeticoes - 1:
            if not continuar_programa(max_repeticoes - i - 1):
                print(f"Programa encerrado após {i + 1} repetições.")
                break
        else:
            print(f"Limite de {max_repeticoes} repetições atingido. Programa encerrado.")

if __name__ == "__main__":
    main()