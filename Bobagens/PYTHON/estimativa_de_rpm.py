def main():
    while True:
        try:
            print("\n=== ESTIMATIVA DE RPM ===")
            n = int(input("Digite o número de visualizações do vídeo: "))
            
            if n < 0:
                raise ValueError("O valor não pode ser negativo.")
            
            print("\n=== VALORES MÉDIOS DE RPM ===")
            print("RPM baixo: 2$ | RPM médio: 8$ | RPM alto: 20$")
            
            escolha = input("Digite o tipo de RPM (baixo, medio ou alto): ").strip().lower()
            
            if escolha == "baixo":
                rpm_valor = 2
            elif escolha == "medio":
                rpm_valor = 8
            elif escolha == "alto":
                rpm_valor = 20
            else:
                print("Tipo inválido, tente novamente.")
                continue
            
            ganho_estimado = (n / 1000) * rpm_valor
            print(f"\nSeu ganho estimado é: {ganho_estimado}$")
            break

        except ValueError as e:
            print(f"Erro: {e}")

main()
