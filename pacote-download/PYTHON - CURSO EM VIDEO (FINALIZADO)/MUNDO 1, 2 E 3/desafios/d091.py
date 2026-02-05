# DESAFIO 091 - Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em rodem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}
ranking = []

for c in range(0,4):
    jogadores[f'jogador{c+1}'] = randint(1, 6)
    

print('Valores sorteados: ')
for k, v in jogadores.items():
    sleep(0.5)
    print(f'O {k} tirou {v}')


print('Ranking dos jogadores:')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')

#corrigido


