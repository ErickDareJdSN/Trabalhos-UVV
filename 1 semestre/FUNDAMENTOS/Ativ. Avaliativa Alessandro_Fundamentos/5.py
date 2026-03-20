def calculo(h,m):
    imc = m/(h**2)
    return imc

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

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    print("=== CALCULADORA DE IMC ===")
    print()
    
    while True:
        h = ler_valor("Digite a altura em metros (ou 0 para sair): ")
        if h == 0:
            print("Encerrando o programa.")
            break

        if h < 1 or h > 2.5:
            print("Erro: altura deve estar entre 1m e 2.5m.")
            continue

        m = ler_valor("Agora, digite o peso em kg (ou 0 para sair): ")
        if m == 0:
            print("Encerrando o programa.")
            break

        if m < 1 or m > 500:
            print("Erro: peso deve estar entre 1kg e 500kg.")
            continue
        
        imc = calculo(h, m)
        print(f"Seu IMC é: {imc:.2f}")
        print()

        classificacao = classificar_imc(imc)
        print(f"Classificação: {classificacao}")
        print()
        print("Deseja calcular novamente? (s/n)")
        resposta = input().strip().lower()
        while resposta not in ['s', 'n']:
            print("Resposta inválida. Digite 's' para sim ou 'n' para não.")
            resposta = input().strip().lower()
        if resposta == 'n':
            print("Encerrando o programa.")
            break

main()