def calculo(n,h):
    area=n*h

    return area

def main():
    print("===CALCULDADORA DE ÁREA DE UM RETÂNGULO===")

    while True:
        entradaN=input("Digite o valor do lado (ou 0 para sair): ")
        if entradaN.strip()=="":
            print("Erro: Entrada vazia.")
            continue
        try:
            n=float(entradaN)

            if n==0:
                print("Programa encerrado.")
                break

            if n<1 or n>100:
                print("Erro: valor deve estar entre 1 e 100.")
                continue
            
            entradaH=input("Agora, digite o valor da altura (ou 0 para sair): ")
            if entradaH.strip()=="":
                print("Erro: entrada vazia.")
                continue

            h=float(entradaH)

            if h==0:
                    print("Programa encerrado.")
                    break

            if h<1 or h>100:
                    print("Erro: valor deve estar entre 1 e 100.")
                    continue

            resultado=calculo(n,h)
            print(f"Área do retângulo de lado {n} e altura {h}: {resultado:.2f}")

        except ValueError:
             print("Erro: Entrada inválida.")

main()