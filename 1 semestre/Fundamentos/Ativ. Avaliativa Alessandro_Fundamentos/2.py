def calculo(n):
    return n**2


def main():
    print("=== CALCULADORA DE ÁREA DE UM QUADRADO ===")

    while True:
        entrada = input("Digite o valor do lado (ou 0 para sair): ")

        if entrada.strip() == "":
            print("Erro: entrada vazia.")
            continue

        try:
            n = float(entrada)

            if n == 0:
                print("Programa encerrado.")
                break

            if n < 1 or n > 100:
                print("Erro: valor deve estar entre 1 e 100.")
                continue

            resultado = calculo(n)
            print(f"Área: {resultado:.2f}")

        except ValueError:
            print("Erro: digite um número válido.")


main()