from enum import Enum
from typing import Tuple

# Constantes
QUILOS_POR_TONELADA = 1000
ONCAS_POR_QUILO = 35.274
LIMITES_MAXIMOS = {
    'quilos': 10000,
    'toneladas': 10,
    'onças': 352740
}

class Unidade(Enum):
    QUILOS = 1
    TONELADAS = 2
    ONÇAS = 3
    SAIR = 0

def validar_peso(peso: float, unidade: str) -> None:
    """Valida se o peso é positivo e está dentro dos limites."""
    if peso <= 0:
        raise ValueError(f"O peso em {unidade} deve ser um número positivo.")
    if peso > LIMITES_MAXIMOS[unidade]:
        raise ValueError(f"O peso em {unidade} deve ser menor que {LIMITES_MAXIMOS[unidade]}.")

def converter_peso(peso: float, unidade_entrada: Unidade) -> Tuple[float, float]:
    """Converte peso entre quilos, toneladas e onças."""
    if unidade_entrada == Unidade.QUILOS:
        validar_peso(peso, 'quilos')
        toneladas = peso / QUILOS_POR_TONELADA
        onças = peso * ONCAS_POR_QUILO
        return toneladas, onças
    elif unidade_entrada == Unidade.TONELADAS:
        validar_peso(peso, 'toneladas')
        quilos = peso * QUILOS_POR_TONELADA
        onças = quilos * ONCAS_POR_QUILO
        return quilos, onças
    else:  # Unidade.ONÇAS
        validar_peso(peso, 'onças')
        quilos = peso / ONCAS_POR_QUILO
        toneladas = quilos / QUILOS_POR_TONELADA
        return quilos, toneladas

def exibir_resultado(peso: float, unidade_entrada: Unidade, resultado: Tuple[float, float]) -> None:
    """Exibe os resultados da conversão."""
    if unidade_entrada == Unidade.QUILOS:
        print(f"Conversão de quilos para toneladas: {resultado[0]:.2f} toneladas")
        print(f"Conversão de quilos para onças: {resultado[1]:.2f} onças")
    elif unidade_entrada == Unidade.TONELADAS:
        print(f"Conversão de toneladas para quilos: {resultado[0]:.2f} quilos")
        print(f"Conversão de toneladas para onças: {resultado[1]:.2f} onças")
    else:  # Unidade.ONÇAS
        print(f"Conversão de onças para quilos: {resultado[0]:.2f} quilos")
        print(f"Conversão de onças para toneladas: {resultado[1]:.2f} toneladas")

def main():
    print("=== Conversor de Unidades de Peso ===")
    
    while True:
        try:
            unidade = int(input("Escolha a unidade de entrada (1-Quilos, 2-Toneladas, 3-Onças, 0-Sair): "))
            if unidade == Unidade.SAIR.value:
                print("Programa encerrado.")
                break

            if unidade not in (Unidade.QUILOS.value, Unidade.TONELADAS.value, Unidade.ONÇAS.value):
                print("Opção inválida. Tente novamente.")
                continue

            peso = float(input("Digite o peso a ser convertido: "))
            unidade_entrada = Unidade(unidade)
            resultado = converter_peso(peso, unidade_entrada)
            exibir_resultado(peso, unidade_entrada, resultado)
            break

        except ValueError as e:
            if str(e).startswith("O peso em"):
                print(f"Erro: {e}")
            else:
                print("Entrada inválida. Tente novamente.")

if __name__ == "__main__":
    main()