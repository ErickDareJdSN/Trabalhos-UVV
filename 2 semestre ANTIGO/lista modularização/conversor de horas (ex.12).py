def converter_horas(horas_float):
    if horas_float < 0 or horas_float > 1000000:
        raise ValueError("A quantidade de horas deve ser entre 0 e 1000000.")
    if horas_float == 0:
        return (0, 0, 0)

    horas = int(horas_float)
    minutos_float = (horas_float - horas) * 60
    minutos = int(minutos_float)
    segundos = (minutos_float - minutos) * 60

    return horas, minutos, round(segundos)  # Arredonda segundos para evitar imprecisões

def main():
    while True:
        try:
            horas_float = float(input("Digite o valor de horas a ser convertido, incluindo decimais (ou 0 para sair): "))
            if horas_float == 0:
                print("Programa encerrado.")
                break

            horas, minutos, segundos = converter_horas(horas_float)
            print(f"A conversão do número é de: {horas} horas, {minutos} minutos, {segundos} segundos")
            break

        except ValueError as e:
            if str(e).startswith("A quantidade"):
                print(f"Erro: {e}")
            else:
                print("Erro: Insira uma entrada válida (um número com ou sem decimais).")

if __name__ == "__main__":
    main()