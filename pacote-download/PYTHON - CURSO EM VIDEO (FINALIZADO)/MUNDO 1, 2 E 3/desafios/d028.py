# DESAFIO 028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint # usei choice
from time import sleep

# programa que faça o computador "pensar" em um número inteiro entre 0 e 5
nome = str(input('Digite o seu nome: '))
num = randint(0,5)

# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
print('Olá {}! Vamos jogar um jogo.'.format(nome))
print('Vou pensar em um número de 0 a 5 e você terá que adivinhá-lo.')
numesc = int(input('Digite o número escolhido: '))
print('PROCESSANDO...')
sleep(2)

# variáveis de respostas 
if numesc == num:
    print('Parabéns {}! Você leu a minha mente, eu realmente pensei no número {}.'.format(nome,numesc))
else:
    numesc != num
    print('Você errou {}! Tente outra vez, o número que eu pensei foi {}.'.format(nome,num))

# corrigido