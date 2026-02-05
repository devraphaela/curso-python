# DESAFIO 099 - Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.

# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(* num):
    qtd = mai = 0
    print('-='*30)
    print('Analisando os valores informados...')
    for n in num:
        print(f'{n} ', end=' ', flush=True)
        sleep(0.5)
        if mai == 0:
            mai = n
        else:
            if n > mai:
                mai = n
        qtd += 1
    sleep(2)   
    print(f'Foram informados {qtd} valores ao todo.')
    print(f'O maior valor informado foi {mai}')
    
                
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

#corrigido
