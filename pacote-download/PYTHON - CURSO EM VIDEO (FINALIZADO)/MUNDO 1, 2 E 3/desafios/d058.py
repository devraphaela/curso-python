# DESAFIO 058 - Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep


numPC = randint(0,10)

nome = str(input('Digite o seu nome para começar: '))

print(f'Olá {nome}! Vamos jogar um jogo.')
print('Vou pensar em um número de 0 a 10 e você terá que adivinhá-lo, você terá várias tentativas até acertar.')

numJOG = int(input('Digite o número escolhido: '))
somaJOG = 0

print('PROCESSANDO...')
sleep(1)

while numJOG != numPC:
    print('Você errou! Tente novamente.')
    numJOG = int(input('Digite o número escolhido: '))
    somaJOG += 1

if numJOG == numPC:
    print(f'Parabéns {nome}, você acertou!')

if somaJOG == 0:
    print('Foi de primeira.')
else:
    print(f'ao todo foram {somaJOG} tentativas até você acertar.')

#CORRIGIDO 
