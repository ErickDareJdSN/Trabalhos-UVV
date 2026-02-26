def calcular_numeros(n1: float, n2: float, operacao: int) -> float | str:
    """
    Realiza uma operação matemática entre dois números com base na operação escolhida.

    Args:
        n1: Primeiro número (entre -1.000.000 e 1.000.000).
        n2: Segundo número (entre -1.000.000 e 1.000.000).
        operacao: Número da operação (1 a 6).

    Returns:
        O resultado da operação ou uma mensagem de erro (str) se inválido.
    """
    if n1 > 1000000 or n2 > 1000000 or n1 < -1000000 or n2 < -1000000:
        return "Número inválido! Deve estar entre -1.000.000 e 1.000.000."
    
    if operacao == 1:
        return n1 + n2
    elif operacao == 2:
        return n1 - n2
    elif operacao == 3:
        return n1 * n2
    elif operacao == 4:
        if n2 == 0:
            return "Divisão por zero não permitida!"
        return n1 / n2
    elif operacao == 5:
        if n2 == 0:
            return "Divisão por zero não permitida!"
        return n1 % n2
    elif operacao == 6:
        if n2 == 0:
            return "Divisão por zero não permitida!"
        return n1 // n2
    else:
        return "Operação inválida!"

def valida_numero(mensagem: str) -> float:
    """
    Solicita e valida um número entre -1.000.000 e 1.000.000.

    Args:
        mensagem: Mensagem a ser exibida para o usuário.

    Returns:
        Um número float válido.
    """
    while True:
        try:
            numero = float(input(mensagem))
            if -1000000 < numero < 1000000:
                return numero
            print("Número inválido! Deve estar entre -1.000.000 e 1.000.000.")
        except ValueError:
            print("Entrada inválida! Digite um número válido (ex.: 123.45).")

def valida_operacao() -> int:
    """
    Solicita e valida a operação escolhida (1 a 6).

    Returns:
        Um número inteiro representando a operação válida.
    """
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Módulo")
    print("6 - Divisão inteira")
    
    while True:
        try:
            operacao = int(input("Digite o número da operação desejada: "))
            if 1 <= operacao <= 6:
                return operacao
            print("Operação inválida! Escolha um número entre 1 e 6.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

def continuar_programa() -> bool:
    """
    Pergunta ao usuário se deseja continuar o programa.

    Returns:
        True se o usuário deseja continuar, False caso contrário.
    """
    print("Deseja realizar outra operação? (S/N)")
    resposta = input().strip().upper()
    return resposta == 'S'

def main():
    """
    Função principal que executa a calculadora em um loop.
    Solicita dois números, a operação desejada, calcula o resultado e pergunta se o usuário deseja continuar.
    """
    while True:
        n1 = valida_numero("Digite o primeiro número (entre -1.000.000 e 1.000.000): ")
        n2 = valida_numero("Digite o segundo número (entre -1.000.000 e 1.000.000): ")
        operacao = valida_operacao()
        resultado = calcular_numeros(n1, n2, operacao)
        print("Resultado:", resultado)
        
        if not continuar_programa():
            print("Programa encerrado.")
            break

if __name__ == "__main__":
    main()