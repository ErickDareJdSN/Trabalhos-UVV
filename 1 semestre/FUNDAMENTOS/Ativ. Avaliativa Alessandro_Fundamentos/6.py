import math

def calculo(r):
    volume = (4/3) * math.pi * (r ** 3)
    return volume

def ler_valor(mensagem):
    while True:
        entrada = input(mensagem)

        if entrada.strip() == "":
            print("Valor não pode ser vazio. Tente novamente.")
            continue

        try:
            valor = float(entrada)

            if valor == 0:
                return 0

            return valor

        except ValueError:
            print("Erro: Insira um valor numérico válido.")

def main():
    print("=== CALCULADORA DE VOLUME DE ESFERA ===")
    print()
    
    while True:
        r = ler_valor("Digite o raio da esfera em metros (ou 0 para sair): ")
        if r == 0:
            print("Encerrando o programa.")
            break

        if r < 0.1 or r > 100:
            print("Erro: raio deve estar entre 0.1m e 100m.")
            continue
        
        volume = calculo(r)
        print(f"O volume da esfera é: {volume:.2f} metros cúbicos")
        print()
        print("Deseja calcular o volume de outra esfera? (s/n)")
        resposta = input().strip().lower()
        while resposta not in ['s', 'n']:
            print("Resposta inválida. Digite 's' para sim ou 'n' para não.")
            resposta = input().strip().lower()
        if resposta == 'n':
            print("Encerrando o programa.")
            break

main()