# DESAFIO 020 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

g1 = str(input('Digite o nome do grupo:'))
g2 = str(input('Digite o nome do grupo:'))
g3 = str(input('Digite o nome do grupo:'))
g4 = str(input('Digite o nome do grupo:'))

g_lista = [g1, g2, g3, g4]

sorteio = shuffle(g_lista)

print('A ordem de apresentação será:')
print('1.{}'.format(g_lista[0]))
print('2.{}'.format(g_lista[1]))
print('3.{}'.format(g_lista[2]))
print('4.{}'.format(g_lista[3]))

#CORRIGIDO 