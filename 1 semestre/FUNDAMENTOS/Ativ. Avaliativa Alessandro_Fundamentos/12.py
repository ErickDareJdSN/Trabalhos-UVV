def calcular_autonomia(lado, h):
    volume = lado**2 * h
    litros = volume * 1000
    autonomia = litros * 10

    return autonomia

def ler_valor(mensagem):
    while True:
        entrada = input(mensagem).strip().lower()

        if entrada == "sair":
            return None
        
        if entrada == "":
            print("Erro: Entrada Vazia. Tente novamente.")
            continue

        try:
            valor = float(entrada)
            if valor <= 0:
                print("Erro: O valor deve ser maior que zero.")
                continue

            return valor
        except ValueError:
            print("Erro: Insira um valor numérico válido ou 'sair' para encerrar.")

def main():
    print("=== CALCULADORA DE AUTONOMIA DE UM CARRO ===")
    print()

    while True:
        lado = ler_valor("Digite o lado do tanque de combustível em metros (ou 'sair' para encerrar): ")

        if lado is None:
            print("Encerrando o programa.")
            break

        print()

        h = ler_valor("Agora, digite a altura de preenchimento do tanque de combustível em metros (ou 'sair' para encerrar): ")

        if h is None:
            print("Encerrando o programa.")
            break

        if h > lado:
            print("Erro: altura deve ser maior que zero e menor ou igual ao valor do lado.")
            continue

        print()

        autonomia = calcular_autonomia(lado, h)
        print(f"A autonomia máxima do carro é: {autonomia:.2f} km")
        print()
        resposta = input("Deseja calcular a autonomia de outro tanque? (s/n): ").strip().lower()
        while resposta not in ['s', 'n']:
            resposta = input("Resposta inválida. Digite 's' para sim ou 'n' para não: ").strip().lower()
        if resposta == 'n':
            print("Encerrando o programa.")
            break

        print()

main()
