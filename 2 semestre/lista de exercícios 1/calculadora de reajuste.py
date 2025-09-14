def calcular_reajuste(preco, reajuste):
    if preco <= 0:
        raise ValueError("O preço deve ser um número positivo maior que zero.")
    if preco > 10000:
        raise ValueError("O preço deve ser menor ou igual a 10.000.")
    
    if reajuste == 1:
        return preco * 1.03  # Acréscimo de 3%
    elif reajuste == 2:
        return preco * 0.97  # Desconto de 3%
    else:
        raise ValueError("Reajuste inválido. Use 1 para acréscimo ou 2 para desconto.")

def main():
    while True:
        try:
            reajuste = int(input("Digite '1' para acréscimo, '2' para desconto ou '0' para sair: "))
            if reajuste == 0:
                print("Programa encerrado.")
                break
            if reajuste not in (1, 2):
                print("Erro: Opção inválida. Digite 1, 2 ou 0.")
                continue

            preco = float(input("Digite o preço do produto (ou 0 para sair): "))
            if preco == 0:
                print("Programa encerrado.")
                break

            resultado = calcular_reajuste(preco, reajuste)
            if reajuste == 1:
                print(f"O produto com acréscimo de 3% é: R$ {resultado:.2f}")
            elif reajuste == 2:
                print(f"O produto com desconto de 3% é: R$ {resultado:.2f}")

        except ValueError as e:
            if str(e).startswith("O preço") or str(e).startswith("Reajuste"):
                print(f"Erro: {e}")
            else:
                print("Erro: Entrada inválida. Digite um número válido para preço ou reajuste.")

if __name__ == "__main__":
    main()