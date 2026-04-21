import math
from functools import reduce


def instrucoes():
    print("\n=== CALCULADORA DE TERMOS ===")
    print("Digite os valores um por um, quando terminar, digite 'feito'")
    print("Máximo de 10 termos.")
    print("Mínimo de 2 termos.\n")


def ler_valores():
    valores = []

    while len(valores) < 10:
        entrada = input(f"Digite o {len(valores) + 1}º valor: ").strip().lower()

        if entrada == "feito":
            if len(valores) < 2:
                print("Você precisa digitar pelo menos 2 valores antes de finalizar.")
                continue
            break

        try:
            num = float(entrada)
            valores.append(num)

            if len(valores) == 10:
                print("Limite de 10 termos atingido. Continuando automaticamente.")
                break

        except ValueError:
            print("Valor inválido. Digite um número ou 'feito'.")

    return valores


def calcular(valores):
    resultados = {}

    resultados["soma"] = sum(valores)
    resultados["subtracao"] = reduce(lambda x, y: x - y, valores)
    resultados["multiplicacao"] = math.prod(valores)
    resultados["media"] = sum(valores) / len(valores)

    try:
        resultados["divisao"] = reduce(lambda x, y: x / y, valores)
    except ZeroDivisionError:
        resultados["divisao"] = "Erro: divisão por zero."

    try:
        resultados["potencia"] = reduce(lambda x, y: x ** y, valores)
    except OverflowError:
        resultados["potencia"] = "Erro: resultado muito grande."
    except ValueError:
        resultados["potencia"] = "Erro: operação de potência inválida."

    raizes = []
    for n in valores:
        if n < 0:
            raizes.append(f"Erro: raiz de {n} não é real.")
        else:
            raizes.append(math.sqrt(n))
    resultados["raizes_individuais"] = raizes

    soma_total = sum(valores)
    if soma_total < 0:
        resultados["raiz_da_soma"] = "Erro: a soma é negativa, não possui raiz real."
    else:
        resultados["raiz_da_soma"] = math.sqrt(soma_total)

    return resultados

def formatar(valor):
    if isinstance(valor, (int, float)):
        return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return valor

def formatar_lista(lista):
    return [formatar(v) for v in lista]


def mostrar_resultados(valores, resultados):
    print("\n=== RESULTADOS ===")

    valores_formatados = formatar_lista(valores)
    print(f"Valores digitados: {valores_formatados}")

    print(f"Soma = {formatar(resultados['soma'])}")
    print(f"Subtração = {formatar(resultados['subtracao'])}")
    print(f"Multiplicação = {formatar(resultados['multiplicacao'])}")
    print(f"Divisão = {formatar(resultados['divisao'])}")
    print(f"Potência = {formatar(resultados['potencia'])}")

    raizes_formatadas = formatar_lista(resultados['raizes_individuais'])
    print(f"Raízes individuais = {raizes_formatadas}")

    print(f"Raiz da soma = {formatar(resultados['raiz_da_soma'])}")
    print(f"Média = {formatar(resultados['media'])}")


def main():
    while True:
        instrucoes()
        valores = ler_valores()
        resultados = calcular(valores)
        mostrar_resultados(valores, resultados)

        continuar = input("\nDeseja fazer outro cálculo? (s/n): ").strip().lower()
        if continuar != "s":
            print("Encerrando a calculadora.")
            break


main()