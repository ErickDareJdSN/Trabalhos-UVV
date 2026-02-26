# Inicializando a lista para armazenar os múltiplos de 11
multiplos = []

# Encontrando os múltiplos de 11 no intervalo [200, 100] em ordem decrescente
for num in range(200, 99, -1):
    if num % 11 == 0:
        multiplos.append(num)

# Calculando a soma dos múltiplos
soma = sum(multiplos)

# Calculando a média dos múltiplos, se houver múltiplos
media = soma / len(multiplos) if multiplos else 0

# Exibindo os resultados
print("Múltiplos de 11 no intervalo [200, 100] em ordem decrescente:")
print(multiplos)
print("Soma dos múltiplos:", soma)
print("Média dos múltiplos:", media)