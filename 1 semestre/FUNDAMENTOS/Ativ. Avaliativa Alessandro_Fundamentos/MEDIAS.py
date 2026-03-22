def medias(a, b, c):   
    if a == b or a == c or b == c:
        raise ValueError("Os valores devem ser distintos.")
    
    valores = [a, b, c]
    valores.sort()
    maiores = valores[1:]
    media = sum(maiores) / 2

    return media


def ler_valor(mensagem):
    while True:
        entrada = input(mensagem).strip().lower()
        
        if entrada == "sair":
            return None

        if entrada == "":
            print("Entrada vazia. Por favor, insira um valor válido.")
            continue

        try:
            valor = float(entrada)
            return valor
        except ValueError:
            print()
            print("Entrada inválida. Insira um número real válido ou 'sair' para encerrar.")
            print()


def main():
    print("=== CALCULADORA DE MÉDIAS ===")
    print()

    while True:
        a = ler_valor("Digite o primeiro número (ou 'sair' para encerrar): ")
        if a is None:
            print("Encerrando o programa.")
            break
        
        print()

        b = ler_valor("Digite o segundo número (ou 'sair' para encerrar): ")
        if b is None:
            print("Encerrando o programa.")
            break

        print()

        c = ler_valor("Digite o terceiro número (ou 'sair' para encerrar): ")
        if c is None:
            print("Encerrando o programa.")
            break

        print()

        try:
            media = medias(a, b, c)
            print("-" * 40)
            print(f"A média dos dois maiores números é: {media:.2f}")
            print("-" * 40)
        except ValueError as e:
            print(f"Erro: {e}")
            print()
            continue

        print()
        resposta = input("Deseja calcular novamente? (s/n): ").strip().lower()
        while resposta not in ['s', 'n']:
            resposta = input("Resposta inválida. Deseja calcular novamente? (s/n): ").strip().lower()
        
        if resposta == 'n':
            print("Encerrando o programa.")
            break

        print()


if __name__ == "__main__":
    main()