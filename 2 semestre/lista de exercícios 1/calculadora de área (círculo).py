import math

print('CALCULADORA DE ÁREA E COMPRIMENTO.')

try:
    R = float(input('Valor do raio (R): '))
    if R <= 0:
        print('Erro: O raio deve ser maior que zero.')
    else:
        area = math.pi * R ** 2
        comprimento = 2 * math.pi * R
        print(f'ÁREA DA CIRCUNFERÊNCIA: {area:.2f} unidades²')
        print(f'COMPRIMENTO DA CIRCUNFERÊNCIA: {comprimento:.2f} unidades')
except ValueError:
    print('Erro: Insira um valor numérico válido.')