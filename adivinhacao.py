
def jogar():

    print("********************************")
    print("bem vindo ao jogo de adivinhação")
    print("********************************")

    import random
    numero_secreto = random.randrange(1,101)
    tentativa = 0
    pontos = 1000

    print(numero_secreto)
    print('Escolha a dificuldade')
    print('facil(1), médio(2), difícil(3)')

    dificuldade = int(input('insira a dificuldade:'))

    if(dificuldade == 1):
        tentativa = 20

    elif(dificuldade == 2):
        tentativa = 10

    else:
        tentativa = 5

    for rodada in range(1,tentativa + 1):

        print('tentativa', rodada, 'de', tentativa)

        chute_str = input("digite o seu número:")
        chute_int = int(chute_str)

        print("Você digitou" , chute_int)

        igual = numero_secreto == chute_int
        maior = numero_secreto > chute_int
        menor = numero_secreto < chute_int

        if(chute_int < 1 or chute_int > 100):
            print("digite um número entre 1 e 100")
            continue

        if(igual):
            print('Você acertou!!! sua pontuação é de {} pontos'.format(pontos))
            break
        else:
            if(maior):
                print('você errou, o numero que você digitou é menor do que o número secreto')
            elif(menor):
                print('você errou, o numero que você digitou é maior do que o número secreto')
            if(rodada == tentativa):
                print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))

            pontos_perdidos = abs(numero_secreto - chute_int)
            pontos = pontos - pontos_perdidos

if(__name__ == "__main__"):
    jogar()





