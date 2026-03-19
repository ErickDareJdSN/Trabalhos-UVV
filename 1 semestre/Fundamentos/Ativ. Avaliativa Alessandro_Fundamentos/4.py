import math
def calculo(r):
    area=math.pi *r**2
    comprimento=2*math.pi*r

    return area, comprimento

def main():
    print("===CALCULADORA DE ÁREA E COMPRIMENTO DE UM CÍRCULO===")

    while True:
        entrada=input("Digite o valor do raio do círculo (ou 0 para sair): ")
        if entrada.strip()=="":
            print("Erro: Entrada vazia.")
            continue
        try:
            r=float(entrada)
            if r==0:
                print("Programa encerrado.")
                break
            if r <1 or r>100:
                print("Erro: valor deve ser entre 1 e 100.")
                continue

            resultado_area, resultado_comp=calculo(r)
            
            print(f"Área do círculo de raio {r}: {resultado_area:.2f}")
            print(f"Comprimento do círculo de raio {r}: {resultado_comp:.2f}")
        except ValueError:
            print("Erro: Entrada inválida.")
main()