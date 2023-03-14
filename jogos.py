import advinhacao
import forca
import palavras

def escolher_jogos():

    print("Escolha o jogo!")

    print("Digite: 1 para Jogo da Forca e 2 para Jogo da Advinhação.")

    jogo = int(input("Qual o jogo?"))

    if(jogo == 1):
        print("Jogo da Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogo da Advinhação")
        advinhacao.jogar()

if(__name__ == "__main__"):
    escolher_jogos()
