# DESAFIO 033 - Faça um programa que leia 3 números e mostre qual é o maior e o menor.

print('Vamos descobrir qual é o maior e o menor número:')
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número:'))

if n1 > n2 and n1 > n3:
    print('{} é o maior número.'.format(n1))
elif n2 > n1 and n2 > n3:
    print('{} é o maior número.'.format(n2))
else:
    print('{} é o maior número'.format(n3))

if n1 < n2 and n3:
    print('E {} é o menor número.'.format(n1))
elif n2 < n1 and n3:
    print('E {} é o menor número.'.format(n2))
else:
    print('E {} é o menor número'.format(n3))

# corrigido