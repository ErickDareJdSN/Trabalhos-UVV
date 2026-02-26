def variavel(n):
    if n <= 0:
        raise ValueError("Número inválido. Por favor, insira um número positivo.")
    num = []  # Inicializa a lista dentro da função
    a = 6
    b = 6 * n
    for i in range(a, b + 1, 6):
        num.append(i)
    return num

def media(num):
    if not num:  # Verifica se a lista está vazia
        return 0, 0
    soma = sum(num)
    media_num = soma / len(num)
    return soma, media_num

def main():
    try:
        n = int(input("Digite um número positivo: "))
        multiplos = variavel(n)
        soma, media_num = media(multiplos)
        
        print(f"Múltiplos de 6 no intervalo [6, {6*n}]: {multiplos}")
        print(f"Soma dos múltiplos de 6: {soma}")
        print(f"Média dos múltiplos de 6: {media_num}")
    except ValueError as e:
        print(e if str(e).startswith("Número inválido") else "Erro, insira um valor numérico válido.")

if __name__ == "__main__":
    main()