import random

def jogar():

    print("Vamos jogar?")
    print("Este é um jogo de adivinhação. Digite um número entre 1 e 100 e tente acertar. Boa sorte!")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Níveis:")
    print("1 (Fácil: 10 tentativas) \n2 (Médio: 5 tentativas) \n3 (Difícil: 3 tentativas)")

    nivel = int(input("Escolha o nível: "))

    if(nivel == 1):
        total_de_tentativas = 10
    elif(nivel == 2):
        total_de_tentativas = 5
    else:
        total_de_tentativas = 3

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if(maior):
                print("O seu chute foi maior que o número secreto")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} pontos!".format(
                        numero_secreto, pontos))
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} pontos!".format(
                        numero_secreto, pontos))

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()