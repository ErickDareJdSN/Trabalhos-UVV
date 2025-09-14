def calcular_celcius(graus_c):
    if graus_c < -273.15:  # Zero absoluto em Celsius
        raise ValueError("A temperatura não pode ser menor que o zero absoluto (-273.15°C).")
    if graus_c > 10000:
        raise ValueError("A temperatura é muito alta, escolha um valor menor ou igual a 10.000°C.")
    
    celcius_fahrenheit = (graus_c * 9/5) + 32
    return celcius_fahrenheit

def calcular_fahrenheit(graus_f):
    if graus_f < -459.67:  # Zero absoluto em Fahrenheit
        raise ValueError("A temperatura não pode ser menor que o zero absoluto (-459.67°F).")
    if graus_f > 10000:
        raise ValueError("A temperatura é muito alta, escolha um valor menor ou igual a 10.000°F.")
    
    fahrenheit_celcius = (graus_f - 32) * 5/9
    return fahrenheit_celcius

def main():
    print("=== Conversor de temperaturas ===\n")

    while True:
        try:
            unidade = int(input("Digite 1 para converter C para F, 2 para F para C, ou 0 para sair: "))
            if unidade == 0:
                print("Programa encerrado.")
                break
            if unidade not in (1, 2):
                print("Erro: Opção inválida. Digite 1, 2 ou 0.")
                continue

            temperatura = float(input("Digite a temperatura a ser convertida (ou 0 para sair): "))
            if temperatura == 0:
                print("Programa encerrado.")
                break

            if unidade == 1:
                resultado = calcular_celcius(temperatura)
                print(f"A temperatura {temperatura:.1f}°C equivale a {resultado:.1f}°F.")
            elif unidade == 2:
                resultado = calcular_fahrenheit(temperatura)
                print(f"A temperatura {temperatura:.1f}°F equivale a {resultado:.1f}°C.")
                break

        except ValueError as e:
            if str(e).startswith("A temperatura") or str(e).startswith("Opção"):
                print(f"Erro: {e}")
            else:
                print("Erro: Entrada inválida. Digite um número válido para a temperatura ou opção.")

if __name__ == "__main__":
    main()