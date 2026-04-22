def main():
    fases = [
        'cheia',
        'minguante gibosa',
        'quarto minguante',
        'minguante crescente',
        'nova',
        'crescente',
        'quarto crescente',
        'crescente gibosa'
    ]

    while True:
        try:
            print('Fases da lua para spawn de slimes, da mais à menos eficiente:')
            print()
            print(f'1. {fases[0]}')
            print(f'2. {fases[1]} e {fases[7]}')
            print(f'3. {fases[2]} e {fases[6]}')
            print(f'4. {fases[3]} e {fases[5]}')
            print(f'5. {fases[4]}')

            dia = int(input('\nDigite o número do dia em jogo: '))

            calculo = dia % 8
            fase = fases[calculo]

            print(f'\nHoje é noite de lua {fase}.\n')

            if calculo == 0:
                print('SLIMES!')
            elif calculo == 4:
                print('Sem slimes ):')
            else:
                print('Chance intermediária de spawn de slimes.')

            break

        except ValueError:
            print('Erro: por favor insira um valor válido.')


main()