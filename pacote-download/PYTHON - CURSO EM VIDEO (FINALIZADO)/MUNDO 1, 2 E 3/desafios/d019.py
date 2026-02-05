# DESAFIO 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

#nomes dos alunos
aluno1 = str(input('Digite o nome do 1 aluno:'))
aluno2 = str(input('Digite o nome do 2 aluno:'))
aluno3 = str(input('Digite o nome do 3 aluno:'))
aluno4 = str(input('Digite o nome do 4 aluno:'))

#lista de alunos
lista = [aluno1, aluno2, aluno3, aluno4]

#sorteio
sorteado = random.choice(lista)

#resultado
print('O aluno escolhido foi {}'.format(sorteado))

#CORRIGIDO