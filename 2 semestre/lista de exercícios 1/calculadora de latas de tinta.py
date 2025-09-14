import math

def calcular_area (raio, altura):
    if raio <=0 or altura <=0:
         raise ValueError("O raio e a altura devem ser maiores que zero.")
    if raio >1000 or altura >1000: #Limite realista para o raio e a altura
         raise ValueError("O raio ou a altura são muito grandes, insira um valor realista.")
    
    # Calculo da área lateral de um cilindro: A = 2 * π * r * h
    area_lateral = 2 * math.pi * raio * altura

    # Valores das latas de tinta.
    litro_lata = 5
    metro_litro = 3
    preco_lata = 50

    # Cálculo do custo e quantidade de tinta.
    quantidade_latas = (area_lateral /metro_litro) /litro_lata
    custo = preco_lata * quantidade_latas

    return area_lateral, litro_lata, metro_litro, preco_lata

def main():
    print("===Calculadora de latas de tinta===")

    try:
        raio = float(input("Digite o raio do cilindro que você quer pintar: "))
        altura = float(input("Agora, digite a altura do cilindro: "))

        quantidade_latas, custo = calcular_area(raio, altura)

        print("\nResumo dos valores:")
        print(f"Quantidade total de latas de tinta: {quantidade_latas:.2f}")
        print(f"Custo total: {custo:.2f}")

    except ValueError as e:
        if str(e).startswith("O raio"):
            print(f"Erro: {e}")
        else:
            print("Erro, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()
