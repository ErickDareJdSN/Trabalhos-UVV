def calcular_imc(peso, altura):
    if peso <= 0 or altura <= 0:
        raise ValueError("Peso e altura devem ser maiores que zero.")
    if peso > 500 or altura > 3:  # Limites realistas
        raise ValueError("Valores fora do intervalo realista.")
    
    imc = peso / (altura ** 2)
    
    # Classificação do IMC
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc < 25:
        classificacao = "Peso normal"
    elif 25 <= imc < 30:
        classificacao = "Sobrepeso"
    elif 30 <= imc < 35:
        classificacao = "Obesidade grau I"
    elif 35 <= imc < 40:
        classificacao = "Obesidade grau II"
    else:
        classificacao = "Obesidade grau III"
    
    return imc, classificacao

def main():
    print("=== Calculadora de IMC ===")
    
    try:
        peso = float(input("Digite seu peso em quilogramas (Kg): "))
        altura = float(input("Digite sua altura em metros (m): "))
        
        imc, classificacao = calcular_imc(peso, altura)
        print(f"\nSeu IMC é: {imc:.1f}")
        print(f"Classificação: {classificacao}")
        
    except ValueError as e:
        if str(e).startswith("Peso") or str(e).startswith("Valores"):
            print(f"Erro: {e}")
        else:
            print("Erro: Insira valores numéricos válidos.")

if __name__ == "__main__":
    main()