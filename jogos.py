import forca
import adivinhacao

def choose_game():
    print("***************************")
    print("Escolha o seu jogo, bro!!!!")
    print("***************************")

    print("Jogos disponíveis:")
    print("(1) - Forca   (2) - Adivinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando Forca")
        forca.play()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.play()

if(__name__ == "__main__"):
    choose_game()