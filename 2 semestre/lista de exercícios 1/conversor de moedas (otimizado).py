from enum import Enum
from typing import Tuple

# Constantes para cotações (baseadas em 04/09/2025) e limites
COTACOES = {
    'dolar': {'real': 5.44, 'libra': 0.74},
    'real': {'dolar': 0.18, 'libra': 0.14},
    'libra': {'dolar': 1.34, 'real': 7.32}
}
LIMITE_MAXIMO = 1_000_000_000  # Limite máximo para todas as moedas

class Moeda(Enum):
    REAL = 1
    DOLAR = 2
    LIBRA = 3
    SAIR = 0

def validar_valor(valor: float, moeda: str) -> None:
    """Valida se o valor é positivo e está dentro do limite."""
    if valor <= 0:
        raise ValueError(f"O valor em {moeda} deve ser maior que zero.")
    if valor > LIMITE_MAXIMO:
        raise ValueError(f"O valor em {moeda} deve ser menor que {LIMITE_MAXIMO:,}.")

def converter_moeda(valor: float, moeda_entrada: Moeda) -> Tuple[float, float]:
    """Converte o valor entre real, dólar e libra."""
    if moeda_entrada == Moeda.REAL:
        validar_valor(valor, 'real')
        dolar = valor * COTACOES['real']['dolar']
        libra = valor * COTACOES['real']['libra']
        return dolar, libra
    elif moeda_entrada == Moeda.DOLAR:
        validar_valor(valor, 'dólar')
        real = valor * COTACOES['dolar']['real']
        libra = valor * COTACOES['dolar']['libra']
        return real, libra
    else:  # Moeda.LIBRA
        validar_valor(valor, 'libra')
        dolar = valor * COTACOES['libra']['dolar']
        real = valor * COTACOES['libra']['real']
        return dolar, real

def exibir_resultado(valor: float, moeda_entrada: Moeda, resultado: Tuple[float, float]) -> None:
    """Exibe os resultados da conversão."""
    if moeda_entrada == Moeda.REAL:
        print(f"Conversão de real para dólar: {resultado[0]:.2f} dólares")
        print(f"Conversão de real para libra: {resultado[1]:.2f} libras")
    elif moeda_entrada == Moeda.DOLAR:
        print(f"Conversão de dólar para real: {resultado[0]:.2f} reais")
        print(f"Conversão de dólar para libra: {resultado[1]:.2f} libras")
    else:  # Moeda.LIBRA
        print(f"Conversão de libra para dólar: {resultado[0]:.2f} dólares")
        print(f"Conversão de libra para real: {resultado[1]:.2f} reais")

def main():
    print("=== Conversor de Moedas ===")
    
    while True:
        try:
            moeda = int(input("Digite 1 para R$, 2 para U$, 3 para £ ou 0 para sair: "))
            if moeda == Moeda.SAIR.value:
                print("Programa encerrado.")
                break

            if moeda not in (Moeda.REAL.value, Moeda.DOLAR.value, Moeda.LIBRA.value):
                print("Opção inválida. Tente novamente.")
                continue

            valor = float(input("Digite o valor a ser convertido: "))
            moeda_entrada = Moeda(moeda)
            resultado = converter_moeda(valor, moeda_entrada)
            exibir_resultado(valor, moeda_entrada, resultado)
            break

        except ValueError as e:
            if str(e).startswith("O valor em"):
                print(f"Erro: {e}")
            else:
                print("Erro: Entrada inválida, digite um número válido.")

if __name__ == "__main__":
    main()