import math

def hipotenusa(n1,n2):
    if n1 <1 or n1>100 or n2<1 or n2>100:
        raise ValueError("O tamanho dos lados deve ser entre 1 e 100.")

    h= (math.sqrt(n1**2 +n2**2))

    return h

def main():
    print("===CALCULADORA DE HIPOTENUSA===")
    
    try:
        n1= int(input("Digite o valor do primeiro lado: "))
        n2= int(input("Agora, digite o valor do segundo lado: "))

        resultado = hipotenusa(n1,n2)
        print(f"Valor da hipotenusa de {n1} e {n2}: {resultado:.2f}")

    except ValueError as e:
     if str(e).startswith("O tamanho") or str(e).startswith("Os lados"):
         print(f"Erro: {e}")
     else:
         print("Digite um valor numérico válido.")

main()