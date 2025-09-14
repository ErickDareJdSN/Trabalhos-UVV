def calcular_tempo(segundos):
    if segundos <=0:
        raise ValueError("O tempo deve ser um número positivo.")
    if segundos > 31536000: # Limite realista de 1 ano
        raise ValueError("O valor é muito grande, insira um valor realista.")
    
    # Cálculo de horas, minutos e segundos
    horas = segundos // 3600
    minutos = segundos % 3600 // 60
    segundos_restantes = segundos % 60

    return horas, minutos, segundos_restantes

def main():
    print("=== Calculadora de Tempo ===")

    try:
        segundos = int(input("Digite o tempo em segundos: "))
        horas, minutos, segundos_restantes = calcular_tempo(segundos)
        print(f"\nTempo convertido:")
        print(f"{horas} horas, {minutos} minutos e {segundos_restantes} segundos.")

    except ValueError as e:
        if str(e).startswith("O tempo") or str(e).startswith("O valor"):
            print(f"Erro: {e}")
        else:
            print("Erro: Insira um valor numérico válido.")

if __name__ == "__main__":
    main()