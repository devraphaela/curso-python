# DESAFIO 100 - Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocar dentro da lista e a segunda vai mostrar a soma de todos os valores PARES sorteados pela função anterior.

from random import randint
from time import sleep


def sorteia(num):
    print('Sorteando 5 valores da lista: ', end='')
    while len(num) < 5:
        n = randint(1, 10)
        if n not in num:
            num.append(n)
            sleep(0.5)
            print(f'{n}', end=' ', flush=True)    
    print('PRONTO!')
    

def somaPar(num):
    s = 0
    for n in num:
        if n % 2 == 0:
            s += n
    print(f'Somando os valores pares de {num}, temos {s}')

    
numeros = list()
sorteia(numeros)
somaPar(numeros)

#corrigido

