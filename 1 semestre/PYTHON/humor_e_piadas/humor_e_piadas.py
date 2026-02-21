import random
import time
import webbrowser
import sys

def perguntas():
    pergunta1 = "Lado esquerdo ao contrário invertido:"
    alternativas1 = ["Esquerdo", "Direito", "Ok", "???"]
    resposta_certa1 = "Esquerdo"

    pergunta2 = "Qual o passatempo favorito do Luan Gameplay?"
    alternativas2 = ["Matar criança de sniper", "Bater na mãe", "Dar pro Renan Play", "Nenhuma das anteriores (ele é um homem bonzinho <3)"]
    resposta_certa2 = "Nenhuma das anteriores (ele é um homem bonzinho <3)"

    pergunta3 = "E nessa loucura"
    alternativas3 = ["?????", "Sim <3", "De dizer que não te quero", "Evidências em 2026? Sério?"]
    resposta_certa3 = "De dizer que não te quero"

    pergunta4 = "A raposa rouba, o cachorro toma, e o lobo?"
    alternativas4 = ["O lobo pede!", "O lobo come o cu de quem ta lendo!", "O lobo sofre!", "Nenhuma das anteriores"]
    resposta_certa4 = "O lobo pede!"

    pergunta5 = "Life goes oninoninoninoninonin"
    alternativas5 = ["Life goes on", "Oninoninon", "Ok????", "Não"]
    resposta_certa5 = "Oninoninon"

    pergunta6 = "Qual o número total de combinações possíveis de um cubo mágico 4x4x4?"
    alternativas6 = ["7.4 x 10^45 +1", "7.4 x 10^40", "7.4 x 10^50", "Bastante"]
    resposta_certa6 = "Bastante"

    pergunta7 = "Qual o nome do personagem principal de 'O Senhor dos Anéis'?"
    alternativas7 = ["Frodo", "Gerço", "Luciano Hang", "Bolsonaro"]
    resposta_certa7 = "Frodo"

    pergunta8 = "Você está jogando esse jogo pello arquivo enviado pelo seu amigão Erick?"
    alternativas8 = ["Sim", "Claro!", "Não, vai tomar no cu seu gordo escroto", "Quem é esse mlk?"]
    resposta_certa8 = "Claro!"

    pergunta9 = "Você ia preferir nunca mais precisar dormir ou nunca mais precisar comer?"
    alternativas9 = ["Nunca mais dormir", "Nunca mais comer", "Nenhuma das anteriores, eu amo dormir e comer", "Morte"]
    resposta_certa9 = "Nunca mais comer"

    pergunta_final = "Você vai compartir esse jogo com seus amigos?"
    alternativas_final = ["Sim, claro!", "Não, eu sou um otário(a)", "Não, morra, sucumba", "Sobra nada pro beta"]
    resposta_certa_final = "Sim, claro!"

    perguntas_list = [
        {"texto": pergunta1, "alternativas": alternativas1, "resposta_certa": resposta_certa1},
        {"texto": pergunta2, "alternativas": alternativas2, "resposta_certa": resposta_certa2},
        {"texto": pergunta3, "alternativas": alternativas3, "resposta_certa": resposta_certa3},
        {"texto": pergunta4, "alternativas": alternativas4, "resposta_certa": resposta_certa4},
        {"texto": pergunta5, "alternativas": alternativas5, "resposta_certa": resposta_certa5},
        {"texto": pergunta6, "alternativas": alternativas6, "resposta_certa": resposta_certa6},
        {"texto": pergunta7, "alternativas": alternativas7, "resposta_certa": resposta_certa7},
        {"texto": pergunta8, "alternativas": alternativas8, "resposta_certa": resposta_certa8},
        {"texto": pergunta9, "alternativas": alternativas9, "resposta_certa": resposta_certa9, "mensagem_errado": "Sua opinião não vale de nada."} 
    ]

    pergunta_final_dict = {"texto": pergunta_final, "alternativas": alternativas_final, "resposta_certa": resposta_certa_final}

    return perguntas_list, pergunta_final_dict

def apresentar_pergunta(pergunta_dict):
    print(pergunta_dict["texto"])
    print()  
    alternativas_embaralhadas = pergunta_dict["alternativas"][:]
    random.shuffle(alternativas_embaralhadas)
    for i, alt in enumerate(alternativas_embaralhadas, 1):
        print(f"{i}. {alt}")
    resposta_usuario = input("Escolha a alternativa (digite o número): ").strip()
    try:
        indice = int(resposta_usuario) - 1
        if 0 <= indice < len(alternativas_embaralhadas):
            return alternativas_embaralhadas[indice] == pergunta_dict["resposta_certa"]
        else:
            return False
    except ValueError:
        return False

def main():
    video_url = "https://youtu.be/tZzWdKc6-lI?si=6-VC0kvKQ1MDNI231"
    # Forma mais confiável de adicionar autoplay
    autoplay_url = video_url + "&autoplay=1" if "?" in video_url else video_url + "?autoplay=1"

    while True:
        print("Bem-vindo a um Quiz nada convencional com perguntas nada convencionais!")
        time.sleep(1)  

        perguntas_list, pergunta_final = perguntas()
        random.shuffle(perguntas_list)

        for pergunta in perguntas_list:
            correto = apresentar_pergunta(pergunta)
            if correto:
                print("Correto!\n")
            else:
                if "mensagem_errado" in pergunta:
                    print(pergunta["mensagem_errado"] + "\n")
                else:
                    print("XD\n")
                
                time.sleep(1)                      # ← pausa de 1 segundo para ler a mensagem
                webbrowser.open(autoplay_url)      # só depois abre o vídeo
                time.sleep(1)
                sys.exit(0)  
            time.sleep(1)

        # Pergunta final
        print("Pergunta final:")
        if apresentar_pergunta(pergunta_final):
            print("Parabéns! Você completou o quiz com sucesso!\n")
        else:
            print("):<\n")
            time.sleep(1)                      # ← mesma pausa aqui também
            webbrowser.open(autoplay_url)
            time.sleep(1)
            sys.exit(0)  
        time.sleep(1)

        reiniciar = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if reiniciar != 's':
            print("Obrigado por jogar!")
            break

if __name__ == "__main__":
    main()