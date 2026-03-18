def calcular_ingredientes_bolo(xicaras_farinha):
    # Receita base para 2 xícaras de farinha
    proporcao = xicaras_farinha / 2

    cenouras = 3 * proporcao
    ovos = 4 * proporcao
    oleo = 1 * proporcao
    acucar = 2 * proporcao
    fermento = 1 * proporcao

    print(f"\n📘 Receita ajustada para {xicaras_farinha:.2f} xícaras de farinha:")
    print(f"- {cenouras:.2f} cenouras médias")
    print(f"- {ovos:.2f} ovos")
    print(f"- {oleo:.2f} xícara(s) de óleo")
    print(f"- {acucar:.2f} xícara(s) de açúcar")
    print(f"- {fermento:.2f} colher(es) de sopa de fermento\n")

def calcular_calda_chocolate(colheres_manteiga):
    # Receita base para 1 colher de manteiga
    proporcao = colheres_manteiga / 1

    chocolate = 3 * proporcao
    acucar = 1 * proporcao
    leite = 1 * proporcao

    print(f"\n🍫 Calda de chocolate ajustada para {colheres_manteiga:.2f} colher(es) de manteiga:")
    print(f"- {chocolate:.2f} colher(es) de sopa de chocolate em pó")
    print(f"- {acucar:.2f} xícara(s) de açúcar")
    print(f"- {leite:.2f} xícara(s) de leite\n")

# Programa principal
print("=== Simulador de Receita de Bolo de Cenoura ===")

try:
    xicaras = float(input("Quantas xícaras de farinha você vai usar para o bolo? "))
    if xicaras <= 0:
        print("Por favor, informe um número positivo.")
    else:
        calcular_ingredientes_bolo(xicaras)

        # Perguntar se o usuário quer calcular a calda
        resposta = input("Deseja calcular a calda de chocolate também? (s/n): ").strip().lower()
        if resposta == 's':
            colheres = float(input("Quantas colheres de sopa de manteiga você vai usar na calda? "))
            if colheres <= 0:
                print("Quantidade inválida de manteiga.")
            else:
                calcular_calda_chocolate(colheres)
        else:
            print("\n Beleza! Receita de bolo finalizada sem calda.")
except ValueError:
    print("Entrada inválida. Por favor, digite um número.")
