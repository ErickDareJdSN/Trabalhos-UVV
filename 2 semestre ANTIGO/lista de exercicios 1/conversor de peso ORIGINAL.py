def conversão_quilos(quilos):
    if quilos <= 0:
        raise ValueError("O peso em quilos deve ser um número positivo.")
    if quilos > 10000:
        raise ValueError("O peso em quilos deve ser menor que 10.000.")
    
    # Conversão de quilos para toneladas / onças
    
    quilos_toneladas = quilos / 1000
    quilos_onças = quilos * 35.274
    return quilos_toneladas, quilos_onças

def conversão_toneladas(toneladas):
    if toneladas <= 0:
        raise ValueError("O peso em toneladas deve ser um número positivo.")
    if toneladas > 10:
        raise ValueError("O peso em toneladas deve ser menor que 10.")
    
    # Conversão de toneladas para quilos / onças
    
    toneladas_quilos = toneladas * 1000
    toneladas_onças = toneladas_quilos * 35.274
    return toneladas_quilos, toneladas_onças

def conversão_onças(onças):
    if onças <= 0:
        raise ValueError("O peso em onças deve ser um número positivo.")
    if onças > 352740:
        raise ValueError("O peso em onças deve ser menor que 352.740.")
    
    # Conversão de onças para quilos / toneladas
    
    oncas_quilos = onças / 35.274
    oncas_toneladas = oncas_quilos / 1000
    return oncas_quilos, oncas_toneladas

def main():
    (print("===Conversor de Unidades de Peso==="),)

    while True:
        try:
            unidade = (int(input("Escolha a unidade de entrada (1-Quilos, 2-Toneladas, 3-Onças, 0-Sair): ")))
            if unidade == 0:
                print("Programa encerrado.")
                break

            if unidade not in (1, 2, 3):
                print("Opção inválida. Tente novamente.")
                continue

            peso = float(input("Digite o peso a ser convertido, ou 0 para sair: "))
            if peso == 0:
                print("Programa encerrado.")
                break

            if unidade == 1:
                quilos_toneladas, quilos_onças = conversão_quilos(peso)
                print(f"Conversão de quilos pra toneladas: {quilos_toneladas:.2f} toneladas")
                print(f"Conversão de quilos pra onças: {quilos_onças:.2f} onças")

            elif unidade == 2:
                toneladas_quilos, toneladas_onças = conversão_toneladas(peso)
                print(f"Conversão de toneladas pra quilos: {toneladas_quilos:.2f} quilos")
                print(f"Conversão de toneladas pra onças: {toneladas_onças:.2f} onças")

            else:
                oncas_quilos, oncas_toneladas = conversão_onças(peso)
                print(f"Conversão de onças pra quilos: {oncas_quilos:.2f} quilos")
                print(f"Conversão de onças pra toneladas: {oncas_toneladas:.2f} toneladas")
                break

        except ValueError as e:
            if str(e).startswith("O peso em"):
                print(f"Erro: {e}")
            
            else:
                print("Enrtrada inválida. Tente novamente.")

if __name__ == "__main__":
    main()
