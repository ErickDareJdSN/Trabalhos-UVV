def calcular_reajuste(preco: float, reajuste: float) -> float:
    """
    Calcula o novo preço de um produto após aplicar um percentual de reajuste.

    Args:
        preco: Preço original do produto (entre 0 e 1.000.000).
        reajuste: Percentual de reajuste (entre -100% e 100%).

    Returns:
        O novo preço após o reajuste.
    """
    novo_preco = preco + (preco * reajuste / 100)
    return novo_preco

def valida_preco() -> float:
    """
    Solicita e valida o preço do produto (entre 0 e 1.000.000).

    Returns:
        Um número float representando o preço válido.
    """
    while True:
        try:
            preco = float(input("Digite o preço do produto (entre 0 e 1.000.000): "))
            if 0 <= preco <= 1000000:
                return preco
            print("Preço inválido! Deve estar entre 0 e 1.000.000.")
        except ValueError:
            print("Entrada inválida! Digite um número válido (ex.: 123.45).")

def valida_reajuste() -> float:
    """
    Solicita e valida o percentual de reajuste (entre -100% e 100%).

    Returns:
        Um número float representando o percentual de reajuste válido.
    """
    while True:
        try:
            reajuste = float(input("Digite o percentual de reajuste (entre -100% e 100%): "))
            if -100 <= reajuste <= 100:
                return reajuste
            print("Reajuste inválido! Deve estar entre -100% e 100%.")
        except ValueError:
            print("Entrada inválida! Digite um número válido (ex.: 10 ou -10).")

def continuar_programa(repeticoes_restantes: int) -> bool:
    """
    Pergunta ao usuário se deseja continuar o programa.

    Args:
        repeticoes_restantes: Número de tentativas restantes.

    Returns:
        True se o usuário deseja continuar, False caso contrário.
    """
    resposta = input(f"Deseja calcular novamente? Restam {repeticoes_restantes} tentativas (S/N): ").strip().upper()
    return resposta == 'S'

def main():
    """
    Função principal que executa o programa em um loop de até 100 iterações.
    Solicita preço e percentual de reajuste, calcula o novo preço e pergunta se o usuário deseja continuar.
    """
    max_repeticoes = 100
    contador = 0
    while contador < max_repeticoes:
        preco = valida_preco()
        reajuste = valida_reajuste()
        novo_preco = calcular_reajuste(preco, reajuste)
        print(f"O novo preço do produto após o reajuste é: R${novo_preco:.2f}")
        
        contador += 1
        if contador < max_repeticoes:
            if not continuar_programa(max_repeticoes - contador):
                print(f"Programa encerrado após {contador} repetições.")
                break
        else:
            print(f"Limite de {max_repeticoes} repetições atingido. Programa encerrado.")

if __name__ == "__main__":
    main()