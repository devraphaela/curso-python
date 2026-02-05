# DESAFIO 098 - Faça um progrramaa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo e realize a contagem.

# Seu programa tem que realizar três contagens atravês da função criada:

# De 1 até 10, de 1 em 1
# De 10 até 0, de 2 em 2
# Uma contagem personalizada  

from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1

    if passo < 0:
        passo = passo * -1

    if inicio < fim:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for n in range(inicio, fim + 1, passo):
            sleep(0.5)
            print(f'{n}', end=' ', flush=True)
        print('FIM')
        sleep(1)    
    else: 
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for n in range(inicio, fim -1, -passo):
            sleep(0.5)
            print(f'{n}', end=' ', flush=True)
        print('FIM')
        sleep(1)
    

      

contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)


#corrigido

