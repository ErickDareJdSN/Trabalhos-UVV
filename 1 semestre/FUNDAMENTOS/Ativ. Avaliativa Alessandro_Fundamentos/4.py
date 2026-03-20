import math

def calcular_circulo(raio):
    area = math.pi * raio ** 2
    comprimento = 2 * math.pi * raio
    return area, comprimento

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
            print()

def main():
    print("=== CALCULADORA DE ÁREA E COMPRIMENTO DO CÍRCULO ===")
    print()
    while True:
        raio = ler_valor("Digite o valor do raio do círculo (ou 'sair' para encerrar): ")
        if raio is None:
            print("Encerrando o programa.")
            break
        print()
        area, comprimento = calcular_circulo(raio)
        print("-" * 40)
        print(f"O círculo com raio {raio:.2f} tem área: {area:.2f} e comprimento: {comprimento:.2f}")
        print("-" * 40)
        print()
        resposta = input("Deseja calcular para outro círculo? (s/n): ").strip().lower()
        while resposta not in ['s', 'n']:
            resposta = input("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não: ").strip().lower()
        if resposta == 'n':
            print("Encerrando o programa.")
            break

        print()

main()