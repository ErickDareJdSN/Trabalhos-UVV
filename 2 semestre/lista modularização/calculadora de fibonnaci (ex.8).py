def fibonacci(n):
    if n <= 0 or n > 100:
        raise ValueError("A quantidade de termos deve ser um número positivo entre 1 e 100")
    if n == 1:
        return [0]
    
    # Calculo da sequência
    sequencia = [0, 1]
    while len(sequencia) < n: #Checa se a quantidade de números na sequência é menor que n
        prox_numero = sequencia[-1] + sequencia[-2]
        sequencia.append(prox_numero)  # Adiciona o próximo número à sequência até atingir n termos
    return sequencia

def soma_fibonacci(n):
    seq = fibonacci(n)
    return sum(seq) #Soma os n primeiros números da sequência

def main():
    print("CALCULADORA DE FIBONACCI")
    print("Calcule a soma de uma quantidade de termos na sequência de Fibonacci")
    
    while True:
        try:
            n = int(input("Digite a quantidade de termos (ou 0 para sair): "))
            if n == 0:
                print("Programa encerrado.")
                break
            
            resultado = soma_fibonacci(n)
            print(f"A soma dos {n} primeiros termos da sequência de Fibonacci é: {resultado}")
            break
        
        except ValueError as e:
            if str(e).startswith("A quantidade"):
                print(f"Erro: {e}")
            else:
                print("Erro: Insira uma entrada válida.")

if __name__ == "__main__":
    main()