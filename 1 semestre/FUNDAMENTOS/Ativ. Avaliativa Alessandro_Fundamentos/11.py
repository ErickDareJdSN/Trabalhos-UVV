def calculo_tempo(mb, velocidade):
    return mb / velocidade


def ler_valor(mensagem, limite):
    while True:
        entrada = input(mensagem).strip().lower()

        if entrada == "sair":
            return None

        if entrada == "":
            print("Valor não pode ser vazio. Tente novamente.")
            continue

        try:
            valor = float(entrada)

            if valor <= 0 or valor > limite:
                print(f"Valor deve estar entre 0 e {limite}.")
                continue

            return valor

        except ValueError:
            print("Erro: insira um número válido.")


def converter_tempo(segundos_totais):
    horas = int(segundos_totais // 3600)
    minutos = int((segundos_totais % 3600) // 60)
    segundos = round(segundos_totais % 60)

    if segundos == 60:
        segundos = 0
        minutos += 1

    if minutos == 60:
        minutos = 0
        horas += 1

    return horas, minutos, segundos


def converter_tamanho(mb):
    if mb >= 1024**3:  # PB
        pb = mb / (1024**3)
        return f"{pb:.2f} PB"
    elif mb >= 1024**2:  # TB
        tb = mb / (1024**2)
        return f"{tb:.2f} TB"
    elif mb >= 1024:  # GB
        gb = mb / 1024
        return f"{gb:.2f} GB"
    else:
        return f"{mb:.2f} MB"


def main():
    print("=== CALCULADORA DE TEMPO DE DOWNLOAD ===")
    print()

    LIMITE_ARQUIVO = 1024**3
    LIMITE_VELOCIDADE = 10**6

    while True:
        mb = ler_valor(
            "Digite o tamanho do arquivo em MB (até 1 PB) ou 'sair': ",
            LIMITE_ARQUIVO
        )
        if mb is None:
            print("Encerrando o programa.")
            break

        velocidade = ler_valor(
            "Digite a velocidade em MB/s (ou 'sair'): ",
            LIMITE_VELOCIDADE
        )
        if velocidade is None:
            print("Encerrando o programa.")
            break

        tempo_total = calculo_tempo(mb, velocidade)
        horas, minutos, segundos = converter_tempo(tempo_total)
        tamanho_convertido = converter_tamanho(mb)

        print("-" * 40)
        print(f"Tamanho do arquivo: {tamanho_convertido}")
        print(f"Velocidade: {velocidade:.2f} MB/s")
        print(f"Tempo estimado: {horas}h {minutos}m {segundos}s")
        print("-" * 40)
        print()

        resposta = input("Deseja calcular novamente? (s/n): ").strip().lower()
        while resposta not in ["s", "n"]:
            resposta = input("Resposta inválida. Digite 's' ou 'n': ").strip().lower()

        if resposta == "n":
            print("Encerrando o programa.")
            break

        print()


main()