import random

def jogar():

    imprime_boas_vindas()

    palavra = carrega_palavra_secreta()

    letras_acertadas = incializa_letras_acertadas(palavra)

    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0

    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra):
            marca_chute_correto(chute, letras_acertadas, palavra)
        else:
            tentativas += 1
            desenha_forca(tentativas)

        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas

        total_tentativas = 6 - tentativas
        if(total_tentativas >= 0):
            print("tentativas restantes {}".format(total_tentativas))

        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra)

def imprime_boas_vindas():
    print("********************************")
    print("bem vindo ao jogo de forca")
    print("********************************")

def carrega_palavra_secreta():
    with open("palavras.txt") as arquivo:
        frutas = []

        for linha in arquivo:
             linha = linha.strip()
             frutas.append(linha)

        numero = random.randrange(0, len(frutas))
        palavra = frutas[numero].upper()
        return palavra

def incializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
     chute = input("Qual letra? ")
     chute = chute.strip().upper()
     return chute

def marca_chute_correto(chute, letras_acertadas, palavra):
    index = 0
    for letra in palavra:

        if (chute == letra):
                letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
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

def imprime_mensagem_perdedor(palavra):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar()
