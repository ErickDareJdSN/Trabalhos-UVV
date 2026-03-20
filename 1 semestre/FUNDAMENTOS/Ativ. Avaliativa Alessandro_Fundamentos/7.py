def salario(ganho_hora, horas_mes):
    bruto = ganho_hora * horas_mes
    imposto = bruto * 0.11
    inss = bruto * 0.08
    sindicato = bruto * 0.05
    liquido = bruto - imposto - inss - sindicato

    return bruto, imposto, inss, sindicato, liquido

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
    print("=== CALCULADORA DE SALÁRIO ===")
    print()
    
    while True:
        ganho_hora = ler_valor("Digite o valor ganho por hora (ou 0 para sair): ")
        if ganho_hora == 0:
            print("Encerrando o programa.")
            break

        if ganho_hora < 1 or ganho_hora > 1000000:
            print("Erro: valor por hora deve estar entre R$1 e R$1000000.")
            continue

        horas_mes = ler_valor("Agora, digite a quantidade de horas trabalhadas no mês (ou 0 para sair): ")
        if horas_mes == 0:
            print("Encerrando o programa.")
            break
        print()

        if horas_mes < 1 or horas_mes > 744:
            print("Erro: horas trabalhadas no mês devem estar entre 1 e 744.")
            continue
        
        bruto, imposto, inss, sindicato, liquido = salario(ganho_hora, horas_mes)
        print(f"Salário Bruto: R${bruto:.2f}")
        print(f"Imposto (11%): R${imposto:.2f}")
        print(f"INSS (8%): R${inss:.2f}")
        print(f"Sindicato (5%): R${sindicato:.2f}")
        print(f"Salário Líquido: R${liquido:.2f}")
        print()
        print("Deseja calcular o salário de outro funcionário? (s/n)")
        resposta = input().strip().lower()
        while resposta not in ['s', 'n']:
            print("Resposta inválida. Digite 's' para sim ou 'n' para não.")
            resposta = input().strip().lower()
        if resposta == 'n':
            print("Encerrando o programa.")
            break
main()