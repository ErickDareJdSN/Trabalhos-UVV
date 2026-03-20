def calcular_area_quadrado(lado):
    return lado ** 2

def ler_valor(mensagem):
    while True:
        entrada = input(mensagem).strip().lower()

        if entrada == "sair":
            return None

        if entrada == "":
            print("Erro: Entrada vazia, tente novamente.")
            continue

        try:
            valor = float(entrada)
            
            if valor <= 0:
                print("Erro: Por favor, insira um número positivo.")
                continue

            return valor
        
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira um número ou 'sair' para encerrar.")
            print

def main():
    print("=== CALCULADORA DE ÁREA DO QUADRADO ===")
    print()
    while True:
        lado = ler_valor("Digite o valor do lado do quadrado (ou 'sair' para encerrar): ")
        if lado is None:
            print("Encerrando o programa.")
            break
        print()
        print("-" * 40)
        area = calcular_area_quadrado(lado)
        print(f"A área do quadrado com lado {lado:.2f} é: {area:.2f}")
        print("-" * 40)
        print()
        resposta = input("Deseja calcular a área de outro quadrado? (s/n): ").strip().lower()
        while resposta not in ['s', 'n']:
            resposta = input("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não: ").strip().lower()
        if resposta == 'n':
            print("Encerrando o programa.")
            break

        print()

main()