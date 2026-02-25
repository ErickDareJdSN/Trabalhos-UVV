def sequencia(numero):
    if numero <= 0 or numero >= 10000:
        raise ValueError("O número deve ser maior que 0 e menor que 10000.")

    multiplos = []
    for i in range(0, 101):
        multiplos.append(numero * i)

    return multiplos


def main():
    while True:
        try:
            print("=== CALCULADORA DE MÚLTIPLOS ===")
            numero = int(input(
                "Digite um número para calcular os múltiplos (até 10000), ou 0 para sair: "
            ))

            if numero == 0:
                print("Programa encerrado.")
                break

            resultado = sequencia(numero)

            print(f"Sequência de múltiplos de {numero}:")
            for valor in resultado:
                print(valor)

        except ValueError as e:
            if str(e).startswith("O número"):
                print(f"Erro: {e}")
            else:
                print("Erro: Por favor, insira um valor numérico válido.")


main()