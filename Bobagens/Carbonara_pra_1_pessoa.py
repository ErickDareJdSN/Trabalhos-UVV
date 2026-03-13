def main():
    while True:
        try:
            print("=== Calcule os ingredientes pro seu carbonara aqui! ===")

            n = int(input("Digite a quantidade de porções de carbonara (ou 0 para sair): "))

            if n < 0:
                raise ValueError("A quantidade de porções não pode ser menor que 1. Tente novamente.")

            if n == 0:
                print("Programa encerrado.")
                break

            print(f"\n=== INGREDIENTES PARA {n} PORÇÕES DE CARBONARA ===")

            print(f"{100 * n} g de espaguete")
            print(f"{1.5 * n} ovos")
            print(f"{30 * n} g de guanciale")
            print(f"{25 * n} g de queijo pecorino")

            print("\n=== ESTIMATIVA DE PREÇO DOS INGREDIENTES ===")

            espaguete = 1
            ovo = 1.35
            pecorino = 9
            guanciale = 4.5

            preco = espaguete + ovo + pecorino + guanciale

            print(f"Espaguete: R${espaguete * n:.2f}")
            print(f"Ovo(s): R${ovo * n:.2f}")
            print(f"Pecorino: R${pecorino * n:.2f}")
            print(f"Guanciale: R${guanciale * n:.2f}")

            print(f"\nVALOR TOTAL: R${preco * n:.2f}\n")
            break

        except ValueError as e:
            if str(e).startswith("A quantidade"):
                print(f"Erro: {e}")
            else:
                print("Erro: Por favor, insira um valor numérico válido.")


main()