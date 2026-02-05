# DESAFIO 052 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

total = 0

num = int(input('Digite um número para saber se ele é ou não um número primo: '))

for c in range (1, num+1):
    if num % c == 0:
        print('\033[34m')
        total += 1 #se for ele guarda aqui +1
    else:
        print('\033[m')
    print(f'{c} ')
    
print(f'o número {num} foi divisível {total} vezes')

if total == 2:
    print('Por isso ele é primo')
else:
    print('por isso ele não é primo')

#CORRIGIDO 
