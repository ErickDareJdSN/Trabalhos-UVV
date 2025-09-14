def calcular_peso(altura, homem, mulher):
   if altura <=0:
       raise ValueError("A altura deve ser um número positivo.")
   if altura >300: # Limite realista de altura em cm
       raise ValueError("A altura deve ser um valor realista.")

   # Calculo do peso ideal
   peso_homem = 72.7 * (altura/100) - 58
   peso_mulher = 62.1 * (altura/100) - 44.7

   return altura, round(peso_homem, 2), round(peso_mulher, 2)

def main():
   print("Calculadora de Peso Ideal")
   while True:
       try:
           altura = float(input("Digite sua altura em cm (ou 0 para sair): "))
           if altura == 0:
               print("Encerrando o programa.")
               break
           homem, mulher = calcular_peso(altura, True, True)
           print(f"Para uma altura de {altura} cm:")
           print(f" - Peso ideal para homens: {homem} kg")
           print(f" - Peso ideal para mulheres: {mulher} kg")
       except ValueError as e:
           if str(e).startswith("A altura"):
               print(f"Erro: {e}")
           else:
                print("Erro: Insira valores numéricos válidos.")

if __name__ == "__main__":
    main()