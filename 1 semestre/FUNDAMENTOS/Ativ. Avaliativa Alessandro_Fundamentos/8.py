import math

def calculo(r,h):
    area_total = 2*math.pi*r*(r+h)

    litros_tinta = area_total/3
    total_latas = litros_tinta/5
    preco_latas = total_latas*50

    return total_latas, preco_latas

def ler_valor(mensagem):
    while True:
        entrada= input(mensagem)

        if entrada.strip()=="":
            print("Erro: Entrada vazia")

        try:
            valor= float(entrada)
            
            if valor ==0:
                return 0
            
            return valor
        
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira um número válido.")

def main():
    print("===CALCULADORA DE LATAS DE TINTA===")
    print()

    while True:
        r = ler_valor("Digite o raio do cilindro (ou 0 para sair): ")
        if r == 0:
            print("Encerrando o programa.")
            break
        if r<1 or r>10000:
            print("Erro: O raio deve ser entre 1 e 10000.")
            continue
        print

        h = ler_valor("Agora, digite a altura do cilindro (ou 0 para sair): ")
        if h == 0:
            print("Encerrando o programa.")
            break
        if h<1 or h>10000:
            print("Erro: A altura deve ser entre 1 e 10000.")
            continue
        print()

        total_latas, preco_latas = calculo(r,h)
        print(f"Total de latas de tinta necessárias: {total_latas:.2f}")
        print(f"Preço total das latas: R$ {preco_latas:.2f}")
        print()
        print("Deseja calcular para outro cilindro? (s/n)")
        resposta = input().strip().lower()
        while resposta not in ['s', 'n']:
            print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")
            resposta = input().strip().lower()
        if resposta == 'n':
            print("Encerrando o programa.")
            break
        print()

main()