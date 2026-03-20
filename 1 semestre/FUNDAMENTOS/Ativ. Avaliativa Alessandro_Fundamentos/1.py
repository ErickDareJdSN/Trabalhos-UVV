import math

def calculo_hipotenisa(n1, n2):
    hipotenusa = math.sqrt(n1**2 + n2**2)
    return hipotenusa

def ler_valor(mensagem):
    while True:
        entrada = input(mensagem).strip().lower()

        if entrada == "sair":
            print("Encerrando o programa.")
            break

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

def classificar_triangulo(n1, n2, hipotenusa):
    if n1 == n2:
        return "Isósceles."
    elif n1 != n2:
        return "Escaleno."
    else:
        return "Equilátero."

def main():
    print("=== CALCULADORA DE HIPOTENUSA ===")
    print()
    while True:

        n1 = ler_valor("Digite o valor do primeiro cateto (ou 'sair' para encerrar): ")
        if n1 is None:
            print("Encerrando o programa.")
            break

        print()

        n2 = ler_valor("Digite o valor do segundo cateto (ou 'sair' para encerrar): ")
        if n2 is None:
            print("Encerrando o programa.")
            break

        print()

        hipotenusa = calculo_hipotenisa(n1, n2)
        print("-" * 40)
        print(f"Valor dos catetos: {n1:.2f} e {n2:.2f}")
        print(f"A hipotenusa é: {hipotenusa:.2f}")
        print(f"O triângulo formado é: {classificar_triangulo(n1, n2, hipotenusa)}")
        print("-" * 40)
        print()
        resposta = input("Deseja calcular novamente? (s/n): ").strip().lower()
        while resposta not in ['s', 'n']:
            resposta = input("Resposta inválida. Deseja calcular novamente? (s/n): ").strip().lower()
        if resposta == 'n':
            print("Encerrando o programa.")
            break

        print()

main()