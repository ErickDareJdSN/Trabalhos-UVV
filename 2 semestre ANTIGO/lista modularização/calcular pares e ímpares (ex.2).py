def multiplica_intervalo(numero: int, opcao: str) -> int:
    """
    Calcula o produto dos números pares ou ímpares de 1 até numero.
    
    Args:
        numero: Um número inteiro positivo.
        opcao: 'P' para multiplicar pares, 'I' para multiplicar ímpares.
    
    Returns:
        O produto dos números no intervalo especificado ou 0 se numero <= 0.
    """
    if numero <= 0:
        return 0
    
    resultado = 1
    inicio = 2 if opcao.upper() == 'P' else 1
    incremento = 2
    for i in range(inicio, numero + 1, incremento):
        resultado *= i
    return resultado

def valida_numero() -> int:
    """
    Solicita e valida um número inteiro positivo do usuário.
    
    Returns:
        Um número inteiro positivo.
    """
    while True:
        try:
            numero = int(input("Digite um número inteiro positivo: "))
            if numero > 0:
                return numero
            print("Número inválido! Deve ser maior que 0.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

def valida_opcao() -> str:
    """
    Solicita e valida a opção (P para pares, I para ímpares).
    
    Returns:
        A opção 'P' ou 'I'.
    """
    while True:
        opcao = input("Digite a opção (P para pares, I para ímpares): ").upper()
        if opcao in ['P', 'I']:
            return opcao
        print("Opção inválida! Use P ou I.")

def main():
    """
    Função principal que executa o programa em um loop de até 100 iterações.
    Solicita número e opção, calcula o produto e exibe o resultado.
    """
    for _ in range(100):  # Limite de 100 iterações
        numero = valida_numero()
        opcao = valida_opcao()
        resultado = multiplica_intervalo(numero, opcao)
        tipo = "pares" if opcao == 'P' else "ímpares"
        print(f"Multiplicação dos {tipo} de 1 a {numero}: {resultado}")

if __name__ == "__main__":
    main()