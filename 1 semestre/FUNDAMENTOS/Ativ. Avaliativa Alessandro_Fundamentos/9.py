import math

def calculo(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distancia


def ler_valor(mensagem):
    while True:
        entrada = input(mensagem).strip().lower()

        if entrada == "sair":
            return None

        if entrada == "":
            print("Valor não pode ser vazio. Tente novamente.")
            continue

        try:
            valor = float(entrada)

            if valor < -100 or valor > 100:
                print("Valor deve estar entre -100 e 100.")
                continue

            return valor

        except ValueError:
            print("Erro: insira um número válido ou digite 'sair'.")


def main():
    print("=== CALCULADORA DE DISTÂNCIA ENTRE DOIS PONTOS ===")
    print()

    while True:
        x1 = ler_valor("Digite a coordenada x do primeiro ponto (ou 'sair' para encerrar): ")
        if x1 is None:
            print("Encerrando o programa.")
            break

        y1 = ler_valor("Agora, digite a coordenada y do primeiro ponto (ou 'sair' para encerrar): ")
        if y1 is None:
            print("Encerrando o programa.")
            break

        print()
        print("=== PRIMEIRO PONTO REGISTRADO ===")
        print(f"({x1:.2f}, {y1:.2f})")
        print()

        x2 = ler_valor("Digite a coordenada x do segundo ponto (ou 'sair' para encerrar): ")
        if x2 is None:
            print("Encerrando o programa.")
            break

        y2 = ler_valor("Agora, digite a coordenada y do segundo ponto (ou 'sair' para encerrar): ")
        if y2 is None:
            print("Encerrando o programa.")
            break

        print()
        print("=== COORDENADAS ESCOLHIDAS ===")
        print(f"({x1:.2f}, {y1:.2f}) e ({x2:.2f}, {y2:.2f})")

        distancia = calculo(x1, y1, x2, y2)
        print(f"A distância entre os pontos é: {distancia:.2f}")
        print()

        resposta = input("Deseja calcular a distância entre outros pontos? (s/n): ").strip().lower()

        while resposta not in ["s", "n"]:
            resposta = input("Resposta inválida. Digite 's' para sim ou 'n' para não: ").strip().lower()

        if resposta == "n":
            print("Encerrando o programa.")
            break

        print()


main()