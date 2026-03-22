def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Magreza"
    elif 18.5 <= imc < 25:
        return "Saudável"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade Grau I"
    elif 35 <= imc < 40:
        return "Obesidade Grau II (Severa)"
    else:
        return "Obesidade Grau III (Mórbida)"
    
def ler_valor(mensagem):
    while True:
        entrada = input(mensagem).strip().lower()
        
        if entrada == "sair":
            print("Encerrando o programa.")
            break

        if entrada == "":
            print("Entrada vazia. Por favor, insira um valor válido.")
            continue

        try:
            valor = float(entrada)
            if valor <= 0:
                print("Valor deve ser maior que zero. Tente novamente.")
                print()
                continue
            
            return valor
        except ValueError:
            print()
            print("Entrada inválida. Por favor, insira um número válido ou 'sair' para encerrar.")
            print("Valores decimais devem usar ponto (ex: 1.75).")
            print()

def main():
    print("=== CALCULADORA DE IMC ===")
    print()

    while True:
        peso = ler_valor("Digite seu peso em kg (ou 'sair' para encerrar): ")
        if peso is None:
            print("Programa encerrado.")
            break
        
        print()

        altura = ler_valor("Digite sua altura em metros (ou 'sair' para encerrar): ")
        if altura is None:
            print("Programa encerrado.")
            break

        print()

        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        print("-" * 40)
        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
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