import math

def calcular_autonomia(r, h):
    volume_m3 = math.pi * (r ** 2) * h
    litros = volume_m3 * 1000
    tempo_horas = litros / 1350

    return volume_m3, litros, tempo_horas


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

            if valor <= 0 or valor > 100:
                print("Valor deve estar entre 0 e 100.")
                continue

            return valor
        
        except ValueError:
            print("Erro: insira um número válido ou digite 'sair'.")


def main():
    print("=== CALCULADORA DE AUTONOMIA DE CAIXA D'ÁGUA ===")
    print()

    while True:
        r = ler_valor("Digite o raio da caixa d'água em metros (ou 'sair' para encerrar): ")
        if r is None:
            print("Encerrando o programa.")
            break

        h = ler_valor("Agora, digite a altura da caixa d'água em metros (ou 'sair' para encerrar): ")
        if h is None:
            print("Encerrando o programa.")
            break
        print()

        volume, litros, tempo = calcular_autonomia(r, h)

        print("===RESULTADOS===")
        print()

        print(f"Volume da caixa d'água: {volume:.2f} m³")
        print(f"Capacidade da caixa d'água: {litros:.2f} litros")
        print(f"Autonomia da caixa d'água: {tempo:.2f} horas")
        print()

        resposta = input("Deseja calcular para outro tanque? (s/n): ").strip().lower()
        while resposta not in ["s", "n"]:
            resposta = input("Resposta inválida. Digite 's' para sim ou 'n' para não: ").strip().lower()

        if resposta == "n":
            print("Encerrando o programa.")
            break

        print()


main()