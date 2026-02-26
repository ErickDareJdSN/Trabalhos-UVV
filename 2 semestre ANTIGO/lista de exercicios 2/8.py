def encontrar_impares_multiplos_7(quantidade):
    numeros = []
    k = 0
    while len(numeros) < quantidade:
        # Gera múltiplos de 7 ímpares: 7 * (2k + 1)
        num = 7 * (2 * k + 1)
        numeros.append(num)
        k += 1
    return numeros

def calcular_media(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

def main():
    # Encontrar os 100 primeiros números ímpares e múltiplos de 7
    quantidade = 100
    numeros = encontrar_impares_multiplos_7(quantidade)
    
    # Calcular a média
    media = calcular_media(numeros)
    
    # Exibir resultados
    print(f"Os {quantidade} primeiros números ímpares e múltiplos de 7 são:")
    print(numeros)
    print(f"Média dos números: {media}")

if __name__ == "__main__":
    main()