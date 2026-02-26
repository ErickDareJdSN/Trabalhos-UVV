import math

def calcular_volume(raio):
    if raio <= 0:
        raise ValueError("O raio deve ser maior que zero.")
    if raio > 1000:  # Limite realista para o raio
        raise ValueError("O raio é muito grande, insira um valor realista (até 1000 metros).")
    
    # Volume em metros cúbicos: V = (4/3) * π * r³
    volume_m3 = (4/3) * math.pi * raio ** 3
    # Converter para litros: 1 m³ = 1000 litros
    volume_litros = volume_m3 * 1000
    
    return volume_litros

def main():
    print("=== Calculadora de Volume de Esfera ===")
    
    try:
        raio = float(input("Digite o raio da esfera em metros: "))
        volume = calcular_volume(raio)
        print(f"\nO volume da esfera é: {volume:.2f} litros")
        
    except ValueError as e:
        if str(e).startswith("O raio"):
            print(f"Erro: {e}")
        else:
            print("Erro: Insira um valor numérico válido.")

if __name__ == "__main__":
    main()