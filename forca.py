import random

def play():

    print_header()
    secret_word = choose_word()
    found_letters = initialize_found_letters(secret_word)
    print(found_letters)

    dead = False
    win = False
    attempts = 0


    #Enquanto não enforcou e não acertou
    while(not dead and not win ):

        letter = input("Qual letra? Resp: ")
        letter = letter.strip().upper()


        if(letter in secret_word):
           set_found_letter(secret_word, letter, found_letters)
        else:
            attempts += 1
            draw_gallows(attempts)

        dead = attempts == 7
        win = "_" not in found_letters
        print(found_letters)

    if(win):
        print_winner_message()
    else:
        print_loser_message(secret_word)


def print_header():
    
    print("------ Bem vindo ao jogo de Forca! ------")


def choose_word():
    archive = open("words.txt", "r")
    palavras = []

    for linha in archive:
        linha = linha.strip()
        palavras.append(linha)

    archive.close()

    secret_word = palavras[random.randrange(0, len(palavras))].upper()

    # Forma mais separada de fazer a seleção de palavras
    # indice = random.randrange(0, len(palavras))
    # palavra_secreta = palavras[indice].upper()

    return secret_word

def initialize_found_letters(word):
    return ["_" for letter in word]

def set_found_letter(secret_word, letter, found_letters):
    index = 0

    for letra in secret_word:
        if (letter.upper() == letra.upper()):
            found_letters[index] = letra.upper()
        index += 1

def print_winner_message():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def print_loser_message(secret_word):
    print("#########################")
    print("   VOCÊ FOI ENFORCADO!!  ")
    print("#########################\n")
    print("A palavra era {}".format(secret_word))


def draw_gallows(attempts):
    print("  _______     ")
    print(" |/      |    ")

    if(attempts == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(attempts == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(attempts == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(attempts == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(attempts == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(attempts == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (attempts == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

# Início do programa

if(__name__ == "__main__"):
    play()
