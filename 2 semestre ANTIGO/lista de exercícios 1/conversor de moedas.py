def conversao_dolar(dolar):
    if dolar <=0:
         raise ValueError("O valor deve ser maior que zero")
    if dolar >1000000000:
         raise ValueError("O valor deve ser menor que 1 bilhão")

    # Cotação dolar [dia 04/09/2025]          

    dolar_real = 5.44
    dolar_libra = 0.74
    return dolar_real, dolar_libra

def conversao_real(real):
    if real <=0:
        raise ValueError("O valor deve ser maior que zero")
    if real >1000000000:
         raise ValueError("O valor deve ser menor que 1 bilhão")

    # Cotação real [dia 04/09/2025]  

    real_dolar = 0.18
    real_libra = 0.14
    return real_dolar, real_libra

def conversao_libra(libra):
    if libra <=0:
         raise ValueError("O valor deve ser maior que zero")
    if libra >1000000000:
         raise ValueError("O valor deve ser menor que 1 bilhão")

    # Cotação libra [dia 04/09/2025]

    libra_dolar = 1.34
    libra_real = 7.32
    return libra_dolar, libra_real

def main():
    print("===Conversor de moedas===")

    while True:
        try:
            moeda = int(input("Digite 1 para converter R$, 2 para converter U$, 3 para converter £ ou 0 para sair: "))
            if moeda == 0:
                print("Programa encerrado.")
                break
            if moeda not in (1, 2, 3):
                print("Opção inválida.")
                continue

            valor = int(input("Digite o valor a ser convertido, ou 0 para sair: "))
            if valor == 0:
                print("Programa encerrado")
                break

            if moeda == 1:
               real_dolar, real_libra = conversao_real
               print(f"\nConversão de real pra dólar: {real_dolar:.2f}")
               print(f"\nConversão de real pra libra: {real_libra:.2f}")
            
            elif moeda == 2:
                dolar_real, dolar_libra = conversao_dolar
                print(f"\nConversão de dólar pra real: {dolar_real:.2f}")
                print(f"\nConversão de dólar pra libra: {dolar_libra:.2f}")

            else:
                libra_dolar, libra_real = conversao_libra
                print(f"\nConversão de libra pra dólar: {libra_dolar:.2f}")
                print(f"\nConversão de libra pra real: {libra_real:.2f}")

        except ValueError as e:
            if str (e).startswith("O valor"):
                print(f"Erro: {e}")
            else:
                print("Erro: Entrada inválida, digite um número válido.")

if __name__ == "__main__":
 main()    
                

