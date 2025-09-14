def calcular_salario(reais_hora, horas):
    """Calcula o salário bruto, descontos e salário líquido com base no valor por hora e horas trabalhadas."""
    if reais_hora <= 0 or horas <= 0:
        raise ValueError("O salário por hora e as horas trabalhadas devem ser maiores que zero.")
    if reais_hora > 1000 or horas > 744:  # Limites realistas: R$1000/h e 31 dias * 24h
        raise ValueError("Valores fora da realidade (salário/hora até R$1000, horas até 744/mês).")
    
    # Cálculo do salário bruto
    salario_bruto = reais_hora * horas
    
    # Taxas de desconto
    TAXA_IMPOSTO_RENDA = 0.11  # 11%
    TAXA_INSS = 0.08  # 8%
    TAXA_SINDICATO = 0.05  # 5%
    
    # Cálculo dos descontos
    imposto_renda = salario_bruto * TAXA_IMPOSTO_RENDA
    inss = salario_bruto * TAXA_INSS
    sindicato = salario_bruto * TAXA_SINDICATO
    impostos = imposto_renda + inss + sindicato
    salario_liquido = salario_bruto - impostos
    
    return salario_bruto, imposto_renda, inss, sindicato, salario_liquido

def main():
    print("=== Calculadora de Salário ===")
    
    try:
        reais_hora = float(input("Digite quantos reais você ganha por hora: "))
        horas = float(input("Digite quantas horas você trabalha por mês: "))
        
        salario_bruto, imposto_renda, inss, sindicato, salario_liquido = calcular_salario(reais_hora, horas)
        
        print("\nResumo do salário:")
        print(f"Salário bruto: R${salario_bruto:.2f}")
        print(f"Imposto de renda (11%): R${imposto_renda:.2f}")
        print(f"INSS (8%): R${inss:.2f}")
        print(f"Sindicato (5%): R${sindicato:.2f}")
        print(f"Salário líquido: R${salario_liquido:.2f}")
        
    except ValueError as e:
        if str(e).startswith("O salário") or str(e).startswith("Valores"):
            print(f"Erro: {e}")
        else:
            print("Erro: Insira valores numéricos válidos.")

if __name__ == "__main__":
    main()