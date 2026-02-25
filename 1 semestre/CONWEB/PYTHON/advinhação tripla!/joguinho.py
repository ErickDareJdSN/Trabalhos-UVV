import random
import time
import webbrowser

def jogo_adivinhacao():
    """
    Jogo de adivinhação de três rodadas. Advinhe os números :)
    """
    acertos = 0
    video_url = "https://www.youtube.com/watch?v=tZzWdKc6-lI"  # Exemplo de vídeo (Rick Roll). Mude se quiser outro.

    for rodada in range(1, 4):  # 3 rodadas
        # Gera 3 números aleatórios únicos de 1 a 100
        numeros = random.sample(range(1, 101), 3)
        # Escolhe um dos 3 como correto
        correto = random.choice(numeros)
        
        # Mostra os números ao usuário
        print(f"\nRodada {rodada}: Escolha o número correto: {numeros[0]}, {numeros[1]}, {numeros[2]}")
        
        # Pega a entrada do usuário
        try:
            palpite = int(input("Escolha um número: "))
        except ValueError:
            print("Entrada inválida! Deve ser um número inteiro.")
            continue  # Pula para a próxima rodada se inválido
        
        # Verifica se acertou
        if palpite == correto:
            print("Correto!")
            acertos += 1
        else:
            print(f"Errado! O correto era {correto}.")
            break
    
    # Verifica o resultado final
    if acertos == 3:
        print("\nParabéns! Você venceu!")
    else:
        print("\nVocê perdeu ):")
        time.sleep(1)
        # Adiciona autoplay à URL
        autoplay_url = f"{video_url}&autoplay=1" if '?' in video_url else f"{video_url}?autoplay=1"
        webbrowser.open(autoplay_url)

# Executa o jogo
if __name__ == "__main__":
    jogo_adivinhacao()