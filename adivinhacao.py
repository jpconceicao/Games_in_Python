import random

def play():
    
    print("\n-----  Bem vindo ao jogo de Adivinhação! -----\n\n")
    
    # Iniciando variáveis e escolhendo número aleatório
    secret_number = random.randrange(1, 101)
    attempts = 0
    score = 1000

    # Escolhendo nível e definindo nº de tentativas
    print("Qual o nível de dificuldade?")
    print("(1)- Fácil  (2) - Médio  (3) - Difícil")

    level = int(input("Defina o nível: "))

    if(level == 1):
        attempts = 20
    elif(level == 2):
        attempts = 10
    else:
        attempts = 5

    # Coletando entradas e comparando com número aleatório
    for round in range(1,attempts+1):
        print("Tentativa {} de {}".format(round, attempts))

        number_str = input("\nDigite o seu número entre 1 e 100: ")
        print("\nVocê digitou " , number_str)
        number = int(number_str)

        if(number < 1 or number > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        win = number == secret_number
        bigger = number > secret_number
        lower = number < secret_number

        if(win):
            print("Parabéns! Você acertou! Sua pontuação foi {}".format(score))
            break
        else:
            lost_score = abs(secret_number - number)
            score = score - lost_score

            if(bigger):
                print("O seu chute foi maior do que o número secreto!")
                if(round == attempts):
                    print("O número secreto era {}. A sua pontuação foi {}".format(secret_number, score))
            elif(lower):
                print("O seu chute foi menor do que o número secreto!")

                if (round == attempts):
                    print("O número secreto era {}. A sua pontuação foi {}".format(secret_number, score))

    print("Fim do jogo")

# Forma de executar o python diretamente e por chamada de arquivo
# sem ter problemas
if(__name__ == "__main__"):
    play()