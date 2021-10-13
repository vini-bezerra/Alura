import forca
import adivinhacao

print("********************************")
print("escolha o seu jogo")
print("********************************")
print('(01)forca (02)advinhação')

jogo = int(input('qual jogo?'))

if(jogo == 1):
    print('jogando forca')
    forca.jogar()
elif(jogo == 2):
    print('jogando adivinhação')
    adivinhacao.jogar() 


