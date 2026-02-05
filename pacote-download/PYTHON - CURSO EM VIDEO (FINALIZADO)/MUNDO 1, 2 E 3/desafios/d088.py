# DESAFIO 088 - Faça um programa que ajude um jogador da MEGASENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from time import sleep
from random import randint

jogos = []


perg = int(input('Quantos jogos você quer que eu sorteie?'))

print(f'-=-=-=-= SORTEANDO {perg} JOGOS -=-=-=')
for c in range(perg):
    sleep(0.5)
    jogo = []
    while len(jogo) < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)

    jogo.sort()
    jogos.append(jogo)
    print(f'Jogo {c+1}: ', end='')
    print(jogo)
    sleep(0.5)

print('Aqui estão os seus palpites!')



#corrigido


